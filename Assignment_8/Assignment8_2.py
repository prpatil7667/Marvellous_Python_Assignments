import threading

def calculateEvenFactors(inputNumber):
     for i in range(2,inputNumber+1):
          if (((inputNumber % i) == 0) and (i % 2 == 0)):
               print(f"Even factor: {i}")
               
def calculateOddFactors(inputNumber):
     for i in range(2,inputNumber+1):
          if (((inputNumber % i) == 0) and (i % 2 != 0)):
               print(f"Odd factor: {i}")    

def main():
    T1 = threading.Thread(target = calculateEvenFactors, args=(10,))
    T2 = threading.Thread(target = calculateOddFactors, args=(10,))
    T1.start()
    T2.start()

if __name__ == "__main__":
    main()