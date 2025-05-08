import random

def who_wins(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "\n\033[93mIt's a Tie!\033[0m"
    
    if (user_choice == "r" and computer_choice == "s") or (user_choice == "p" and computer_choice == "r") or (user_choice == "s" and computer_choice == "p"):
        return "\n\033[92mYou Win!\033[0m"

    return "\n\033[91mYou Lose!\033[0m"

def main():
    print("\nWelcome to Rock, Paper, Scissors Game!\n")

    print("\033[01m\033[03mChoose 'q' for Quit.\033[0m")
    
    while True:
        user_choice = input("\n\033[01m\033[03mEnter your choice 'r' for rock, 'p' for paper, or 's' for scissors: \033[0m").lower()
        
        if user_choice == "q":
            print("\n\033[94m\033[01m\033[03mThanks for Playing!\033[0m\n")
            break

        if user_choice != "r" and user_choice != "p" and user_choice != "s":
            print("\033[93mPlease Enter a Valid Choice!\033[0m")
            continue
        
        computer_choice = random.choice(["r", "p", "s"])
        print(f"\nComputer's Choice: {computer_choice}")
        
        print(who_wins(user_choice, computer_choice))

if __name__ == '__main__':
    main()