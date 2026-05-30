'''
TASKS:
1) String in lowercase
2) Frequency of all words in a given string
3) Frequency of a specific word

'''

# ---------------------- PART A: DEFINING CLASS

# DEFINE A STRING
givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

# DEFINE CLASS AND ATTRIBUTES
class TextAnalyzer(object):

    # constructor
    def __init__(self, text):

        # remove punctuation
        newText = text.replace('!','').replace('?','').replace(',','').replace('.','')

        # make text lowercase
        newText = newText.lower()

        self.fmtText = newText  # this is my attribute

    # Instance: count occurrence of words - how many unique words are there
    def freqAll(self):
        # split text into individual words
        wordList = self.fmtText.split(' ')      # splits with a space delimeter

        # create dictionary
        freqMap = {}    # introduce an empty dictionary

        # remove duplicates
        for word in set(wordList):                  # set() is a built-in data type that cannot contain duplicates
            freqMap[word] = wordList.count(word)    # this will count how many times words repeats in the original list
        
        return freqMap

    def freqOf(self, word):
        # get frequency map
        freqDict = self.freqAll()   # gets the number of the specific word from freqMap

        if word in freqDict:
            return freqDict[word]
        else:
            return 0                # to avoid error: in case the word entered is not in the list, it shall return 0
        
# ---------------------- PART B: CALLING FUNCTIONS

# Create object/instance: givenstring
analyzed = TextAnalyzer(givenstring)

# convert to lowercase by calling attribute .fmtText 
print("Formatted Text: ",analyzed.fmtText)

# counts frequency of all unique words by calling function freqAll()
freqMap = analyzed.freqAll()
print(freqMap)

# count frequency of a specific word "lorem" by calling function freqOf()
word="lorem"
frequency = analyzed.freqOf(word)
print("The word ",word," appears ",frequency," times.")