def MultiplicationTable(number):
     for i in range(1, 11):
        print(i*number)

def main():
    number = int(input("Enter number :"))
    MultiplicationTable(number)

if __name__ == "__main__":
    main()