
def Add(f, s):
    return f + s


def main():
    print("This program will perform the addition and provide out put on console")
  
    print("Plese enter the first number :")
    fNum = int(input())
    print("Plese enter the second number :")
    sNum = int(input())

    addition = Add(fNum, sNum)

    print("Addition of 2 numbers is:",addition)
  
if __name__ == "__main__":
    main()