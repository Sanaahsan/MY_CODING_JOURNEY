##Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.Based on a user's order, work out their final billSmall Pizza: $15Medium Pizza: $20Large Pizza: $25Pepperoni for Small Pizza: +$2Pepperoni for Medium or Large Pizza: +$3Extra cheese for any size pizza: + $1
print("Welcome to Python Pizza Deliveries!")
sime = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill=0
if sime=="S":
    bill+=15
elif sime=="M":
    bill+=20
elif sime =="L":
    bill+=25
else:
    bill+="0"
    
if  add_pepperoni =="Y":
    if sime =="S":
        bill +=2
    else:
        bill +=3    
if   extra_cheese=="Y":
    bill +=1                     
print(f"Your final bill is ${bill}")
