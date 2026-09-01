print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("You will pay 5 dollars")
    elif age <= 18:
        bill = 10
        print("You will pay 10 dollars")
    elif age <= 22:
        bill = 15
        print("You will pay 15 dollars")
    else:
        bill = 20
        print("You will pay 20 dollars")
    picture = input("you will be chagared 3 dollar for a picture! Press y for Yes and n for No: ")
    if picture == "y":
        bill += 3
        print(f"your final bill is: {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")

