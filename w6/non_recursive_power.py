def power(a, b):
    x = 1
    counter = 0
    while(b):
        if b%2 == 0:
            a = a*a
            b = b/2
        else:
            x = x*a
            b -= 1
        counter += 1
    print("total = ", counter, "\n")
    return x

print(power(5, 6))
