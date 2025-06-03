def increase(no):
    return no+1

def main():
    number = int(input("Enter number of elements:"))
    numberList = []
    for i in range(number):
        numberList.append(int(input()))
    print("numberlist", numberList)

    incrementedList = list(map(increase,numberList))
    print(incrementedList)

if __name__ == "__main__":
    main()