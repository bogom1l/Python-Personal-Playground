
def DisplayTheWord(word, guessedLetters):
    displayedWord = ''
    for letter in word:
        if letter in guessedLetters:
            displayedWord += letter
        else:
            displayedWord += '_'
    return displayedWord

def StartGame():
    guessedLetters = []
    attempts = 5

    print("--STARTED HANGMAN GAME--")
    print(DisplayTheWord(word, guessedLetters))

    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessedLetters:
            print("You've already guessed that letter.")
            continue

        guessedLetters.append(guess)

        if guess not in word:
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts left.")
            if attempts == 0:
                print("Game over! The word was:", word)
                break
        else:
            print("Correct letter!")

        displayedWord = DisplayTheWord(word, guessedLetters)
        print(displayedWord)

        if '_' not in displayedWord:
            print("Congratulations! You've guessed the word:", word)
            break

if __name__ == "__main__":
    word = 'bogomil'
    StartGame()
    