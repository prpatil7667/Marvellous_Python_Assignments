from functools import reduce

def numberCheck(no):
    if(no >= 70 and no <= 90):
        print("condition match for : ",no)
        return True
    else:
        print("condition not matched for : ",no)
        return False

def increase(no):
    return no + 10

def mult(A,B):
    return A * B

def main():

    inputList = []

    number = int(input("Number of entries:"))
    
    for i in range(number):
        inputList.append(int(input("input")))
    
    print(inputList)

    FData = list(filter(numberCheck, inputList))
    print("FData: ", FData)

    MData = list(map(increase, FData))
    print("MData: ", MData)

    RData = reduce(mult, MData)
    print("RData: ", RData)

if __name__ == "__main__":
    main()