import random

choice_list=["rock","paper","scissors"]


print("welcome to the rock-paper-scissor game")
while True:
    user_score=0
    computer_score=0
    while user_score<5 and computer_score<5:
        print("\nchoices\n1.rock\n2.paper\n3.scissors")
        user_choice=int(input("\nenter your choice:"))
        match user_choice :
            case 1:
                user_choice="rock"
            case 2:
                user_choice="paper"
            case 3:
                user_choice="scissors"

            case _:
                print("\ninvalid choice")

        cchoice=random.choice(choice_list)
        print(f"\ncomputer chose {cchoice}")
        if user_choice==cchoice:
            print("no points")
            
        elif user_choice=="rock" and cchoice=="scissors":
            user_score+=1
            print("user scores")
        elif   user_choice=="scissors" and cchoice=="rock":  
            computer_score+=1
            print("computer scores")
        elif user_choice=="paper" and cchoice=="rock":
            user_score+=1
            print("user scores")
        elif user_choice=="rock" and cchoice=="paper":
            computer_score+=1
            print("computer scores")
        elif user_choice=="scissors" and cchoice=="paper":
            user_score+=1
            print("user scores")
        else:
            computer_score+=1
            print("computer scores")
        print(f"user score={user_score}  computer score={computer_score}")    
    if user_score > computer_score:
        print("user wins")
        break
        
    else:
        print("computer wins")
        break
        









            
