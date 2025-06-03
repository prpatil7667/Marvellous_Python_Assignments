square = lambda num : num**2
cube = lambda num : num**3

def main():
    number = int(input("Enter number"))
    print("square: ", square(number))
    print("Cube: ", cube(number))
    
if __name__ == "__main__":
    main()