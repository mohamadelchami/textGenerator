import re
import operator
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader
import os
import fnmatch
from warnings import warn
import pathlib

'''
Library Overview:
re - Used for regular expressions when extracting substrings from files
operator - Used in the sorting of the interests dictionary
bs4 - Used for the reformatting of the HTML documents
jinja2 - Used in the template completion
os - Used for getcwd() for stand alone execution
'''

'''
A user class was created to store information on a user. The reason a class was chosen was
because we wanted to be able to store multiple users within the same execution. It was
also more convenient to have methods with simple names for higher level thinking.
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
cleanHTML will take the file initially read and clean it up in a typical HTML format for better data extraction
'''
def cleanHTML(inputFile):
    with open(inputFile, 'r', encoding='utf-8') as file:
        f = BeautifulSoup(file, "html.parser")
        return f.prettify()
    warn(f"Error: \"{inputFile}\" is not a valid file path")
    return ''

def extractUserName(user, file, cssSearchClass="gmql0nx0 l94mrbxd p1ri9a11 lzcic4wl bp9cbjyn j83agx80"):
    nextLine = False
    for line in file:
        if nextLine:
            line = re.search('^\s+(.+?)\n', line)
            user.setName(line.group(1))
            nextLine = False
            break;

        if f'class="{cssSearchClass}"' in line:
            nextLine= True
            

'''
extractInterests() will extract all the interest from the users like page, as well as sort them in order of least
to most occurring, and then extract the top 3 occurring interests
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
function takes an user object and template and then saves the output in the given output file
'''
def generatePhishingText(user, outputFile, templateFile):
    template_dir = str(pathlib.Path(__file__).parent.absolute())+ "/templates"
    env = Environment(loader = FileSystemLoader(template_dir))
    #Load the template we will be using
    template = env.get_template(templateFile)
    #render out the template with the variables
    userIntrests = user.getThreeInterests()
    html = template.render( name=user.getName(), interest1=userIntrests[0], 
                           interest2=userIntrests[1], interest3=userIntrests[2])
    #This will output our results
    with open(outputFile, "w", encoding='utf-8') as f:
        f.write(html)

'''
generateEmail() will generate a HTML file based off the provided template using the data gather on the user.
The parameters are the user object, for relevant user data, and the current file count, to create a consistent
file naming convention
'''
def generateEmail(user, i, outputPath):
    outputFile = outputPath + f"/email{i}.html"
    generatePhishingText(user, outputFile, 'template.html')

'''
generateText() will generate a TXT file based off the provided template using the data gather on the user.
The parameters are the user object, for relevant user data, and the current file count, to create a consistent
file naming convention
'''
def generateText(user, i, outputPath):
    outputFile = outputPath+f"/message{i}.txt"
    generatePhishingText(user, outputFile, 'text.txt')
   

#call this function when executing from another python script.
def main(inputPath=os.getcwd(), outputPath=os.getcwd()):
    friendLikesPages = fnmatch.filter(os.listdir(inputPath), 'friendLikesPage*.html')
    for friendLikesPage in friendLikesPages:
        # we can be sure the pattern matches because we used fmatch earlier
        i=int(re.search('friendLikesPage(\d+?)\.html', friendLikesPage).group(1))
        inputFile = f"{inputPath}/{friendLikesPage}"

        #Store the reformatted HTML content into file
        file = cleanHTML(inputFile)

        #Because the file is no longer needed we will overwrite it with the reformatted HTML
        with open(inputFile, "w", encoding='utf-8') as createCleanedFile:
            createCleanedFile.write(file)

        #We will then reopen this in read-mode and begin
        with open(inputFile, "r", encoding='utf-8') as f:
            file = f.readlines()
            #We will create a new user object
            user = User()
            #We begin to extract data from the file
            #We will pass the current user object by using the file format counting variable(i)
            extractUserName(user, file)
            extractInterests(user, file)
            #We will then generate then email and message files
            generateEmail(user, i, outputPath)
            generateText(user, i, outputPath)

#This was created to allow the file to execute alone
if __name__ == "__main__":
    main()

    
