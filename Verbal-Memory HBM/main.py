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

    # Current test: 100 words
    for i in range(100):
        currentWord = elementInteractions.getWord()
        seenWordButton = elementInteractions.getSeenWordButton()
        newWordButton = elementInteractions.getNewWordButton()

        # Check if a word with a new starting letter exists in the dictionary. If yes, check if its a new word
        if not currentWord[0] in wordDict:
            print(f"Made inside, current word: %s", currentWord)
            wordDict[currentWord[0]].append(currentWord)
            time.sleep(1)
            elementInteractions.clickNew(newWordButton)
            
        else:
            for word in wordDict[currentWord[0]]:
                if currentWord == word:
                    elementInteractions.clickSeen(seenWordButton)
                    break
            wordDict[currentWord[0]].append(currentWord)
            time.sleep(1)
            elementInteractions.clickNew(newWordButton)


if __name__ == "__main__":
    main()






