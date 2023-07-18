import random, time, sys

    #PROBLEMS

    #sometimes plays action twice?
    #lose treasure if not play??
    #Rohan does not work
    #Throne room does not work
    #Chapel can't see last(some) card in hand (only before drawing any cards)
    #Error if no cards left to draw and try to - trys to take len() of nothing  - Make try else
    #Shuffles deck after first buy...
    #doesn't print cards drawn

    #NEW FEATURES

    #Make option to choose starting hands
    #reprint out kingdom if ask

#add more expan
#put in specific cards
#limit cost - works but not only that num - no gives one?
#What can do: choose num cards in expan, cost of cards in kingdom, check cards in kingdom
trash = []
dom_expansions = []
base = []
dark_ages = []
JL_Expansion = []
coded = []
kingdom = []
dictionary = []
expan_used = []
expan = []
card_cost = []
not_cost = []
num_cost_had = 0
num_cost_total = 0
king = 0
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

bridge = ('Bridge','4','Action','+1 Buy +$1 everything costs 1 less but not less than 0')
rohan = ('Rohan','3','Action','You may discard a Victory card for +1 Action +3 Cards.')
misty_mountians = ('Misty Mountians','3','Action','Discard a card, +1 Card You may trash up to 2 cards from your discard pile.')
bill_ferny = ('Bill Ferny','5','Action','+$2, if you have excactly 4 cards in hand +$2')

JL_Expansion.append(bridge)
JL_Expansion.append(rohan)
JL_Expansion.append(misty_mountians)
JL_Expansion.append(bill_ferny)

coded.append(bridge)
coded.append(laboratory)
coded.append(workshop)
coded.append(witch)
coded.append(village)
coded.append(smithy)
coded.append(bill_ferny)
coded.append(junk_dealer)
coded.append(chapel)
coded.append(market)
coded.append(bridge)
coded.append(throne_room)
coded.append(moneylender)

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

#AI Attributes
ActionAI = False
#Player Attributes
PlayerOnePoints = 3
PlayerTwoPoints = 3
hand1 = []
deck1 = []
discard1 =[]
hand2 = []
deck2 = []
discard2 = []
#Turn
CostReduction = 0
ActionsInHand = 0
AI = False
money = 0
InPlay = []
TreasureInHand = []
Drawn = []
Buy = 1
Action = 1
Auto = False
HandSize = 5
TurnCount = 1
#Card Piles
CopperPile = 60
SilverPile = 40
GoldPile = 30
EstatePile = 14
DutchyPile = 8
ProvincePile = 8
CursePile = 10
EmptyPile = 0
Pile1 = 10
Pile2 = 10
Pile3 = 10
Pile4 = 10
Pile5 = 10
Pile6 = 10
Pile7 = 10
Pile8 = 10
Pile9 = 10
Pile10 = 10
Pile1Name = None
Pile2Name = None
Pile3Name = None
Pile4Name = None
Pile5Name = None
Pile6Name = None
Pile7Name = None
Pile8Name = None
Pile9Name = None
Pile10Name = None #set cards to names
               
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

def DrawCards(FirstPlayer, NumCards) :
    global ActionsInHand
    Drawn = []
    NewHandSize = len(PlayerHand(FirstPlayer)) + NumCards
    while len(PlayerHand(FirstPlayer)) < NewHandSize :
        try :
            PlayerHand(FirstPlayer).append(PlayerDeck(FirstPlayer)[0]) #draw card
            PlayerDeck(FirstPlayer).pop(0)
            Drawn.append(PlayerDeck(FirstPlayer)[0])
        except : #if deck is empty
            if len(PlayerDiscard(FirstPlayer)) == 0 : #if you drew your deck
                #return Drawn #return how many cards drawn
                break
            if FirstPlayer :
                print("Shuffling", str(P1Name) + "'s deck") 
            else :
                print("Shuffling", str(P2Name) + "'s deck")
            PlayerDeck(FirstPlayer).extend(PlayerDiscard(FirstPlayer))#add discard to deck
            while len(PlayerDiscard(FirstPlayer)) > 0 : #delete discard
                PlayerDiscard(FirstPlayer).pop(0) 
            random.shuffle(PlayerDeck(FirstPlayer)) #shuffle deck
        else :
            if str(PlayerHand(FirstPlayer)[-1][2]) == 'Action' : #check for action cards
                ActionsInHand += 1
    #return Drawn #return how many cards drawn

def AddCards(Num,List,FirstPlayer,Cardspot) :
    for i in range(Num) :
        List = str(Cardspot(FirstPlayer)[-i][0]) + ' ' + List
    return List
def CardsInHand(Num,FirstPlayer,Cardspot) :
    cardsinhand = ''
    Hand = AddCards(Num,cardsinhand,FirstPlayer,Cardspot)
    return Hand
    
def PrintCards(FirstPlayer,Place,CardSpot) :
    Num = len(CardSpot(FirstPlayer))

    #prints Cran's hand
    print(Place + ':',CardsInHand(Num,FirstPlayer,CardSpot))

    '''      
    if Num == 0 :
        print(Place)
    if Num == 1 :
        print(Place + ':',str(PlayerHand(FirstPlayer)[-1][0]))
    if Num == 2 :
        print(Place + ':',str(PlayerHand(FirstPlayer)[-2][0]),str(PlayerHand(FirstPlayer)[-1][0]))
    if Num == 3 :
        print(Place + ':',str(PlayerHand(FirstPlayer)[-3][0]),str(PlayerHand(FirstPlayer)[-2][0]),str(PlayerHand(FirstPlayer)[-1][0]))
    if Num == 4 :
        print(Place + ':',str(PlayerHand(FirstPlayer)[-4][0]),str(PlayerHand(FirstPlayer)[-3][0]),str(PlayerHand(FirstPlayer)[-2][0]),str(PlayerHand(FirstPlayer)[-1][0]))
    if Num == 5 :
        print(Place + ':',str(PlayerHand(FirstPlayer)[-5][0]),str(PlayerHand(FirstPlayer)[-4][0]),str(PlayerHand(FirstPlayer)[-3][0]),str(PlayerHand(FirstPlayer)[-2][0]),str(PlayerHand(FirstPlayer)[-1][0]))
    if Num == 6 :
        print(Place + ':',str(PlayerHand(FirstPlayer)[-6][0]),str(PlayerHand(FirstPlayer)[-5][0]),str(PlayerHand(FirstPlayer)[-4][0]),str(PlayerHand(FirstPlayer)[-3][0]),str(PlayerHand(FirstPlayer)[-2][0]),str(PlayerHand(FirstPlayer)[-1][0]))
    if Num == 7 :
        print(Place + ':',str(PlayerHand(FirstPlayer)[-7][0]),str(PlayerHand(FirstPlayer)[-6][0]),str(PlayerHand(FirstPlayer)[-5][0]),str(PlayerHand(FirstPlayer)[-4][0]),str(PlayerHand(FirstPlayer)[-3][0]),str(PlayerHand(FirstPlayer)[-2][0]),str(PlayerHand(FirstPlayer)[-1][0]))
    if Num == 8 :
        print(Place + ':',str(PlayerHand(FirstPlayer)[-8][0]),str(PlayerHand(FirstPlayer)[-7][0]),str(PlayerHand(FirstPlayer)[-6][0]),str(PlayerHand(FirstPlayer)[-5][0]),str(PlayerHand(FirstPlayer)[-4][0]),str(PlayerHand(FirstPlayer)[-3][0]),str(PlayerHand(FirstPlayer)[-2][0]),str(PlayerHand(FirstPlayer)[-1][0]))
    if Num == 9 :
        print(Place + ':',str(PlayerHand(FirstPlayer)[-9][0]),str(PlayerHand(FirstPlayer)[-8][0]),str(PlayerHand(FirstPlayer)[-7][0]),str(PlayerHand(FirstPlayer)[-6][0]),str(PlayerHand(FirstPlayer)[-5][0]),str(PlayerHand(FirstPlayer)[-4][0]),str(PlayerHand(FirstPlayer)[-3][0]),str(PlayerHand(FirstPlayer)[-2][0]),str(PlayerHand(FirstPlayer)[-1][0]))
    if Num == 10 :
        print(Place + ':',str(PlayerHand(FirstPlayer)[-10][0]),str(PlayerHand(FirstPlayer)[-9][0]),str(PlayerHand(FirstPlayer)[-8][0]),str(PlayerHand(FirstPlayer)[-7][0]),str(PlayerHand(FirstPlayer)[-6][0]),str(PlayerHand(FirstPlayer)[-5][0]),str(PlayerHand(FirstPlayer)[-4][0]),str(PlayerHand(FirstPlayer)[-3][0]),str(PlayerHand(FirstPlayer)[-2][0]),str(PlayerHand(FirstPlayer)[-1][0]))
    if Num == 11 :
        print(Place + ':',str(PlayerHand(FirstPlayer)[-11][0]),str(PlayerHand(FirstPlayer)[-10][0]),str(PlayerHand(FirstPlayer)[-9][0]),str(PlayerHand(FirstPlayer)[-8][0]),str(PlayerHand(FirstPlayer)[-7][0]),str(PlayerHand(FirstPlayer)[-6][0]),str(PlayerHand(FirstPlayer)[-5][0]),str(PlayerHand(FirstPlayer)[-4][0]),str(PlayerHand(FirstPlayer)[-3][0]),str(PlayerHand(FirstPlayer)[-2][0]),str(PlayerHand(FirstPlayer)[-1][0]))
    if Num == 12 :
        print(Place + ':',str(PlayerHand(FirstPlayer)[-12][0]),str(PlayerHand(FirstPlayer)[-11][0]),str(PlayerHand(FirstPlayer)[-10][0]),str(PlayerHand(FirstPlayer)[-9][0]),str(PlayerHand(FirstPlayer)[-8][0]),str(PlayerHand(FirstPlayer)[-7][0]),str(PlayerHand(FirstPlayer)[-6][0]),str(PlayerHand(FirstPlayer)[-5][0]),str(PlayerHand(FirstPlayer)[-4][0]),str(PlayerHand(FirstPlayer)[-3][0]),str(PlayerHand(FirstPlayer)[-2][0]),str(PlayerHand(FirstPlayer)[-1][0]))
    if Num == 13 :
        print(Place + ':',str(PlayerHand(FirstPlayer)[-13][0]),str(PlayerHand(FirstPlayer)[-12][0]),str(PlayerHand(FirstPlayer)[-11][0]),str(PlayerHand(FirstPlayer)[-10][0]),str(PlayerHand(FirstPlayer)[-9][0]),str(PlayerHand(FirstPlayer)[-8][0]),str(PlayerHand(FirstPlayer)[-7][0]),str(PlayerHand(FirstPlayer)[-6][0]),str(PlayerHand(FirstPlayer)[-5][0]),str(PlayerHand(FirstPlayer)[-4][0]),str(PlayerHand(FirstPlayer)[-3][0]),str(PlayerHand(FirstPlayer)[-2][0]),str(PlayerHand(FirstPlayer)[-1][0]))
    if Num == 14 :
        print(Place + ':',str(PlayerHand(FirstPlayer)[-14][0]),str(PlayerHand(FirstPlayer)[-13][0]),str(PlayerHand(FirstPlayer)[-12][0]),str(PlayerHand(FirstPlayer)[-11][0]),str(PlayerHand(FirstPlayer)[-10][0]),str(PlayerHand(FirstPlayer)[-9][0]),str(PlayerHand(FirstPlayer)[-8][0]),str(PlayerHand(FirstPlayer)[-7][0]),str(PlayerHand(FirstPlayer)[-6][0]),str(PlayerHand(FirstPlayer)[-5][0]),str(PlayerHand(FirstPlayer)[-4][0]),str(PlayerHand(FirstPlayer)[-3][0]),str(PlayerHand(FirstPlayer)[-2][0]),str(PlayerHand(FirstPlayer)[-1][0]))
    if Num == 15 :
        print(Place + ':',str(PlayerHand(FirstPlayer)[-15][0]),str(PlayerHand(FirstPlayer)[-14][0]),str(PlayerHand(FirstPlayer)[-13][0]),str(PlayerHand(FirstPlayer)[-12][0]),str(PlayerHand(FirstPlayer)[-11][0]),str(PlayerHand(FirstPlayer)[-10][0]),str(PlayerHand(FirstPlayer)[-9][0]),str(PlayerHand(FirstPlayer)[-8][0]),str(PlayerHand(FirstPlayer)[-7][0]),str(PlayerHand(FirstPlayer)[-6][0]),str(PlayerHand(FirstPlayer)[-5][0]),str(PlayerHand(FirstPlayer)[-4][0]),str(PlayerHand(FirstPlayer)[-3][0]),str(PlayerHand(FirstPlayer)[-2][0]),str(PlayerHand(FirstPlayer)[-1][0]))
    if Num == 16 :
        print(Place + ':',str(PlayerHand(FirstPlayer)[-16][0]),str(PlayerHand(FirstPlayer)[-15][0]),str(PlayerHand(FirstPlayer)[-14][0]),str(PlayerHand(FirstPlayer)[-13][0]),str(PlayerHand(FirstPlayer)[-12][0]),str(PlayerHand(FirstPlayer)[-11][0]),str(PlayerHand(FirstPlayer)[-10][0]),str(PlayerHand(FirstPlayer)[-9][0]),str(PlayerHand(FirstPlayer)[-8][0]),str(PlayerHand(FirstPlayer)[-7][0]),str(PlayerHand(FirstPlayer)[-6][0]),str(PlayerHand(FirstPlayer)[-5][0]),str(PlayerHand(FirstPlayer)[-4][0]),str(PlayerHand(FirstPlayer)[-3][0]),str(PlayerHand(FirstPlayer)[-2][0]),str(PlayerHand(FirstPlayer)[-1][0]))
    '''
    
def PlayActionCard(FirstPlayer, ActionCount) :
    global Action, ActionsInHand
    ActionsInHand = ActionCount
    while Action > 0 and ActionsInHand > 0:
        played_card = False
        ans = TranslateCardNames(input('Which Action card do you want to play? '))
        if ans == 'n' :
            Action = 0
            ActionsInHand = 0
        elif ans == 'info' :
            PrintInfo(FirstPlayer)
        for i in range(0,len(PlayerHand(FirstPlayer))) :
            #print(str(PlayerHand(FirstPlayer)[i][0]))
            try :
                str(ans) == PlayerHand(FirstPlayer)[i][0]
            except :
                pass
            else :
                if str(ans) == PlayerHand(FirstPlayer)[i][0] and str(PlayerHand(FirstPlayer)[i][2]) == 'Action' and played_card == False :
                    time.sleep(0.5)
                    print('Played ' + str(PlayerHand(FirstPlayer)[i][0]))
                    InPlay.append(PlayerHand(FirstPlayer)[i])
                    ActionsInHand -= 1
                    PlayActionBank(FirstPlayer,PlayerHand(FirstPlayer)[i][0],PlayerHand(FirstPlayer)[i])
                    played_card = True
        if played_card == False :
            print('You do not have that card')
            PlayActionCard(FirstPlayer, ActionsInHand)

def PlayActionBank(FirstPlayer, CardName, CardPlayed) :
    global Action
    Action -= 1
    PlayerHand(FirstPlayer).remove(CardPlayed)
    if CardName == 'Chapel' :
        PlayChapel(FirstPlayer)
    if CardName == 'Smithy' :
        PlaySmithy(FirstPlayer)
    if CardName == 'Village' :
        PlayVillage(FirstPlayer)
    if CardName == 'Market' :
        PlayMarket(FirstPlayer)
    if CardName == 'Workshop' :
        PlayWorkshop(FirstPlayer)
    if CardName == 'Laboratory' :
        PlayLaboratory(FirstPlayer)
    if CardName == 'Witch' :
        PlayWitch(FirstPlayer)
    if CardName == 'Junk Dealer' :
        PlayJunkDealer(FirstPlayer)
    if CardName == 'Bridge' :
        PlayBridge()
    if CardName == 'Bill Ferny' :
        PlayBillFerny(FirstPlayer)
    if CardName == 'Rohan' :
        PlayRohan(FirstPlayer)
    if CardName == 'Throne Room' :
        PlayThroneRoom(FirstPlayer)
    if CardName == 'Moneylender' :
        PlayMoneylender(FirstPlayer)

def TranslateCardNames(Name) :
    if Name == 'Lab' or Name == 'lab' :
        return 'Laboratory'
    elif Name == 'Vil' or Name == 'Vill' or Name == 'vil' :
        return 'Village'
    elif Name == 'Ferny' or Name == 'fern' or Name == 'ferny' :
        return 'Bill Ferny'
    elif Name == 'Junk' or Name == 'junk' :
        return 'Junk Dealer'
    elif Name == 'Work' or Name == 'work' :
        return 'Workshop'
    elif Name == 'Smi' or Name == 'smi' :
        return 'Smithy'
    elif Name == 'throne' or Name == 'Throne' or Name == 'thro' :
        return 'Throne Room'
    elif Name == 'mark' :
        return 'Market'
    elif Name == 'chap' :
        return 'Chapel'
    elif Name == 'money' or Name == 'Money' or Name == 'ml' :
        return 'Moneylender'
    else :
        return Name

def PlayMoneylender(FirstPlayer) :
    global money
    time.sleep(0.25)
    if TrashCards(FirstPlayer, 1, 'Copper') :
        money += 3
    time.sleep(0.25)
    print('Actions:',str(Action))
    print('Money:',str(money))
    
def PlayThroneRoom(FirstPlayer) :
    global Action
    while True :
        ans = TranslateCardNames(input('What Action card do you want to throne? '))
        if ans == 'n' :
            break
        for i in range(0, len(PlayerHand(FirstPlayer))) :
            if ans == PlayerHand(FirstPlayer)[i][0] and 'Action' == PlayerHand(FirstPlayer)[i][2]:
                CardName = PlayerHand(FirstPlayer)[i][0]
                CardPlayed = PlayerHand(FirstPlayer)[i]
                PlayActionBank(FirstPlayer, CardName, CardPlayed)
                Action += 1
                PlayActionBank(FirstPlayer, CardName, CardPlayed)
                break
            else :
                #print('That is not in your hand')
                pass

def PlayRohan(FirstPlayer) :
    global Action
    card_discarded = False
    ans = input('What Victory card do you want to discard? ')
    for i in range(0, len(PlayerHand(FirstPlayer))) :
        if str(ans) == PlayerHand(FirstPlayer)[i] and 'Victory' == PlayerHand(FirstPlayer)[i][2] :
            DiscardCard(FirstPlayer, i)
            Action += 1
            ActionDrawCards(FirstPlayer, 3)
        else :
            print('Actions: ' + str(Action))
            time.sleep(0.25)

def PlayBillFerny(FirstPlayer) :
    global money
    print('Actions: ' + str(Action))
    money += 2
    if len(PlayerHand(FirstPlayer)) == 4 :
        money += 2
    print('Money:',str(money))

def PlayBridge() :
    global money, Buy, CostReduction
    print('Actions: ' + str(Action))
    time.sleep(0.25)
    Buy += 1
    money += 1
    CostReduction += 1

def PlayJunkDealer(FirstPlayer) :
    global Action, money
    Action += 1
    money += 1
    ActionDrawCards(FirstPlayer, 1)
    TrashCards(FirstPlayer, 1)

def PlayWitch(FirstPlayer) :
    global PlayerOnePoints, PlayerTwoPoints
    ActionDrawCards(FirstPlayer, 2)
    if CursePile >= 1 :
        if FirstPlayer :
            print(P2Name, 'gained a Curse')
            PlayerDiscard(False).append(kingdom[16])
            PlayerTwoPoints -= 1
        else :
            print(P1Name, 'gained a Curse')
            PlayerDiscard(True).append(kingdom[16])
            PlayerOnePoints -= 1
        RemoveCardFromSupply('Curse')

def PlayWorkshop(FirstPlayer) :
    while True :
        CardBought = input('What do you want to gain? ')
        for i in range(0,len(kingdom)) :
                if str(CardBought) == kingdom[i][0] :
                    #checks if the card you named is in the kingdom 
                    if int(kingdom[i][1]) <= 4 :
                    #and if you have enough money to buy it
                        if RemoveCardFromSupply(CardBought) :
                            #and if there are any left
                            PlayerDiscard(FirstPlayer).append(kingdom[i])
                            print('You gained a', CardBought)
                            if kingdom[i][2] == 'Victory' :
                                if FirstPlayer :
                                    PlayerOnePoints += int(kingdom[i][3])
                                else :
                                    PlayerTwoPoints += int(kingdom[i][3])
                            break
                        else :
                            print('There are no more',str(kingdom[i][0]) + 's')
                    else :
                        print('That costs too much')
                else :
                    #print('That card is not in the kingdom')
                    pass

def ActionDrawCards(FirstPlayer, CardNum) :
    print('Actions: ' + str(Action))
    time.sleep(0.25)
    DrawCards(FirstPlayer, CardNum)
    PrintCards(FirstPlayer, 'Drew', FindDrawn)
    time.sleep(0.25)

def DiscardCard(FirstPlayer, CardPos) :
    print('Discarded',PlayerHand(FirstPlayer)[CardPos])
    PlayerDiscard(FirstPlayer).append(PlayerHand(FirstPlayer)[CardPos])
    PlayerHand(FirstPlayer).pop(CardPos)
        
def PlayMarket(FirstPlayer) :
    global Action, money, Buy
    Action += 1
    money += 1
    Buy += 1
    ActionDrawCards(FirstPlayer, 1) #draw and show which card(s) drawn
    #PrintDrawAction(FirstPlayer, 1)
    
def PlayLaboratory(FirstPlayer) :
    global Action
    Action += 1
    ActionDrawCards(FirstPlayer, 2)

def PlaySmithy(FirstPlayer) :
    ActionDrawCards(FirstPlayer, 3)
    
def PlayVillage(FirstPlayer) :
    global Action
    Action += 2
    ActionDrawCards(FirstPlayer, 1)

def PlayChapel(FirstPlayer) :
    print('Actions: ' + str(Action))
    time.sleep(0.25)
    TrashCards(FirstPlayer, 4)

def TrashCards(FirstPlayer, TrashNum, *SpefCard) :
    trashcount = 0
    while trashcount < TrashNum :
        card_trashed = False
        try :
            tryit = SpefCard[0]
        except :
            time.sleep(0.25)
            ans = TranslateCardNames(input('Which card do you want to trash? '))
        else :
            ans = SpefCard[0]
        if ans == 'n' :
            break
        for i in range(0,len(PlayerHand(FirstPlayer)) - 1) :
            #print(len(PlayerHand(FirstPlayer)))
            #print(i)
            if ans == PlayerHand(FirstPlayer)[i][0] and card_trashed == False :
                Trash(FirstPlayer, i, PlayerHand(FirstPlayer)[i])
                trashcount += 1
                card_trashed = True
        if not card_trashed :
            print("You can't trash that card")
    if card_trashed :
        return True

def Trash(FirstPlayer, HandPos, Card) :
    global PlayerOnePoints, PlayerTwoPoints, ActionsInHand
    trash.append(PlayerHand(FirstPlayer)[HandPos])
    if Card[2] == 'Victory' :
        if FirstPlayer :
            PlayerOnePoints -= int(Card[3])
        else :
            PlayerTwoPoints -= int(Card[3])
    elif Card[2] == 'Curse' :
        if FirstPlayer :
            PlayerOnePoints += 1
        else :
            PlayerTwoPoints += 1
    elif Card[2] == 'Action' :
        ActionsInHand -= 1
    PlayerHand(FirstPlayer).remove(Card)
    print('Trashed',str(Card[0]))

def ActionPhase(FirstPlayer) :
    action_count = 0
    for i in range(0,len(PlayerHand(FirstPlayer))) :
        #print(PlayerHand(FirstPlayer)[i][2])
        if PlayerHand(FirstPlayer)[i][2] == 'Action' :
            #print('added action')
            action_count += 1
    if int(action_count) >= 1 :
        PlayActionCard(FirstPlayer, action_count)
    else :
        pass
    
def BuyPhase(FirstPlayer) :
    Auto = False
    if AI == False or FirstPlayer:
        Info = input('Do you want to autoplay all treasures? ')
        if Info == 'y' :
            Auto = True
        elif Info == 'info' :
            PrintInfo(FirstPlayer)
        PlayTreasures(FirstPlayer, Auto, AI)
        PrintCards(FirstPlayer,'InPlay',FindInPlay)
        print('Money:',money)
        if CostReduction > 0 :
            print('CostReduction:',CostReduction)
        BuyCard(FirstPlayer, AI)
    else :
        Auto = True
        PlayTreasures(FirstPlayer, Auto, AI)
        BuyCard(FirstPlayer, AI)
        
def RemoveCardFromSupply(Card) :
    global CopperPile, SilverPile, GoldPile, EstatePile, DutchyPile, ProvincePile, CursePile, Pile1, Pile2, Pile3, Pile4, Pile5, Pile6, Pile7, Pile8, Pile9, Pile10
    pilefull = True
    if Card == 'Copper' and CopperPile > 0:
        CopperPile -= 1
    elif Card == 'Silver'  and SilverPile > 0:
        SilverPile -= 1
    elif Card == 'Gold'  and GoldPile > 0:
        GoldPile -= 1
    elif Card == 'Estate'  and EstatePile > 0:
        EstatePile -= 1
    elif Card == 'Dutchy'  and DutchyPile > 0:
        DutchyPile -= 1
    elif Card == 'Province'  and ProvincePile > 0:
        ProvincePile -= 1
    elif Card == 'Curse' and CursePile > 0:
        CursePile -= 1
    elif str(Card) == Pile1Name  and int(Pile1) > 0:
        Pile1 -= 1
    elif Card == Pile2Name  and int(Pile2) > 0:
        Pile2 -= 1
    elif Card == Pile3Name  and Pile3 > 0:
        Pile3 -= 1
    elif Card == Pile4Name  and Pile4 > 0:
        Pile4 -= 1
    elif Card == Pile5Name  and Pile5 > 0:
        Pile5 -= 1
    elif Card == Pile6Name  and Pile6 > 0:
        Pile6 -= 1
    elif Card == Pile7Name  and Pile7 > 0:
        Pile7 -= 1
    elif Card == Pile8Name  and Pile8 > 0:
        Pile8 -= 1
    elif Card == Pile9Name  and Pile9 > 0:
        Pile9 -= 1
    elif Card == Pile10Name  and Pile10 > 0:
        Pile10 -= 1
    else :
        pilefull = False
    return pilefull

def PrintInfo(FirstPlayer) :
    PrintCards(FirstPlayer,'Deck',PlayerDeck)
    PrintCards(FirstPlayer,'Discard',PlayerDiscard)
    PrintCards(FirstPlayer,'InPlay',FindInPlay)
    PrintCards(FirstPlayer,'Hand',PlayerHand)
    PrintCards(FirstPlayer,'Trash',FindTrash)
    print('Turn: ' + str(TurnCount))

def CostFormula(CardPos) :
    cost = int(kingdom[CardPos][1]) - CostReduction
    if int(cost) < 0 :
        return 0
    else :
        return int(cost)
    
def BuyCard(FirstPlayer, AI) :
    global Buy, money, PlayerOnePoints, PlayerTwoPoints
    if AI and not FirstPlayer :
        Buy = 0
        if 'witch' in kingdom and int(money) > 4 and TurnCount < 6 and ActionAI :
            print('Lord Cranberry bought a Witch.')
            money = 0
            PlayerDiscard(FirstPlayer).append(kingdom[14])
            RemoveCardFromSupply('Dutchy')
        if ProvincePile == 2 and PlayerOnePoints == PlayerTwoPoints and int(money) >= 5 and DutchyPile > 0:
            print('Lord Cranberry bought a Dutchy.')
            money = 0
            PlayerDiscard(FirstPlayer).append(kingdom[14])
            RemoveCardFromSupply('Dutchy')
            PlayerTwoPoints += 3
        elif int(money) > 7 and ProvincePile > 0:
            print('Lord Cranberry bought a Province.')
            money = 0
            PlayerDiscard(FirstPlayer).append(kingdom[15])
            RemoveCardFromSupply('Province')
            PlayerTwoPoints += 6
        elif PlayerOnePoints >= 21 and PlayerTwoPoints < 21 and DutchyPile > 0:
            print('Lord Cranberry bought a Dutchy.')
            money = 0
            PlayerDiscard(FirstPlayer).append(kingdom[14])
            RemoveCardFromSupply('Dutchy')
            PlayerTwoPoints += 3
        elif int(money) > 5 and GoldPile > 0:
            print('Lord Cranberry bought a Gold.')
            money = 0
            PlayerDiscard(FirstPlayer).append(kingdom[12])
            RemoveCardFromSupply('Gold')
        elif int(money) == 5 and PlayerTwoPoints >= 27 and DutchyPile > 0:
            print('Lord Cranberry bought a Dutchy.')
            money = 0
            PlayerDiscard(FirstPlayer).append(kingdom[14])
            RemoveCardFromSupply('Dutchy')
            PlayerTwoPoints += 3
        elif int(money) > 2 and SilverPile > 0:
            print('Lord Cranberry bought a Silver.')
            money = 0
            PlayerDiscard(FirstPlayer).append(kingdom[11])
            RemoveCardFromSupply('Silver')
        else :
            pass
    while Buy > 0 :
        print('Buy:',Buy)
        CardBought = TranslateCardNames(input('What do you want to buy? '))
        if CardBought == 'n' :
            Buy = 0
            #check if card is in supply
        if CardBought == 'Cheat' :
            print('You bought 4 Provinces :-0 ')
            if FirstPlayer :
                PlayerOnePoints += 24
            else :
                PlayerTwoPoints += 24
            for i in range(4) :
                PlayerDiscard(FirstPlayer).append(province)
                RemoveCardFromSupply('Province')
        elif CardBought == 'info' :
            PrintInfo(FirstPlayer)     
        for i in range(0,len(kingdom)) :
            if str(CardBought) == kingdom[i][0] :
                #checks if the card you named is in the kingdom
                if int(kingdom[i][1]) <= int(money) + int(CostReduction) :
                #and if you have enough money to buy it
                    #print('CardBought:',str(CardBought),str(Pile1Name))
                    if RemoveCardFromSupply(CardBought) :
                        money -= CostFormula(i)
                        PlayerDiscard(FirstPlayer).append(kingdom[i])
                        Buy -= 1
                        print('You bought a', CardBought)
                        if kingdom[i][2] == 'Victory' :
                            if FirstPlayer :
                                PlayerOnePoints += int(kingdom[i][3])
                            else :
                                PlayerTwoPoints += int(kingdom[i][3])
                        #Add 'takes away card from supply pile'
                        #puts card into discard and takes away money and buy
                    else :
                        print('There are no more',str(kingdom[i][0]) + 's')
                else :
                    print('You do not have enough money')
                    print('Money:',money)  
            else :
                #print('That card is not in the kingdom')
                pass
                
def PlayTreasures(FirstPlayer, AutoplayTreasures, AI) :
    NumTreasurePlayed = 0
    if AutoplayTreasures :
        Auto = True
    else :
        Auto = False
    for i in range(len(PlayerHand(FirstPlayer))) :
        if IsTreasure(FirstPlayer,i) :
            TreasureInHand.append(PlayerHand(FirstPlayer)[i])
            AddMoney(NumTreasurePlayed, Auto, FirstPlayer)
            NumTreasurePlayed += 1
        else :
            pass
    '''
    while NumTreasurePlayed > 0 :
        for i in range(0, len(InPlay) - 1) :
            if InPlay[i][2] == 'Treasure' :
                PlayerHand(FirstPlayer).remove(InPlay[i])
                NumTreasurePlayed -= 1
    '''
def IsTreasure(FirstPlayer,CardSpot) :
    if 'Treasure' == PlayerHand(FirstPlayer)[CardSpot][2] :
        return True
    else : 
        return False

def AddMoney(CardSpot,AutoPlayTreasures, FirstPlayer) :
    global money
    if AutoPlayTreasures :
        #CardSpot is referring last treasure played
        money += int(TreasureInHand[CardSpot][3])
        InPlay.append(TreasureInHand[CardSpot])
    elif input('Do you want to play ' + str(TreasureInHand[CardSpot][0]) + '?') == 'y' :
        money += int(TreasureInHand[CardSpot][3])
        InPlay.append(TreasureInHand[CardSpot])

def CleanUp(FirstPlayer) :
    while len(TreasureInHand) > 0 :
        PlayerHand(FirstPlayer).remove(TreasureInHand[0])
        TreasureInHand.pop(0)
    PlayerDiscard(FirstPlayer).extend(PlayerHand(FirstPlayer))
    PlayerDiscard(FirstPlayer).extend(InPlay)
    while len(PlayerHand(FirstPlayer)) > 0 :
        PlayerHand(FirstPlayer).pop(0)    
    while len(InPlay) > 0 :
        InPlay.pop(0)

def pick_kingdom() :
    global king
    #card = base[random.randint(0,len(base) - 1)]
    #kingdom.append(card)
    card = None
    num_of_times = 1
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
    #check_kingdom() - works but unneeded

def PopPiles() :
    global Pile1Name, Pile2Name, Pile3Name, Pile4Name, Pile5Name, Pile6Name, Pile7Name, Pile8Name, Pile9Name, Pile10Name
    Pile1Name = kingdom[0][0]
    Pile2Name = kingdom[1][0]
    Pile3Name = kingdom[2][0]
    Pile4Name = kingdom[3][0]
    Pile5Name = kingdom[4][0]
    Pile6Name = kingdom[5][0]
    Pile7Name = kingdom[6][0]
    Pile8Name = kingdom[7][0]
    Pile9Name = kingdom[8][0]
    Pile10Name = kingdom[9][0]

def check_kingdom() :
    done = False
    while done == False :
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
def pop_word(word) :
    if word in actual :
        actual.pop(actual.index(word))
def insert_word(word,new_word) :
    global actual
    if word in actual :
        actual.insert(actual.index(word),new_word)
        actual.pop(actual.index(word))
def translate() :
    global actual
    insert_word('one','1')
    insert_word('two','2')
    insert_word('three','3')
    insert_word('four','4')
    insert_word('five','5')
    insert_word('six','6')
    insert_word('seven','7')
    insert_word('eight','8')
    insert_word('nine','9')
    insert_word('ten','10')
    insert_word('expansions','expansion')
    insert_word('money','cost')
    insert_word('worth','cost')
    insert_word('costs','cost')
    insert_word('set','expansion')
    insert_word('none','no')
    insert_word('a','1')
    insert_word('jl','JL')
    if 'Junk' in actual :
        actual.insert(actual.index('Junk'),'Junk Dealer')
        actual.pop(actual.index('Junk'))
        actual.pop(actual.index('Dealer'))
    if 'Throne' in actual :
        actual.insert(actual.index('Throne'),'Throne Room')
        actual.pop(actual.index('Throne'))
        actual.pop(actual.index('Room'))
    if 'Poor' in actual :
        actual.insert(actual.index('Poor'),'Poor House')
        actual.pop(actual.index('Poor'))
        actual.pop(actual.index('House'))
    if 'Council' in actual :
        actual.insert(actual.index('Council'),'Council Room')
        actual.pop(actual.index('Council'))
        actual.pop(actual.index('Room'))
    if 'Market' in actual and 'Square' in actual :
        actual.insert(actual.index('Market'),'Market Square')
        actual.pop(actual.index('Market'))
        actual.pop(actual.index('Square'))
    if 'Death' in actual :
        actual.insert(actual.index('Death'),'Death Cart')
        actual.pop(actual.index('Death'))
        actual.pop(actual.index('Cart'))
    if 'Misty' in actual and 'Mountains' in actual :
        actual.insert(actual.index('Misty'),'Misty Mountains')
        actual.pop(actual.index('Misty'))
        actual.pop(actual.index('Mountains'))
    if 'Bill' in actual :
        actual.insert(actual.index('Bill'),'Bill Ferny')
        actual.pop(actual.index('Bill'))
        actual.pop(actual.index('Ferny'))
    pop_word('the')
    pop_word('I')
    pop_word('want')
    pop_word('my')
    pop_word('card')
    pop_word('cards')
    pop_word('of')
    pop_word('to')
    pop_word('be')
    pop_word('that')
    pop_word('i')
    pop_word('can')
    pop_word('would')
    pop_word('like')
    pop_word('not')
    pop_word('ages')
    pop_word('with')
    if 'any' in actual and actual[actual.index('any') - 1] == 'not' :
        actual.insert(actual.index('any'),'no')
        actual.pop(actual.index('any')) 

def CheckExpansion(Name, sent) :
    global not_expan
    if Name in sent :
        if sent[sent.index(Name) - 1] == 'from' :
            if sent[sent.index(Name) - 2].isnumeric() == True :
                for i in range(int(sent[sent.index(Name) - 2])) :
                    expan_used.append(Name)
                less_base = int(sent[sent.index(Name) - 2]) + 10
            if sent[sent.index(Name) - 2] == 'rest' :
                while len(expan_used) < 10 :
                    expan_used.append(Name)
            if sent[sent.index(Name) - 2] == 'no' :
                not_expan.append(Name)
def AddSpecificCards(Name,sent) :
    global king
    for i in range(0,len(Name)) :
        if str(Name[i][0]) in sent :
            kingdom.append(Name[i])
            king += 1
def sortMethod(coded) :
    return coded[1]
def check_keywords(sent) :
    if 'working' in sent :
        run = 0
        used = []
        while len(used) < 10 :
            run += 1
            cardPos = random.randint(0,len(coded) - 1)
            if coded[cardPos] not in used :
                kingdom.append(coded[cardPos])
                used.append(coded[cardPos])
            if run > 600 :
                print('did not work')
                break
        kingdom.sort(key=sortMethod)
    global working, less_dark, less_base, less_JL, num_cost_total, not_cost
    #sees how many from base
    if 'less' in sent and sent[sent.index('less') + 1] == 'than' and sent[sent.index('less') + 2].isnumeric() == True and sent[sent.index('less') + 3] == 'from' :
        if sent[sent.index('less') + 4] == 'base' :
            less_base = sent[sent.index('less') + 2]
        elif sent[sent.index('less') + 4] == 'dark' :
            less_dark = sent[sent.index('less') + 2]
        elif sent[sent.index('less') + 4] == 'JL' :
            less_JL = sent[sent.index('less') + 2]
    CheckExpansion('base',sent)
    CheckExpansion('dark',sent)
    CheckExpansion('JL',sent)
    AddSpecificCards(base,sent)
    AddSpecificCards(dark_ages,sent)
    AddSpecificCards(JL_Expansion,sent)
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
        print('What do you want in your kingdom?')
    if len(card_cost) > 10 :
        print('You have too many cost restrictions in the kingdom. There are ten cards in a kingdom.')
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
    print('What do you want in your kingdom? ')
    split_ans()



def SetupPlayers() :
    global AI, P1Name, P2Name, ActionAI
    ans = input('Do you want an AI? ')
    if ans == 'y' or ans == 'yes' :
        AI = True
        ans = input('Do you want it to buy Actions? ')
        if ans == 'y' or ans == 'yes' :
            ActionAI = True
    P1Name = input("What is Player 1's name? ")
    if P1Name == '' :
        P1Name = 'Player 1'
    if AI == False :
        P2Name = input("What is Player 2's name? ")
        if P2Name == '' :
            P2Name = 'Player 2'
    else :
        P2Name = 'Lord Cranberry'
    
def StartTurn(FirstPlayer) :
    global money, Buy, Action, CostReduction
    CostReduction = 0
    Buy = 1
    Action = 1
    money = 0
    PrintCards(FirstPlayer,'Hand',PlayerHand)

def GameEnd(FirstPlayer) :
    print('Game Over.')
    CountPoints(FirstPlayer)
    sys.exit('Thanks for playing!')
                            
def CheckWin(FirstPlayer) :
    EmptyPile = 0
    if ProvincePile <= 0 :
        GameEnd(FirstPlayer)
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
    if CursePile == 0 :
        EmptyPile += 1
    if Pile1 == 0 :
        EmptyPile += 1
    if Pile2 == 0 :
        EmptyPile += 1
    if Pile3 == 0 :
        EmptyPile += 1
    if Pile4 == 0 :
        EmptyPile += 1
    if Pile5 == 0 :
        EmptyPile += 1
    if Pile6 == 0 :
        EmptyPile += 1
    if Pile7 == 0 :
        EmptyPile += 1
    if Pile8 == 0 :
        EmptyPile += 1
    if Pile9 == 0 :
        EmptyPile += 1
    if Pile10 == 0 :
        EmptyPile += 1
    if EmptyPile >= 3 :
        GameEnd(FirstPlayer)

def CountPoints(FirstPlayer) :
    if PlayerOnePoints > PlayerTwoPoints :
        print(str(P1Name), 'wins!')
        time.sleep(0.5)
    elif PlayerOnePoints < PlayerTwoPoints :
        print(str(P2Name), 'wins!')
        time.sleep(0.5)
    elif FirstPlayer :
        print(str(P2Name), 'wins!')
        time.sleep(0.5)
    else :
        print('It is a tie.')
        time.sleep(0.5)
    print(str(P1Name), 'Points: ' + str(PlayerOnePoints))
    print(str(P2Name), 'Points: ' + str(PlayerTwoPoints))
    time.sleep(0.5)
    
def ShowPoints(FirstPlayer) :
    global TurnCount
    print(str(P1Name), 'Points: ' + str(PlayerOnePoints))
    print(str(P2Name), 'Points: ' + str(PlayerTwoPoints))
    time.sleep(0.5)
    if FirstPlayer :
        print(str(P2Name) + "'s", TurnCount, 'turn.')
        Turn(False)
    else :
        TurnCount += 1
        print(str(P1Name) + "'s", TurnCount, 'turn.')
        Turn(True)

def FindTrash(FirstPlayer) :
    return trash

def FindDrawn(FirstPlayer) :
    return Drawn

def FindInPlay(Firstplayer) :
    return InPlay

def PlayerHand(FirstPlayer) :
    if FirstPlayer :
        return hand1
    else :
        return hand2

def PlayerDeck(FirstPlayer) :
    if FirstPlayer :
        return deck1
    else :
        return deck2

def PlayerDiscard(FirstPlayer) :
    if FirstPlayer :
        return discard1
    else :
        return discard2

def Turn(FirstPlayer) :
    global TurnCount
    StartTurn(FirstPlayer)
    ActionPhase(FirstPlayer)
    BuyPhase(FirstPlayer)
    CleanUp(FirstPlayer)
    CheckWin(FirstPlayer)    
    DrawCards(FirstPlayer, HandSize) #draw hand
    ShowPoints(FirstPlayer)

def StartGame() :
    customise_kingdom()
    PopPiles()
    CreateDeck()
    random.shuffle(PlayerDeck(True))
    random.shuffle(PlayerDeck(False))
    SetupPlayers()
    print(str(P1Name) + "'s 1 turn.")
    DrawCards(True, 5) #draw player 1's hand
    DrawCards(False, 5) #draw player 2's hand
    Turn(True)
    
StartGame()
