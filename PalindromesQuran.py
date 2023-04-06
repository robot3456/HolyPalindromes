import os 


#INPUT_FILE = "resources/quran-simple-clean.txt"
INPUT_FILE = "resources/quran-simple-clean-no-bismillah.txt"
#INPUT_FILE = "resources/extract.txt"
#INPUT_FILE = "resources/output.txt"

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






def main():
    print("Je suis dans le main")
    
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
        os.remove(INPUT_FILE)
    except OSError:
        print(f"The file {INPUT_FILE} doesn't exists ! Cannot delete it !")

    f = open("resources/output.txt", "a")
    f.write(nqsSingleLine)
    f.close()


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

