import random
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback =input (f"is {guess} too small(S), too big(B),or correct(C)??").lower()
        if feedback =="S":
            guess = low + 1
        elif feedback == "B":
            guess = high - 1
    print (f"Yay, computer got your number {guess} right")
    
    
computer_guess(20)
    

        