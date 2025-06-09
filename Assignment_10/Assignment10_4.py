import functools

def main():
    inputList = []
    inputList = list(map(int, input("Enter space separated integers: ").split()))
    print("Input List:", inputList)

    filteredList = list(filter(lambda x: x % 2 == 0 , inputList))
    print("Filtered List (Even Numbers):", filteredList)
    mappedList = list(map(lambda x: x**2, filteredList))
    print("Mapped List (squared Values):", mappedList)
    reducedValue = functools.reduce(lambda x, y: x + y, mappedList)
    print("Reduced Value (addition of Mapped List):", reducedValue)
    
if __name__ == "__main__":
    main()

   