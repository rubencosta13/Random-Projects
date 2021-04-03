from random import randint

Computer_wins = 0
Player_wins = 0
counter = 0
objects = ['Rock','Paper','Scissors']
Cplay = objects[randint(0,2)]


while counter != 3:
    player = input('\nRock, Paper or Scissors: ')
    if player == Cplay:
        print('Tie!')
    elif player == 'Rock':
        if Cplay == 'Paper':
            print('You loose',Cplay,'is able to cover the',player)
            counter += 1
            Computer_wins += 1
        else:
            print('You win', player,'smashes', Cplay)
            counter += 1
            Player_wins += 1
    elif player == 'Paper':
        if Cplay == 'Scissors':
            print('You loose',Cplay,'are able to cut',player)
            counter += 1
            Computer_wins += 1
        else:
            print('You win',player, 'covers ' ,Cplay)
            counter += 1
            Player_wins += 1
    elif player == 'Scissors':
        if Cplay == 'Rock':
            print('You loose, Rock is able to destroy the Scissors')
            counter += 1
            Computer_wins += 1
        else:
            print('You win',player, 'cuts ' ,Cplay)
            counter += 1
            Player_wins += 1
    else:
        print('Not a valid play! Check your spelling and try again!')



if Player_wins > Computer_wins:
    print('You won the game!')
else:
    print('You have lost the game!')