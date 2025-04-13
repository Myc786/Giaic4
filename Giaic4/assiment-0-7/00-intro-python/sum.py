"""
Add two Numbers program 
"""

def main():
    print("Add Two numbers For Sum : ")
    num1 : str = input("Enter your first Number : ")
    num1 : int = int(num1)
    num2 : str = input("Enter Your second Number : ")
    num2 : int = int(num2)
    total : int = num1 + num2
    print("the sum of two numbers is : " + str(total) + " .")
if __name__ == '__main__':
    main()    