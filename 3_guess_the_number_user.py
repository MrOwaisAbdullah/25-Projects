import random

def main(x):    
    print(f"\nPlease Guess a number between 1 and {x}...")
    low = 1
    high = x
    feedback = ''

    while True:
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"\n\033[01m\033[03mIs {guess} is too high(h), too low(l) or correct(c): \033[0m")
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        elif feedback == "c":
            break
        else:
            print("\033[93mPlease Enter a Valid Input!\033[0m")
        if low == high:
            guess = low
            break

        
    print(f"\n\033[92m\033[1mComputer Guessed the correct number, The number was: {str(guess)}\n\033[0m")
    
if __name__ == '__main__':
    main(99)