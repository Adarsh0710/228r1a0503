def greatest_of_three(a, b, c):
    if a >= b:
        if a >= c:
            return a
        else:
            return c
    else:
        if b >= c:
            return b
        else:
            return c

num1 = 10
num2 = 25
num3 = 15
print(greatest_of_three(num1, num2, num3))
