
def main():
    no = int(input("Please enter number"))
    for i in range(no):
        for j in range(no):
            print("* ", end=" " )
        print()

if __name__ == "__main__":
    main()