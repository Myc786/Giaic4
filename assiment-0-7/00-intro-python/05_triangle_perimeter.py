def main():
    Side1 = float(input("\033[1m\033[3m Enter the length of side 1 : \033[0m"))
    Side2 = float(input("\033[1m\033[3m Enter the length of side 2 : \033[0m"))
    Side3 = float(input("\033[1m\033[3m Enter the length of side 3 : \033[0m"))
    Perimeter = Side1 + Side2 + Side3

    print(f"The perimeter of the triangle is {Perimeter} ")
if __name__ == "__main__":
    main()    
    