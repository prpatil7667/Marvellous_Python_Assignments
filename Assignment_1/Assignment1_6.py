
def ChkNum(num):

    if num > 0:
        print("Positive Number")
    elif num == 0:
        print("Zero")
    else:
        print("Negative Number")        


def main():
    print("This program will provide output on console whether the given number is positive or negative or zero")
    print("Plese enter the number :")
    num = int(input())
    ChkNum(num)

  
if __name__ == "__main__":
    main()