def factorial(number):
    fact = 1
    for i in range(1,number+1):
        fact = fact * i
    return fact

def main():
    number = int(input("Enter number :"))
    print("Factorial of", number, "is", factorial(number))

if __name__ == "__main__":
    main()