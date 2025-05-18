def AddElementsAndReturnMin(number):
    ret = []
    for i in range(number):
        number = int(input("input ="))
        ret.append(number)
    
    min = ret[0]

    for i in ret:
        if(i < min):
            min = i
    return min

def main():
    number = int(input("Enter number of entries: "))
    print("Min number from list is : ",AddElementsAndReturnMin(number))

if __name__ == "__main__":
    main()