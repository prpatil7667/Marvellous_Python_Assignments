
def ChkNum(num):

    if num%2 == 0:
        print("Even number")
    else:
        print("Odd number")    


def main():
    print("This program will provide output on console whether the given number is even or odd")
    print("Plese enter the number :")
    num = int(input())
    ChkNum(num)

  
if __name__ == "__main__":
    main()