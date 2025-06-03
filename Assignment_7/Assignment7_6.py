from functools import reduce

def checkPrime(no):
    for i in range(2, no):
        if (no % i) == 0:
            return False
    return True

def main():
    inputData = int(input("Enter number of elements:"))
    numberlist = []
    
    for i in range(inputData):
        numberlist.append(int(input()))

    print("numberlist: ", numberlist)
    print(list(filter(checkPrime,numberlist)))



if __name__ == "__main__":
    main()