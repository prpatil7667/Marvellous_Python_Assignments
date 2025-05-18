def AddElementsAndReturnMax(number):
    ret = []
    for i in range(number):
        number = int(input("input ="))
        ret.append(number)
    
    max = ret[0]

    for i in ret:
        if(i > max):
            max = i
    return max

def main():
    number = int(input("Enter number of entries: "))
    print("Max number from list is : ",AddElementsAndReturnMax(number))

if __name__ == "__main__":
    main()