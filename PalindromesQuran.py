

INPUT_FILE = "resources/quran-simple-clean.txt"

class QuranStats():
    
    def __init__(self):
        
        self.ignore_bismillah = False

        self.letters = 0
        self.words = 0
        self.verses = 0
        self.sourates = 0
        
    def countLetters(self, inputFile):
        with open(inputFile) as quran: 
            for verse in quran : 
                for letter in verse : 
                    self.letters += 1

        return self.letters

    def countWords(self, inputFile):
        with open(inputFile) as quran: 
            for verse in quran : 
                #print(verse)
                for letter in verse : 
                    print(letter)
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




def main():
    print("Je suis dans le main")
    
    newQuranStats = QuranStats()
    nqsSourates = newQuranStats.countSourates(INPUT_FILE)
    nqsVerses = newQuranStats.countVerses(INPUT_FILE)
    nqsWords = newQuranStats.countWords(INPUT_FILE)
    nqsLetters = newQuranStats.countLetters(INPUT_FILE)
    
    print("Sourates : " , nqsSourates)
    print("Verses : " , nqsVerses)
    print("Words : " , nqsWords)
    print("Letters : " , nqsLetters)


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

