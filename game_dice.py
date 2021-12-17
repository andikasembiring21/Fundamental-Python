import random

def rool_dice():
    die1=random.randrange(1,7)
    die2=random.randrange(1,7)
    return(die1,die2)

def display_dice(dice):
   die1,die2=dice
   print(f'player rolled {die1}+{die2}={sum(dice)}')

die_value=rool_dice()
display_dice(die_value)

sum_of_dice=sum(die_value)
if sum_of_dice in (7,11):
    game_status ="won"
elif sum_of_dice in (2,3,12):
    game_status = "lost"
else :
    game_status = "continue"
    my_point=sum_of_dice
    print("point is ",my_point)

while game_status == "continue":
    die_value=rool_dice()
    display_dice(die_value)
    sum_of_dice=sum(die_value)

    if sum_of_dice == my_point:
        game_status ="won"
    elif sum_of_dice == 7:
        game_status = "lost"

if game_status == "won":
    print("player won")
else:
    print("player loses")
    
        
