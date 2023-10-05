# 1st input : enter height in meters e.g: 1.65
print("Welcome to BMI Calculator App.")
print("Enter you height in meter : ")
height = float(input())
# 2nd input : enter weight in kilograms e.g: 72
print("Enter you weight in kg: ")
weight = float(input())
# Don't change the code above
# Write your code below this line
# Note: BMI - weight(kg)/height*height(m*m)


def bmi():
    bmi_value = weight/(height*height)
    print(f"your BMI is : {bmi_value}")


bmi()
