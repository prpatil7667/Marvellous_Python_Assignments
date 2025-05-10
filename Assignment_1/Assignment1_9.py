
def printStars(num):
    for i in range(2, (num*2)+1, 2):
        print(i, end=" ")
    print()


def main():
    print("This program will provide output the the first n even numbers")
    print("Plese enter the number :")
    num = int(input())
    printStars(num)
  
if __name__ == "__main__":
    main()