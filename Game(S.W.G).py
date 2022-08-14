import random

print("Snake Water Gun \n")

print("Enter your name : ",end=" ")
n1= str(input())
count = 1

option =['s','w','g']
player_win=0
computer_win=0

while (count<=10):

    print("Choose s for snake ,w for water , g for gun : ",end=" ")
    player = str(input())

    if player!='s' and player!= 'w' and player!='g':

        print("Enter a valid input")
       
    computer=random.choice(option)
    print("Computer choice =  "+ computer)

    if player == 's':
        if computer == 'w':
            print("Winnner = Player\n")
            player_win+=1


        elif computer =='g':
            print("Winner = Computer\n ")
            computer_win+=1
        elif player == computer:
            print("It is a Draw")
    
    elif player == 'w':
        if computer == 'g':
            print("Winnner = Player\n")
            player_win+=1
        elif computer =='s':
            print("Winner = Computer\n ")
            computer_win+=1
        elif player == computer:
            print("It is a Draw")

    elif player == 'g':
        if computer == 's':
            print("Winnner = Player\n")
            player_win+=1
        elif computer =='w':
            print("Winner = Computer \n")
            computer_win+=1
        elif player == computer:
            print("It is a Draw")
    
    

    count+=1

print("Score 0f " + n1 +" =",player_win)
print("Score 0f Computer =",computer_win)

        
if player_win > computer_win :
    print( n1+" is the winner\n")
elif computer_win > player_win :
    print("\nComputer is the winner\n")
else:
    print("Match draw\n")
