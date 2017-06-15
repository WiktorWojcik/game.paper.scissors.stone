#"Paper, Scissors, Stone" game
#@author Wiktor Wójcik
#@version 16 V 2017

from random import choice
from time import sleep

print("""Hello! My name is Victor and I'm honored to introduce you my own:\n
\t>> PAPER, SCISSORS, STONE game! <<\n
You know rules of this game, right??
Paper beats Stone, Stone beats Scissors and Scissors beats Paper..
GOOD LUCK:)""")
         
PC_HAND = ["paper", "scissors", "stone"]
pc_points = 0
player_points = 0
turns = 0

#introduce
while type(turns) != int or turns == 0:
    turns = input("\nHow much rounds do you want to take? (insert integer, please): ")
    try:
        turns = int(turns)
        
        if turns == 0:
            print("Don't you even want to try? Come on! I assure you that PC won't be cheating!")
        elif turns <= 3:
            print("That's gonna be a fast game...")
        elif turns >= 10:
            print("A loooong journey..")
    except ValueError:
        print("Oops! You didn't insert integer, right?")
else:
    print("OK!", turns, "rounds. Let's get started!")
        
#player choice and battle
for i in range(1, turns+1):
    print("\nROUND", i, "\n")
    player_choice = input("What do you want to throw now? (type one of: paper / scissors / stone) ")
    while player_choice not in PC_HAND:
        print("Probably you've made a mistake. Try again.")
        player_choice = input("What do you want to throw now? (type one of: paper / scissors / stone) ")
    else:
        pc_choice = choice(PC_HAND)
        print("\nYour hand >>", player_choice.upper(), "vs", pc_choice.upper(), "<< PC's hand")
        if player_choice == pc_choice:
            print("Draw! You've got the same hand")
        elif player_choice == "paper" and pc_choice == "scissors":
            pc_points += 1
            print("Point goes to PC")
        elif player_choice == "paper" and pc_choice == "stone":
            player_points += 1
            print("Point goes to YOU")
        elif player_choice == "scissors" and pc_choice == "stone":
            pc_points += 1
            print("Point goes to PC")
        elif player_choice == "scissors" and pc_choice == "paper":
            player_points += 1
            print("Point goes to YOU")
        elif player_choice == "stone" and pc_choice == "paper":
            pc_points += 1
            print("Point goes to PC")
        elif player_choice == "stone" and pc_choice == "scissors":
            player_points += 1
            print("Point goes to YOU")
            
#announcement of results
print("\n\nRESULTS\nYou:", player_points, "\n PC:", pc_points)
if player_points > pc_points:
    print("You've WIN! Congratulations!:D")
elif pc_points > player_points:
    print("PC WINS! \t\t...Wish you luck next time;)")
elif player_points == pc_points:
    print("DEAD-HEAT. \t\t...That was pretty close;)")

#goodbye
print("\n\nTHANKS for spending time together!\n (Had a fun? See any errors? Know better code-solution? Let me know!)")
sleep(3)




    
