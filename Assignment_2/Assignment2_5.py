import Arithmetic
def main():
    no = int(input("Please enter number"))   
    for i in range(2, no):
        if (no % i) == 0:
            print("Number is not a prime")
            return
    print("number is prime")   
if __name__ == "__main__":
    main()