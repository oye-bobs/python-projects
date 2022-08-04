import random
from word import words
import string

def get_valid_word(words):
    word = random.choice(words) #Randomly Choose a word from the list (words)
    while '-'in word  or ' ' in word :
        word = random.choice(words)
        
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #Letters in word
    alphabets = set(string.ascii_uppercase)
    used_letters =set() #This includes the letters in the word that the user has guessed
    lives = 7
    
    #This gets the users letter input
    while len(word_letters) > 0 and lives > 0:
        
        # letters used
        # ' '.join(['a','b','cd']) --> 'a b cd' it converts the sets of values into a string
        print('You have', lives,'lives left and You have used these letters :', ' '.join(used_letters))
        #What current word is (i.e  T H - R D )this displays both the letters you have guessed correctly the ones you havent indicated by(-)
       
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print ('Current word: ', ' '.join(word_list))
    
         
    
        user_letter =input('Guess a letter friend: ').upper() 
        if user_letter in alphabets - used_letters:
             
            used_letters.add(user_letter)
            if user_letter in word_letters:
                
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('Letter is not in word.')
               
               
        elif user_letter in used_letters:  
            print ('You have already used that Character. Please Try Again')
        
        else:
             print ('Invalid Character, Please Try Again.')
            
   # Code gets here when len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print ('Sorry you died, The word was', word)
    else:
        print('Congrats Champ,You Got the Word', word,'correct') 
        
if __name__ =='__main__':
     hangman()
   
