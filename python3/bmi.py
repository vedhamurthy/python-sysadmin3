#!/usr/bin/env python3.6

def gather_info():
    height = float(input("what is your height? (inches or meters) "))
    weight = float(input("what is your weight? (pounds or kilograms) "))
    system = input("Are you measurment in metric or imperial system? ").lower().strip()
    return (height, weight, system)

#ved = gather_info()
#print(ved)

def calculate_bmi(weight, height, system="matric"):
    if system == "matric":
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2))
    return bmi

while True:
    height, weight, system  = gather_info()
    #print(height, weight, system)
    if system.startswith("i"):
        bmi = calculate_bmi(weight, height, system="imperial")
        print(f"you BMI is {bmi}")
        break
    elif system.startswith("m"):
        bmi = calculate_bmi(weight, height, system="matric")
        print(f"you BMI is {bmi}")
        break
    else:
        print("Error: Unknown measurement system. Please use imperial or metric.")
#bmi = calculate_bmi(height, weight, system)

#print(bmi)

