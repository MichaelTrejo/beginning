#rps GAME CODE
#LIBRARIES
import random
#GAME CODE START
print("""welcome to rock paper scissors!
pick an option
1.) rock
2.) Paper
3.) scissors """)
user_choice = int(input("player_1, input a choice "))
print("you choose ")
print(user_choice)
print(" ONly a HuMan CouLd maKe suCh a DumB moVe!")
print("MY TURN HUMAN SCUM!")
print(" WELL PIKACHU I CHOOS--.... Wrong game...my bad.")
print(" I choose ")
random_number = int(random.randrange(1, 3))
print(random_number) 
if ((user_choice == 1 and random_number == 3) and (user_choice == 2 and random_number == 1) and (user_choice == 3 and random_number == 2)):
    print("WHAT!? how did you win this round?! CheAAAATEERRRR!!")
elif ((user_choice == 1 and random_number == 2) and (user_choice == 2 and random_number == 3) and (user_choice == 3 and random_number == 1)):
    print("HA! SUCK. IT. LOSER!!! 'evil laugh emoticon' ")
if ((user_choice == 1 and random_number == 1) and (user_choice == 2 and random_number == 2) and (user_choice == 3 and random_number == 3)):
    print("""a draw!?!?!?!? how insulting that i am put in the same placement as something as devoid of intelligence as you!
    A DISGRACE!
    ARRRRRRRRRRRRRRRRRRRRRRGHHHHHHHHHHHH!!!!!!!!!!!!!!! """)