def triangle(row):
    k = 0
    for i in range(1, row+1):
        for space in range(1, (row-i)+1):
            print(end="  ")
        while k != (2*i-1):
            print("* ", end="")
            k = k + 1
        k = 0
        print()