def sumDigits(num):
    digits = []
    sum = 0
    for i in range (0, len(str(num))):
        digits.append(int(str(num)[i]))
    for r in range (0, len(digits)):
        sum += digits[r]
    return sum

num = int(input("Enter a number: "))
print(sumDigits(num))
