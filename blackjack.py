##blackjack
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
first_gameon=True
gameon=True
your_list=[]
your_sum=0
dealer_list=[]
dealer_sum=0

    
def pick_your_first_card():
    global your_list
    global your_sum
    your_init_card1 = cards[random.randrange(0,9,1)]
    your_init_card2 = cards[random.randrange(0,9,1)]
    your_list.append(your_init_card1)
    your_list.append(your_init_card2)
    global your_sum
    your_sum = sum(your_list) #sum of integers in list 
    print(f'Your cards: [{your_init_card1}, {your_init_card2}], current score: {your_sum}') #prints integers in list and sum of integers in list 
    return your_sum #returns sum integer not list 

def pick_dealer_first_card():
    dealer_card = cards[random.randrange(0,9,1)]
    global dealer_list
    dealer_list.append(dealer_card)
    global dealer_sum
    dealer_sum = sum(dealer_list) #sum of integers in list 
    print(f'Computer\'s first card: {dealer_sum}') #prints sum of integers in list 
    return dealer_sum #returns sum of integers in list 

def pick_your_nx_card():
    your_nx_card = cards[random.randrange(0,9,1)]
    global your_list
    your_list.append(your_nx_card)
    global your_sum
    your_sum = sum(your_list)    
    print(f'Your cards {your_list}, current score {your_sum}')
    return your_sum

def pick_dealer_nx_card():
    dealer_nx_card = cards[random.randrange(0,9,1)]
    global dealer_list
    dealer_list.append(dealer_nx_card)
    global dealer_sum
    dealer_sum= sum(dealer_list)
    print(f'Dealer cards {dealer_list}, current score {dealer_sum}')
    return dealer_sum
    
start_question = str (input('Do you want to play a game of blackjack? Type \'y\' or \'n\' ')).lower()
while gameon and start_question=='y':
    
    pick_your_first_card()
    pick_dealer_first_card() #returns int. prints total score 
    break

next_question = str(input('Type \'y\' to get another card, type \'n\' to pass: ')).lower()    
while next_question == 'y' and gameon and your_sum <22:
    if your_sum == 21:
        print ('Your cards {your_list}. \'Yout hit a blackjack!')
        next_question == 'n'
        break
        while dealer_sum<your_sum and dealer_sum <= 17 and dealer_sum <=21:
            pick_dealer_nx_card()
            if dealer_sum > 21:
                gameon=False
                break
    while your_sum < 21 and next_question == 'y':
        pick_your_nx_card()
        while your_sum < 21 and next_question == 'y':
            next_question = str(input('Type \'y\' to get another card, type \'n\' to pass: ')).lower()    
            if next_question == 'y':
                pick_your_nx_card()
    if your_sum > 21:
        gameon=False
        break
    
while dealer_sum<your_sum and dealer_sum <= 17 and dealer_sum <=21 and your_sum<22:
        pick_dealer_nx_card()
        if dealer_sum > 21:
            gameon=False
            break
            
    

if your_sum > 21: 
    print(f'Dealer wins! Dealer\'s cards {dealer_list}, {dealer_sum} against your cards {your_list}, {your_sum}.') 
elif dealer_sum > 21: 
    print (f'You win! Your cards {your_list}, {your_sum} against dealer\'s {dealer_list}, {dealer_sum}.')    
        
elif dealer_sum > your_sum:  
    print('')
    print(f'Dealer wins! Dealer\'s cards {dealer_list}, {dealer_sum} against your cards {your_list}, {your_sum}.') 
    
elif your_sum > dealer_sum:
    print('')
    print (f'You win! Your cards {your_list}, {your_sum} against dealer\'s {dealer_list}, {dealer_sum}.')
      
elif dealer_sum == your_sum: #tying scenario
    print('')
    print(f'You tie! Your cards {your_list}, {your_sum} against dealer\'s cards {dealer_list}, {dealer_sum}.')    
   
    
    

    
            
            
            
        

    












            



    

        
        
    


    
    

