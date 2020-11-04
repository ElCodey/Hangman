import string
import random

#Opening and loop through to get words from txt file

words = []
with open ("words.txt", "r") as my_words:
    read= my_words.read()
    #seperating words to append to list
    for word in read.split():
        words.append(word)

#Choose random word from list

def pick_word():
    return random.choice(words)

#To show the word in underscores 

def reveal(word):
    return list(len(word) * "_")


#Check if letter is in picked word

def letter_checker(word, user_guess):
    return user_guess in word

#To show user the letters still avialable 

def letters_left(letters_guessed):
    letters = [i for i in string.ascii_lowercase]
    for i in letters_guessed:
        if i in letters:
            letters.remove(i)
    
    return "".join(letters)

#When guessed letter is in word, this will be called to show index of the letters that have been guessed


def correct_guess(word, letters_guessed):
    temp_reveal = list(len(word) * "_")
    for i in letters_guessed:
        index = 0
        for j in word:
            if i == j:
                temp_reveal[index] = j
                index += 1
            else:
                index += 1

    return temp_reveal

#Welcome message and revealing the word

def game_intro():
    print("Welcome to Hangman, you have 6 lives and can only guess one letter at a time.")
    print("Good luck, the secret word is: ")
    word = pick_word()

    print(reveal(word))
    print("-------------------------------------------------------")

    return word


# Function for main game where user guesses 

def game(word):
    letters_guessed = []
    lives = 6

    while lives > 0:
        
        print("You haven't guessed these letters so far: {}".format(
               letters_left(letters_guessed)))
        user_guess = input("Please guess a letter: ").lower()

        #Check to make sure user hasn't guessed letter already
        if user_guess in letters_guessed:
            print("You already guessed that.")
            continue

       
        #Appending guess to list of guessed letters
        letters_guessed.append(user_guess)

        #Guess so far variable to display later
        guess_so_far = correct_guess(word, letters_guessed)

        
        #Conditional to see if letter guessed is correct
        if letter_checker(word, user_guess) == False:
            lives -= 1
            letters_guessed.append(user_guess)
            print("Unlucky, {} is not in the word. You have {} lives left".format(
                   user_guess, lives
                   ))  
            print(guess_so_far)             
            print("-------------------------------------------------------")
        else:
            #Prints for when user guesses a letter correctly
            print("Good guess!")

            #Checking to see if user has guessed whole word
            if guess_so_far == list(word):
                print(guess_so_far)
                print("Well done, you guessed correctly.")
                print("-------------------------------------------------------")
                return
            #When user guessed a letter but hasn't got the whole word
            else:
                print(guess_so_far)
                print("-------------------------------------------------------")

    
    #Closing message when user didn't guess correctly
    print("The word was: {}".format(word))


#Exit message to see if user wants to play again

def exit_message():
    play_again = input("Would you like to play again? y/n").lower()
    if play_again == "y":
        new_game = game_intro()
        game(new_game)
        exit_message()
    else:
        print("Thanks for playing.")


#Program start

if __name__ == "__main__":
    game(game_intro())
    exit_message()

