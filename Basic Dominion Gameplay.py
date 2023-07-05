import random, time
#Silver is counting as copper?
#added two extra coppers

#add more expan
#put in specific cards
#limit cost - works but not only that num - no gives one?
#What can do: choose num cards in expan, cost of cards in kingdom, check cards in kingdom
dom_expansions = []
base = []
dark_ages = []
kingdom = []
dictionary = []
expan_used = []
expan = []
card_cost = []
not_cost = []
num_cost_had = 0
num_cost_total = 0
not_expan = []
num = ('1','2','3','4','5','6','7','8','9','10')
working = False
one = ('one','1')
two = ('two','2')
three = ('three','3')
four = ('four','4')
five = ('five','5')
six = ('six','6')
seven = ('seven','7')
eight = ('eight','8')
nine = ('nine','9')
ten = ('ten','10')
cellar = ('Cellar','2','Action','+1 Action, Discard any number of cards, then draw that many.')
chapel = ('Chapel','2','Action','Trash up to 4 cards from your hand.')
moat = ('Moat','2','Action','Reaction','+2 Cards|When another player plays an Attack card, you may first reveal this from your hand, to be unaffected by it.')
harbinger = ('Harbinger','3','Action','+1 Card +1 Action, Look through your discard pile. You may put a card from it onto your deck.')
merchant = ('Merchant','3','Action''+1 Card +1 Action, The first time you play a Silver this turn, +$1.')
vassal = ('Vassal','3','Action','+$2 Discard the top card of your deck. If it\'s an Action card, you may play it.')
village = ('Village','3','Action','+1 Card +2 Actions.')
workshop = ('Workshop','3','Action','Gain a card costing up to $4.')
bureaucrat = ('Bureaucrat','4','Action','Attack','Gain a Silver onto your deck. Each other player reveals a Victory card from their hand and puts it onto their deck (or reveals a hand with no Victory cards).')
gardens = ('Gardens','4','Victory','Worth 1VP per 10 cards you have (round down).')
militia = ('Militia','4','Action','Attack','$4','+$2, Each other player discards down to 3 cards in hand.')
moneylender = ('Moneylender','4','Action','You may trash a Copper from your hand for +$3.')
poacher = ('Poacher','4','Action','+1 Card +1 Action +$1, Discard a card per empty Supply pile.')
remodel = ('Remodel','4','Action','Trash a card from your hand. Gain a card costing up to $2 more than it.')
smithy = ('Smithy','4','Action','+3 Cards')
throne_room = ('Throne Room','4','Action','You may play an Action card from your hand twice.')
bandit = ('Bandit','5','Action','Attack','Gain a Gold. Each other player reveals the top 2 cards of their deck, trashes a revealed Treasure other than Copper, and discards the rest.')
council_room = ('Council Room','5','Action','+4 Cards +1 Buy, Each other player draws a card.')
festival = ('Festival','5','Action','+2 Actions +1 Buy +$2')
laboratory = ('Laboratory','5','Action','+2 Cards +1 Action')
library = ('Library','5','Action','Draw until you have 7 cards in hand, skipping any Action cards you choose to; set those aside, discarding them afterwards.')
market = ('Market','5','Action','+1 Card +1 Action +1 Buy +$1')
mine = ('Mine','5','Action','You may trash a Treasure card from your hand. Gain a Treasure card to your hand costing up to $3 more than it.')
sentry = ('Sentry','5','Action','+1 Card +1 Action Look at the top 2 cards of your deck. Trash and/or discard any number of them. Put the rest back on top in any order.')
witch = ('Witch','5','Action','Attack','+2 Cards, Each other player gains a Curse.')
artisan = ('Artisan','6','Action','Gain a card to your hand costing up to $5. Put a card from your hand onto your deck.')
copper = ('Copper','0','Treasure','1')	
silver = ('Silver','3','Treasure','2')
gold = ('Gold','6','Treasure','3')	
estate = ('Estate','2','Victory','1')
dutchy = ('Dutchy','5','Victory','3')
province = ('Province','8','Victory','6')
curse = ('Curse','0','Curse','-1')

poor_house = ('Poor House','1','Action','+$4, Reveal your hand. –$1 per Treasure card in your hand. (You cannot go below $0.)')
beggar = ('Beggar','2','Action','Reaction','Gain 3 Coppers to your hand. When another player plays an Attack card, you may first discard this to gain 2 Silvers, putting one onto your deck.')
squire = ('Squire','2','Action','+$1, Choose one: +2 Actions; or +2 Buys; or gain a Silver. When you trash this, gain an Attack card.')
vagrant = ('Vagrant','2','Action','+1 Card +1 Action, Reveal the top card of your deck. If it’s a Curse, Ruins, Shelter, or Victory card, put it into your hand.')
forager = ('Forager','3','Action','+1 Action +1 Buy, Trash a card from your hand, then +$1 per differently named Treasure in the trash.')
hermit = ('Hermit','3','Action','Look through your discard pile. You may trash a non-Treasure card from your discard pile or hand. Gain a card costing up to $3. | When you discard this from play, if you didn’t buy any cards this turn, trash this and gain a Madman from the Madman pile.')
market_square = ('Market Square','3','Action','Reaction','+1 Card +1 Action +1 Buy, When one of your cards is trashed, you may discard this from your hand to gain a Gold.')
sage = ('Sage','3','Action','+1 Action, Reveal cards from the top of your deck until you reveal one costing $3 or more. Put that card into your hand and discard the rest.')
storeroom = ('Storeroom','3','Action','+1 Buy Discard any number of cards, then draw that many. Then discard any number of cards for +$1 each.')
urchin = ('Urchin','3','Action','Attack','+1 Card +1 Action, Each other player discards down to 4 cards in hand. | When you play another Attack card with this in play, you may first trash this, to gain a Mercenary from the Mercenary pile.')
armory = ('Armory','4','Action','Gain a card onto your deck costing up to $4.')
death_cart = ('Death Cart','4','Action','Looter','You may trash this or an Action card from your hand, for +$5. When you gain this, gain 2 Ruins.')
feodum = ('Feodum','4','Victory','Worth 1VP per 3 Silvers you have (round down), When you trash this, gain 3 Silvers.')
fortress = ('Fortress','4','Action','+1 Card +2 Actions, When you trash this, put it into your hand.')
ironmonger = ('Ironmonger','4','Action','+1 Card +1 Action, Reveal the top card of your deck; you may discard it. Either way, if it is an…     Action card, +1 Action  Treasure card, +$1  Victory card, +1 Card')
maurader = ('Marauder','4','Action','Attack','Looter','Gain a Spoils from the Spoils pile. Each other player gains a Ruins.')
procession = ('Procession','4','Action','You may play a non-Duration Action card from your hand twice. Trash it. Gain an Action card costing exactly $1 more than it.')
rats = ('Rats','4','Action','+1 Card +1 Action, Gain a Rats. Trash a card from your hand other than a Rats (or reveal a hand of all Rats). | When you trash this, +1 Card.')
scavenger = ('Scavenger','4','Action','+$2, You may put your deck into your discard pile. Look through your discard pile and put one card from it onto your deck.')
wandering_minstrel = ('Wandering Minstrel','4','Action','+1 Card +2 Actions, Reveal the top 3 cards of your deck. Put the Action cards back in any order and discard the rest.')
band_of_misfits = ('Band of Misfits','5','Action','Command','Play a non-Command Action card from the Supply that costs less than this, leaving it there.')									
bandit_camp = ('Bandit Camp','5','Action','+1 Card +2 Actions, Gain a Spoils from the Spoils pile.')
catacombs = ('Catacombs','5','Action','Look at the top 3 cards of your deck. Choose one: Put them into your hand; or discard them and +3 Cards. | When you trash this, gain a cheaper card.')
count = ('Count','5','Action','Choose one: Discard 2 cards; or put a card from your hand onto your deck; or gain a Copper. Choose one: +$3; or trash your hand; or gain a Duchy.')
counterfit = ('Counterfeit','5','Treasure','$1 +1 Buy, When you play this, you may play a Treasure from your hand twice. If you do, trash that Treasure.')
cultist = ('Cultist','5','Action','Attack','Looter','+2 Cards. Each other player gains a Ruins. You may play a Cultist from your hand. | When you trash this, +3 Cards.')
graverobber = ('Graverobber','5','Action','Choose one: Gain a card from the trash costing from $3 to $6, onto your deck; or trash an Action card from your hand and gain a card costing up to $3 more than it.')
junk_dealer = ('Junk Dealer','5','Action','+1 Card +1 Action +$1. | Trash a card from your hand.')
mystic = ('Mystic','5','Action','+1 Action +$2, Name a card, then reveal the top card of your deck. If you named it, put it into your hand.')
pillage = ('Pillage','5','Action','Attack','Trash this. If you did, gain 2 Spoils, and each other player with 5 or more cards in hand reveals their hand and discards a card that you choose.')
rebuild = ('Rebuild','5','Action','+1 Action, Name a card. Reveal cards from your deck until you reveal a Victory card you did not name. Discard the rest, trash the Victory card, and gain a Victory card costing up to $3 more than it.')
rogue = ('Rogue','5','Action','Attack','+$2, If there are any cards in the trash costing from $3 to $6, gain one of them. Otherwise, each other player reveals the top 2 cards of their deck, trashes one of them costing from $3 to $6, and discards the rest.')
alter = ('Altar','6','Action','Trash a card from your hand. Gain a card costing up to $5.')
hunting_grounds = ('Hunting Grounds','6','Action','+4 Cards | When you trash this, gain a Duchy or 3 Estates.')

dark_ages.append(poor_house)
dark_ages.append(beggar)
dark_ages.append(squire)
dark_ages.append(vagrant)
dark_ages.append(forager)
dark_ages.append(hermit) 
dark_ages.append(market_square)
dark_ages.append(sage)
dark_ages.append(storeroom)
dark_ages.append(urchin)
dark_ages.append(armory)
dark_ages.append(death_cart)
dark_ages.append(feodum)
dark_ages.append(fortress)
dark_ages.append(ironmonger)
dark_ages.append(maurader)
dark_ages.append(procession)
dark_ages.append(rats)
dark_ages.append(scavenger)
dark_ages.append(wandering_minstrel)
dark_ages.append(bandit_camp)
dark_ages.append(catacombs)
dark_ages.append(count)
dark_ages.append(counterfit)
dark_ages.append(cultist)
dark_ages.append(graverobber)
dark_ages.append(junk_dealer)
dark_ages.append(mystic)
dark_ages.append(pillage)
dark_ages.append(rebuild)
dark_ages.append(rogue)
dark_ages.append(alter)
dark_ages.append(hunting_grounds)
'''
Abandoned Mine	Dark Ages	Action - Ruins	$0	+$1				+$1					
Ruined Library	Dark Ages	Action - Ruins	$0	+1 Card		+1							
Ruined Market	Dark Ages	Action - Ruins	$0	+1 Buy			+1						
Ruined Village	Dark Ages	Action - Ruins	$0	+1 Action	+1								
Survivors	Dark Ages	Action - Ruins	$0	Look at the top 2 cards of your deck. Discard them or put them back in any order.									
Dame Anna	Dark Ages	Action - Attack - Knight	$5	You may trash up to 2 cards from your hand.
Each other player reveals the top 2 cards of their deck, trashes one of them costing from $3 to $6, and discards the rest. If a Knight is trashed by this, trash this.					0-2, Self?				
Dame Josephine	Dark Ages	Action - Attack - Victory - Knight	$5	Each other player reveals the top 2 cards of their deck, trashes one of them costing from $3 to $6, and discards the rest. If a Knight is trashed by this, trash this.
2VP					Self?				2VP
Dame Molly	Dark Ages	Action - Attack - Knight	$5	+2 Actions
Each other player discards the top 2 cards of their deck, trashes one of them costing from $3 to $6, and discards the rest. If a Knight is trashed by this, trash this.	+2				Self?				
Dame Natalie	Dark Ages	Action - Attack - Knight	$5	You may gain a card costing up to $3.
Each other player reveals the top 2 cards of their deck, trashes one of them costing from $3 to $6, and discards the rest. If a Knight is trashed by this, trash this.					Self?			1?	
Dame Sylvia	Dark Ages	Action - Attack - Knight	$5	+$2
Each other player reveals the top 2 cards of their deck, trashes one of them costing from $3 to $6, and discards the rest. If a Knight is trashed by this, trash this.				+$2	Self?				
Sir Bailey	Dark Ages	Action - Attack - Knight	$5	+1 Card
+1 Action
Each other player reveals the top 2 cards of their deck, trashes one of them costing from $3 to $6, and discards the rest. If a Knight is trashed by this, trash this.	+1	+1			Self?				
Sir Destry	Dark Ages	Action - Attack - Knight	$5	+2 Cards
Each other player reveals the top 2 cards of their deck, trashes one of them costing from $3 to $6, and discards the rest. If a Knight is trashed by this, trash this.		+2			Self?				
Sir Martin	Dark Ages	Action - Attack - Knight	$4	+2 Buys
Each other player reveals the top 2 cards of their deck, trashes one of them costing from $3 to $6, and discards the rest. If a Knight is trashed by this, trash this.			+2		Self?				
Sir Michael	Dark Ages	Action - Attack - Knight	$5	Each other player discards down to 3 cards in hand.
Each other player reveals the top 2 cards of their deck, trashes one of them costing from $3 to $6, and discards the rest. If a Knight is trashed by this, trash this.					Self?				
Sir Vander	Dark Ages	Action - Attack - Knight	$5	Each other player reveals the top 2 cards of their deck, trashes one of them costing from $3 to $6, and discards the rest. If a Knight is trashed by this, trash this.
When you trash this, gain a Gold.					Self?			*1	
Madman	Dark Ages	Action	$0star	+2 Actions
Return this to the Madman pile. If you do, +1 Card per card in your hand.
(This is not in the Supply.)	+2	+X			Self				
Mercenary	Dark Ages	Action - Attack	$0star	You may trash 2 cards from your hand. If you did, +2 Cards, + $2, and each other player discards down to 3 cards in hand.
(This is not in the Supply.)		+2?		+$2?	2?				
Spoils	Dark Ages	Treasure	$0star	$3
When you play this, return it to the Spoils pile.
(This is not in the Supply.)				+$3	Self				
Hovel	Dark Ages	Reaction - Shelter	$1	When you buy a Victory card, you may trash this from your hand.									
Necropolis	Dark Ages	Action - Shelter	$1	+2 Actions	+2								
Overgrown Estate	Dark Ages	Victory - Shelter	$1	0VP
When you trash this, +1 Card
'''
dictionary.append(one)
dictionary.append(two)
dictionary.append(three)
dictionary.append(four)
dictionary.append(five)
dictionary.append(six)
dictionary.append(seven)
dictionary.append(eight)
dictionary.append(nine)
dictionary.append(ten)
base.append(cellar)
base.append(chapel)
base.append(moat)
base.append(harbinger)
base.append(merchant)
base.append(vassal)
base.append(village)
base.append(workshop)
base.append(bureaucrat)
base.append(gardens)
base.append(militia)
base.append(moneylender)
base.append(poacher)
base.append(remodel)
base.append(smithy)
base.append(throne_room)
base.append(bandit)
base.append(council_room)
base.append(festival)
base.append(laboratory)
base.append(library)
base.append(market)
base.append(mine)
base.append(sentry)
base.append(witch)
base.append(artisan)

#change so base just prints 'base' not everything
dom_expansions.append(base)
dom_expansions.append(dark_ages)

#give cards attributes

hand1 = []
deck1 = []
discard1 =[]
hand2 = []
deck2 = []
discard2 = []
money = 0
InPlay = []
TreasureInHand = []
Buy = 1
Action = 1
Auto = False
HandSize = 5
TurnCount = 1
CopperPile = 60
SilverPile = 40
GoldPile = 30
EstatePile = 14
DutchyPile = 8
ProvincePile = 8
CursePile = 10
EmptyPile = 0

def ShuffleDeck(FirstPlayer) :
    if FirstPlayer :
        for i in range(len(deck1)*5) :
            OldSpot = random.randint(1,len(deck1) - 1)
            NewSpot = random.randint(1,len(deck1) - 1)
            #puts card from oldspot to newspot
            deck1.insert(NewSpot,deck1[OldSpot])
            #takes away card from oldspot
            if NewSpot <= OldSpot :
                deck1.pop(OldSpot + 1)
            else :
                deck1.pop(OldSpot)
    else :
        for i in range(len(deck2)*5) :
            OldSpot = random.randint(1,len(deck2) - 1)
            NewSpot = random.randint(1,len(deck2) - 1)
            #puts card from oldspot to newspot
            deck2.insert(NewSpot,deck2[OldSpot])
            #takes away card from oldspot
            if NewSpot <= OldSpot :
                deck2.pop(OldSpot + 1)
            else :
                deck2.pop(OldSpot)
    
    
def CreateDeck() :
    global CopperPile, EstatePile
    for i in range(7) :
        deck1.append(copper)
        deck2.append(copper)
        CopperPile -= 2
    for i in range(3) :
        deck1.append(estate)
        deck2.append(estate)
        EstatePile -= 2
        
def DrawHand(FirstPlayer, HandSize) :
    #FirstPlayer is true or false
    #HandSize is number - 5
    if FirstPlayer :
        #checks for first player
        while len(hand1) < HandSize :
            try :
                hand1.append(deck1[0])
                #copys top of deck into hand
                deck1.pop(0)
                #takes of top of deck
            except :
                print('')
                print("Shuffling Player 1's deck")
                for i in range(0, len(discard1)) :
                    deck1.append(discard1[0])
                    discard1.pop(0)
                ShuffleDeck(True)
                print('')
                print(deck1)
                print('')
                print('Card count:',str(len(deck1)))
    else :
        while len(hand2) < HandSize :
            try :
                hand2.append(deck2[0])
                #copys top of deck into hand
                deck2.pop(0)
                #takes of top of deck
            except :
                print('')
                print("Shuffling Player 2's deck")
                for i in range(0, len(discard2)) :
                    deck2.append(discard2[0])
                    discard2.pop(0)
                ShuffleDeck(True)
                print('')
                print(deck2)
                print('')
                print('Card count:',str(len(deck2)))
                #puts card into hand since shuffling didn't
                #hand2.append(deck2[0])
                #copys top of deck into hand
                #deck2.pop(0)
                #takes of top of deck

def ActionPhase(FirstPlayer) :
    pass

def BuyPhase(FirstPlayer) :
    if FirstPlayer :
        print('')
        if input('Do you want to autoplay all treasures? ') == 'y' :
            print('')
            Auto = True
        else :
            Auto = False
        PlayTreasures(True, Auto)
        for i in range(0, len(InPlay) - 1) :
            if InPlay[i][2] == 'Treasure' :
                hand1.remove(InPlay[i])
        print('')
        print('Money:', money)
        BuyCard(True)
    else :
        print('')
        if input('Do you want to autoplay all treasures? ') == 'y' :
            print('')
            Auto = True
        else :
            Auto = False
        PlayTreasures(False, Auto)
        for i in range(0, len(InPlay) - 1) :
            if InPlay[i][2] == 'Treasure' :
                #print(InPlay[i],InPlay)
                #print(hand2)
                hand2.remove(InPlay[i])
            #if there are treasures in play take them from the hand
        print('')
        print('Money:', money)
        BuyCard(False)

def RemoveCardFromSupply(Card) :
    global CopperPile, SilverPile, GoldPile, EstatePile, DutchyPile, ProvincePile, CursePile
    if Card == 'Copper' :
        CopperPile -= 1
    elif Card == 'Silver' :
        SilverPile -= 1
    elif Card == 'Gold' :
        GoldPile -= 1
    elif Card == 'Estate' :
        EstatePile -= 1
    elif Card == 'Dutchy' :
        DutchyPile -= 1
    elif Card == 'Province' :
        ProvincePile -= 1
    elif Card == 'Curse' :
        CursePile -= 1
    
def BuyCard(FirstPlayer) :
    global Buy, money
    while Buy > 0 :
        print('')
        CardBought = input('What do you want to buy? ')
        if CardBought == 'n' :
            Buy = 0
        for i in range(0,len(kingdom)) :
            if str(CardBought) == kingdom[i][0] :
                #checks if the card you named is in the kingdom
                if int(kingdom[i][1]) <= int(money) :
                #and if you have enough money to buy it
                    money -= int(kingdom[i][1])
                    if FirstPlayer :
                        discard1.append(kingdom[i])
                    else :
                        discard2.append(kingdom[i])
                    RemoveCardFromSupply(CardBought)
                    Buy -= 1
                    print('')
                    print('You bought a', CardBought)
                    #Add 'takes away card from supply pile'
                    #puts card into discard and takes away money and buy
                else :
                    print('')
                    print('You do not have enough money')
            else :
                #print('That card is not in the kingdom')
                pass
def PlayTreasures(FirstPlayer, AutoplayTreasures) :
    NumTreasurePlayed = 0
    if AutoplayTreasures :
        Auto = True
    else :
        Auto = False
    if FirstPlayer :
        for i in range(len(hand1)) :
            if IsTreasure(True,i) :
                TreasureInHand.append(hand1[i])
                AddMoney(NumTreasurePlayed, Auto)
                NumTreasurePlayed += 1
            else :
                pass
    else :
        for i in range(0, len(hand2)) :
            if IsTreasure(False,i) :
                TreasureInHand.append(hand2[i])
                AddMoney(NumTreasurePlayed, Auto)
                #NumTPlayed will give the right spot for card in hand
                NumTreasurePlayed += 1
            else :
                pass
def IsTreasure(FirstPlayer,CardSpot) :
    if FirstPlayer :
        if 'Treasure' == hand1[CardSpot][2] :
            return True
        else :
            return False
    else :
        if 'Treasure' == hand2[CardSpot][2] :
            return True
        else :
            return False
def AddMoney(CardSpot,AutoPlayTreasures) :
    global money
    if AutoPlayTreasures :
        #CardSpot is referring last treasure played
        money += int(TreasureInHand[CardSpot][3])
        InPlay.append(TreasureInHand[CardSpot])
        print('played',TreasureInHand[CardSpot][0])
    elif input('Do you want to play ' + str(TreasureInHand[CardSpot][0]) + '?') == 'y' :
        money += int(TreasureInHand[CardSpot][3])
        InPlay.append(TreasureInHand[CardSpot])
    else :
        pass

def CleanUp(FirstPlayer) :
    if FirstPlayer :
        for i in range(0,len(hand1)) :
            try :
                discard1.append(hand1[0])
                hand1.pop(0)
            except :
                print('cannot discard from hand')
        for i in range(0, len(InPlay)) :
            try :
                discard1.append(InPlay[0])
                InPlay.pop(0)
            except :
                print('cannot discard from play')
    else :
        for i in range(0,len(hand2)) :
            try :
                discard2.append(hand2[0])
                hand2.pop(0)
            except :
                pass
        for i in range(0, len(InPlay)) :
            try :
                discard2.append(InPlay[0])
                InPlay.pop(0)
            except :
                pass   


def pick_kingdom() :
    #card = base[random.randint(0,len(base) - 1)]
    #kingdom.append(card)
    card = None
    num_of_times = 1
    king = 0
    base_num = 0
    dark_num = 0
    less_base = 1
    less_dark = 1
    tries = 0
    while len(kingdom) < 10 :
        if tries > 5000 :
            print('That was too hard')
            break
        tries = tries + 1
        global num_cost_had
        if expan_used[king] == 'base' :
            card = base[random.randint(0,len(base) - 1)]
        elif expan_used[king] == 'dark' :
            card = dark_ages[random.randint(0,len(dark_ages) - 1)]
        elif expan_used[king] == 'random' :
            dom_set = random.randint(0,len(dom_expansions) - 1)
            if len(not_expan) >= 1 :
                if not_expan[0] == 'base' :
                    dom_set = 1
                if not_expan[0] == 'dark' :
                    dom_set = 0
                #not full
            if base_num >= less_base :
                dom_set = 1
                #this is dark ages index
            if dark_num >= less_dark :
                dom_set = 0
                #this is base index
            #dom_set = index of a random expansion
            card = dom_expansions[dom_set][random.randint(0,len(dom_expansions[dom_set]) - 1)]
        if card[1] == not_cost :
            card = None
        if card_cost[king] == 'random' :
            if card_cost[0] == 'random' :
                pass
            elif card[1] == card_cost[0] :
                card = None
        elif card[1] == card_cost[king] :
            num_cost_had = num_cost_had + 1
            if num_cost_had > num_cost_total :
                card = None
        else :
            card = None      
        #do this with sort
        if card not in kingdom and card != None :
            if expan_used[king] == 'base' :
                base_num = base_num + 1
            if expan_used[king] == 'dark' :
                dark_num = dark_num + 1
            king = king + 1
            if not kingdom :
                kingdom.append(card)
            elif int(card[1]) >= int(kingdom[len(kingdom) - 1][1]) :
                kingdom.append(card)
            elif int(card[1]) <= int(kingdom[0][1]) :
                kingdom.insert(0,card)
            elif int(card[1]) <= int(kingdom[1][1]) :
                kingdom.insert(1,card)
            elif int(card[1]) <= int(kingdom[2][1]) :
                kingdom.insert(2,card)
            elif int(card[1]) <= int(kingdom[3][1]) :
                kingdom.insert(3,card)
            elif int(card[1]) <= int(kingdom[4][1]) :
                kingdom.insert(4,card)
            elif int(card[1]) <= int(kingdom[5][1]) :
                kingdom.insert(5,card)
            elif int(card[1]) <= int(kingdom[6][1]) :
                kingdom.insert(6,card)
            elif int(card[1]) <= int(kingdom[7][1]) :
                kingdom.insert(7,card)
            elif int(card[1]) <= int(kingdom[8][1]) :
                kingdom.insert(8,card)
            elif int(card[1]) <= int(kingdom[9][1]) :
                kingdom.insert(9,card)
            num_of_times = num_of_times + 1
    kingdom.append(copper)
    kingdom.append(silver)
    kingdom.append(gold)
    kingdom.append(estate)
    kingdom.append(dutchy)
    kingdom.append(province)
    kingdom.append(curse)
    for i in range(0,17) :
        print(kingdom[i][0])
    check_kingdom()
    
def check_kingdom() :
    done = False
    while done == False :
        print('')
        print('what is the position of the card do you want to check?')
        try : 
            what_card = int(input()) - 1
            print('Name: ' + str(kingdom[what_card][0]))
            print('Cost: ' + str(kingdom[what_card][1]))
            print('Type: ' + str(kingdom[what_card][2]))
            if len(kingdom[what_card]) >= 5 :
                print('Type: ' + str(kingdom[what_card][3]))
                print('Text: ' + str(kingdom[what_card][4]))
            else :
                print('Text: ' + str(kingdom[what_card][3]))
        except :
            print('That is not a number')
        more = input('Are you done?')
        if more == 'yes' or more == '' :
            done = True
def split_ans() :
    global actual
    while working == False :
        want = input()
        actual = want.split()
        translate()
        print(actual)
        check_keywords(actual)
    pick_kingdom()
def translate() :
    global actual
    if 'one' in actual :
        actual.insert(actual.index('one'),'1')
        actual.pop(actual.index('one'))
    if 'two' in actual :
        actual.insert(actual.index('two'),'2')
        actual.pop(actual.index('two'))
    if 'three' in actual :
        actual.insert(actual.index('three'),'3')
        actual.pop(actual.index('three'))
    if 'four' in actual :
        actual.insert(actual.index('four'),'4')
        actual.pop(actual.index('four'))
    if 'five' in actual :
        actual.insert(actual.index('five'),'5')
        actual.pop(actual.index('five'))
    if 'six' in actual :
        actual.insert(actual.index('six'),'6')
        actual.pop(actual.index('six'))
    if 'seven' in actual :
        actual.insert(actual.index('seven'),'7')
        actual.pop(actual.index('seven'))
    if 'eight' in actual :
        actual.insert(actual.index('eight'),'8')
        actual.pop(actual.index('eight'))
    if 'nine' in actual :
        actual.insert(actual.index('nine'),'9')
        actual.pop(actual.index('nine'))
    if 'ten' in actual :
        actual.insert(actual.index('ten'),'10')
        actual.pop(actual.index('ten'))
    if 'expansions' in actual :
        actual.insert(actual.index('expansions'),'expansion')
        actual.pop(actual.index('expansions'))
    if 'money' in actual :
        actual.insert(actual.index('money'),'cost')
        actual.pop(actual.index('money'))
    if 'worth' in actual :
        actual.insert(actual.index('worth'),'cost')
        actual.pop(actual.index('worth'))
    if 'costs' in actual :
        actual.insert(actual.index('costs'),'cost')
        actual.pop(actual.index('costs'))   
    if 'set' in actual :
        actual.insert(actual.index('set'),'expansion')
        actual.pop(actual.index('set'))
    if 'none' in actual :
        actual.insert(actual.index('none'),'no')
        actual.pop(actual.index('none'))
    if 'a' in actual :
        actual.insert(actual.index('a'),'1')
        actual.pop(actual.index('a'))
    if 'the' in actual :
        actual.pop(actual.index('the'))
    if 'I' in actual :
        actual.pop(actual.index('I'))
    if 'want' in actual :
        actual.pop(actual.index('want'))
    if 'there' in actual :
        actual.pop(actual.index('there'))
    if 'my' in actual :
        actual.pop(actual.index('my'))
    if 'card' in actual :
        actual.pop(actual.index('card'))
    if 'cards' in actual :
        actual.pop(actual.index('cards'))
    if 'of' in actual :
        actual.pop(actual.index('of'))
    if 'to' in actual :
        actual.pop(actual.index('to'))
    if 'be' in actual :
        actual.pop(actual.index('be'))
    if 'that' in actual :
        actual.pop(actual.index('that'))
    if 'i' in actual :
        actual.pop(actual.index('i'))
    if 'can' in actual :
        actual.pop(actual.index('can'))
    if 'have' in actual :
        actual.pop(actual.index('have'))
    if 'with' in actual :
        actual.pop(actual.index('with'))
    if 'like' in actual :
        actual.pop(actual.index('like'))
    if 'would' in actual :
        actual.pop(actual.index('would'))
    if 'any' in actual and actual[actual.index('any') - 1] == 'not' :
        actual.insert(actual.index('any'),'no')
        actual.pop(actual.index('any')) 
    if 'not' in actual :
        actual.pop(actual.index('not'))
def check_keywords(sent) :
    global working, less_dark, less_base, num_cost_total, not_cost, not_expan
    #sees how many from base
    if 'less' in sent and sent[sent.index('less') + 1] == 'than' and sent[sent.index('less') + 2].isnumeric() == True and sent[sent.index('less') + 3] == 'from' :
        if sent[sent.index('less') + 4] == 'base' :
            less_base = sent[sent.index('less') + 2]
        elif sent[sent.index('less') + 4] == 'dark' :
            less_dark = sent[sent.index('less') + 2]
    if 'base' in sent :
        if sent[sent.index('base') - 1] == 'from' :
            if sent[sent.index('base') - 2].isnumeric() == True :
                for i in range(int(sent[sent.index('base') - 2])) :
                    expan_used.append('base')
                less_base = int(sent[sent.index('base') - 2]) + 10
            if sent[sent.index('base') - 2] == 'rest' :
                while len(expan_used) < 10 :
                    expan_used.append('base')
            if sent[sent.index('base') - 2] == 'no' :
                not_expan.append('base')
    if 'dark' in sent :
        if sent[sent.index('dark') + 1] == 'ages' and sent[sent.index('dark') - 1] == 'from' :
            if sent[sent.index('dark') - 2].isnumeric() == True :   
                for i in range(int(sent[sent.index('dark') - 2])) :
                    expan_used.append('dark')
                less_dark = int(sent[sent.index('dark') - 2]) + 2
            if sent[sent.index('dark') - 2] == 'rest' :
                while len(expan_used) < 10 :
                    expan_used.append('dark')
            if sent[sent.index('dark') - 2] == 'no' :
                not_expan.append('dark')
    if 'expansion' in sent :
        if str(sent[sent.index('expansion') - 1]) not in dom_expansions :
            print(str(sent[sent.index('expansion') - 1]) + ' is not an expansion.')
    if 'cost' in sent :
        if sent[sent.index('cost') + 1].isnumeric() == True :
            if sent[sent.index('cost') - 1].isnumeric() == True :   
                for i in range(int(sent[sent.index('cost') - 1])) :
                    card_cost.append(sent[sent.index('cost') + 1])
                    num_cost_total = int(sent[sent.index('cost') - 1])
                    
            if sent[sent.index('cost') - 1] == 'no' :
                not_cost = sent[sent.index('cost') + 1]
    
    '''
    for i in range(0,len(card_list) - 1) :
        if card_list[i] in sent :
            kingdom.append(card_list[i])
    '''
    if len(expan_used) > 10 :
        print('You have too many cards in the kingdom. There are ten cards in a kingdom.')
        print('')
        print('What do you want in your kingdom?')
    if len(card_cost) > 10 :
        print('You have too many cost restrictions in the kingdom. There are ten cards in a kingdom.')
        print('')
        print('What do you want in your kingdom?')
    if len(expan_used) < 10 :
        while len(expan_used) < 10 :
            expan_used.append('random')
    if len(card_cost) < 10 :
        while len(card_cost) < 10 :
            card_cost.append('random')
    if len(expan_used) == 10 and len(card_cost) == 10 :
        working = True
def customise_kingdom() :
    print('What do you want in your kingdom?')
    split_ans()

def StartGame() :
    customise_kingdom()
    CreateDeck()
    ShuffleDeck(True)
    ShuffleDeck(False)
    print('')
    print("Player 1's 1 turn.")
    DrawHand(True, 5)
    DrawHand(False, 5)
    Turn(True)
    
def StartTurn(FirstPlayer) :
    global money, Buy, Action
    Buy = 1
    Action = 1
    money = 0
    if FirstPlayer :
        print('')
        print('Hand:', hand1[0][0],hand1[1][0],hand1[2][0],hand1[3][0],hand1[4][0])
    else :
        print('')
        print('Hand:', hand2[0][0],hand2[1][0],hand2[2][0],hand2[3][0],hand2[4][0])
    
def CheckWin() :
    global EmptyPile
    if ProvincePile == 0 :
        print('')
        print('Game over')
    if CopperPile == 0 :
        EmptyPile += 1
    if SilverPile == 0 :
        EmptyPile += 1
    if GoldPile == 0 :
        EmptyPile += 1
    if EstatePile == 0 :
        EmptyPile += 1
    if DutchyPile == 0 :
        EmptyPile += 1
    if ProvincePile == 0 :
        EmptyPile += 1
    if CursePile == 0 :
        EmptyPile += 1
    if EmptyPile >= 3 :
        print('')
        print('Game over')

def Turn(FirstPlayer) :
    global TurnCount
    StartTurn(FirstPlayer)
    ActionPhase(FirstPlayer)
    BuyPhase(FirstPlayer)
    CleanUp(FirstPlayer)
    CheckWin()
    DrawHand(FirstPlayer, HandSize)
    if FirstPlayer :
        print('')
        print("Player 2's", TurnCount, 'turn.')
        Turn(False)
    else :
        TurnCount += 1
        print('')
        print("Player 1's", TurnCount, 'turn.')
        Turn(True)
StartGame()
