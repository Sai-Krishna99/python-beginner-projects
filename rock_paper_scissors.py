import random 

user_wins=0
comp_wins=0

options=['rock','paper','scissors']

while True:
    user_ip=input("Type Rock/Paper/Scissors or Q to Quit: ").lower()
    if user_ip=="q":
        break

    if user_ip not in options:
        print("Please type a valid input")
        continue
    
    random_number=random.randint(0,2)
    #rock=0,paper=1,scissors=2
    computer_pick = options[random_number]
    print("Computer picked",computer_pick + '.')

    if user_ip== "rock" and computer_pick == "scissors":
        print("You won!!")
        user_wins+=1
    elif user_ip== "paper" and computer_pick == "rock":
        print("You won!!")
        user_wins+=1
    elif user_ip== "scissors" and computer_pick == "paper":
        print("You won!!")
        user_wins+=1
    else:
        print("You lost!")
        comp_wins+=1
       
print("You won",user_wins,"times")
print("Computer won",comp_wins,"times")
print("Goodbye!!")