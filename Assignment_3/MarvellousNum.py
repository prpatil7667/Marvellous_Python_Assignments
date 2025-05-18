def ChkPrime(num):
    for i in range(2, num):
        if (num % i) == 0:
            print("",num,": Not prime")
            return False
    print("",num,": Prime")
    return True