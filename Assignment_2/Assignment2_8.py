
def main():
    no = int(input("Please enter number"))
    outer = no
    inner = 1
    for i in range(outer):
        for j in range(inner):
            print("* ", end=" " )
        print()
        inner = inner + 1
        
if __name__ == "__main__":
    main()