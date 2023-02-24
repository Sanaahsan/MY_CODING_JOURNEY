#You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.Important: You are not allowed to use the choice() function.

import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
list_items=len(names)
select=random.randint(0,list_items-1)
person_who_will_pay=names[select]
print(person_who_will_pay + " is going to buy the meal today!")