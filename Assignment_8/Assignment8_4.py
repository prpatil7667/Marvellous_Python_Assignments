import threading

def identifysmallCount(inputString):
    count = 0
    for i in list(inputString):
        if i.isalpha() and i.islower():
            count += 1
    print("Small case: ",count)

def identifyCapitalCount(inputString):
    count = 0
    for i in list(inputString):
        if i.isalpha() and i.isupper():
            count += 1
    print("Capital case: ",count)

def identifyDigitCount(inputString):
    count = 0
    for i in list(inputString):
        if i.isdigit():
            count += 1
    print("DIgit: ",count)    

def main():
    inputString = "12345XYZTuz"
    print(inputString)
    smallThread = threading.Thread(target = identifysmallCount, args=(inputString,))
    capitalThread = threading.Thread(target = identifyCapitalCount, args=(inputString,))
    digitThread = threading.Thread(target = identifyDigitCount, args=(inputString,))
    smallThread.start()
    capitalThread.start()
    digitThread.start()
    print(f"smallThread_id: {smallThread.ident}, capitalThread_id: {capitalThread.ident}, digitThread_id: {digitThread.ident}")
    print(f"smallThread_name: {smallThread.name}, capitalThread_name: {capitalThread.name}, digitThread_name: {digitThread.name}")

if __name__ == "__main__":
    main()