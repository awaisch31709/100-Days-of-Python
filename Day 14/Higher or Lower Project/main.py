from game_data import data
from art import logo,vs
import random

print(logo)

Compare_A = random.choice(data)
Against_B = random.choice(data)

while Against_B == Compare_A:
    Against_B = random.choice(data)


score = 0
resume_game = True


while resume_game:
    print(f"Compare A: {Compare_A['name']} ,a {Compare_A['description']} from {Compare_A['country']}")
    print(vs)
    print(f"Against B: {Against_B['name']} ,a {Against_B['description']} from {Against_B['country']}\n")

    followers = input("Who has more Followers? Type 'A' or 'B': ").lower()
    if followers == 'a':
        if Compare_A['follower_count'] > Against_B['follower_count']:
            score += 1
            print(f"You Are Right,Current Score is : {score}")
            Compare_A = Against_B
            Against_B = random.choice(data)
            print('\n' * 20)
            while Against_B == Compare_A:
                Against_B = random.choice(data)
        else:
            print(f"That's Wrong, Your Final score is {score}")
            resume_game = False

    elif followers == 'b':
        if Against_B['follower_count'] > Compare_A['follower_count']:
            score += 1
            print(f"You Are Right,Current Score is : {score}")
            Compare_A = Against_B
            Against_B = random.choice(data)
            print('\n' * 20)
            while Against_B == Compare_A:
                Against_B = random.choice(data)
        else:
            print(f"That's Wrong, Your Final score is {score}")
            resume_game = False

# Compare_A = random.choice(game_data.data)
# # print(f"Compare_A: data[name], a data[description] from data[country]."
# for info in data:
#     # data["name"],data["description"],data["country"]
#     Compare_A = random.choice(data)
#     print(f"{data[0]}")


# Against_B = random.choice(game_data.data)