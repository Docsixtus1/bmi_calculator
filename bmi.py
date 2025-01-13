def check_bmi():
    weight=float(input("enter your weight in kilograms:"))
    height=float(input("enter your height in meters:"))
    bmi=weight/height**2
    if bmi<=18.5:
        print("underweight")
    elif 18.5<=bmi<24.9:
        print("normal weight")
    elif 25<=bmi<29.9:
        print("overweight")
    elif bmi >=30:
        print("obese")
    print(bmi)
check_bmi()
