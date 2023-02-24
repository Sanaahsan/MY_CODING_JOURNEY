#Rock Paper Scissor Game
Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

Player_1=input("Rock, Paper or Scissors?")
Player_2=input("Rock , Paper or Scissors?")

if Player_1=="Rock" and Player_2=="Scissor":
    print(Rock+"Player_1 won!")
elif Player_1=="Scissor" and Player_2=="Rock":
    print(Rock+ "Player_1 won!")
elif Player_1=="Rock" and Player_2=="Paper":
    print(Paper+"Player_2 won!")
elif Player_1=="Paper" and Player_2=="Rock":
    print(Paper+ "Player_1 won!")
elif Player_1=="Paper" and Player_2=="Scissor":
    print(Scissor+ "Player_2 won!")
elif Player_1=="Scissor" and Player_2=="Paper":
    print(Scissor+ "Player_1 won!") 
else:
    print("Draw") 