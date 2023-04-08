import os 


#INPUT_FILE = "resources/text/quran-simple-clean.txt"
INPUT_FILE = "resources/text/quran-simple-clean-no-bismillah.txt"
#INPUT_FILE = "resources/text/extract.txt"
OUTPUT_FILE = "resources/text/output.txt"

class QuranStats():
    
    def __init__(self):
        
        self.ignore_bismillah = False

        self.letters = 0
        self.words = 0
        self.verses = 0
        self.sourates = 0

        self.singleLineQuran = ""
        
    def countLetters(self, inputFile):
        with open(inputFile) as quran: 
            for verse in quran : 
                for letter in verse :
                    if(letter != " ") and (letter != "\n"):
                        self.letters += 1

        return self.letters
    
    # Not giving expected result ()
    def countWords(self, inputFile):
        with open(inputFile) as quran: 
            for verse in quran : 
                #print(verse)
                for letter in verse : 
                    #print(letter)
                    if (letter==" ") or (letter=="\n"):
                        self.words += 1

        return self.words
        
        
    def countVerses(self, inputFile):
        with open(inputFile) as quran :
            nbQuranVerses = len(quran.readlines())
            return nbQuranVerses

    def countSourates(self, inputFile):
        with open(inputFile) as quran:
            for verse in quran:
                if "بسم الله الرحمن الرحيم" in verse:
                    self.sourates += 1
        return self.sourates

    def createOneLineQuran(self, inputFile):
        with open(inputFile) as quran : 
            for verse in quran : 
                self.singleLineQuran += verse

        return self.singleLineQuran

    def findPalindromes(self, inputFile, starting_length=1, ignore_spaces=True):
        with open(inputFile) as oneLineQuran:
            for line in oneLineQuran : 
                for characters in line : 
                    print(characters)



class QuranFormatting():
    def __init__(self):
        self.loadTextInMemory(INPUT_FILE)

    def loadTextInMemory(self, inputFile):
        with open(inputFile) as quran : 
            self.quranTxt = quran.readlines()
            #print(self.quranTxt)
            #print(type(self.quranTxt))

    def printQuranTxt(self):
        for i in range(len(self.quranTxt)):
            print(self.quranTxt[i], end='')

    # Not OP
    def readOneLine(self, inputFile):
        with open(INPUT_FILE) as quran:
            print("oneline")

    def deleteSpacesAndEOLInString(self, oString):
        oString = oString.replace(" ", "")
        oString = oString.replace("\n", "")
        return oString

    def writeToTxt(self, foundPalindrome, outputFile):
        try:
            os.remove(outputFile)
        except OSError:
            print(f"The file {OUTPUT_FILE} doesn't exists ! Cannot delete it !")

        f = open(outputFile, "a")
        f.write(foundPalindrome)
        f.close()






class QuranPalindromes(QuranFormatting):
    def __init__(self):
        super().__init__()

    def extractNLetters(self, N, offset=0):
        """
        Used to extract any string of N letters in the text
        N : String size
        offset : to move across the text
        """    
        pass
        
    def isPalindrome(self, palindromeCandidate):
        if palindromeCandidate == palindromeCandidate[::-1]:
            return True
        return False





def main():

    quran = QuranPalindromes()
    quran.printQuranTxt()
    print(quran.isPalindrome(""))

    myString = "Bonjoour azeori  pazo\n ier poe\n a poiaez pzae"
    #print(myString)
    quran.deleteSpacesAndEOLInString(myString)

    #print("After function : ")


    #print(myString)
    

    """
    newQuranStats = QuranStats()
    nqsSourates = newQuranStats.countSourates(INPUT_FILE)
    nqsVerses = newQuranStats.countVerses(INPUT_FILE)
    nqsWords = newQuranStats.countWords(INPUT_FILE)
    nqsLetters = newQuranStats.countLetters(INPUT_FILE)
    nqsSingleLine = newQuranStats.createOneLineQuran(INPUT_FILE)
    nqsSingleLine = nqsSingleLine.replace("\n", " ")

    print("Sourates : " , nqsSourates)
    print("Verses : " , nqsVerses)
    print("Words : " , nqsWords)
    print("Letters : " , nqsLetters)
    #print(nqsSingleLine)

    try:
        os.remove(OUTPUT_FILE)
    except OSError:
        print(f"The file {OUTPUT_FILE} doesn't exists ! Cannot delete it !")

    f = open(OUTPUT_FILE, "a")
    f.write(nqsSingleLine)
    f.close()

    print("######### FINDING PALINDROMES #########")
    f = open(OUTPUT_FILE, "a")
    abc = QuranStats()
    abc.findPalindromes(OUTPUT_FILE)
    f.close()

"""

"""
    with open("resources/extract.txt", "r") as op: 
    for i in op :
        for j in i :
            
            if (j == "\n"):
                print("retour chariot")
            print(i)
"""



if __name__=="__main__":
    main()

