import random

print("0 to quit, 1 for Rock, 2 for Paper, 3 for Scissor\n")
choices = {1:"Rock", 2:"Paper", 3:"Scissor"}

while True:
    computer_choice = random.randint(1,3)

    try:
        user_choice = int(input("\nEnter your choice: "))
        if user_choice == 0:
            break
        if user_choice not in [1,2,3]:
            print("Invalid choice!")
            continue
        
        print(f"You chose: {user_choice} - {choices[user_choice]}")
        print(f"Computer chose: {computer_choice} - {choices[computer_choice]}\n")
        
        result = (user_choice - computer_choice)%3
        
        if result == 1:
            print("You win")
            
        elif result == 2:
            print("Computer Wins!")
            
        else:
            print("It's a draw!")

    except ValueError:
        print("Exiting")



