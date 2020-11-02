import random
import string

#Opening and looping through word file
words = []
with open("words.txt", "r") as my_words:
    read = my_words.read()
    #Seperating the words and appending to list
    for word in read.split():
        words.append(word)


#Fcuntion to pick random word from list
def pick_word():
    return random.choice(words)


#Function to see if user has guessed word, returning a bool
def word_guessed(word, letters_guessed):
    return letters_guessed == list(word)

#Function to returns list of correct letters and underscores for letters that haven't been guessed  
# Takes the secret word and the letters guessed     
def get_reveal(word, letters_guessed):
    reveal = len(word) * "_"
    reveal = list(reveal)
    for i in letters_guessed:
        index = 0
        for j in word:
            if i == j:
                reveal[index] = j
                index += 1
            else:
                index += 1
      
    return reveal

#Function to return letters in alphabet left as string
def available_letters(letters_guessed):
    alphabet = [i for i in string.ascii_lowercase]
    for i in letters_guessed:
        if i in alphabet:
            alphabet.remove(i)
    return "".join(alphabet)


#Game

def hangman(word):
    global lives_left
    global letters_guessed

    word = word
    lives_left = 6
    letters_guessed = []

    print("Welcome to Hangman. The word is {}.".format(get_reveal(word, letters_guessed)))
    

    while lives_left > 0:
        print("Available letters are: {}".format(available_letters(letters_guessed)))
        print("You have {} guesses left.".format(lives_left))
        guess = input("Please guess a letter: ").lower()

        if guess in letters_guessed:
            print("You have already guessed that letter, please guess again!")
            continue


        letters_guessed.append(guess)

        if word_guessed(word, get_reveal(word, letters_guessed)) == True:
            print("Well done! You guessed correctly.")
            print("The word was {}!".format(word))
            break
        else:
            if guess not in word:
                lives_left -= 1
                if lives_left == 0:
                    print("Unlucky, you have no more guesses left, the word was {}.".format(word))
                else:
                    print("Incorrect, that is not in the word. {}".format(get_reveal(word, letters_guessed)))
            else:
                print("Correct, good guess. {}".format(get_reveal(word, letters_guessed)))


#Loop so user can play as many times as they like
while True:
    play = input("Would you like to play hangman? y/n").lower()
    if play == "y":
        hangman(pick_word())
    else:
        print("Have a good day, goodbye!")
        break






