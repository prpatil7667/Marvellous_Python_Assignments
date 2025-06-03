
def main():
   number = 5
   inputArray = []
   print('Enter 5 numbers')
   for i in range(5):
      inputArray.append(int(input()))
   print(inputArray)   
   largest = inputArray[0]
   for i in inputArray:
      if i > largest:
         largest = i

   print("Maximum number is: ",largest)

        
if __name__ == "__main__":
    main()