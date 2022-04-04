name= input("Type your name")
print("Welcome",name,"to this adventure")
answer=input("You are on a dirt road,it has come to an end and you can go left or right. Which way would you like to go?").lower()

if answer == "left":
    answer=input("Okay, you come to a river, do you want to walk around it or swim across? Type walk or swim: ")
    if answer=="swim":
        print("You swam across and were eaten by an aligator.")
    elif answer =="walk":
        print("You walked for many miles, lost out of water and you lost the game")
    else:
        print("Not a valid option, you lose!!")
elif answer == "right":
    answer=input("You come to a bridge, it is wobbly, do you want to cross it or head back? Type cross/back")
    if answer=="cross":
        print("You crossed the bridge and meet a stranger. Do you talk to them or not? Type yes/no")
        if answer=="yes":
            print("You talked to the starnger and they gave you the reward. You win!!")
        elif answer =="no":
            print("You ignored the stranger and they are offended. You lost the game")
        else:
            print("Not a valid option, you lose!!")
    elif answer =="back":
        print("You go back and lose")
    else:
        print("Not a valid option, you lose!!")
else:
    print("Not a valid option, you lose!!")

print("Thank you for trying",name)