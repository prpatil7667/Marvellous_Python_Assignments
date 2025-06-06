import multiprocessing
    
def square(n, result):
    result.append(n * n)

def main():
    numberlist = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    result = multiprocessing.Manager().list()  # Use a Manager to create a shared list
    for i in numberlist:    
        process = multiprocessing.Process(target=square, args=(i,result))  # Start a new process for each number
        process.start()  # Start the process
        process.join()  # Wait for the process to finish

    print(result)

if __name__ == "__main__":
    main()

