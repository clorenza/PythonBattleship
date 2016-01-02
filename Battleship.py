Celia = 'Celia'

from random import randint

#Making the 'Ocean' 6x6 board
ocean = []
for item in range(6):
    ocean.append(['o']*6)
def print_ocean(ocean):
    for row in ocean:
        print ' '.join(row)
        
#Having the ship randomly assigned to a spot in the ocean
#Note that randint includes the second number....
ship_row = randint(0,5)
ship_column = randint(0,5)


#for temporary debugging
print ship_row
print ship_column

#Game!
print 'BATTLESHIP!'
print 'Your mission objective is to destroy the enemy ship. Aim your cannon for coordinates between 1 and 6.'

while True:
    guess_row = int(raw_input('Guess Row?')) - 1
    guess_column = int(raw_input('Guess Column?')) - 1
    
    if guess_row == ship_row and guess_column == ship_column :
        print 'You sunk the enemy ship! You win!'
        break
    elif guess_row < 0 or guess_row > 5 or guess_column < 0 or guess_column > 5:
        print 'Out of range. Aim your cannon better.'
        print_ocean(ocean)
    else:
        print 'Oh no, you missed! Try harder!'
        ocean[guess_row][guess_column] = 'x'
        print_ocean(ocean)