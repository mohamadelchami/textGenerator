import re
import operator
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader

'''
Library Overview:
re - Used for regular expressions when extracting substrings from files
operator - Used in the sorting of the interests dictionary
bs4 - Used for the reformatting of the HTML documents
jinja2 - Used in the template completion
'''

'''
A user class was created to store information on a user. The reason a class was chosen was
because we wanted to be able to store multiple users within the same execution. It was
also more convient to have methods with simple names for higher level thinking.
'''
class User:
    def __init__(self):
        self.name = ""
        self.allInterests = {}
        self.threeInterests=[]

    def setName(self, newName):
        self.name = newName

    def appendAllInterests(self, interest):
        if interest not in self.allInterests:
            self.allInterests[interest] = 1
        else:
            self.allInterests[interest] += 1

    def sortAllInterests(self):
        self.allInterests = dict( sorted(self.allInterests.items(), key=operator.itemgetter(1))) 

    def appendThreeInterests(self, interest):
        self.threeInterests.append(interest)

    def getName(self):
        return self.name

    def getAllInterests(self):
        return self.allInterests

    def getThreeInterests(self):
        return self.threeInterests

'''
cleanHTML will take the file initially read and clean it up in a typical html format for better data extraction
'''
def cleanHTML(file):
    f = BeautifulSoup(file, "html.parser")
    return f.prettify()


def extractUserName(user, file):
    nextLine = False
    for line in file:
        if nextLine:
            line = re.search('^\s+(.+?)\n', line)
            user.setName(line.group(1))
            nextLine = False
            break;

        if 'class="gmql0nx0 l94mrbxd p1ri9a11 lzcic4wl bp9cbjyn j83agx80"' in line:
            nextLine= True
            

'''
extractInterests() will exract all the interest from the users like page, as well as sort them in order of least
to most occuring, and then extract the top 3 occuring interests
The parameters are the user object, this enables us to record the data that we need, as well as the file that the
interests will be extracted from.
'''
def extractInterests(user, file):
    nextLine = False  
    for line in file:
        if nextLine:
            line = re.search('^\s+(.+?)\n', line)
            user.appendAllInterests(line.group(1))
            nextLine=False
            continue

        if '<div dir="auto" style="text-align: start;">' in line:
            nextLine=True

        else:
            continue
        
    user.sortAllInterests()
    
 
    for i in range(3):
        user.appendThreeInterests(user.getAllInterests().popitem()[0])

'''
generateEmail() will generate a HTML file based off the provided template using the data gather on the user.
The parameters are the user object, for relavent user data, and the current file count, to create a consistent
file naming convention
'''
def generateEmail(user, i):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    #Load the template we will be using
    template = env.get_template('template.html')
    #render out the template with the variables
    html = template.render(name=user.getName(), interest1=user.getThreeInterests()[0], interest2=user.getThreeInterests()[1], interest3=user.getThreeInterests()[2])

    #This will create the email file
    f = open(f"email{i}.html", 'w')
    f.write(html)
    f.close()

'''
generateText() will generate a TXT file based off the provided template using the data gather on the user.
The parameters are the user object, for relavent user data, and the current file count, to create a consistent
file naming convention
'''
def generateText(user, i):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    #Load the template we will be using
    template = env.get_template('text.txt')
    #render out the template with the variables
    msg = template.render(name=user.getName(), interest1=user.getThreeInterests()[0], interest2=user.getThreeInterests()[1], interest3=user.getThreeInterests()[2])

    #This will create the text
    f = open(f"message{i}.txt", 'w')
    f.write(msg)
    f.close()

#call this function when executing from another python script.
def main():

    #We will use this variable to format the file naming 
    i = 0
    #users will hold a list of all the user objects (Mainly done because of a runtime error)
    users = []

    while True:
        try:
            #Store the reformatted HTML content into file
            file = cleanHTML(open(f"friendLikesPage{i}.html", 'r'))

            #Becuase the file is no longer needed we will overwrite it with the reformatted HTML
            createCleanedFile = open(f"friendLikesPage{i}.html", 'w')
            createCleanedFile.write(file)
            createCleanedFile.close()

            #We will then reopen this in read-mode and begin
            file = open(f"friendLikesPage{i}.html", 'r')
            file = file.readlines()

            #We will create a new user object and append it to the users list
            users.append(User())

            #We begin to extract data from the file
            #We will pass the current user object by using the file format counting varaible(i)
            extractUserName(users[i], file)
            extractInterests(users[i], file)

            #We will then generate then email and message files
            generateEmail(users[i], i)
            generateText(users[i], i)

            #We then increment the file format counter(i)
            i += 1

        #Once we reach the end of the provided files, an error will occur and this will catch it and end the program
        except:
            break

#This was created to allow the file to execute alone
if __name__ == "__main__":
    main()

    
