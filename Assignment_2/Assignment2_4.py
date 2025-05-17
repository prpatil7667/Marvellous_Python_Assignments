import Arithmetic
def main():
    no = int(input("Please enter number"))
    output = 0
    for i in range(1,no):
        if (no % i) == 0:
            output = output + i
    print("Addition of factors is :", output)

if __name__ == "__main__":
    main()