
def main():
    no = int(input("Please enter number: "))
    count = 0

    while no > 0:
        count = count + no % 10
        no //= 10
        print(no)

    print("Digits are :", count)

if __name__ == "__main__":
    main()