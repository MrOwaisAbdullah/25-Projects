import random

def main():
    print("\nWelcome to the Password Generator!\n")

    while True:
        password_qty = input("\033[01m\033[03mHow many Passwords do you want: \033[0m")
        if password_qty.isdigit():
            password_qty = int(password_qty)
            break
        else:
            print("\033[93mPlease enter a valid number.\033[0m")

    while True:
        password_length = input("\033[01m\033[03mPlease enter the length of the password: \033[0m")
        if password_length.isdigit():
            password_length = int(password_length)
            break
        else:
            print("\033[93mPlease enter a valid number.\033[0m")
    
    print("\n\033[01mYour PasswordS:\033[0m\n")

    for i in range(password_qty):
        password = ""
        for _ in range(password_length):
            password += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()")
        print(f"\033[01m{i+1}.\033[0m {password}")
    
    print("\n\033[01m\033[96mPassword Generation Completed!\033[0m\n")

if __name__ == "__main__":
    main()