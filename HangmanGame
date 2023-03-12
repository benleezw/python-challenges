BLANK = (" _ ")
MaxGuesses = 10

def GetWord():
    print("Player 1 look away while Player 2 inputs a word for you to guess")
    Word = input("Player 2 type a word for Player 1 to guess: ")
    for i in range(35):
        print()
    return Word.upper()

def MakeGuess(GuessedLetters):
    print()
    Guess = input("Try to guess a letter in the word: ")
    while Guess in GuessedLetters:
        print()
        Guess = input("Letter has been guessed. Guess a different letter: ")
    print()
    GuessedLetters.append(Guess)
    return Guess.upper()

def DisplayWord1(Word):
    print("This is the hidden word:")
    print()
    for L in range(0, len(Word)):
        print(BLANK, end="")
    print()

def DisplayWordGuess(Word, WordList, Guess, GameWon):
    print("These are the spaces remaining:")
    print()
    for L in range(0, len(Word)):
        if Guess == Word[L]:
            WordList[L] = Word[L]
    if Guess not in Word:
        print("The letter", Guess, "is not in the word")
        print()
    NewWordList = "".join(WordList)
    print(NewWordList)
    print()
    return NewWordList

def PlayGame(GetWord):
    Guesses = 0
    GameWon = False
    WordList = []
    GuessedLetters = []
    Word = GetWord()
    for R in range(0, len(Word)):
        WordList.append(BLANK)
    DisplayWord1(Word)
    while GameWon == False and Guesses < MaxGuesses:
        Guess = MakeGuess(GuessedLetters)
        NewWordList = DisplayWordGuess(Word, WordList, Guess, GameWon)
        if Guess not in Word:
            Guesses = Guesses + 1
        print("You have", MaxGuesses - Guesses, "guesses remaining")
        print()
        if NewWordList == Word.upper():
            GameWon = True
    if GameWon:
        print("Player 1 got the word! The word was", Word)
        print("Player 1 wins!")
        print()
    else:
        print("Oh no! Player 1 has lost. The word was", Word)
        print("Player 2 wins!")
        print()

if __name__ == "__main__":
    PlayGame(GetWord)

