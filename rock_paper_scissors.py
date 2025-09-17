import random
print("Condition:0 for ROCK, 1 for PAPER and 2 for SCISSORS.")
user_choice=int(input("Enter your choice:"))
if user_choice>=3 or user_choice<0:
    print("Invalid choice. you lose.")
else:
    computer_choice=random.randint(0,2)
    print(f"Computer choice is: {computer_choice}")
    if user_choice==computer_choice:
        print("Match draw, to play again.")
    elif user_choice==0 and computer_choice==2:
        print("you win the match.")
    elif user_choice==2 and computer_choice==0:
        print("computer win the match.")
    elif user_choice>computer_choice:
        print("you win the match.")
    elif user_choice<computer_choice:
        print("computer win the match.")