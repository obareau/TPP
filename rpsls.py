# A Rock, Paper, Scissors and maybe more Programs

import random

choices = ["R", "P", "S"]

def get_choice(imput):
    if input == "R":
        return "Rock"
    elif input == "P":
        return "Paper"
    elif input =="S":
        return "Scissors"
    else:
        return "Not [R, P or S]"

print("----------------------------------------------")    
print("Rock, Paper, Scissors - Shoot !")
print("[R]=Rock [P]=Paper [S]=Scissors and...[Q]=Quit")
print("----------------------------------------------")

counter = 1
player_score = 0
computer_score = 0



while True:
    print("----------------------------------------------")
    # Scoreboard
    p_score_str = str(player_score)
    c_score_str = str(computer_score)
    print ("Player score : " + p_score_str)
    print("Computer score : " +c_score_str)
    
    if player_score < computer_score:
        print("Computer has advantage")
    elif player_score > computer_score:
        print("Player has advantage")
    else:
        print("It's a Tie")    
        
    
    print("Game" +str(counter)+":")
    print("Please choose a letter:")
    user_choice = input()
    
    # Quit
    if user_choice == "Q":
        print("Thanks for playing !!!") 
        break;
    
    random_index = random.randint(0,2)
    computer_choice = choices[random_index]
    
    player_choice = user_choice
    
    print("You choose : " + player_choice)
    print("Computer choose : " + computer_choice)
    
    if user_choice == "R" and computer_choice == "S":
        print("You win, Rock beats Scissors ")
        player_score = player_score+1
    elif user_choice == "P" and computer_choice == "R":
        print("You win, Paper beats Rocks ")
        player_score = player_score+1
    elif user_choice == "S" and computer_choice == "P":
        print("You win, Scissors beats Paper ") 
        player_score = player_score+1
    #  Computer
    
    elif user_choice == "R" and computer_choice == "P":
        print("Computer wins, Paper beats Rocks ")
        computer_score = computer_score+1
    elif user_choice == "P" and computer_choice == "S":
        print("Computer wins, Scissors beats Paper ")
        computer_score = computer_score+1
    elif user_choice == "S" and computer_choice == "R":
        print("Computer wins, Rock beats Scissors ")
        computer_score = computer_score+1
    
    elif user_choice == computer_choice:
        print("It's a trap !!!, ahem sorry it's a tie !")
    else:
        print("Please enter [ R, P, S or Q ]")
        
    counter = counter+1
    
    
            
                   
           