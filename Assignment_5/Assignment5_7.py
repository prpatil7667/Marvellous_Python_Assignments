
def CalculateAreaAndPerimeterOfRectangle(length,width):
    area = length * width
    print("Area: ",area)
    perimeter = (length*2) + (width*2)
    print("Perimeter : ",perimeter)

def main():
    length = int(input("Enter length :"))
    width = int(input("Enter width :"))
    CalculateAreaAndPerimeterOfRectangle(length,width)

if __name__ == "__main__":
    main()