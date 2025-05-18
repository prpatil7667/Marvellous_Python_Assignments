from functools import reduce

def CheckPrime(no):
    for i in range(2, no):
        if (no % i) == 0:
            print("Number is not a prime")
            return False
    print("Number is prime")   
    return True


def mult(no):
    return no * 2

def maxNumbers(A,B):
    if(A>B):
        return A 
    else:
        return B


def main():

    inputList = []

    number = int(input("Number of entries:"))
    
    for i in range(number):
        inputList.append(int(input("input")))
    
    print(inputList)

    FData = list(filter(CheckPrime, inputList))
    print("FData: ", FData)

    MData = list(map(mult, FData))
    print("MData: ", MData)

    RData = reduce(maxNumbers, MData)
    print("RData: ", RData)

if __name__ == "__main__":
    main()