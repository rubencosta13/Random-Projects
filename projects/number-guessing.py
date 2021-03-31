import random
nUser = 0
counter = 0  #Counting the attempts, when reaches to the 3rd attempt it stops the game!
MAX = 100   
MIN = 1
Slimit = 100 #Maximum Limit
Mlimit = 1   #Minimum Limit
Npc=random.randint(MIN, MAX)

while Npc != nUser:
    raw_nUser = input("What's your guess?")
    nUser = int(raw_nUser)
    #if statement in order to verify if Npc == nUser
    if(Npc == nUser):
        counter += 1
        print("\n\n\nNice you successfully guess the number!")
        print("Atempt number: %d"%(counter))
    else:
        counter += 1
        print("\n\nTry again!")
        print("The number is between %d and %d"%(nUser, Npc + 10) )
        print("Atempt number: %d"%(counter))
    if(counter == 3):
        print("You have reached the maximum amount of attempts the number was %d "%(Npc))
        exit()