def CelsiusToFahrenheit(cel):
    return (cel *9/5) + 32
           
def main():
    cel = int(input("Enter temperature in Celcius: "))
    print("Temperature in Fahrenheit is : ", CelsiusToFahrenheit(cel),"°F")

if __name__ == "__main__":
    main()