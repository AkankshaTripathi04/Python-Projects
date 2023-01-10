#in a hangman game you guess the letters that the word has if you get a correct char then that is put in its place then
import random
import words
import string

def valid_word(words):
    word = random.choice(words.words) #get the random word
    if '-' in word or ' ' in word: #if the word has space or hyyphenated then we get another word
      word = random.choice(words)

    return word.upper() #well play the game in upper case only

def hangman():
    word = valid_word(words) #correct word
    word_letters = set(word) #letters that we want
    alphabet = set(string.ascii_uppercase) #all characters
    used_letters = set()
    lives  = 6
    while len(word_letters) > 0 and lives > 0:
        print("You have these letters",' '.join(used_letters)) #adds the letters and the alphabets that have been used
        print(f"Lives : {lives}")
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list)) #prints the word
        #getting user input
        user_letters = input('Guess a letter: ').upper()  # inputting the character
        if user_letters in alphabet - used_letters:  # if the typed letter is valid and not used then
            used_letters.add(user_letters)
            if user_letters in word_letters:
                word_letters.remove(user_letters)
            else:
                lives -= 1
        elif user_letters in used_letters:
            print("Already in use!")
        else:
            print("Wrong input!")
    if lives == 0:
        print(f"Out of lives! The word was {word}")
    else:
        print(word)

hangman()