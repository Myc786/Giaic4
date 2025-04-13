"""
Feet to inches conversion
"""

INCHES_IN_FEET :int = 12  # there are 12 inches in A feet  

def main():
    feet : float = float(input("Enter Number of feet : ")) # get the number of feet
    inches : float = feet * INCHES_IN_FEET # Perform the Conversion
    print("This is ", inches , "inches")

if __name__ == "__main__":
    main()    