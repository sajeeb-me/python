def sum(num1, num2, num3=0):
    return num1+num2+num3

print(sum(10,2))


def all_sum(num1, *numbers):
    for num in numbers:
        print(num)

total = all_sum(20, 30, 40)
print("all sum: ", total)