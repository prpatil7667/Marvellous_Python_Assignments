def voterEligibilityCheck(age):
    return ( age>=18 )

def main():
    print("Voter Eligibility Checker")
    inputAge = int(input("Enter age: "))

    if voterEligibilityCheck(inputAge):
        print("Eligible for Voting" )
    else:
        print("Not Eligible for Voting" )
if __name__ == "__main__":
    main()