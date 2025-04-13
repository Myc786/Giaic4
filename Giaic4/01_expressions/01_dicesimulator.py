import random

NUM_SIDES = 6

def main():
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print(f" Die 1 is : {die1}, Die 2 is {die2}, Total : {total} ")

def roll_dice():
    die1 : int = 10
    print(f"die1 is  main()  start as {die1} ")
    for _ in range(3):
       roll_dice()

       print(f" Die1 in main() start as {die1}")
if __name__ == "__main__":
    main()       
         