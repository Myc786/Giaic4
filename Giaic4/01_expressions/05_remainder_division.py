def main():
    # get the number we want to divide 
    divident : int = int(input(" Enter the integer to be divided: "))
    divisor  : int = int(input("Enter the integer to divide by : "))

    quotient : int = divident // divisor
    remainder : int = divident % divisor

    print("The result of this division is " + str(quotient) + " With remainder " + str(remainder))


if __name__ == "__main__":
    main()   