import random
print("---------- Rock Paper Scissors Game ----------")
comp_choice = ["rock","paper","scissor"]

you_score = 0
comp_score = 0
while True:
    
    user_choice = input("Enter Your Choice (Rock/Paper/Scissor) : ")
    print(f"You chose : {user_choice}")
    user_choice = user_choice.lower()
    if user_choice not in ["rock","paper","scissor"]:
        print("Invalid input ! choose rock/paper/scissor.")
        continue
    computer_choice = random.choice(comp_choice)
    print(f"Computer Chose : {computer_choice}")

    if(computer_choice == "rock" and user_choice =="paper"):
        print("you won !")
        you_score += 1
    elif(computer_choice == "scissor" and user_choice == "rock"):
        print("you won !")
        you_score += 1
    elif(computer_choice == "paper" and user_choice == "scissor"):
        print("you won !")
        you_score += 1

    elif(computer_choice =="paper" and  user_choice == "rock"):
        print("Computer wins")
        comp_score += 1
    elif(computer_choice == "rock" and user_choice == "scissor"):
        print("Computer wins")
        comp_score += 1
    elif(computer_choice == "scissor" and user_choice == "paper"):
        print("Computer wins")
        comp_score += 1

    elif(computer_choice =="paper" and  user_choice == "paper"):
        print("Draw !")
    elif(computer_choice == "rock" and user_choice == "rock"):
        print("Draw !")
    elif(computer_choice == "scissor" and user_choice == "scissor"):
        print("Draw !")
 
    again = input("Do You Want to Play again ? (yes/no) : ").lower()
    if again != "yes":
        break

print()

print(f"Your Final Score : {you_score}")
print(f"Computer Final Score : {comp_score}")

if you_score > comp_score:
    print("Congratulations ! You Won Finally !!")
elif you_score < comp_score:
    print("Oops ! You Lose , Computer Wins !!")
elif you_score == comp_score:
    print(" Game Draw !!")

print("---------- Thank You For Playing ----------")
