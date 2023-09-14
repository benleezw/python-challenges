# MyString = "abcdef"
# print(MyString)
# print(MyString[0:3])
# print(MyString[3::])
# print(MyString[0:6:2])
# print(MyString[-1:-7:-1])
# print(MyString[0:-2])

MyString = "1234567890"
print(MyString)
print(MyString[::-1]) # reverses string
# outputs 0987654321
print(MyString[:-2:]) # prints every char until position (middle int)
# outputs 12345678
print(MyString[:5:])
# outputs 12345
print(MyString[::3]) # prints every (third int) characters
# outputs 1470
print(MyString[::4])
# outputs 159
print(MyString[2:5:])
# outputs 345
