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

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# user choice
images=[rock, paper, scissors]
user_choice=input("What do you want to choos? 0 for rock,1 for paper, 2 for scissors!!")
user_choice = int(user_choice)
print(images[user_choice])

# computer choice

comp_choice = random.randint(0,1)
print("Computer Choice is:")
print(images[comp_choice])



if (user_choice==comp_choice):
    print("Sorry It's Draw!!")
elif (user_choice == 0 and comp_choice == 2) or (user_choice == 1 and comp_choice == 0) or (user_choice == 2 and comp_choice == 1):
    print("Congrat's You Win....😍😍")
else:
    print("Sorry!Computer Wins.....Better Luck Next Time..😔😔")
