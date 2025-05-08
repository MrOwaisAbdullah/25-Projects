def main():
    adjective_1: str = input("\033[3mPlease type an adjective and press enter: \033[0m")
    noun_1: str = input("\033[3mPlease type a noun and press enter: \033[0m")
    verb_1: str = input("\033[3mPlease type a verb and press enter: \033[0m")
    noun_2: str = input("\033[3mPlease type a noun and press enter: \033[0m")
    adjective_2: str = input("\033[3mPlease type an adjective and press enter: \033[0m")
    noun_3: str = input("\033[3mPlease type a noun and press enter: \033[0m")
    noun_4: str = input("\033[3mPlease type a noun and press enter: \033[0m")
    verb_2: str = input("\033[3mPlease type a verb and press enter: \033[0m")
    noun_5: str = input("\033[3mPlease type a noun and press enter: \033[0m")
    adjective_3: str = input("\033[3mPlease type an adjective and press enter: \033[0m")
    noun_6: str = input("\033[3mPlease type a noun and press enter: \033[0m")

    madlib: str = f"The other day, I saw a/an {noun_1} in the street. It was very {adjective_1} and it started to {verb_1}. I quickly grabbed my {noun_2} and ran away. It was a very {adjective_2} {noun_3}. When I got home, I told my {noun_4} what had {verb_2} and they gave me a {noun_5}. It was a very {adjective_3} {noun_6}."

    print(f"\n{madlib}\n")

if __name__ == '__main__':
    main()