import threading

def DisplayEven(threshold):
        counter = 1
        number = 2
        while counter <= threshold:
            if number % 2 == 0:
                print(f"Even: {number}")
                counter += 1
            number = number + 1

def DisplayOdd(threshold):
        counter = 1
        number = 2
        while counter <= threshold:
            if number % 2 != 0:
                print(f"Odd: {number}")
                counter += 1
            number = number + 1

def main():
    T1 = threading.Thread(target = DisplayEven, args=(10,))
    T2 = threading.Thread(target = DisplayOdd, args=(10,))
    T1.start()
    T2.start()

if __name__ == "__main__":
    main()