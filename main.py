import random
Hangman = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
words = "tuple comprehensions list lambda python iterable jupyter repository random yield return range while break enumerate numpy panda split index branch".split()
alphabet = "abcdefghijklmnopqrstuvwxyz"

def searchrandomword(words_list):
    # Return the random word.
    word_random = random.randint(0, len(words_list) - 1)
    return words_list[word_random]
 
def displayBoard(Hangman, incorrect, correct, word_secret):
    # The incorrect and correct words are indicated.
    print (Hangman[len(incorrect)])
    print (" ")
    print ("Incorrect letters:", end= " ")
    for letter in incorrect:
        print (letter, end= " ")
    print (" ")
    space = "_" * len(word_secret)
    # Replace the blanks with the letter well written.
    for i in range(len(word_secret)): 
        if word_secret[i] in correct:
            space = space[:i] + word_secret[i] + space[i+1:]
    # It will show the secret word with spaces between letters.
    for letter in space: 
        print (letter, end= " ")
    print ("")
 
def chooseletter(some_letter):
    # Print the letter the player has chosen.
    while True:
        print ("Choose a letter:")
        letter = input()
        letter = letter.lower()
        if len(letter) != 1:
            print ("Choose a letter") 
        elif letter in some_letter:
            print ("You already chose this letter before. Try another letter")
        elif letter not in (alphabet):
            print ('Choose another letter.')
        else:
            return letter
 
def start():
    # If the player wants to play again returns True, if he does not want to play again, returns False.
    print ("Would you like play again? (Y / N)")
    return input().lower().startswith("y")
 
print ("Hangman")
incorrect = ""
correct = ""
word_secret = searchrandomword(words)
end_game = False
while True:
    displayBoard(Hangman, incorrect, correct, word_secret)
    # The player choose a letter.
    letter = chooseletter(incorrect + correct)
    if letter in word_secret:
        correct = correct + letter
        # Shows if player wins.
        letters_found = True
        for i in range(len(word_secret)):
            if word_secret[i] not in correct:
                letters_found = False
                break
        if letters_found:
            print ('You win! The correct word is "' + word_secret + '"! Congratulations!')
            end_game = True
    else:
        incorrect = incorrect + letter
        # Indicates the number of correct and incorrect letters chosen by the player and show the correct word.
        if len(incorrect) == len(Hangman) - 1:
            displayBoard(Hangman, incorrect, correct, word_secret)
            print ("You can't put any more letters!")
            print ("After that " + str(len(incorrect)) + " incorrect letters and " + str(len(correct)) + " correct letters")
            print ('The word is "'+ word_secret + '"!')
            end_game = True
    # Asks if the player wants to play again.
    if end_game:
        if start():
            incorrect = ""
            correct = ""
            end_game = False
            word_secret = searchrandomword(words)
        else:
            break