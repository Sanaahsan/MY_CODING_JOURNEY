#Treasure Game
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
path=input("left or right?")
if path== "right":
    print("Game Over.")
else:
     SW=input("swim or wait?") 
if  SW=="swim":
        print("Game Over")
else:
        door=input("Which door? Red , Blue or Yellow?")
if door== "Blue" or "Red":
    print("Game Over.")
else:
    print("You win.")    