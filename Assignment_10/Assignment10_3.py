import functools

def main():
    inputList = []
    inputList = list(map(int, input("Enter space separated integers: ").split()))
    print("Input List:", inputList)

    filteredList = list(filter(lambda x: x >= 70 and x <= 90 , inputList))
    print("Filtered List:", filteredList)
    mappedList = list(map(lambda x: x + 10, filteredList))
    print("Mapped List (Increased Values):", mappedList)
    reducedValue = functools.reduce(lambda x, y: x * y, mappedList)
    print("Reduced Value (product of Mapped List):", reducedValue)

if __name__ == "__main__":
    main()

   