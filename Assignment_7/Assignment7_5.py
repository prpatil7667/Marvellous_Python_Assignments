from functools import reduce

def checkPalindrome(A,B):
    return A == B

def main():
    inputData = input("Enter string to check palindrome:")
    charlist = []
    for i in inputData:
        charlist.append(i)
    print("charlist: ", charlist)
    
    reverselist = []

    for i in range(len(charlist)-1,-1,-1):
        reverselist.append(charlist[i])

    if(checkPalindrome(charlist, reverselist)):
        print(f"{inputData} is a palnidrome")
    else:
        print(f"{inputData} is not a palnidrome")    


if __name__ == "__main__":
    main()