w = float(input("Enter your weight in kg"))
h = float(input("Enter your height in cm"))

r = w / (h / 100)**2
print(f"your BMI is {r}")

if r <= 18.4:
    print("You are underweight.")
elif r <= 24.9:
    print("You are healthy.")
elif r <=29.9:
    print("You are over weight.")
elif r <= 34.9:
    print("You are severely over weight.")
elif r <= 39.9:
    print("you are obese.")
else:
    print("You are severely obese.")
