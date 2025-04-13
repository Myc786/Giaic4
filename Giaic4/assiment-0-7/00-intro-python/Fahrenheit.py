def main():
    Fahrenheit = float(input("\033[1m\033[3m Enter your Temprature in Fahrenheit : \033[0m"))
    Celsius = (Fahrenheit  - 32) * 5.0/9.0
    print (f"Temprature : {Fahrenheit}F = {Celsius}C")
if __name__ == "__main__":
    main()    