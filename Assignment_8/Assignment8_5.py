import threading

def printOneToFifty():
    for i in range(1, 51):
        print(i)

def printFiftyToOne():
    for i in range(50, 0, -1):
        print(i)

def main():
    thread1 = threading.Thread(target = printOneToFifty)
    thread2 = threading.Thread(target = printFiftyToOne)
    thread1.start()
    thread1.join()  # Ensure thread1 completes before starting thread2
    thread2.start()
   
if __name__ == "__main__":
    main()