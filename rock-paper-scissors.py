import random

user_win=0
computer_win=0

options = ["rock","paper","scissors"]

while True:
    user_choice=input("Enter rock/paper/scissors or q to quit the game ").lower()
    if user_choice == "q":
        break
    if user_choice not in options:
        continue
    random_number=random.randint(0,2)
    computer_choice=options[random_number]
    print("The computer picked ",computer_choice)

    if user_choice == "rock" and computer_choice=="scissors":
        print("You won!")
        user_win+=1
        continue

    elif user_choice =="paper" and computer_choice=="rock":
        print("You won!")
        user_win+=1
        continue

    elif user_choice  =="scissors" and computer_choice=="paper":
        print("You won!")
        user_win+=1
        continue

    elif user_choice==computer_choice:
        print("It was a tie")


    else:
        print("You lose")
        computer_win+=1
        continue

print("Total wins you got" ,user_win)
print("Total computer wins are ", computer_win)
print("Good Bie")

        




