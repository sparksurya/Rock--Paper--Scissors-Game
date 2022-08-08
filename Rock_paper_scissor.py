import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors ='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print(" Welcome to Rock paper scissors Game")
rock = '''ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors ='''SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
play=int(input("Enter 0 for rock, 1 for paper, 2 for scissors ?" ))
list=[(rock),(paper),(scissors)]
print(list[(play)])
bot_list =[(rock),(paper),(scissors)]
random=random.randint(0,2)
print(bot_list[(random)])
if play==0 and random ==0 :
    print("Tie")
if play==0 and random ==1 :
    print("You Loose")
if play==0 and random ==2 :
    print("You Win")
if play==1 and random ==1 :
    print("Tie")
if play==1 and random ==2 :
    print("You Loose")
if play==1 and random ==0 :
    print("You Win")
if play==2 and random ==2 :
    print("Tie")
if play==2 and random ==0 :
    print("You Loose")
if play==2 and random ==1 :
    print("You Win")
 #elif (list[(play)])==scissors and bot_list[(random)]==paper:
    #print("You Won")
