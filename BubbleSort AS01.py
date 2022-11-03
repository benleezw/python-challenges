array = [8, 4, 3, 5, 7, 6, 1, 2, 9, 0]
MaxIndex = len(array)
n = MaxIndex - 2
r = 0
i = 0
while r <= MaxIndex - 1:
    while i <= n:
        if array[i] > array[i + 1]:
            temp = array[i]
            array[i] = array[i + 1]
            array[i + 1] = temp
            i = i + 1
        else:
            i = i + 1
    r = r + 1
    i = 0

