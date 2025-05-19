
def Mult(first,second):
    result = first*second
    return result

def Add(first,second):
    result = first+second
    return result

def Sub(first,second):
    result = first - second
    return result

def Div(first,second):
    result = first / second
    return result

def main():
    print("Arithmetic program which will perform Add, sub, mult, divide operation for provided parameters...")
    firstNo = int(input("Please enter first number"))
    secondNo = int(input("Please enter second number"))

    print("Addition is : ", Add(firstNo, secondNo))
    print("Multiplication is : ", Mult(firstNo, secondNo))
    print("Substraction is : ", Sub(firstNo, secondNo))
    print("division is : ", Div(firstNo, secondNo))


if __name__ == "__main__":
    main()