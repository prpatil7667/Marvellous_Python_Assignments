from functools import reduce

def product(A,B):
    return A * B

def main():
    number = int(input("Enter number of elements:"))
    numberList = []
    for i in range(number):
        numberList.append(int(input()))
    print("numberlist", numberList)

    answer = reduce(product,numberList)
    print(answer)

if __name__ == "__main__":
    main()