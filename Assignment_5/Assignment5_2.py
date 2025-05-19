
def main():
    print("Vowel or Consonent Check")
    vowelList = ["a", "e", "i" , "o" , "u"]
    inputStr = input("Enter char: ")
    if inputStr in vowelList:
        print("input :",inputStr," is a vowel" )
    else:
        print("input :",inputStr," is a consonent" )
if __name__ == "__main__":
    main()