import threading
import multiprocessing
import time
    
def sumof1toN(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

def main():

    time_start1 = time.time()
    print(sumof1toN(1000000))
    time_start2 = time.time()
    print(f"time took for normal call {time_start2 - time_start1}")

if __name__ == "__main__":
    main()

