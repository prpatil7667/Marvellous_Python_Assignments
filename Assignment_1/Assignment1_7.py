
def ChkNumIfDivisibleBy5(num):

    if num % 5 == 0:
        return True
    else:
        return False


def main():
    print("This program will provide output on console whether the given number is divisible by 5")
    print("Plese enter the number :")
    num = int(input())
    output = ChkNumIfDivisibleBy5(num)
    print(output)
  
if __name__ == "__main__":
    main()