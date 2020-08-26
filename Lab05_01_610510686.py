def dec_to_bi():
    n = int(input("Input N: "))
    res = ""
    while (n != 0):
        res = str(n % 2) + res
        n //= 2
    print("Equal to binary number:",res)

dec_to_bi()