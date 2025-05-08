import time

def main():
    print("\n\033[01mWelcome to the countdown timer!\033[0m")
    while True:
        time_input = input("\n\033[01m\033[03mPlease enter the time in seconds:\033[0m ")
        if time_input.isdigit():
            time_input = int(time_input)
            break
        else:
            print("Please enter a valid number.")
    print("\nStarting countdown...")
    
    while time_input >= 0:
        mins, secs = divmod(time_input, 60)
        timeformat = f"{mins:02}:{secs:02}"
        print(timeformat, end='\r')
        time.sleep(1)
        time_input -= 1

    print("\n\n\033[01m\033[96mTime's up!\033[0m\n")

if __name__ == "__main__":
    main()