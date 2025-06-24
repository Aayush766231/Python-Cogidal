height = float(input("What is your height? "))
weight = float(input("What is your weight? "))
bmi = weight/(height/100)**2
print(bmi)

if bmi <= 18.4:
    print("You are underweight")
elif bmi <= 24.9:
    print("You are healthy")
elif bmi <= 29.9:
    print("You are overweight")
elif bmi <=34.9:
    print("You are severely overweight")
elif bmi <= 39.9:
    print("You are obese")
else:
    print("You are severely obese")