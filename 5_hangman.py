import random
from words import words
import string

def get_valid_word(words_list):
    word = random.choice(words_list)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def main():
    print("\n\033[1mWelcome to Hangman Game!\n\033[0m")
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    lives = 8
    
    while len(word_letters) > 0 and lives > 0:
        print(f"\nYou have \033[1m{lives}\033[0m lives left and you have used these letters: {' '.join(used_letters)}")
        
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("\nCurrent Word: ", ' '.join(word_list))
        
        user_letter = input("\nEnter a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print(f"\nYour letter \033[93m\033[1m{user_letter}\033[0m is not in the word.")
        elif user_letter in used_letters:
            print("\n\033[93mYou have already used that character. Please try again.\033[0m")
        else:
            print("\n\033[93mInvalid character. Please try again.\033[0m")
    
    if lives == 0:
        print(f"\n\033[91mYou died, sorry. The word was: \033[1m{word}\033[0m\n")
    else:
        print(f"\n\033[92mCongratulations! You guessed the word: \033[1m{word}\033[0m\n")

if __name__ == '__main__':
    main()