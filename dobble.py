#Dobble generator to store 57 unique cards in a dictionary with keys of 1 -57 and values of sets
# all of which are related by only one card

# figure out what numbers to write on each card
nIm = 8
n = nIm - 1
r = range(n)
rp1 = range(n+1)
c = 0

dict_card_nums = {} # instruction dictionary - crack the code 
num_set = set()  # card 1 numbers
c += 1

for i in rp1:
    num_set.add(i+1)

dict_card_nums[c] = num_set 

for j in r:
    num_set = set() #card_x_numbers
    c = c+1

    num_set.add(1)
    for k in r:
    	vari = set()

    	vari = n+2 + n*j + k 
    	num_set.add(vari)
    dict_card_nums[c] = num_set

num_set = set()
for i in r:
    num_set = set()
    for j in r:
        num_set = set()

        c += 1

        num_set.add(i+2)

        for k in r:

            vari = set()
            vari = ((n+1 + n*k + (i*k+j) % n) + 1) # remainders of 7 

            num_set.add(vari)

        dict_card_nums[c] = num_set

dict_card_nums


# OVERVIEW With my Dobble program, I've tried to make clear distictions beteern the DobbleCard and Dobbledeck classes and have all of the game logic 
# contained within the game. With this in mind, I've imagined a scenario where I have purchased a Dobble set, but with a twist. 
# The cards are not pre-made. In order to uset up the cards, I must first decode the instructions. The instructions will then tell me what numbers to 
# have on each of my cards. Each one of these numbers will then have a unique sticker emoji associated with them. 
# So after I've cracked the code for each card I'll affix the stcikers in the right place, until I have 57 cards fully covered in sticker 
# emojis and ready for a game.

# -- The Dobble generator code above was modified to store the key, value pairs with the card template number being the key, and the values on the card 
# being the 8 numbers contained within the set.

# -- My check validity function code below, sets verbose to False as a default. Only if verbose == True, will the verbose checks occur. 
# I decided to take in the 'deck' template and make an exact copy of it. Then I reverse iterate through the outer loop starting from card_template 57. 
# This will then perform checks against all the other card_templates in the deck except itself (if x == y ; pass). 
# The outer loop will then decrement by 1 and checks will be made for card_template 56 againt every other card template. 
# On the non-verbose checks, if a relationship between two cards greater than length 1 is found (i.e. more than one character), 
# then the function exits immediatly and returns false.

# instruction booklet 
# check validity
# check that you've passed this portion of the instructions so you can move onto building your first card 
# and ultimately the whole deck. 


def check_validity(deck,verbose=False):
    deck_2 = deck.copy() # create a duplicate of the instructions
    y = 57 # reverse iterate back through y
    verb_check_counter = 0 # a counter for the verbose checks
    while y > 0: #all checks will commence for card 57 against the other 56, excpet for itself
        for x in range(1,58): # go forwards through x 
            if x == y: # then it's the same card_template  
                pass # don't check this as the answer will always be 8
            elif verbose == True: # if verbose=True - print all matches 
                verb_check = (deck[x].intersection(deck_2[y])) 
                print("The number common between card ", x , " and card " ,y,  " is ",verb_check)
                if len(verb_check) > 1:
                    verb_check_counter +=1 # so if verb_check is ever greater than 1 - increment this counter by 1
            else:
                check = set() # this a scenario where verbpse isn't true 
                check = deck[x].intersection(deck_2[y])
                if len(check) > 1: 
                    return False 
                    break # if there is any instance where the length of check is > 1 break immediatly and return False
                else:
                    return True # otherwise the checks were a success

        y -= 1
    if verb_check_counter == 0:
        return True # here if the counter for verb_check_counter hasn't incremented the checks were a success
    else:
        return False

print(check_validity(dict_card_nums))


import emoji
imageDict = dict()
fin = open('emoji_names.txt',"r")
lines = fin.readlines()
for i, el in enumerate(lines):
    imageDict[i+1] = emoji.emojize(el.strip())

# The above code imports the emojis into the program. Each emoji is a string value with an associated integer key. The emojis in this context 
# represent the stickers. The emojis each have a unique number associated with them (the key). This number corresponds to the 
# code we cracked earlier in the instructions. Now that we have the code and the sticker pack we can set about building a card, 
# and then repeating the process to build the whole deck.

# -- below Considering that I'd already verified that the values in dict_card_nums had the desired unique relationship, I decided to cast the data type for this dcitionary to have a 
#list type for the values rather than a set. This was mainly because lists are easier to work with below

imageDict = {int(k):str(v) for k,v in imageDict.items()}

dict_card_nums={int(k):list(v) for k,v in dict_card_nums.items()}

# The Dobblecard class will ultimately give us a completed Dobble Card when we utilize its methods. It accepts 3 arguments as the constructors. 
# 1.The unique number of a card_template (the key values of dict_card_nums). 2.The instruction set for the card templates that we decoded earlier 
# (dict_card_nums). 3.The emoji_sticker pack (imageDict).

# Methods:

# take_template_card_from_box This takes a template for a card from the dict_of_numbers dictionary.

# add_and_position_stickers This class initially takes all the keys assocaited with the imageDict which gives us the correct numbers associated with each emoji/sticker. 
#If this number appears in the values of the the card_template, then we convert them ( we know which stickers to use). Then we position the 
# stickers accordingly. I used indexing here of the list (hence the type cast conversion above). 
# I looped through the first three values then added a emoji and a space on the top line. 
# Then I printed a new line and repeated for rows 2 and 3 respectively. I then returned self.card which is the formatted card.

class DobbleCard():
    ''' Formats and builds a Dobble card
    Dobble cards have 8 unique images/emojis which are built from a template pack
    stickers are positioned and added per the instrcutions that were decoded in the making of the Dobble pack'''
    def __init__ (self,card_num,dict_of_numbers,emoji_stickers): 
        self.dict_of_numbers = dict_of_numbers
        self.card_num = card_num 
        self.emoji_stickers = emoji_stickers


    def take_template_card_from_box(self):
        '''take a template card out of the box'''
        self.card_template = self.dict_of_numbers.pop(self.card_num)

        return self.card_template 

    def add_and_position_stickers(self):
        ''' adds stickers on the applicable numbers on a card based on the instruction set'''
        image_key_list =[]
        for k in self.emoji_stickers.keys():
            image_key_list.append(k) # all the unique numbers assocated with a specific emoji

        for n, i in enumerate(self.card_template):
            if i in image_key_list: # if the number for the card_template appears in the key list for the emojis 
                self.card_template[n] = imageDict[i]  #then that number corresponds to that emoji
        
        self.card='' # build the card with correct formatting- i.e. put the stickers in the right place 
        for l in self.card_template[0:3]:
            self.card += l
            self.card += ' ' 

        self.card += "\n"


        for k in self.card_template[3:6]:
            self.card += k
            self.card += ' '

        self.card += "\n"

        for j in self.card_template[6:8]:
            self.card += j
            self.card += ' '
        return self.card # completed card         

from random import shuffle

# Dobbledeck accepts DobbleCard instances and stores them in the deck_holder list (instance variable). There are 57 cards in the deck (class variable).

# Methods:

# add_cards This method iterates through the range from 1 to 57. An instance is called, with i as the card number passed as the argument along 
# with the dict_card_nums and the imageDict. I call the take_template_card_from_box and the add_and_position_stickers methods and store the 
# completed instance/card in the self.deck_holder list.

# shuffle_cards This allows for a shuffle of the deck using the shuffle method imported above.

# play_card with nested remove_card When a card needs to be played, a card is removed from the top of the deck (pop (0)).

class DobbleDeck():
    ''' represents a dobbledeck containing instances of DobbleCards'''
    number_of_cards = 57
    ''' contains a deck of 57 unique dobble cards'''
    def __init__ (self):
        self.deck_holder=[]

    def add_cards(self):
        '''method adds dobblecard instances to the deck_holder '''
        for i in range(1,self.number_of_cards +1):
            dobble_card_inst=DobbleCard(i,dict_card_nums,imageDict)
            #self.deck_holder.append(dobble_card_inst.pop_card())
            dobble_card_inst.take_template_card_from_box()
            self.deck_holder.append(dobble_card_inst.add_and_position_stickers())

    def shuffle_cards(self):
        ''' shuffles the deck to randomise the cards'''
        shuffle(self.deck_holder)


    def play_card(self):
        '''nested method which plays a card by removing it from the deck_holder'''
        
        def remove_card():
            self.card = self.deck_holder.pop(0)
            return self.card 
        remove_card()
        return self.card


# To keep things consistent and to make sure we're keeping track Dobble has two card positions - position 1 and 2 In the first game cards 1 and 2 are 
# dealt from recently shuffled deck Then the card at position 2 moves into position 1 at the end of the round- Then we peel a new card off the deck- 
# face down- and then pop it up And a new round begins! It's a game of speed The cards are positioned as above to keep things fair!

#Score_A and score_B keep track of players scores. There is also an incrementer i which keeps track of how many rounds have been played. 
# The number of cards (rounds) is chosen by one of the players. An instance of the deck is generated and the add card method calls all 57 cards. 
# They are then shuffled once. A card is put into position 1. Then a second card in called/pulled from deck (within the while loop). 
# Whoever wins, gets a point (or it's a draw). At the end of a round, the card at position 2 is moved to position 1. 
# In the next round a card will be taken from the deck for position 2. The game continues until all rounds have been played, then the score is 
# tallied and shown to the players.

def play_dobble():
    ''' plays a game of dobble'''
    score_A = 0
    score_B = 0
    i = 0 #used to control the number of rounds played 


    how_many_cards = int(input("How many cards (<56)?")) #it really refers to how many rounds we'll play
    print("If you want to record a draw type 'd' or 'D'.")
    
    d_deck_inst = DobbleDeck() #call an instance of Dobble Deck
    d_deck_inst.add_cards()# Add all 57 Dobble cards
    d_deck_inst.shuffle_cards()# shuffle the deck once 


    card_position_1 = d_deck_inst.play_card() # play a card at position 1
    while i <= how_many_cards + 1: # this is how many games we play 


        if i == how_many_cards: # then all rounds have been played, show the score and exit
            print("Score")
            print("A: ",score_A)
            print("B: ",score_B)
            break #exit here 
        else:
            
            card_position_2 = d_deck_inst.play_card() # play a card at position 2 
            # there's only a need for one play card in the loop because we'll be moving --
            # --> card at position 2 to position 1 for the next round


            print(card_position_1)
            print()
            print(card_position_2)
            


            who_wins = input("Who wins (A or B)?") 
            if who_wins == 'd' or who_wins == 'D':
                pass # a draw will increment neither A nor B
            elif who_wins == 'a' or who_wins == 'A':
                score_A += 1
            elif who_wins == 'b' or who_wins == 'B':
                score_B += 1

            i+=1 # increment round counter 
            temp = card_position_2 # change the position of the cards- the second card moves to position 1
            card_position_1 = temp # card has moved from position 2 to 1 for next round

play_dobble()
