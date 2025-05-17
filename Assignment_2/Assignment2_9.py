
def main():
    no = int(input("Please enter number: "))
    count = 0

    while no > 0:
        no //= 10
        count = count + 1

    print("Digits are :", count)

if __name__ == "__main__":
    main()