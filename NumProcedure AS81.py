numlist = [2,3,4,5132,6,3456,23,5,7,34,5,75,2,35,9]

def num_sum(numlist):
    sum = 0
    for num in numlist:
        sum += num
    print(sum)

def num_prod(numlist):
    prod = numlist[0]
    for num in range (1, len(numlist)):
        prod = prod * numlist[num]
    print(prod)
