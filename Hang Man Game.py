import random
ChooseWordList = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'python']

def ChooseWordFun():
    return random.choice(ChooseWordList)

def InitializeGame():
    word = ChooseWordFun()
    GuessedLetters = set()
    IncorrectGuess, MaxAttempts  = 0, 10 
    return word, GuessedLetters, IncorrectGuess, MaxAttempts

def DisplayWord(word, GuessedLetters):
    displayed_word = ''
    for letter in word:
        if letter in GuessedLetters:
            displayed_word += letter + ' '
        else:
            displayed_word += '_ '
    return displayed_word.strip()

def CheckWin(word, GuessedLetters):
    for letter in word:
        if letter not in GuessedLetters:
            return False
    return True

def PlayHangman():
    print("Welcome to Hangman!")
    word, GuessedLetters, IncorrectGuess, MaxAttempts = InitializeGame()
    while IncorrectGuess < MaxAttempts:
        print("\nWord to guess: ", DisplayWord(word, GuessedLetters))
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue
        if guess in GuessedLetters:
            print("You've already guessed that letter!")
            continue
        GuessedLetters.add(guess)
        if guess in word:
            print("Nice guess!")
        else:
            print("Oops! Incorrect guess.")
            IncorrectGuess += 1 
        if CheckWin(word, GuessedLetters):
            print(f"\nCongratulations! You guessed the word: {word}")
            break
        print(f"Attempts left: {MaxAttempts - IncorrectGuess}")
    else:
        print(f"\nGame over! The word was: {word}")
        
PlayHangman()