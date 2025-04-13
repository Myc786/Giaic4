SENTENCE_START_FROM : str = "Panaversity is fun. I learned to program and used Python to make my "

def main():
    # get the input from user 
    adjective : str = str(input("Enter the adjective and press the Enter button.  "))
    noun : str = str(input(" Enter the noun and press the Enter button "))
    verb: str =str(input("Enter the verb and press the Enter button"))
    print(SENTENCE_START_FROM + adjective + "" + noun + " " + verb + "!")

if __name__ == "__main__":
    main()    