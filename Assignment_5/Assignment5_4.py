def LargestNumberfromThreenumbers(firstNo, secondNo, thirdNo):
    if (firstNo > secondNo):
        if(firstNo > thirdNo):
            return firstNo
        else:
            return thirdNo
    else:
        if(secondNo > thirdNo):
            return secondNo
        else:
            return thirdNo

def main():
   
    firstNo = int(input("firstNo: "))
    secondNo = int(input("secondNo: "))
    thirdNo = int(input("thirdNo: "))
    
    print("Largest number among 3 is :",LargestNumberfromThreenumbers(firstNo, secondNo, thirdNo))


if __name__ == "__main__":
    main()