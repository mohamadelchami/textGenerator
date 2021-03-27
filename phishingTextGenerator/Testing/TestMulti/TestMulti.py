import unittest
import sys
import os
# hacky fix to get parent directory
sys.path.append(os.getcwd() + '/../..')
import textGenerator

class testTextGenerator(unittest.TestCase):
    inputPath = os.getcwd()
    outputPath = os.getcwd()
    textGenerator.main(inputPath, outputPath)

    def testFormatting(self):
        for i in range(0, 1):
            formatted = open(f"friendLikesPage{i}.html", 'r')
            expected = open(f"expectedValues/{i}/expectedFormatting{i}.html", 'r')
            self.assertTrue(formatted.read() == expected.read(), "HTML was not formatted properly")
            formatted.close()
            expected.close()
    
    def testHTMLGeneration(self):
        for i in range(0, 1):
            expectedHTML = open(f"expectedValues/{i}/expectedhtml{i}.html", 'r')
            generatedHTML = open(f"email{i}.html", 'r')
            self.assertTrue(generatedHTML.read() == expectedHTML.read(), "HTML was not generated or generated incorrectly")
            expectedHTML.close()
            generatedHTML.close()

    def testMessageGeneration(self):
        for i in range(0, 1):
            expectedMessage = open(f"expectedValues/{i}/expectedmessage{i}.txt", 'r')
            generatedMessage = open(f"message{i}.txt", 'r')
            self.assertTrue(generatedMessage.read() == expectedMessage.read(), "TXT was not generated or generated incorrectly")
            expectedMessage.close()
            generatedMessage.close()

if __name__ == '__main__':
    unittest.main()
