
def main():
    no = int(input("Please enter number"))

    for i in range(no):
        for j in range(1,no+1):
            print(j, end=" " )
        print()

        
if __name__ == "__main__":
    main()