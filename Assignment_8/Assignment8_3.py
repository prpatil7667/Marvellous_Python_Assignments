import threading

sum = lambda A, B : A + B

def reduceXEven(Task, values):
    result = 0 
    for i in values:
        if i% 2 == 0:
             result = Task(result, i)
    print("Even numbers sum: ", result)         
    return result

def reduceXOdd(Task, values):
    result = 0 
    for i in values:
        if i% 2 != 0:
             result = Task(result, i)
    print("Odd numbers sum: ",result)         
    return result

def main():
    
    inputList =  input("Enter number elements seperated by spaces : ").split()
    inputList = list(map(int,inputList)) 
    print(inputList)
    T1 = threading.Thread(target = reduceXEven, args=(sum,inputList))
    T2 = threading.Thread(target = reduceXOdd, args=(sum,inputList))
    T1.start()
    T2.start()

if __name__ == "__main__":
    main()