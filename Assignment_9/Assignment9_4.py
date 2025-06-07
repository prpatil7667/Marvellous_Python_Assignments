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
    time_end1 = time.time()
    print(f"time took for normal call {time_end1 - time_start1}")

    time_start2 = time.time()
    threading.Thread(target=sumof1toN, args=(1000000,)).start()
    time_end2 = time.time()
    print(f"time took for threading call {time_end2 - time_start2}")

    time_start3 = time.time()
    multiprocessing.Process(target=sumof1toN, args=(1000000,)).start()
    time_end3 = time.time()
    print(f"time took for multiprocessing call {time_end3 - time_start3}")


if __name__ == "__main__":
    main()

