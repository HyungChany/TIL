for _ in range(int(input())):         
    x = [0] * 11
    x[1] = 1
    x[2] = 2
    x[3] = 4

    for i in range(4, 11):
        x[i] = sum(x[i-3:i])

    print(x[int(input())])