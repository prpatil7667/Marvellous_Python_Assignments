import MarvellousNum

def ListPrime(number):
    ret = []
    for i in range(number):
        number = int(input("input ="))
        ret.append(number)
    
    additionOfPrimeNumbers = 0

    for i in ret:
        if(MarvellousNum.ChkPrime(i) == True):
            additionOfPrimeNumbers = additionOfPrimeNumbers + i

    return additionOfPrimeNumbers

def main():
    number = int(input("Enter number of entries: "))
    print("Addition of prime numbers from list is : ",ListPrime(number))

if __name__ == "__main__":
    main()