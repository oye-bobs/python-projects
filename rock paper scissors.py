import random

def play():
    user = input(str("What\'s your choice? 'r' for rock, 'p' for paper 's' for scissors:"))
    computer = random.choice(['r','p','s'])
    
    if user==computer:
        return "it\'s a tie"
    
    if is_win(user,computer):
        return 'You Won!!'
    
    if user != str('r' or 's' or 'p'):
        return 'wrong input'

       

    return  'You Lost!!'

    
  
    
    
def is_win(user,computer) : 
    if (user== 'r' and computer == 's') or (user == 's' and computer == 'p') or (user== 'p' and computer == 'r'):
        return True
    

print (play())
    