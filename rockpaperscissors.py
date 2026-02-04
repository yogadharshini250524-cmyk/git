rock="""    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""
paper="""    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)"""
scissors="""    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""
print("welcome to play rock paper scissors")
user_choice=int(input("what do you choose? type 0 for rock, 1 for paper or 2 for scissors.\n"))
import random
computer_choice=random.randint(0,2)
if user_choice>=3 or user_choice<0:
    print("you typed an invalid number, you lose!")
else:
    print("you chose:")
    if user_choice==0:
        print(rock)
    elif user_choice==1:
        print(paper)
    else:
        print(scissors)
    print("computer chose:")
    if computer_choice==0:
        print(rock)
    elif computer_choice==1:
        print(paper)
    else:
        print(scissors)
    if user_choice==0 and computer_choice==2:
        print("you win!")
    elif computer_choice==0 and user_choice==2:
        print("you lose")
    elif computer_choice>user_choice:
        print("you lose")
    elif user_choice>computer_choice:
        print("you win!")
    elif computer_choice==user_choice:
        print("it's a draw")