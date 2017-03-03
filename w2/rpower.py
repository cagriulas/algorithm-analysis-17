i = 0
def rpower(x, y):
    global i
    if(y == 0):
        i = i + 1
        return 1
    elif(y == 1):
        i = i + 1
        return x
    elif((y % 2) == 0):
        i = i + 1
        return rpower(x * x, y / 2)
    else:
        i = i + 1
        return rpower(x * x, y / 2)

print(rpower(2, 8), i)
