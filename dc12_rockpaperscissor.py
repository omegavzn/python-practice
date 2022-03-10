# Rock Paper Scissors
import random

def play():
    computer = random.choice(['Rock','Paper','Scissors'])
    user = input("'Rock','Paper','Scissors'")
                
    if user == computer:
        return 'It\'s a tie'
    
    if is_win(user, computer):
        return 'You won!'
        
    return 'You lost!'
d
ef is_win(player, opponent):

    if (player == 'Rock' and opponent =='Scissors') or 
    (player == 'Scissors' and opponent == 'Paper') or
    (player == 'Paper' and opponent == 'Rock'):
        return true
        
print(play())

