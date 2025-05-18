def AddElementsAndReturnAddition(number):
    ret = []
    addition = 0
    for i in range(number):
        number = int(input("input ="))
        ret.append(number)
    
    for i in ret:
        addition = addition + i

    print(ret)    
    return addition

def main():
    number = int(input("Enter number of entries: "))
    print("Addition of all elements from list is : ",AddElementsAndReturnAddition(number))

if __name__ == "__main__":
    main()