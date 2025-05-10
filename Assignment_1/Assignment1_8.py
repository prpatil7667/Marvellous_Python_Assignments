
def printStars(num):
    star = "*"
    for i in range(num):
        print(star, end=" ")
    print()


def main():
    print("This program will provide output the * on console based on inputs provided")
    print("Plese enter the number :")
    num = int(input())
    printStars(num)
  
if __name__ == "__main__":
    main()