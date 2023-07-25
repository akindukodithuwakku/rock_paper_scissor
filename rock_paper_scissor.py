import random

gameImages = ['Rock' , 'paper' , 'scissors']

user = int(input("enter 0 for rock, 1 for paper, 2 for scissors: \n"))

if user < 0 or user > 2:
    print("invalid number you lose...")
else:
    computer = random.randint(0,2)
    print("you chose : ")
    print(gameImages[user])
    print("computer chose:  ")
    print(gameImages[computer])

    if computer == user:
        print("that's a draw ! ")
        

    elif computer == 0 and user == 1:
        print("you win! \n")
       
    
    elif computer ==1 and user == 2 :
        print("you win! ")
    
    elif user > computer:
        print("you lose! ")
    
    else:
        print("you lose! ")
        

