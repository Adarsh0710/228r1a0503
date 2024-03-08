def greatest_of_two(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Both numbers are equal"
number1 = 10
number2 = 20
print("The greatest number is:", greatest_of_two(number1, number2))
