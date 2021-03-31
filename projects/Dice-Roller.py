import random
def roll():
    dice=random.randint(1,6)
    print("The rolled number is %d"%(dice))
roll()
while input != 'E':
    raw_input = input("Want to roll again? [R] \nWant to exit [E]")
    input1 = str(raw_input)
    if(input1 == 'R'):
        roll()
    if(input1 == 'E'):
        exit()