import Arithmetic
def main():
    no = int(input("Please enter number"))
    output = 1
    for i in range(no,1,-1):
        output = output * i
    print("Factorial is :", output)    

if __name__ == "__main__":
    main()