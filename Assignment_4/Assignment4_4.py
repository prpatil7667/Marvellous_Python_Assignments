from functools import reduce

def CheckEven(no):
    return (no % 2 == 0)
   
def square(no):
    return no ** 2

def add(A,B):
    return A + B

def main():

    inputList = []

    number = int(input("Number of entries:"))
    
    for i in range(number):
        inputList.append(int(input("input")))
    
    print(inputList)

    FData = list(filter(CheckEven, inputList))
    print("FData: ", FData)

    MData = list(map(square, FData))
    print("MData: ", MData)

    RData = reduce(add, MData)
    print("RData: ", RData)

if __name__ == "__main__":
    main()