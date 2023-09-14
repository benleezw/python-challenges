# exercise 1

val = 129
ringgit = f"RM{val:.2f}"
print(ringgit)

# exercise 2

col1 = [1, 345.2345870, 1239871]
col2 = [456, 3, 1435.2348756]
col3 = [72, 9, 2.2319786872354]

print("\nthis is a header")
print()
for i in range (0, len(col1)):
    print(f"{col1[i]:^15.2f} {col2[i]:^15.2f} {col3[i]:^15.2f}")

# ^15 for centered
# >15 for right justify
# <15 for left justify
# .2f for two decimal place


# exercise 3

binary = f"{int(val):b}"
print(f"\n{binary}")
hex = f"{int(val):x}"
print(hex)



