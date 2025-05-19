def EvenOddNumberCheck(num):
    if(num % 2 == 0):
        print("",num ," is an Even number")
    else:
        print("",num ," is an Odd number")
        


def main():
    number = int(input("Enter number: "))
    EvenOddNumberCheck(number)


if __name__ == "__main__":
    main()