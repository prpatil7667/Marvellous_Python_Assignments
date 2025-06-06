import multiprocessing

def factorial(n):
    #Function to calculate the factorial of a number
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
def main():
    numberlist = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    result = []
    # Create a pool of processes
    p1 = multiprocessing.Pool()
        # Map the square function to the number_list
    result = p1.map(factorial, numberlist)
    print(result)
    p1.close  

if __name__ == "__main__":
    main()

