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
game_images = [rock, paper, scissors]
user_choice = int(input("Type 0 for 'Rock',1 for 'Paper',2 for 'Scissors'\n "))
print(game_images[user_choice])
computer_choice = random.randint(0,2)
print(f"Computer choice is : {computer_choice}")
print(game_images[computer_choice])
if user_choice == 0 and computer_choice == 1:
    print("Computer wins")
elif user_choice == 1 and computer_choice == 0:
    print("user wins")
elif user_choice == 1 and computer_choice == 2:
    print("computer wins")
elif user_choice == 2 and computer_choice == 0:
    print("computer wins")
elif user_choice == 2 and computer_choice == 1:
    print("user wins")
elif user_choice == 0 and computer_choice == 2:
    print("user wins")
elif user_choice == 0 and computer_choice == 0:
    print("DRAW!")
else:
    print("Invalid choice! YOU LOST 'TRY AGAIN!'")





