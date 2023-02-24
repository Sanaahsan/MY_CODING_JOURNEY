print("123"+"456")
print("Hello World")
#Day 1 part 1
print("Sana\nSana")

print("Sana"+ " "+"Ahsan")

input("What is your name?")

print('Hello '+ input ("What is your name?"))

print(len(input("What is your name?")))

age=input("How old are you?")
print(age)

name=input("Who is your friend")
length=len(name)
print (length)

#1st Project
print("Welcome to the Band Name Generator.")
name=(input("What's the name of your city you grew up in?\n"))
pet=(input("What's your pet's name?\n"))
print("Your band name could be " +  name +" "+ pet)

#Day 2
print("Hello"[3])
print("123"+"456")
print(123+456)

num=input("What is your name?")
print(type(num))

num1=len(input("What is your name?"))
new_num=str(num1)
print("Your name has " + new_num+" characters.")

two_digit_number = input("Type a two digit number: ")

#diff result
print(int(8/3))
print(round(8/3))
print(8//3)
print(8/3)

#f-string
score=20
height=5.7
isWinning=True
print(f"your score is {score},your height is {height},you are winning{isWinning}")

#Day 3
print("Welcome to the rollercoaster")
height=int(input("What is your height in cm?"))
if height>=120:
    print("You can ride")
else:
    print("Sorry! You cannot ride")

#Day 3
#check it
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])

##Day 5
#LOOP
fruits=["Apple" ,"Peach" ,"Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit +"pie")