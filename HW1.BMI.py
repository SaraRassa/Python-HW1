W=float(input("Enter your weight(kg): "))
H=float(input("Enter your height(m): "))
if H>3:
    print("you have entered your height in cm")
    print("the program converts your height to m")
    H=H/100
BMI= W/H**2

if BMI<18.5:
    print("BMI= ", round(BMI), "You are underweight")
if BMI>18.5 and BMI<24.9:
    print("BMI= ", round(BMI), "Your weight is normal")
if BMI>25 and BMI<29.9:
    print("BMI= ", round(BMI), "You are overweight")
if BMI>35:
    print("BMI= ", round(BMI), "You are EXTREMELY obese")

