import random
user_score = 0
computer_score = 0
    
for i in range(50):
    x = random.randint(1, 3)

    if x == 1:
        computer_choice = "rock"
    elif x == 2:
        computer_choice = "paper"
    elif x == 3:
        computer_choice = "scissors"

    user_choice = input()
    print("..............")
    print("😊 ", user_choice, "🖥️ ", computer_choice)
    print("..............")
    if computer_choice == "rock" and user_choice == "paper":
        user_score = user_score +1
    elif computer_choice == "rock" and user_choice == "scissors":
        computer_score = computer_score +1
    if computer_choice == "scissors" and user_choice == "rock":
        user_score = user_score +1
    elif computer_choice == "scissors" and user_choice == "paper":
        computer_score = computer_score +1    
    if computer_choice == "paper" and user_choice == "scissors":
        user_score = user_score +1
    elif computer_choice == "paper" and user_choice == "rock":
        computer_score = computer_score +1  
    print ("😊 ",user_score,   "🖥️ ",computer_score)    
    while computer_score > 5:
        print("😒 Computer Win 😒")
        break
    while user_score > 4:
        print("🎉 You Win 🎉")  
        break  
