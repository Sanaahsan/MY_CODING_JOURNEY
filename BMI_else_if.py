#Write a program that interprets the Body Mass Index (BMI) based on a user's weight and heigh.It should tell them the interpretation of their BMI based on the BMI value.Under 18.they are underweight.Over 18.5 but below 25 they have a normal weight.Over 25 but below 30 they are slightly overweight.Over 30 but below 35 they are obese.Above 35 they are clinically obese. 

 height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
BMI=round(weight/(height**2))
if BMI<18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif  25>BMI:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif 30>BMI:
    print(f"Your BMI is {BMI}, you are slightly overweight.") 
elif 35>BMI :
    print(f"Your BMI is {BMI}, you are obese.")     
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")
