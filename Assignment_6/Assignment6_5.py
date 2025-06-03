def CheckPrime(no):
    for i in range(2, no):
        if (no % i) == 0:
            return False
    return True

def main():
    number = int(input("Enter number :"))
    if(CheckPrime(number)):
        print("",number , " is a prime number")
    else:
        print("",number , " is not a prime number")
if __name__ == "__main__":
    main()