def AddElementsAndReturnAddition(number):
    ret = []
    for i in range(number):
        number = int(input("input ="))
        ret.append(number)
    occurance = 0
    elementToSearch = int(input("Element occurances to search :"))
     
    for i in ret:
        if(i == elementToSearch):
            occurance = occurance +1
    return occurance

def main():
    number = int(input("Enter number of entries: "))
    print("occurance from list is : ",AddElementsAndReturnAddition(number))

if __name__ == "__main__":
    main()