weight = float(input("input weight in kgs: "))
height = float(input("input height in metres: "))
BMI = weight/(height * height)
if BMI < 18.5:
    print(BMI)
    print("Underweight")
elif 25.0 > BMI >= 18.5:
    print(BMI)
    print("Normal")
elif 25.0 <= BMI < 30.0:
    print(BMI)
    print("Overweight")
elif 30 <= BMI:
    print(BMI)
    print("Obesity")
