import random

def main(x):
    secret_number = random.randint(1, x)
    
    print(f"\nI am thinking of a number between 1 and {x}...")
    
    while True:
        guess = input("\n\033[01m\033[03mEnter a guess: \033[0m")
        if guess.isdigit():
            guess = int(guess)
            if guess < 1 or guess > 99:
                print("\033[93mPlease Enter a Valid Number!\033[0m") 
            else:
                break
        else:
            print("\033[93mPlease Enter a Valid Number!\033[0m") 

    while guess != secret_number:
        if guess < secret_number: 
            print("Your guess is too low")
        else:
            print("Your guess is too high")
            
        while True:
            guess = input("\n\033[01m\033[03mEnter a guess: \033[0m")
            if guess.isdigit():
                guess = int(guess)
                if guess < 1 or guess > 99:
                    print("\033[93mPlease Enter a Valid Number!\033[0m")
                else:
                    break
            else:
                print("\033[93mPlease Enter a Valid Number!\033[0m") 
        
    print(f"\n\033[92m\033[1mCongrats! The number was: {str(secret_number)}\n\033[0m")
    
if __name__ == '__main__':
    main(99)