import random
allWords = ['apple', 'banana', 'cherry', 'dog', 'elephant', 'fox', 'giraffe', 'house', 'igloo', 'jacket']
guessedWords = []
words = int(input("How many words do you want to memorize: "))
newWords = []
for i in range(words):
    newWords.append(allWords[random.randint(0, (len(allWords))-1)])
print(f"Memorize these words: {newWords}")
hold = input("Press enter to continue.....")
print("\n\n\n\n\n\n\n\n\n\n")
run = True
run2 = False
correctGuesses = 0
while run:
    guess = input("Enter the words you can remember separated by only a comma: ")
    guessList = guess.split(",")
    for guess in guessList:
        if guess in guessedWords:
            print(f"You have already guessed the word {guess}")
        elif guess in newWords:
            run2 = True
            while run2:
                newWords.remove(guess)
                correctGuesses+=1
                run2 = True if guess in newWords else False
        else:
            print(f"{guess} was not one of the words")
        guessedWords.append(guess)
    print(f"Words left: {len(newWords)}")
    if len(newWords)==0:
        print("You have guessed all the words!")
        break
    tryAgain = input(f"You remembered {correctGuesses} words correctly. Try again? y/n: ").lower()
    run = True if tryAgain == "y" else False