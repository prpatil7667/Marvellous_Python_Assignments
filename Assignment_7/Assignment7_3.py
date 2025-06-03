def checkEven(no):
    return (no%2==0)

def main():
    number = int(input("Enter number of elements:"))
    numberList = []
    for i in range(number):
        numberList.append(int(input()))
    print("numberlist", numberList)

    filteredList = list(filter(checkEven,numberList))
    print(filteredList)

if __name__ == "__main__":
    main()