def sum(num1, num2):
    return num1 + num2


total = sum(2, 2)
print(total)  # 4

# ----------------------


def sum2(num1, num2):
    def another_func(num3, num4):
        return num3+num4
    return another_func


total2 = sum2(10, 12)
print(total2(10, 20))  # 30

# ----------------------


def sum3(num1, num2):
    def another_func(num3, num4):
        return num3+num4
    return another_func(num1, num2)


total3 = sum3(10, 12)
print(total3)  # 22
