import Arithmetic
def main():
    print("Arithmetic program which will perform Add, sub, mult,divide operation for provided parameters...")
    firstNo = int(input("Please enter first number"))
    secondNo = int(input("Please enter second number"))

    print("Addition is : ", Arithmetic.Add(firstNo, secondNo))
    print("Multiplication is : ", Arithmetic.Mult(firstNo, secondNo))
    print("Substraction is : ", Arithmetic.Sub(firstNo, secondNo))
    print("division is : ", Arithmetic.Div(firstNo, secondNo))


if __name__ == "__main__":
    main()