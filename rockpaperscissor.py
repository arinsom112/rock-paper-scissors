import random

print("Hey there hooman!!!")

user_wins = 0
comp_wins = 0
tie_counter = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Choose from rock, paper or scissors or Q to quit: ").lower()
    if user_input == "q":
        print("You chose to quit :(")
        break
    if user_input not in options:
        print("Choose something from the options, please!") 
        continue 

    comp_input = options[random.randint(0, 2)]
    print("Computer chose", comp_input + ".")

    if user_input == "rock" and comp_input == "scissors":
        user_wins += 1
        print("You won!\n\n")
    elif user_input == "paper" and comp_input == "rock":
        user_wins += 1
        print("You won!\n\n")
    elif user_input == "scissors" and comp_input == "paper":
        user_wins += 1
        print("You won!\n\n")
    elif user_input == comp_input:
        print("Both of you chose the same.. TIED!\n\n")
        tie_counter += 1
    else:
        print("The computer won :(\n\n")
        comp_wins += 1

print("\n\nYou won", user_wins, "times!!")
print("The computer won", comp_wins, "times!")
print("Both tied", tie_counter, "times!")
print("SEEEYYAAA!!")
