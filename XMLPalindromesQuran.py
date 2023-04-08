import xml.etree.ElementTree as ET
import xml

#INPUT_FILE = "resources/text/quran-simple-clean.txt"
#INPUT_FILE = "resources/text/quran-simple-clean-no-bismillah.txt"
#INPUT_FILE = "resources/text/extract.txt"
#OUTPUT_FILE = "resources/text/output.txt"
#XML_FILE = "resources/xml/quran-simple-clean.xml"
XML_FILE = "resources/xml/quran-simple-clean.xml"

class QuranXML(ET.ElementTree):

    def __init__(self, xml_file=XML_FILE):
        super().__init__()
        self.tree = ET.parse(XML_FILE)
        self.root = self.tree.getroot()

    def printSurahNames(self):
        for surah in self.root:
            print(surah.get('name'))

    def printAllAyahs(self):
        for surah in self.root:
            for ayah in surah:
                #print( ( surah.get('index'), surah.get('name') ,ayah.get('index'),ayah.get('text')) )
                print(ayah.get('text'))

    def printAllLetters(self):
        for surah in self.root:
            for ayah in surah:
                for letter in ayah.get('text'):
                    print(letter)

    def extractNLetters(self, N=1, offset=0, ignoreSpaces=True):
        """
        Used to extract any string of N letters in the text
        N : String size
        offset : to move across the text
        """    
        
        offset_count = 0
        buffer=""

        for surah in self.root:
            for relativeAyahNumber,ayah in enumerate(surah):                
                for letter in ayah.get('text'):

                    #print(f"oBuffer = {buffer} ")
                    #print(f"oOffsetCount = {offset_count}")
                    #print(relativeAyahNumber)

                    if offset_count==offset:

                        if ignoreSpaces==True:
                            #print(f"letter is {letter}")
                            #print("lkjhlk")
                            if letter!=" ":
                                print(relativeAyahNumber+1)
                                buffer = "".join((buffer, letter))
                                print(f"buffer is {buffer}")
                        else:
                            print(relativeAyahNumber+1)
                            buffer = "".join((buffer, letter))
                            print(f"buffer is {buffer}")


                        #print(f"buffer is : {buffer}")
                        if len(buffer) == N:
                            return buffer
                            
                    else: 
                        print("je suis dans le else")
                        offset_count+=1

        # print("bonjour")

    def analyzeAllQuran(self, igoreSpaces=True):
        pass

    def isPalindrome(self, palindromeCandidate):
        if palindromeCandidate == palindromeCandidate[::-1]:
            return True
        return False

                
#print(ET.tostring(root))



def main():

    xmlq = QuranXML()
    #xmlq.printSurahNames()
    #xmlq.printAllAyahs()
    #xmlq.printAllLetters()
    buf = xmlq.extractNLetters(3,2)

    print(f"final buf -------> {buf}")

"""
    tree = ET.parse(XML_FILE)
    root = tree.getroot()

    #print(ET.tostring(root))

    for child in root:  
        #print(child.get(sura))
        print(child)
        print(child.get('name'))

    print(len(root))

    print(root.get('quran'))
"""


if __name__== "__main__":
    main()







