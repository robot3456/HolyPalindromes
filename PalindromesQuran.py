import os 


#INPUT_FILE = "resources/text/quran-simple-clean.txt"
INPUT_FILE = "resources/text/quran-simple-clean-no-bismillah.txt"
#INPUT_FILE = "resources/text/extract.txt"
OUTPUT_FILE = "resources/text/output.txt"
RESULT_FILE = "resources/text/results.txt"

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




class QuranPalindromes(QuranStats, QuranFormatting):

    def __init__(self):
        QuranStats().__init__()
        QuranFormatting().__init__()
        self.letters = 0
        #super().__init__()

    def countLetters(self, inputFile):
        with open(inputFile) as quran: 
            for verse in quran : 
                for letter in verse :
                    if(letter != " ") and (letter != "\n"):
                        self.letters += 1
        return self.letters

    def extractNLetters(self, N=1, offset=0, ignoreSpaces=True):
        """
        Used to extract any string of N letters in the text
        N : String size
        offset : to move across the text
        """    
        
        offset_count = 0
        buffer=""

        with open(INPUT_FILE) as quran: 
            for absoluteAyahNumber,ayah in enumerate(quran):
                for letter in ayah:
                    

                    if offset_count==offset:
                        if ignoreSpaces==True:
                            # not ok because restarts from beginning of the line
                            if (letter!=" ") and (letter!="\n"):
                                #print(absoluteAyahNumber+1)
                                buffer = "".join((buffer, letter))
                                #print(f"buffer is {buffer}")
                        else:
                            print(absoluteAyahNumber+1)
                            buffer = "".join((buffer, letter))
                            #print(f"buffer is {buffer}")
                            buffer = buffer.replace("\n", " ")

                        if len(buffer) == N:
                            return (absoluteAyahNumber+1, buffer)

                    else: 
                        #print("je suis dans le else")
                        if (letter!=" ") and (letter!="\n"):
                            offset_count+=1

                    #print(f"{absoluteAyahNumber+1} -> {verse}")


    def scanAllQuranForConstantN(self, N=1, ignoreSpaces=True):

        #print(self.letters)
        self.countLetters(INPUT_FILE)

        with open(INPUT_FILE) as quran, open(RESULT_FILE, 'a') as rf:

            # self.letter size is incorrect : we should substract the number of total spaces contained in the text
            for letterNumber in range(0,self.letters-(N)):

                try:
                    absAyatNum, strToAnalyze = self.extractNLetters(N, letterNumber, ignoreSpaces)

                    #print(f"Palindrome found (TRUE) !  : ")
                    #print(f"scan ---> {absAyatNum} : {strToAnalyze}")

                    if QuranPalindromes().isPalindrome(strToAnalyze):
                        
                        print(f"Palindrome found (TRUE) !  : ")
                        print(f"scan ---> {absAyatNum} : {strToAnalyze}")
                        rf.write(f"Absolute Verse : {absAyatNum} --> {strToAnalyze} \n")
                
                except TypeError:
                    break

    def scanAllQuranForAllN(self):
        with open(RESULT_FILE, 'a') as rf:
            for i in range(self.letters):
                rf.write(f"------- For palindrome length = {i} -------\n")
                print(f"------- For palindrome length = {i} -------")
                self.scanAllQuranForConstantN(i)

    def isPalindrome(self, palindromeCandidate):
        if palindromeCandidate == palindromeCandidate[::-1]:
            return True
        return False




def main():

    quran = QuranPalindromes()
    #quran.printQuranTxt()
    print(f"checking palindrome ---> { quran.isPalindrome('dadad') }")

    myString = "Bonjoour azeori  pazo\n ier poe\n a poiaez pzae"
    quran.deleteSpacesAndEOLInString(myString)
    #print(myString)



    """
    # Surah Ya-Sin :  c.300367 / v.3744 / s.36
    num,buf = quran.extractNLetters(1, 3)
    print(f"buf is ---> {buf}")
    print(f"Is this a palindrome ? ---> ANSWER: {quran.isPalindrome(buf)}")

    """
    print(" #------------------- MAIN --------------------# ")


    x = quran.countLetters(INPUT_FILE)
    """
    print(f"x is {x}")
    for i in range(0,10):
        numa, bufa = quran.extractNLetters(1,i)
        print(numa , bufa)
    """
    
    #y = quran.scanAllQuranForConstantN(3)
    quran.scanAllQuranForAllN()
    
    """
    pal = quran.isPalindrome(buf)
    print(pal)

    print(" #------------------- MAIN --------------------# ")

    x = quran.countLetters(INPUT_FILE)
    #print(x)
    quran.scanAllQuran(x)

    print(" #------------------- END --------------------# ")
    """

if __name__=="__main__":
    main()

