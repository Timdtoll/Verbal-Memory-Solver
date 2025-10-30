import elementInteractions

import time
from collections import defaultdict

# Does not work as of now
def main():
    # Stores the words that have been seen so far
    wordDict = defaultdict(list)

    # Create instance of webpage and begin verbal memory test
    elementInteractions.beginDriver()
    elementInteractions.clickStart()

    # Current test: 1000 words
    for i in range(10000):
        currentWord = elementInteractions.getWord()
        seenWordButton = elementInteractions.getSeenWordButton()
        newWordButton = elementInteractions.getNewWordButton()

        # Check if a word with a new starting letter exists in the dictionary, add it to dictionary with new key if yes
        if not currentWord[0] in wordDict:
            wordDict[currentWord[0]].append(currentWord)
            elementInteractions.clickNew(newWordButton)
            
        else:
            for word in wordDict[currentWord[0]]:
                #If word has been seen before, hit seen button
                if currentWord == word:
                    elementInteractions.clickSeen(seenWordButton)
                    break
                #If word has not been seen before, hit new button and add to dictionary
                elif word == wordDict[currentWord[0]][-1]:
                    wordDict[currentWord[0]].append(currentWord)
                    elementInteractions.clickNew(newWordButton)
                    break

                
#Testing
def printDict(wordDict):
    for key in wordDict:
        print(f"{key}: {wordDict[key]}")

if __name__ == "__main__":
    main()






