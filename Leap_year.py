#Write a program that works out whether if a given year is a leap year
Year=int(input("Which year do you want to check? "))
if Year% 4==0:
    print("Leap year.")
elif Year% 100== 0:
    print("Not leap year.")
elif Year%400==0:
    print("Leap year.")   
else:
    print("Not leap year")        