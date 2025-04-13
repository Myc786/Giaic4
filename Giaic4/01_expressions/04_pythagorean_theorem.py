import math  # import math library so we can use sqrt function

def main():
    # get the two side length from user and cast them to be  two numbers 
    ab : float = float(input("Enter the length of Ab : "))
    ac : float = float(input(" Enter the length of AC : "))

    # Calculate the hypotenuse using the two sides and print it out

    bc : float = math.sqrt(ab**2 + ac**2)
    print("The length of bc (hypotenuse) is : " +str(bc))


if __name__ == "__main__":
    main()