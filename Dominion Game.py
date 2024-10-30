import random, time, sys, datetime, csv, DomCardPlays
#import pandas as pd

    #TO PLAY AI GAME
    # kingdom  = 'ai'


    #PROBLEMS

    #Rohan does not work
    #Not sure wether it is better to wait to buy any green cards until have 8 bridges in play...
    #doubleStrat does not work -

    #Duration cards add to deck too many times  - Checkduration
    #Rivendell does not work
    #Militia does not work - discard part discards whole hand? - 1240
    #Kc does it 6 times? - fixed
    #Cannot autoplay silmaril
    #Recursion in Turn function - change?
    
    #CURRENT -------- 2173

    #Add spells to AI board
        #Let AI buy and play spells - (partial)
        #Summon familiar doesn't work - should change cost in kingdom, changes on scroll
        #inspiration doesn't work
    
    #NEW FEATURES

    #Optimize Megaturn - done?
    #Optimize Engine
    #reprint out kingdom if ask (VP cards?)
    #Add real double province deck
    #Add more cards
    #Add more strategies

#add more expan
#put in specific cards
#limit cost - works but not only that num - no gives one?
#What can do: choose num cards in expan, cost of cards in kingdom, check cards in kingdom
trash = []
dom_expansions = []
base = []
dark_ages = []
JL_Expansion = []
test = []
coded = []
AIkingdom = []
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
counterfeit = ('Counterfeit','5','Treasure','$1 +1 Buy, When you play this, you may play a Treasure from your hand twice. If you do, trash that Treasure.')
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
tom_bombadil = ('Tom Bombadil','5','Victory','0','When you gain this, +1 VP per Copper you have in play.')
erebor = ('Erebor','4','Action','Trash a card from your hand per card you have in play, if you trashed at least three cards this way, gain a Gold.')
gollum = ('Gollum','5','Action','+$2, if you have the One Ring, +1 Card +1 Action | when you gain this take the One Ring')
boromir = ('Boromir','5','Action','Choose one: Take the One Ring, if you did +4 Coffers and gain a Gold; or you may play an Action card from your hand twice.')
kings_court = ("King's Court",'7','Action','Play an Action card from your hand three times.')
gimli = ('Gimli','5','Action','Duration','Trash a Treasure card from your hand. If you did, now and at the start of your next turn, +1 Buy | While this is in play when any player gains a non-Treasure card +1 Coffer')
shadowfax = ('Shadowfax','5','Action','+1 Action Trash a card from your hand. Gain 2 Horses')
rivendell = ('Rivendell','4','Treasure','+$1 per card you gained this turn. When you gain a card +$1')
silmaril = ('Silmaril','2','Treasure','You may pay $1 to make cards cost $1 less this turn.')
wharf = ('Wharf','5','Action','Duration','Now and at the start of your next turn, +2 Cards +1 Buy')
scroll = ('Scroll','5','Action','Cast a Spell.')

prestidigitation = ('Prestidigitation','2','Spell')
arcane_bolt = ('Arcane Bolt','2','Spell')
haste = ('Haste','2','Spell')
inspiration = ('Inspiration','3','Spell')
gathering_storm = ('Gathering Storm','3','Spell')
midas_touch = ('Midas Touch','3','Spell')
summon_familiar = ('Summon Familiar','3','Spell')

copper = ('Copper','0','Treasure','1')	
silver = ('Silver','3','Treasure','2')
gold = ('Gold','6','Treasure','3')	
estate = ('Estate','2','Victory','1')
dutchy = ('Dutchy','5','Victory','3')
province = ('Province','8','Victory','6')
curse = ('Curse','0','Curse','-1')
horse = ('Horse','3','Action','+2 Cards +1 Action, return this to the supply.')
'''
CardText = open("Card_Text.py")
#for card in CardText :
#coded.append(card)
coded.append(CardText.readline())
print(coded)
coded.append(CardText.readline())
coded.append(CardText.readline())
coded.append(CardText.readline())
coded.append(CardText.readline())
coded.append(CardText.readline())
coded.append(CardText.readline())
coded.append(CardText.readline())
coded.append(CardText.readline())
coded.append(CardText.readline())
'''
JL_Expansion.append(bridge)
JL_Expansion.append(rohan)
JL_Expansion.append(misty_mountians)
JL_Expansion.append(bill_ferny)
JL_Expansion.append(tom_bombadil)
JL_Expansion.append(erebor)
JL_Expansion.append(gollum)
JL_Expansion.append(boromir)
JL_Expansion.append(kings_court)
JL_Expansion.append(gimli)
JL_Expansion.append(shadowfax)
JL_Expansion.append(rivendell)
JL_Expansion.append(silmaril)
JL_Expansion.append(wharf)
'''
JL_Expansion.append(elrond)
JL_Expansion.append(beorn)
JL_Expansion.append(elendil)
JL_Expansion.append(arkenstone)
JL_Expansion.append(thranduil)
JL_Expansion.append(bridge_troll)
JL_Expansion.append(gil_galad)
'''

AIkingdom.append(chapel)  
AIkingdom.append(workshop)
AIkingdom.append(village)
AIkingdom.append(smithy)
AIkingdom.append(market)
AIkingdom.append(moneylender)
AIkingdom.append(laboratory)
AIkingdom.append(junk_dealer)
AIkingdom.append(bridge)
AIkingdom.append(rats)

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
coded.append(rats)
coded.append(counterfeit)
coded.append(ironmonger)
coded.append(tom_bombadil)
coded.append(erebor)
coded.append(gollum)
coded.append(boromir)
coded.append(kings_court)
coded.append(gimli)
coded.append(shadowfax)
coded.append(rivendell)
coded.append(silmaril)
coded.append(militia)
coded.append(wharf)

test.append(erebor)
test.append(village)
test.append(smithy)
test.append(wharf)
test.append(gimli)
test.append(rats)
test.append(kings_court)
test.append(shadowfax)
test.append(militia)
test.append(silmaril)

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
dark_ages.append(counterfeit)
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

RunSize = 1
RunTimes = 0

class Player :
    def __init__(self,name):
        self.name = name
        self.strat = "BigMoneyStrat"
        self.hand = []
        self.discard = []
        self.deck = []
        self.hasOneRing = False
        self.coffers = 0
        self.spellbook = []
        self.money = 0
        self.buys = 0
        self.actions = 0
        self.handsize = 5

class Pile :
    def __init__(self,name,size):
        self.name = name
        self.size = size


def ClearStats() :
    global CanTrashRats, RunSize, RunTimes, AI, AI2, ActionAI, UnconMega, OneRingFirstPlayer, OneRingSecondPlayer, P1Strat ,P2Strat
    global PlayerOnePoints, PlayerTwoPoints,Coffers1,Coffers2, hand1,deck1,discard1,hand2,deck2,discard2,StartTime,CostReduction
    global ActionsInHand, money, InPlay,TreasureInHand,UnplayedTreasures,DurationLand1,DurationLand2,Drawn,Buy
    global Action,Gain, Auto,HandSize,TurnCount,HorsePile,CopperPile,SilverPile,GoldPile,EstatePile,DutchyPile,ProvincePile
    global CursePile,EmptyPile,Pile1Name,Pile2Name,Pile3Name,Pile4Name,Pile5Name,Pile6Name,Pile7Name,Pile8Name,Pile9Name,Pile10Name
    global trash,ScrollPile,Spellbook1,Spellbook2,landscape
    #Card Attributes
    CanTrashRats = True
    #Deck Attibutes
    landscape = []
    #AI Attributes

    AI = False
    AI2 = False
    ActionAI = False
    UnconMega = True
    #Player Attributes
    OneRingFirstPlayer = False
    OneRingSecondPlayer = False
    P1Strat = None
    P2Strat = None
    PlayerOnePoints = 3
    PlayerTwoPoints = 3
    Coffers1 = 0
    Coffers2 = 0
    Spellbook1 = []
    Spellbook2 = []
    hand1 = []
    deck1 = []
    discard1 =[]
    hand2 = []
    deck2 = []
    discard2 = []
    #Turn
    StartTime = 0
    CostReduction = 0
    ActionsInHand = 0
    money = 0
    InPlay = []
    TreasureInHand = []
    UnplayedTreasures = []
    DurationLand1 = []
    DurationLand2 = []
    Drawn = []
    Buy = 1
    Action = 1
    Gain = 1
    Auto = False
    HandSize = 5
    TurnCount = 1
    #Card Piles
    HorsePile = 30
    CopperPile = 60
    SilverPile = 40
    GoldPile = 30
    EstatePile = 14
    DutchyPile = 8
    ProvincePile = 8
    CursePile = 10
    ScrollPile = 10
    EmptyPile = []
    trash = []
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
    global ActionsInHand, Drawn
    Drawn = []
    NewHandSize = len(PlayerHand(FirstPlayer)) + NumCards
    while len(PlayerHand(FirstPlayer)) < NewHandSize :
        try :
            PlayerHand(FirstPlayer).append(PlayerDeck(FirstPlayer)[0]) #draw card
            Drawn.append(PlayerDeck(FirstPlayer)[0])
            PlayerDeck(FirstPlayer).pop(0)
        except : #if deck is empty
            if len(PlayerDiscard(FirstPlayer)) == 0 : #if you drew your deck
                break
            if FirstPlayer :
                print("Shuffling", str(P1Name) + "'s deck") 
            else :
                print("Shuffling", str(P2Name) + "'s deck")
            PlayerDeck(FirstPlayer).extend(PlayerDiscard(FirstPlayer))#add discard to deck
            PlayerDiscard(FirstPlayer).clear() #delete discard    
            random.shuffle(PlayerDeck(FirstPlayer)) #shuffle deck
        else :
            if str(PlayerHand(FirstPlayer)[-1][2]) == 'Action' : #check for action cards
                ActionsInHand += 1


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
    
    #if not AI or FirstPlayer :
    print(Place + ':',CardsInHand(Num,FirstPlayer,CardSpot))

def AIPlayScroll(Card, Name, FirstPlayer) :
    global Action, ActionsInHand
    #time.sleep(0.5)
    if FirstPlayer :
        print(P1Name,'played Scroll')
    else :
        print(P2Name,'played Scroll')
    InPlay.append(scroll)
    PlayerHand(FirstPlayer).remove(scroll)
    Action -= 1
    ActionsInHand -= 1
    PlayScroll(FirstPlayer, Name)

def AIPlayCard(Card, FirstPlayer, *throne) :
    global Action, ActionsInHand
    #time.sleep(0.5)
    if FirstPlayer :
        print(P1Name,'played ' + str(Card[0]))
    else :
        print(P2Name,'played ' + str(Card[0]))
    try :
        if throne == True :
            #print('THRONE!')
            pass
        else :
            #print('Throne?')
            InPlay.append(Card)
            ActionsInHand -= 1
    except :
        InPlay.append(Card)
        ActionsInHand -= 1
    PlayActionBank(FirstPlayer,Card[0],Card)

def GetCoffers(FirstPlayer, Num) :
    global Coffers1, Coffers2
    if FirstPlayer :
        Coffers1 += Num
    else :
        Coffers2 += Num

def SpecialTreasure(FirstPlayer) :
    while CountTreasures(FirstPlayer) > 0 :
        played_card = False
        ans = DomCardPlays.translate(input('Which Treasure card do you want to play? '))
        if ans == 'n' :
            played_card = True
            for i in range(len(PlayerHand(FirstPlayer))) :
                if IsTreasure(FirstPlayer,i) :
                    UnplayedTreasures.append(PlayerHand(FirstPlayer)[i])
            for i in range(len(UnplayedTreasures)) :
                PlayerHand(FirstPlayer).remove(UnplayedTreasures[i])
        elif ans == 'info' :
            played_card = True
            PrintInfo(FirstPlayer)
        for i in range(0,len(PlayerHand(FirstPlayer))) :
            #print(str(PlayerHand(FirstPlayer)[i][0]))
            try :
                str(ans) == PlayerHand(FirstPlayer)[i][0]
            except :
                pass
            else :
                if str(ans) == PlayerHand(FirstPlayer)[i][0] and str(PlayerHand(FirstPlayer)[i][2]) == 'Treasure' and played_card == False :
                    time.sleep(0.25)
                    print('Played ' + str(PlayerHand(FirstPlayer)[i][0]))
                    InPlay.append(PlayerHand(FirstPlayer)[i])
                    #PlayerHand(FirstPlayer).pop(i)
                    PlayTreasureBank(FirstPlayer,PlayerHand(FirstPlayer)[i][0],PlayerHand(FirstPlayer)[i])
                    played_card = True
        if played_card == False :
            print(str(ans),'is not in your hand')
def CountTreasures(FirstPlayer) :
    Count = 0
    for i in range(len(PlayerHand(FirstPlayer))) :
        if PlayerHand(FirstPlayer)[i][2] == 'Treasure' :
            Count += 1
    return Count

def SpecialPlayCases(FirstPlayer) :
    if GameStrat(FirstPlayer) == 'EngineStrat' : #or GameStrat(FirstPlayer) == 'SpellStrat':
        #Deck and Discard are empty, - for gain and play
        if workshop in PlayerHand(FirstPlayer) and Action > 1 and len(PlayerDeck(FirstPlayer)) == 0 and len(PlayerDiscard(FirstPlayer)) == 0 :
            AIPlayCard(workshop, FirstPlayer)
            return True
        '''
        if scroll in PlayerHand(FirstPlayer) :
            #if gathering_storm in PlayerSpellbook(FirstPlayer) and Action > 1 :
            #    AIPlayScroll(gathering_storm, 'Gathering Storm', FirstPlayer)
            #    return True
            if haste in PlayerSpellbook(FirstPlayer) and Action == 1:
                AIPlayScroll(haste, 'Haste', FirstPlayer)
                return True
        '''
    else :
        return False

def PlayVillageCard(FirstPlayer) :
    if village in PlayerHand(FirstPlayer) :
        AIPlayCard(village, FirstPlayer)
        return True
    elif scroll in PlayerHand(FirstPlayer) and haste in PlayerSpellbook(FirstPlayer) and Action == 1 :
        AIPlayScroll(haste, 'Haste', FirstPlayer)
        return True
    else :
        return False

def PlayActionDraw(FirstPlayer) :
    if laboratory in PlayerHand(FirstPlayer) :
        AIPlayCard(laboratory, FirstPlayer)
        return True
    elif market in PlayerHand(FirstPlayer) :
        AIPlayCard(market, FirstPlayer)
        return True
    elif ironmonger in PlayerHand(FirstPlayer) :
        AIPlayCard(ironmonger, FirstPlayer)
        return True
    else :
        return False
    '''
    elif scroll in PlayerHand(FirstPlayer) and prestidigitation in PlayerSpellbook(FirstPlayer) :
        AIPlayScroll(prestidigitation, 'Prestidigitation', FirstPlayer)
        return True
    elif scroll in PlayerHand(FirstPlayer) and haste in PlayerSpellbook(FirstPlayer) :
        AIPlayScroll(haste, 'Haste', FirstPlayer)
        return True
    '''
    

def PlayActionPayload(FirstPlayer) :
    return False

def PlayTrasher(FirstPlayer,Early) :
    if Early :
        #If JD in hand with Estate or Curse
        if junk_dealer in PlayerHand(FirstPlayer) and estate in PlayerHand(FirstPlayer) or junk_dealer in PlayerHand(FirstPlayer) and curse in PlayerHand(FirstPlayer) :
            AIPlayCard(junk_dealer, FirstPlayer)
            return True
        #If PT in hand with Estate or Curse or Copper
        elif scroll in PlayerHand(FirstPlayer) and prestidigitation in PlayerSpellbook(FirstPlayer) and estate in PlayerHand(FirstPlayer) or scroll in PlayerHand(FirstPlayer) and prestidigitation in PlayerSpellbook(FirstPlayer) and curse in PlayerHand(FirstPlayer) or scroll in PlayerHand(FirstPlayer) and prestidigitation in PlayerSpellbook(FirstPlayer) and copper in PlayerHand(FirstPlayer):
            AIPlayScroll(prestidigitation, 'Prestidigitation', FirstPlayer)
            return True
        #If SF in hand with Estate or Curse
        elif shadowfax in PlayerHand(FirstPlayer) and estate in PlayerHand(FirstPlayer) or shadowfax in PlayerHand(FirstPlayer) and curse in PlayerHand(FirstPlayer) :
            AIPlayCard(shadowfax, FirstPlayer)
            return True
        #If Erebor in hand and 2+ stuff in hand that can trash
        elif erebor in PlayerHand(FirstPlayer) and len(InPlay) > 0 and (PlayerHand(FirstPlayer).count(copper) + PlayerHand(FirstPlayer).count(estate) + PlayerHand(FirstPlayer).count(curse)) > len(InPlay) :
            AIPlayCard(erebor, FirstPlayer)
            return True
        #If Chapel in hand with 3 stuff or 2 estates or curses
        elif chapel in PlayerHand(FirstPlayer) and (PlayerHand(FirstPlayer).count(copper) + PlayerHand(FirstPlayer).count(estate) + PlayerHand(FirstPlayer).count(curse)) > 2 or chapel in PlayerHand(FirstPlayer) and (PlayerHand(FirstPlayer).count(curse) + PlayerHand(FirstPlayer).count(estate)) > 1  :
            AIPlayCard(chapel, FirstPlayer)
            return True
        #If MT in hand with Estate or Curse
        elif scroll in PlayerHand(FirstPlayer) and midas_touch in PlayerSpellbook(FirstPlayer) and estate in PlayerHand(FirstPlayer) or scroll in PlayerHand(FirstPlayer) and midas_touch in PlayerSpellbook(FirstPlayer) and curse in PlayerHand(FirstPlayer):
            AIPlayScroll(midas_touch, 'Midas Touch', FirstPlayer)
            return True
        #If ML in hand and Copper
        elif moneylender in PlayerHand(FirstPlayer) and copper in PlayerHand(FirstPlayer) :
            AIPlayCard(moneylender, FirstPlayer)
            return True
        else :
            return False
    else :
        #If JD in hand with Estate or Curse or Copper
        if junk_dealer in PlayerHand(FirstPlayer) and estate in PlayerHand(FirstPlayer) or junk_dealer in PlayerHand(FirstPlayer) and curse in PlayerHand(FirstPlayer) or junk_dealer in PlayerHand(FirstPlayer) and copper in PlayerHand(FirstPlayer) :
            AIPlayCard(junk_dealer, FirstPlayer)
            return True
        #If PT in hand with Estate or Curse or Copper
        elif scroll in PlayerHand(FirstPlayer) and prestidigitation in PlayerSpellbook(FirstPlayer) and curse in PlayerHand(FirstPlayer) or scroll in PlayerHand(FirstPlayer) and prestidigitation in PlayerSpellbook(FirstPlayer) and copper in PlayerHand(FirstPlayer):
            AIPlayScroll(prestidigitation, 'Prestidigitation', FirstPlayer)
            return True
        #If SF in hand with Estate or Curse or Copper
        elif shadowfax in PlayerHand(FirstPlayer) and estate in PlayerHand(FirstPlayer) or shadowfax in PlayerHand(FirstPlayer) and curse in PlayerHand(FirstPlayer) or shadowfax in PlayerHand(FirstPlayer) and copper in PlayerHand(FirstPlayer) :
            AIPlayCard(shadowfax, FirstPlayer)
            return True
        #If ML in hand and Copper
        elif moneylender in PlayerHand(FirstPlayer) and copper in PlayerHand(FirstPlayer) :
            AIPlayCard(moneylender, FirstPlayer)
            return True
        #If Erebor in hand and 1+ stuff in hand that can trash
        elif erebor in PlayerHand(FirstPlayer) and (PlayerHand(FirstPlayer).count(copper) + PlayerHand(FirstPlayer).count(estate) + PlayerHand(FirstPlayer).count(curse)) > len(InPlay) :
            AIPlayCard(erebor, FirstPlayer)
            return True
        #If chapel in hand with Estate or Curse or Copper
        elif chapel in PlayerHand(FirstPlayer) and estate in PlayerHand(FirstPlayer) or chapel in PlayerHand(FirstPlayer) and curse in PlayerHand(FirstPlayer) or chapel in PlayerHand(FirstPlayer) and copper in PlayerHand(FirstPlayer) :
            AIPlayCard(chapel, FirstPlayer)
            return True
        #If MT in hand with Estate or Curse or Copper
        elif scroll in PlayerHand(FirstPlayer) and midas_touch in PlayerSpellbook(FirstPlayer) and estate in PlayerHand(FirstPlayer) or scroll in PlayerHand(FirstPlayer) and midas_touch in PlayerSpellbook(FirstPlayer) and curse in PlayerHand(FirstPlayer) or scroll in PlayerHand(FirstPlayer) and midas_touch in PlayerSpellbook(FirstPlayer) and copper in PlayerHand(FirstPlayer):
            AIPlayScroll(midas_touch, 'Midas Touch', FirstPlayer)
            return True
        #If ML in hand and Copper
        elif moneylender in PlayerHand(FirstPlayer) and copper in PlayerHand(FirstPlayer) :
            AIPlayCard(moneylender, FirstPlayer)
            return True
        else :
            return False
        
def PlayTerminalDraw(FirstPlayer,Early) :
    if Early and Action > 1 and (len(PlayerDeck(FirstPlayer)) != 0 or len(PlayerDiscard(FirstPlayer)) != 0) :
        if wharf in PlayerHand(FirstPlayer) :
            AIPlayCard(wharf, FirstPlayer)
            return True
        elif smithy in PlayerHand(FirstPlayer) :
            AIPlayCard(smithy, FirstPlayer)
            return True
        elif witch in PlayerHand(FirstPlayer) :
            AIPlayCard(witch, FirstPlayer)
            return True
        elif scroll in PlayerHand(FirstPlayer) and summon_familiar in PlayerSpellbook(FirstPlayer) :
            AIPlayScroll(summon_familiar, 'Summon Familiar', FirstPlayer)
            return True
        else :
            return False
    else :
        if wharf in PlayerHand(FirstPlayer) :
            AIPlayCard(wharf, FirstPlayer)
            return True
        elif smithy in PlayerHand(FirstPlayer) :
            AIPlayCard(smithy, FirstPlayer)
            return True
        elif witch in PlayerHand(FirstPlayer) :
            AIPlayCard(witch, FirstPlayer)
            return True
        elif scroll in PlayerHand(FirstPlayer) and summon_familiar in PlayerSpellbook(FirstPlayer) :
            AIPlayScroll(summon_familiar, 'Summon Familiar', FirstPlayer)
            return True
        else :
            return False

def PlayTerminalPayload(FirstPlayer) :
    if militia in PlayerHand(FirstPlayer) and len(PlayerHand(SecondPlayer(FirstPlayer))) > 3 :
        AIPlayCard(militia, FirstPlayer)
        return True
    elif bill_ferny in PlayerHand(FirstPlayer) and len(PlayerHand(FirstPlayer)) == 5 :
        AIPlayCard(bill_ferny, FirstPlayer)
        return True
    elif bridge in PlayerHand(FirstPlayer) :
        AIPlayCard(bridge, FirstPlayer)
        return True
    elif scroll in PlayerHand(FirstPlayer) and gathering_storm in PlayerSpellbook(FirstPlayer) :
        AIPlayScroll(gathering_storm, 'Gathering Storm', FirstPlayer)
        return True
    elif scroll in PlayerHand(FirstPlayer) and arcane_bolt in PlayerSpellbook(FirstPlayer) :
        AIPlayScroll(arcane_bolt, 'Arcane Bolt', FirstPlayer)
        return True
    elif boromir in PlayerHand(FirstPlayer) :
        AIPlayCard(boromir, FirstPlayer)
        return True
    elif workshop in PlayerHand(FirstPlayer) :
        AIPlayCard(workshop, FirstPlayer)
        return True
    elif bill_ferny in PlayerHand(FirstPlayer) :
        AIPlayCard(bill_ferny, FirstPlayer)
        return True
    elif militia in PlayerHand(FirstPlayer) :
        AIPlayCard(militia, FirstPlayer)
        return True
    else :
        return False

def PlayThroneRoomCard(FirstPlayer) :
    if kings_court in PlayerHand(FirstPlayer) :
        AIPlayCard(kings_court, FirstPlayer)
        return True
    elif throne_room in PlayerHand(FirstPlayer) :
        AIPlayCard(throne_room, FirstPlayer)
        return True
    elif boromir in PlayerHand(FirstPlayer) :
        AIPlayCard(boromir, FirstPlayer)
        return True
    else :
        return False
        
def PlayCurser(FirstPlayer) :
    if witch in PlayerHand(FirstPlayer) :
        AIPlayCard(witch, FirstPlayer)
        return True
    else :
        return False
            
def PlayActionCard(FirstPlayer, ActionCount) :
    global Action, ActionsInHand
    ActionsInHand = ActionCount
    run = 0
    while Action > 0 and ActionsInHand > 0:
        if AI2 or not FirstPlayer and AI :
            #if GameStrat(FirstPlayer) == 'EngineStrat' or GameStrat(FirstPlayer) == 'DoubleStrat' or GameStrat(FirstPlayer) == 'TestStrat' :
            if SpecialPlayCases(FirstPlayer) :
                pass
            elif PlayThroneRoomCard(FirstPlayer) :
                pass
            elif PlayVillageCard(FirstPlayer) :
                pass
            elif PlayActionDraw(FirstPlayer) :
                pass
            elif PlayActionPayload(FirstPlayer) :
                pass
            elif PlayTerminalDraw(FirstPlayer,True) :
                pass
            elif PlayTrasher(FirstPlayer,True) :
                pass
            elif PlayCurser(FirstPlayer) :
                pass
            elif PlayTerminalPayload(FirstPlayer) :
                pass
            elif PlayTerminalDraw(FirstPlayer,False) :
                pass
            elif PlayTrasher(FirstPlayer,False) :
                pass
            else :
                Action = 0
                ActionsInHand = 0
                '''
                elif chapel in PlayerHand(FirstPlayer) and CountCard(FirstPlayer, copper) > 1 or chapel in PlayerHand(FirstPlayer) and estate in PlayerHand(FirstPlayer) :
                    if estate in PlayerHand(FirstPlayer) :
                        AIPlayCard(chapel, FirstPlayer)
                    elif copper in PlayerHand(FirstPlayer) and CountCard(FirstPlayer, copper) > 3 :
                        AIPlayCard(chapel, FirstPlayer)
                    elif copper in PlayerHand(FirstPlayer) and CountCard(FirstPlayer, silver) > 0 and not CountCard(FirstPlayer, copper) == 1 :
                        AIPlayCard(chapel, FirstPlayer)
                    else :
                        run += 1
                        if run > 50 :
                            Action = 0
                            ActionsInHand = 0
                '''
            '''    
            elif GameStrat(FirstPlayer) == 'MegaTurnStrat' or GameStrat(FirstPlayer) == 'MegaTurnStrat#2':
                if SpecialPlayCases(FirstPlayer) :
                    pass
                elif PlayThroneRoomCard(FirstPlayer) :
                    pass
                elif PlayVillageCard(FirstPlayer) :
                    pass
                elif PlayActionDraw(FirstPlayer) :
                    pass
                elif PlayActionPayload(FirstPlayer) :
                    pass
                elif PlayTerminalDraw(FirstPlayer,True) :
                    pass
                elif PlayTrasher(FirstPlayer,True) :
                    pass
                elif PlayCurser(FirstPlayer) :
                    pass
                elif PlayTerminalPayload(FirstPlayer) :
                    pass
                elif PlayTerminalDraw(FirstPlayer,False) :
                    pass
                elif PlayTrasher(FirstPlayer,False) :
                    pass
                else :
                    Action = 0
                    ActionsInHand = 0

                if workshop in PlayerHand(FirstPlayer) and Action > 1 and len(PlayerDeck(FirstPlayer)) == 0 and len(PlayerDiscard(FirstPlayer)) == 0 :
                    AIPlayCard(workshop, FirstPlayer)
                elif village in PlayerHand(FirstPlayer) :
                    AIPlayCard(village, FirstPlayer)
                elif market in PlayerHand(FirstPlayer) :
                    AIPlayCard(market, FirstPlayer)
                elif laboratory in PlayerHand(FirstPlayer) :
                    AIPlayCard(laboratory, FirstPlayer)
                elif Action > 1 and smithy in PlayerHand(FirstPlayer) and (len(PlayerDeck(FirstPlayer)) != 0 or len(PlayerDiscard(FirstPlayer)) != 0) :
                    AIPlayCard(smithy, FirstPlayer)
                elif bridge in PlayerHand(FirstPlayer) and GameStrat(FirstPlayer) == 'MegaTurnStrat' and not UnconMega and not estate in PlayerHand(FirstPlayer) and PlayerHand(FirstPlayer).count(copper) < 3 :
                    AIPlayCard(bridge, FirstPlayer) #if not enough coppers to make it worth trashing
                elif chapel in PlayerHand(FirstPlayer) and CountCard(FirstPlayer, copper) > 2 or chapel in PlayerHand(FirstPlayer) and estate in PlayerHand(FirstPlayer) or chapel in PlayerHand(FirstPlayer) and CountCard(FirstPlayer, bridge) > 1 and CountCard(FirstPlayer, copper) > 0 :
                    if estate in PlayerHand(FirstPlayer) :
                        AIPlayCard(chapel, FirstPlayer)
                    elif copper in PlayerHand(FirstPlayer) and CountCard(FirstPlayer, copper) > 2 :
                        AIPlayCard(chapel, FirstPlayer)
                    elif copper in PlayerHand(FirstPlayer) and CountCard(FirstPlayer, bridge) > 1 :
                        AIPlayCard(chapel, FirstPlayer)
                    else :
                        run += 1
                        if run > 50 :
                            Action = 0
                            ActionsInHand = 0
                elif bridge in PlayerHand(FirstPlayer) :
                    AIPlayCard(bridge, FirstPlayer)
                elif workshop in PlayerHand(FirstPlayer) :
                    AIPlayCard(workshop, FirstPlayer)
                elif smithy in PlayerHand(FirstPlayer) :
                    AIPlayCard(smithy, FirstPlayer)
                else :
                    Action = 0
                    ActionsInHand = 0
            elif GameStrat(FirstPlayer) == 'BigMoneyStrat' :
                if smithy in PlayerHand(FirstPlayer) :
                    AIPlayCard(smithy, FirstPlayer)
            elif GameStrat(FirstPlayer) == 'JoelStrat' :
                if workshop in PlayerHand(FirstPlayer) and Action > 1 and len(PlayerDeck(FirstPlayer)) == 0 and len(PlayerDiscard(FirstPlayer)) == 0 :
                    AIPlayCard(workshop, FirstPlayer)
                elif village in PlayerHand(FirstPlayer) :
                    AIPlayCard(village, FirstPlayer)
                elif market in PlayerHand(FirstPlayer) :
                    AIPlayCard(market, FirstPlayer)
                elif laboratory in PlayerHand(FirstPlayer) :
                    AIPlayCard(laboratory, FirstPlayer)
                elif Action > 1 and smithy in PlayerHand(FirstPlayer) and (len(PlayerDeck(FirstPlayer)) != 0 or len(PlayerDiscard(FirstPlayer)) != 0) :
                    AIPlayCard(smithy, FirstPlayer)
                elif bridge in PlayerHand(FirstPlayer) and (PlayerHand(FirstPlayer).count(gold)*3 + PlayerHand(FirstPlayer).count(silver)*2 + PlayerHand(FirstPlayer).count(copper) + InPlay.count(bridge)*2) >= 6 :
                    AIPlayCard(bridge, FirstPlayer)
                elif smithy in PlayerHand(FirstPlayer) :
                    AIPlayCard(smithy, FirstPlayer)
                elif chapel in PlayerHand(FirstPlayer) and estate in PlayerHand(FirstPlayer) :
                    AIPlayCard(chapel, FirstPlayer)
                elif workshop in PlayerHand(FirstPlayer) :
                    AIPlayCard(workshop, FirstPlayer)
                else :
                    Action = 0
                    ActionsInHand = 0
                    '''
        else :
            played_card = False
            ans = DomCardPlays.translate(input('Which Action card do you want to play? '))
            if ans == 'n' :
                played_card = True
                Action = 0
                ActionsInHand = 0
            elif ans == 'info' :
                played_card = True
                PrintInfo(FirstPlayer)
            elif ans == 'hand' :
                played_card = True
                PrintCards(FirstPlayer,'Hand',PlayerHand)
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
                print(str(ans),'is not in your hand')

def PlayActionBank(FirstPlayer, CardName, CardPlayed, *Throne) :
    global Action
    Action -= 1
    if not Throne :
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
    if CardName == 'Rats' :
        PlayRats(FirstPlayer)
    if CardName == 'Ironmonger' :
        PlayIronmonger(FirstPlayer)
    if CardName == 'Erebor' :
        PlayErebor(FirstPlayer)
    if CardName == 'Gollum' :
        PlayGollum(FirstPlayer)
    if CardName == 'Boromir' :
        PlayBoromir(FirstPlayer)
    if CardName == "King's Court" :
        PlayKingsCourt(FirstPlayer)
    if CardName == 'Gimli' :
        PlayGimli(FirstPlayer)
    if CardName == 'Shadowfax' :
        PlayShadowfax(FirstPlayer)
    if CardName == 'Militia' :
        PlayMilitia(FirstPlayer)
    if CardName == 'Wharf' :
        PlayWharf(FirstPlayer)
    if CardName == 'Horse' :
        PlayHorse(FirstPlayer)
    if CardName == 'Scroll' :
        PlayScroll(FirstPlayer)

def PlayTreasureBank(FirstPlayer, CardName, CardPlayed, *Throne) :
    if not Throne :
        PlayerHand(FirstPlayer).remove(CardPlayed)
    if CardName == 'Counterfeit' :
        PlayCounterfeit(FirstPlayer)
    if CardName == 'Rivendell' :
        PlayRivendell(FirstPlayer)
    if CardName == 'Silmaril' :
        PlaySilmaril(FirstPlayer)
    if CardName == 'Copper' :
        PlayCopper()
    if CardName == 'Silver' :
        PlaySilver()
    if CardName == 'Gold' :
        PlayGold()

def PlayCopper() :
    global money
    money += 1

def PlaySilver() :
    global money
    money += 2

def PlayGold() :
    global money
    money += 3



def CheckWhileInPlayAbilities(FirstPlayer, time) :
    global Coffers1, Coffers2
    if gimli in DurationLand1 and time == 'Gain': #make not for treasures
        Coffers1 += DurationLand1.count(gimli)
    if gimli in DurationLand2 and time == 'Gain':
        Coffers2 += DurationLand2.count(gimli)

def CheckCardDL(Card, FirstPlayer) :
    Num = 0
    if FirstPlayer :
        for i in range(0,len(DurationLand1)) :
            if DurationLand1[i][0] == Card :
                Num += 1
        return Num
    else :
        for i in range(0,len(DurationLand2)) :
            if DurationLand2[i][0] == Card :
                Num += 1
        return Num
    
def CheckNextTurnAbilities(FirstPlayer) :
    global Buy
    for i in range(CheckCardDL(gimli, FirstPlayer)) :
        Buy += 1
    for i in range(CheckCardDL(wharf, FirstPlayer)) :
        Buy += 1
        ActionDrawCards(FirstPlayer, 2)


def PlayCounterfeit(FirstPlayer) :
    global money
    money += 1
    PlayedCard = False
    while not PlayedCard :
        ans = DomCardPlays.translate(input('What Treasure card do you want to counterfeit? '))
        if ans == 'n' :
            PlayedCard = True
        for i in range(0, len(PlayerHand(FirstPlayer))) :
            if ans == PlayerHand(FirstPlayer)[i][0] and 'Treasure' == PlayerHand(FirstPlayer)[i][2] and not PlayedCard :
                CardName = PlayerHand(FirstPlayer)[i][0]
                CardPlayed = PlayerHand(FirstPlayer)[i]
                PlayTreasureBank(FirstPlayer, CardName, CardPlayed, True)
                PlayTreasureBank(FirstPlayer, CardName, CardPlayed, True)
                PlayedCard = True
            else :
                #print('That is not in your hand')
                pass
        if not PlayedCard :
            print(ans,'is not in your hand')
    TrashCards(FirstPlayer, 1, True, CardPlayed[0])

def PlayRivendell(FirstPlayer) :
    global money
    pass

def PlaySilmaril(FirstPlayer) :
    global money, CostReduction
    if money > 0 :
        ans = input('Do you want to spend $1 to make everything cost one less? ')
        if ans == 'y' or ans == 'yes' :
            money -= 1
            CostReduction += 1

def PlayKingsCourt(FirstPlayer) :
    global Action
    PlayedCard = False
    if AI and not FirstPlayer or AI2 :
        #Change to calc what best based on what have in deck
            if PlayTerminalDraw(True) :
                Action += 2
                AIPlayCard(InPlay[-1],FirstPlayer, True)
                AIPlayCard(InPlay[-1],FirstPlayer, True)
            elif PlayActionDraw() :
                Action += 2
                AIPlayCard(InPlay[-1],FirstPlayer, True)
                AIPlayCard(InPlay[-1],FirstPlayer, True)
            elif PlayCurser() :
                Action += 2
                AIPlayCard(InPlay[-1],FirstPlayer, True)
                AIPlayCard(InPlay[-1],FirstPlayer, True)
            elif PlayTerminalPayload() :
                Action += 2
                AIPlayCard(InPlay[-1],FirstPlayer, True)
                AIPlayCard(InPlay[-1],FirstPlayer, True)
            elif PlayVillageCard() :
                Action += 2
                AIPlayCard(InPlay[-1],FirstPlayer, True)
                AIPlayCard(InPlay[-1],FirstPlayer, True)
            elif PlayActionPayload() :
                Action += 2
                AIPlayCard(InPlay[-1],FirstPlayer, True)
                AIPlayCard(InPlay[-1],FirstPlayer, True)
            elif PlayTrasher(True) :
                Action += 2
                AIPlayCard(InPlay[-1],FirstPlayer, True)
                AIPlayCard(InPlay[-1],FirstPlayer, True)
            elif PlayTerminalDraw(False) :
                Action += 2
                AIPlayCard(InPlay[-1],FirstPlayer, True)
                AIPlayCard(InPlay[-1],FirstPlayer, True)
            elif PlayTrasher(False) :
                Action += 2
                AIPlayCard(InPlay[-1],FirstPlayer, True)
                AIPlayCard(InPlay[-1],FirstPlayer, True)
    else :
        while not PlayedCard :
            ans = DomCardPlays.translate(input('What Action card do you want to king? '))
            if ans == 'n' :
                PlayedCard = True
            for i in range(0, len(PlayerHand(FirstPlayer))) :
                try :
                    if ans == PlayerHand(FirstPlayer)[i][0] and 'Action' == PlayerHand(FirstPlayer)[i][2] and not PlayedCard:
                        CardName = PlayerHand(FirstPlayer)[i][0]
                        CardPlayed = PlayerHand(FirstPlayer)[i]
                        Action += 3
                        InPlay.append(CardPlayed)
                        PlayActionBank(FirstPlayer, CardName, CardPlayed)
                        PlayActionBank(FirstPlayer, CardName, CardPlayed, True)
                        PlayActionBank(FirstPlayer, CardName, CardPlayed, True)
                        PlayedCard = True
                    else :
                        #print('That is not in your hand')
                        pass
                except :
                    pass
            if not PlayedCard :
                print(ans,'is not in your hand')

def AddDurationCard(Card,FirstPlayer) :
    DurList = []
    #List = (CardList,IsTurnPlayed)
    DurList.append(Card)
    DurList.append(True)
    if FirstPlayer :
        DurationLand1.append(DurList)
    else :
        DurationLand2.append(DurList)

def PlayGimli(FirstPlayer) :
    global Buy
    TrashCards(FirstPlayer, 1, True, 'Copper') #Should be treasure
    Buy += 1
    AddDurationCard(gimli,FirstPlayer)

def PlayWharf(FirstPlayer) :
    global Buy
    Buy += 1
    ActionDrawCards(FirstPlayer, 2)
    AddDurationCard(wharf,FirstPlayer)

def PlayErebor(FirstPlayer) :
    global Gain
    GetGold = False
    if not FirstPlayer and AI :
        pass
    else :
        print('Actions: ' + str(Action))
    time.sleep(0.25)
    if len(InPlay) >= 3 and len(PlayerHand(FirstPlayer)) >= 3 :
        GetGold = True
    TrashCards(FirstPlayer, len(InPlay), True)
    if gold not in EmptyPile and GetGold :
        Gain = 1
        GainKingdomCard(gold,'Gold',FirstPlayer)

def PlayGollum(FirstPlayer) :
    global Action, money
    money += 2
    if FirstPlayer and OneRingFirstPlayer :
        Action += 1
        ActionDrawCards(FirstPlayer, 1)
    elif not FirstPlayer and OneRingSecondPlayer :
        Action += 1
        ActionDrawCards(FirstPlayer, 1)

def PlayShadowfax(FirstPlayer) :
    global Action
    TrashCards(FirstPlayer, 1, True)
    Action += 1
    print('Actions: ' + str(Action))
    time.sleep(0.25)
    GainKingdomCard(horse,'Horse',FirstPlayer)
    GainKingdomCard(horse,'Horse',FirstPlayer)

def PlayMilitia(FirstPlayer) :
    global money
    money += 2
    time.sleep(0.25)
    print('Actions: ' + str(Action))
    if FirstPlayer and AI and not AI2: #Person and AI - person's turn
        print('Player played')
        while len(PlayerHand(False)) > 3 :
            DiscardCard(True,-1)
    elif not FirstPlayer and AI and not AI2: #Person and AI - AI's turn
        print('AI played')
        while len(PlayerHand(True)) > 3 :
            Discarded = False
            PrintCards(True,'Hand',PlayerHand) 
            ans = DomCardPlays.translate(input(str(P1Name) + ' which card do you want to discard? '))
            for i in range(0,len(PlayerHand(True))) and not Discarded :
                if ans == PlayerHand(True)[i][0] :
                    DiscardCard(True,i)
                    Discarded = True
    elif FirstPlayer and AI2:                           # AI and AI2 - AI2's turn
        print('AI2 played')
        while len(PlayerHand(True)) > 3 :
            DiscardCard(False,-1)
    elif FirstPlayer and AI2:                          # AI and AI2 - AI's turn4
        print('AI1 played')
        while len(PlayerHand(False)) > 3 :
            DiscardCard(False,-1)

    elif FirstPlayer :                                 # Person1 and Person2 - Person1's turn
        print('Player1 played')
        while len(PlayerHand(False)) > 3 :
            Discarded = False
            PrintCards(False,'Hand',PlayerHand) 
            ans = DomCardPlays.translate(input(str(P2Name) + ' which card do you want to discard? '))
            for i in range(0,len(PlayerHand(False))) :
                if ans == PlayerHand(False)[i][0] and not Discarded:
                    DiscardCard(False,i)
                    Discarded = True
    elif not FirstPlayer:                              # Person1 and Person2 - Person2's turn
        print('Player2 played')
        while len(PlayerHand(True)) > 3 :
            Discarded = False
            PrintCards(True,'Hand',PlayerHand) 
            ans = DomCardPlays.translate(input(str(P1Name) + ' which card do you want to discard? '))
            for i in range(0,len(PlayerHand(True))) and not Discarded :
                if ans == PlayerHand(True)[i][0] :
                    DiscardCard(True,i)
                    Discarded = True             

def PlayBoromir(FirstPlayer) :
    global Gain
    choice = ''
    if not FirstPlayer and AI or AI2 :
        if FirstPlayer and OneRingFirstPlayer :
            choice = '1'
        elif not FirstPlayer and OneRingSecondPlayer :
            choice = '1'
        else :
            choice = '2'
    else :
        print('Actions: ' + str(Action))
        time.sleep(0.25)
        print('Choose one: 1 = Take One Ring, +4 Coffers gain Gold; 2 = play an Action from your hand twice.')
        choice = input()
    if choice == '1' :
        if TakeOneRing(FirstPlayer) :
            GetCoffers(FirstPlayer, 4)
            if gold not in EmptyPile  :
                Gain = 1
                GainKingdomCard(gold,'Gold',FirstPlayer)
        else :
            print('You already have the One Ring')
    else :
        PlayThroneRoom(FirstPlayer)
    

def PlayIronmonger(FirstPlayer) :
    global Action, money
    Action += 1
    ActionDrawCards(FirstPlayer, 1)
    Reveal = RevealCards(FirstPlayer, 1)[0]
    if AI and not FirstPlayer or AI2 :
        if Reveal[2] == 'Victory' :
            print('Discarded',Reveal[0])
            PlayerDiscard(FirstPlayer).append(Reveal)
            PlayerDeck(FirstPlayer).pop(0)
        else :
            pass
    else :
        ans = input('Do you want to discard ' + str(Reveal[0]) + '? ')
        if ans == 'y' or ans == 'yes' :
            print('Discarded',Reveal[0])
            PlayerDiscard(FirstPlayer).append(Reveal)
            PlayerDeck(FirstPlayer).pop(0)
        else :
            pass
    if Reveal[2] == 'Victory' :
        ActionDrawCards(FirstPlayer, 1)
    if Reveal[2] == 'Treasure' :
        print('+$1')
        money += 1
    if Reveal[2] == 'Action' :
        Action += 1
        print('+1 Action')

def PlayMoneylender(FirstPlayer) :
    global money
    time.sleep(0.25)
    if TrashCards(FirstPlayer, 1, False, 'Copper') :
        money += 3
    print('Actions:',str(Action))
    print('Money:',str(money))
    
def PlayThroneRoom(FirstPlayer) :
    global Action
    PlayedCard = False
    if AI and not FirstPlayer or AI2 :
        #Change to calc what best based on what have in deck
        if PlayTerminalDraw(True) :
            Action += 1
            AIPlayCard(InPlay[-1],FirstPlayer, True)
        elif PlayActionDraw() :
            Action += 1
            AIPlayCard(InPlay[-1],FirstPlayer, True)
        elif PlayCurser() :
            Action += 1
            AIPlayCard(InPlay[-1],FirstPlayer, True)
        elif PlayTerminalPayload() :
            Action += 1
            AIPlayCard(InPlay[-1],FirstPlayer, True)
        elif PlayVillageCard() :
            Action += 1
            AIPlayCard(InPlay[-1],FirstPlayer, True)
        elif PlayActionPayload() :
            Action += 1
            AIPlayCard(InPlay[-1],FirstPlayer, True)
        elif PlayTrasher(True) :
            Action += 1
            AIPlayCard(InPlay[-1],FirstPlayer, True)
        elif PlayTerminalDraw(False) :
            Action += 1
            AIPlayCard(InPlay[-1],FirstPlayer, True)
        elif PlayTrasher(False) :
            Action += 1
            AIPlayCard(InPlay[-1],FirstPlayer, True)
    else :
        while not PlayedCard :
            ans = DomCardPlays.translate(input('What Action card do you want to throne? '))
            if ans == 'n' :
                PlayedCard = True
            for i in range(0, len(PlayerHand(FirstPlayer))) :
                if ans == PlayerHand(FirstPlayer)[i][0] and 'Action' == PlayerHand(FirstPlayer)[i][2] and not PlayedCard:
                    CardName = PlayerHand(FirstPlayer)[i][0]
                    CardPlayed = PlayerHand(FirstPlayer)[i]
                    Action += 2
                    InPlay.append(CardPlayed)
                    PlayActionBank(FirstPlayer, CardName, CardPlayed)
                    PlayActionBank(FirstPlayer, CardName, CardPlayed, True)
                    PlayedCard = True
                else :
                    #print('That is not in your hand')
                    pass
            if not PlayedCard :
                print(ans,'is not in your hand')
    
def PlayRats(FirstPlayer) :
    global Action, Gain, CanTrashRats
    Action += 1
    ActionDrawCards(FirstPlayer, 1)
    CanTrashRats = False
    TrashCards(FirstPlayer, 1, True)
    CanTrashRats = True
    if rats not in EmptyPile  :
        Gain = 1
        GainKingdomCard(rats,'Rats',FirstPlayer)
    
def PlayRohan(FirstPlayer) :
    global Action
    card_discarded = False
    ans = DomCardPlays.translate(input('What Victory card do you want to discard? '))
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
    TrashCards(FirstPlayer, 1, True)

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

def GainKingdomCard(Card,Name,FirstPlayer, *Hand) :
    global Gain
    if RemoveCardFromSupply(Name) :
        CheckGainBonus(FirstPlayer, Name)
        CheckWhileInPlayAbilities(FirstPlayer, 'Gain')
        if FirstPlayer :
            print(P1Name,'gained a',Name + '.')
        else :
            print(P2Name,'gained a',Name + '.')
        Gain -= 1
        try :
            if Hand :
                PlayerHand(FirstPlayer).append(Card)
            else :
                PlayerDiscard(FirstPlayer).append(Card)
        except :
            PlayerDiscard(FirstPlayer).append(Card)
    else :
        EmptyPile.append(Card)
        print(Name,'pile is empty.')
        
def PlayWorkshop(FirstPlayer) :
    global Gain
    Gain = 1
    while Gain > 0 :
        if AI and not FirstPlayer or AI2 :
            if GameStrat(FirstPlayer) == 'SpellStrat' or GameStrat(FirstPlayer) == 'EngineStrat' or GameStrat(FirstPlayer) == 'DoubleStrat' or GameStrat(FirstPlayer) == 'TestStrat' :
                if CountCard(FirstPlayer, copper) < 5 and CountCard(FirstPlayer, silver) < 2 and silver not in EmptyPile :
                    GainKingdomCard(silver,'Silver',FirstPlayer)
                elif village not in EmptyPile and CountCard(FirstPlayer, smithy) > CountCard(FirstPlayer, village) :
                    GainKingdomCard(village,'Village',FirstPlayer)
                elif smithy not in EmptyPile and (CountCard(FirstPlayer, smithy) == CountCard(FirstPlayer, village) or CountCard(FirstPlayer, smithy) < CountCard(FirstPlayer, village)):
                    GainKingdomCard(smithy,'Smithy',FirstPlayer)
                else :
                    Gain = 0
            elif GameStrat(FirstPlayer) == 'BigMoneyStrat' :
                if smithy in kingdom and smithy not in EmptyPile and CountCard(FirstPlayer, smithy) < len(PlayerDeck(FirstPlayer))/8 :
                    BuyKingdomCard(smithy,'Smithy',FirstPlayer)
                else:
                    BuyKingdomCard(silver,'Silver',FirstPlayer)
        else :
            CardBought = DomCardPlays.translate(input('What do you want to gain? '))
            if CardBought == 'n' :
                Gain = 0
            for i in range(0,len(kingdom)) :
                    if str(CardBought) == kingdom[i][0] :
                        #checks if the card you named is in the kingdom 
                        if int(kingdom[i][1]) <= (4 + CostReduction) :
                        #and if it costs 4 or less
                            if RemoveCardFromSupply(CardBought) :
                                #and if there are any left
                                CheckGainBonus(FirstPlayer, CardBought)
                                CheckWhileInPlayAbilities(FirstPlayer, 'Gain')
                                PlayerDiscard(FirstPlayer).append(kingdom[i])
                                print('You gained a', CardBought)
                                Gain -= 1
                                if kingdom[i][2] == 'Victory' :
                                    if FirstPlayer :
                                        PlayerOnePoints += int(kingdom[i][3])
                                    else :
                                        PlayerTwoPoints += int(kingdom[i][3])
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

def DiscardCard(FirstPlayer, CardPos) :
    if (not FirstPlayer and AI) or AI2 :
        if curse in PlayerHand(FirstPlayer) :
             Card = curse
        elif estate in PlayerHand(FirstPlayer) :
            Card = estate
        elif copper in PlayerHand(FirstPlayer) :
            if PlayerHand(FirstPlayer).count(smithy) > 1 and PlayerHand(FirstPlayer).count(village) == 0 :
                Card = smithy
            else :
                Card = copper
        else :
            try :
                randomVar = random.randint(0,len(PlayerHand(FirstPlayer)) - 1)
            except :
                randomVar = 0
            try : 
                Card = PlayerHand(FirstPlayer)[randomVar]
            except :
                pass
        print('Discarded',Card[0])
        PlayerDiscard(FirstPlayer).append(Card)
        PlayerHand(FirstPlayer).pop(PlayerHand(FirstPlayer).index(Card))
    else :
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

def PlayHorse(FirstPlayer) :
    global Action, HorsePile
    Action += 1
    ActionDrawCards(FirstPlayer, 2)
    InPlay.remove(horse)
    HorsePile += 1

def CastInspiration(FirstPlayer) :
    global money
    RevealCards(FirstPlayer, 1)
    #if action or treasure play
    #+$1
    #else gain wish

def CastGatheringStorm(FirstPlayer) :
    global money, Buy, PlayerOnePoints, PlayerTwoPoints
    money += 3
    Buy += 1
    if FirstPlayer :
        PlayerOnePoints += len(InPlay)//3
        print('Gained',str(len(InPlay)//3),'VP')
    else :
        PlayerTwoPoints += len(InPlay)//3
        print('Gained',str(len(InPlay)//3),'VP')

def CastMidasTouch(FirstPlayer) :
    TrashCards(FirstPlayer, 1, True)
    GainKingdomCard(gold,'Gold',FirstPlayer, True)

def CastSummonFamiliar(FirstPlayer) :
    global scroll
    ActionDrawCards(FirstPlayer, 3)
    SF = int(scroll[1]) - 2
    if SF < 0 :
        Sf = 0
    change = list(scroll)
    change[1] = str(SF)
    scroll = tuple(change)
    print(scroll)

def CastPrestidigitation(FirstPlayer) :
    global Action, money, Buy
    Action += 1
    money += 1
    Buy += 1
    ActionDrawCards(FirstPlayer, 1)
    TrashCards(FirstPlayer, 1, False)

def CastHaste(FirstPlayer) :
    global Action
    Action += 2
    ActionDrawCards(FirstPlayer, 2)

def CastArcaneBolt(FirstPlayer) :
    global CostReduction, Buy
    print('Actions: ' + str(Action))
    Buy += 1
    CostReduction += 2

def PlayScroll(FirstPlayer, *Spell) :
    if not FirstPlayer and AI or AI2:
        if FirstPlayer :
            print(P1Name,'cast ' + str(Spell[0]))
        else :
            print(P2Name,'cast ' + str(Spell[0]))
        if Spell[0] == 'Prestidigitation' :
            CastPrestidigitation(FirstPlayer)
        elif Spell[0] == 'Arcane Bolt' :
            CastArcaneBolt(FirstPlayer)
        elif Spell[0] == 'Haste' :
            CastHaste(FirstPlayer)
        elif Spell[0] == 'Summon Familiar' :
            CastSummonFamiliar(FirstPlayer)
        elif Spell[0] == 'Inspiration' :
            CastInspiration(FirstPlayer)
        elif Spell[0] == 'Gathering Storm' :
            CastGatheringStorm(FirstPlayer)
        elif Spell[0] == 'Midas Touch' :
            CastMidasTouch(FirstPlayer)        
    elif len(PlayerSpellbook(FirstPlayer)) != 0 :
        Played = False
        while Played == False :
            ans = DomCardPlays.translate(input('Which Spell do you want to cast? '))
            if ans == 'Prestidigitation' and prestidigitation in PlayerSpellbook(FirstPlayer) :
                Played = True
                print('You cast Prestidigitation')
                CastPrestidigitation(FirstPlayer)
            elif ans == 'Arcane Bolt' and arcane_bolt in PlayerSpellbook(FirstPlayer) :
                Played = True
                print('You cast Arcane Bolt')
                CastArcaneBolt(FirstPlayer)
            elif ans == 'Haste' and haste in PlayerSpellbook(FirstPlayer) :
                Played = True
                print('You cast Haste')
                CastHaste(FirstPlayer)
            elif ans == 'Summon Familiar' and summon_familiar in PlayerSpellbook(FirstPlayer) :
                Played = True
                print('You cast Summon Familiar')
                CastSummonFamiliar(FirstPlayer)
            elif ans == 'Inspiration' and inspiration in PlayerSpellbook(FirstPlayer) :
                Played = True
                print('You cast Inspiration')
                CastInspiration(FirstPlayer)
            elif ans == 'Gathering Storm' and gathering_storm in PlayerSpellbook(FirstPlayer) :
                Played = True
                print('You cast Gathering Storm')
                CastGatheringStorm(FirstPlayer)
            elif ans == 'Midas Touch' and midas_touch in PlayerSpellbook(FirstPlayer) :
                Played = True
                print('You cast Midas Touch')
                CastMidasTouch(FirstPlayer)
            else :
                print("You don't have",ans,"in your Spellbook.")
    else :
        print("You don't have any Spells in your Spellbook.")
        print('Actions: ' + str(Action))
def PlaySmithy(FirstPlayer) :
    ActionDrawCards(FirstPlayer, 3)
    
def PlayVillage(FirstPlayer) :
    global Action
    Action += 2
    ActionDrawCards(FirstPlayer, 1)

def PlayChapel(FirstPlayer) :
    if not FirstPlayer and AI :
        pass
    else :
        print('Actions: ' + str(Action))
    time.sleep(0.25)
    TrashCards(FirstPlayer, 4, False)

def RevealCards(FirstPlayer, Num) :
    Revealed = []
    for i in range(Num) :
        try :
            print('revealed',PlayerDeck(FirstPlayer)[0][0])
            Revealed.append(PlayerDeck(FirstPlayer)[0])
            PlayerDeck(FirstPlayer).pop(0)
        except :
            if len(PlayerDiscard(FirstPlayer)) == 0 : #if you drew your deck
                break
            if FirstPlayer :
                print("Shuffling", str(P1Name) + "'s deck") 
            else :
                print("Shuffling", str(P2Name) + "'s deck")
            PlayerDeck(FirstPlayer).extend(PlayerDiscard(FirstPlayer))#add discard to deck
            PlayerDiscard(FirstPlayer).clear() #delete discard    
            random.shuffle(PlayerDeck(FirstPlayer)) #shuffle deck
            Revealed.append(PlayerDeck(FirstPlayer)[0])
            PlayerDeck(FirstPlayer).pop(0)
            print('revealed',PlayerDeck(FirstPlayer)[0][0])
    for i in range(0,Num) :
        PlayerDeck(FirstPlayer).insert(0, Revealed[i])
    return Revealed
        
def TrashCards(FirstPlayer, TrashNum, Forced, *SpefCard) :
    trashcount = 0
    Card = ['nothing']
    randomVar = 0
    while trashcount < TrashNum :
        if not FirstPlayer and AI or AI2:
            card_trashed = False
            try :
                tryit = SpefCard[0] #see if a certain card is specified 
            except :
                if curse in PlayerHand(FirstPlayer) :
                    Card = curse
                elif estate in PlayerHand(FirstPlayer) :
                    Card = estate
                elif copper in PlayerHand(FirstPlayer) :
                    if GameStrat(FirstPlayer) == 'JoelStrat' :
                        trashcount = TrashNum
                        break #end trash
                    if GameStrat(FirstPlayer) == 'EngineStrat' or GameStrat(FirstPlayer) == 'SpellStrat' or GameStrat(FirstPlayer) == 'DoubleStrat' or GameStrat(FirstPlayer) == 'TestStrat' :
                        if CountCard(FirstPlayer, copper) == 1 and not Forced :
                            trashcount = TrashNum
                            break #end trash
                        else :
                            Card = copper
                    elif GameStrat(FirstPlayer) == 'MegaTurnStrat' :
                        if CountCard(FirstPlayer, copper) <= 2 and CountCard(FirstPlayer, bridge) < 2 and not Forced :
                            trashcount = TrashNum
                            break #end trash
                        else :
                            Card = copper
                    elif GameStrat(FirstPlayer) == 'MegaTurnStrat#2' :
                        if CountCard(FirstPlayer, copper) <= 2 and CountCard(FirstPlayer, bridge) < 2 and not Forced :
                            trashcount = TrashNum
                            break #end trash
                        else :
                            Card = copper
                elif not Forced :
                    trashcount = TrashNum #end trash
                else :
                    try :
                        randomVar = random.randint(0,len(PlayerHand(FirstPlayer)) - 1)
                    except :
                        randomVar = 0
                    try : 
                        Card = PlayerHand(FirstPlayer)[randomVar]
                    except :
                        trashcount = TrashNum
                        break #end trash
            else :
                Card = SpefCard[0]
            try :
                if Card[0] == 'Rats' and CanTrashRats or Card[0] != 'Rats' :
                    Trash(FirstPlayer, PlayerHand(FirstPlayer).index(Card), Card)
                else :
                    try :
                        randomVar = random.randint(0,len(PlayerHand(FirstPlayer)) - 1)
                    except :
                        randomVar = 0
                    Card = PlayerHand(FirstPlayer)[randomVar]
            except :
                print('failed to trash',Card[0])
                if PlayerHand(FirstPlayer).count(rats) == len(PlayerHand(FirstPlayer)) :
                    print('Only Rats')
                    PrintCards(FirstPlayer,'Hand',PlayerHand) 
                    trashcount = TrashNum
                    break #end trash
            else :
                trashcount += 1
                card_trashed = True
        else : #Real Player
            card_trashed = False
            try :
                tryit = SpefCard[0] #see if a certian card is specified 
            except :
                time.sleep(0.25)
                ans = DomCardPlays.translate(input('Which card do you want to trash? '))
            else :
                ans = SpefCard[0]
            if ans == 'n' and not Forced:
                break
            elif ans == 'n' and Forced :
                print('You need to trash',str((TrashNum - trashcount)),'more card(s)')
            for i in range(0,len(PlayerHand(FirstPlayer))) :
                try :
                    test = PlayerHand(FirstPlayer)[i][0] #check if index is out of range
                except :
                    pass
                else :
                    if ans == PlayerHand(FirstPlayer)[i][0] and card_trashed == False :
                        if ans == 'Rats' and CanTrashRats or ans != 'Rats' :
                            Trash(FirstPlayer, i, PlayerHand(FirstPlayer)[i])
                            trashcount += 1
                            card_trashed = True
                        elif PlayerHand(FirstPlayer).count(rats) == len(PlayerHand(FirstPlayer)) :
                            print('Only Rats')
                            PrintCards(FirstPlayer,'Hand',PlayerHand) 
                            trashcount = TrashNum
                            break #end trash
            if not card_trashed :
                print("You can't trash that card")
    if card_trashed :
        return True
    else :
        return False

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
    if Card[0] == 'Rats' :
        ActionDrawCards(FirstPlayer, 1)
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

def Coffers(FirstPlayer) :
    if FirstPlayer :
        return Coffers1
    else :
        return Coffers2

def PlayerSpellbook(FirstPlayer) :
    if FirstPlayer :
        return Spellbook1
    else :
        return Spellbook2

def PlayCoffers(FirstPlayer) :
    global Coffers1, Coffers2, money
    if not FirstPlayer and AI and Coffers(FirstPlayer) > 0 :
        money += Coffers1
        Coffers1 = 0
    elif AI2 and Coffers(FirstPlayer) > 0 :
        money += Coffers2
        Coffers2 = 0
    elif Coffers(FirstPlayer) > 0 :
        ans = input('How many Coffers do you want to play? ')
        if int(ans) <= Coffers(FirstPlayer) :
            if FirstPlayer :
                Coffers1 -= int(ans)
            else :
                Coffers2 -= int(ans)
            money += int(ans)
        elif ans == 'n' :
            pass
        else :
            print('You do not have that many Coffers.')
            PlayCoffers(FirstPlayer)

def BuyPhase(FirstPlayer) :
    Auto = False
    if AI and not FirstPlayer :
        Auto = True
        PlayCoffers(FirstPlayer)
        PlayTreasures(FirstPlayer, Auto, AI)
        BuyCard(FirstPlayer, AI)
    elif AI2 and FirstPlayer :
        Auto = True
        PlayCoffers(FirstPlayer)
        PlayTreasures(FirstPlayer, Auto, AI)
        BuyCard(FirstPlayer, AI)
    else :
        PlayCoffers(FirstPlayer)
        ans = input('Do you want to autoplay all treasures? ')
        if ans == 'y' :
            Auto = True
        elif ans == 'info' :
            PrintInfo(FirstPlayer)
        PlayTreasures(FirstPlayer, Auto, AI)
        PrintCards(FirstPlayer,'InPlay',FindInPlay)
        BuyCard(FirstPlayer, AI)
        
def RemoveCardFromSupply(Card) :
    global ScrollPile, HorsePile, CopperPile, SilverPile, GoldPile, EstatePile, DutchyPile, ProvincePile, CursePile, Pile1, Pile2, Pile3, Pile4, Pile5, Pile6, Pile7, Pile8, Pile9, Pile10
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
    elif Card == 'Horse' and HorsePile > 0 :
        HorsePile -= 1
    elif Card == 'Scroll' and ScrollPile > 0 :
        ScrollPile -= 1
    elif Card == Pile1Name  and Pile1 > 0:
        Pile1 -= 1
    elif Card == Pile2Name  and Pile2 > 0:
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
    PrintCards(FirstPlayer,'Spellbook',PlayerSpellbook)
    print('Turn: ' + str(TurnCount))

def AddPlayerPoints(FirstPlayer,Num) :
    global PlayerOnePoints, PlayerTwoPoints
    if FirstPlayer :
        PlayerOnePoints += Num
    else :
        PlayerTwoPoints += Num

def GameStrat(FirstPlayer) :
    #Strats: EngineStrat, DoubleStrat, JoelStrat, MegaTurnStrat, MegaTurnStrat#2, TestStrat, BigMoneyStrat
    #if chapel in kingdom and village in kingdom and market in kingdom and smithy or witch in kingdom :
    #    return 'EngineStrat'
    if FirstPlayer :
        return P1Strat
        
        #return 'SpellStrat'
        #return 'MegaTurnStrat#2'
        #return 'JoelStrat' 
        #return 'DoubleStrat'
    else :
        #return 'MegaTurnStrat'
    
        return P2Strat
        #return 'EngineStrat'
        #return 'TestStrat'
def ChooseStrat() :
    global P1Strat, P2Strat
    P1Strat = 'BigMoneyStrat'
    P2Strat = 'BigMoneyStrat' #'MegaTurnStrat'
    #P1Strat = ChooseAIStrat()
    #P2Strat = ChooseAIStrat()
    
def CheckVillageSmithy(FirstPlayer) : #Unused
    if CountCard(FirstPlayer, smithy) > CountCard(FirstPlayer, village) :
        print('more smithies')
    elif CountCard(FirstPlayer, smithy) < CountCard(FirstPlayer, village) :
        print('more villages')
    elif CountCard(FirstPlayer, smithy) == CountCard(FirstPlayer, village) :
        print('same ratio')
    else :
        print('check does not work')

def CheckPhase(FirstPlayer, Strat) :
    if TurnCount < 3 :
        return 'Open'
    elif Strat == 'TestStrat' :
        return 'Build'
    elif Strat == 'EngineStrat' :
        if money > 7 and TurnCount > 7 :
            return 'Green'
        else :
            return 'Build'
    elif Strat == 'SpellStrat' :
        if money > 7 and TurnCount > 7 :
            return 'Green'
        else :
            return 'Build'
    elif Strat == 'BigMoneyStrat' :
        if TurnCount > 6 and money > 7:
            return 'Green'
        elif PlayerOnePoints > 15 and abs(PlayerOnePoints - PlayerTwoPoints) <= 3 :
            return 'Green'
        else :
            return 'Build'
    elif Strat == 'DoubleStrat' :
        if money > 15 :
            return 'Green'
        elif PlayerOnePoints > 15 and abs(PlayerOnePoints - PlayerTwoPoints) <= 3 :
            return 'Green'
        #elif PlayerPoints(FirstPlayer) >
        else :
            return 'Build'
    elif Strat == 'MegaTurnStrat' :
        if UnconMega :
            if InPlay.count(bridge) < 7 :
                return 'Build'
            else :
                return 'Green'
        else :
            if InPlay.count(bridge) > 6 :
                return 'Green'
            elif village not in EmptyPile or bridge not in EmptyPile :
                return 'Build'
            else :
                return 'Green'
    elif Strat == 'MegaTurnStrat#2' :
        if UnconMega :
            if InPlay.count(bridge) < 7 :
                return 'Build'
            else :
                return 'Green'
        else :
            if InPlay.count(bridge) > 6 :
                return 'Green'
            elif village not in EmptyPile or bridge not in EmptyPile or CountCard(FirstPlayer,bridge) > 6 :
                return 'Build'
            else :
                return 'Green'
    elif Strat == 'JoelStrat' :
        if CountCard(FirstPlayer, gold) >= 2 and CountCard(FirstPlayer, silver) >= 1 and money > 7:
            return 'Green'
        elif PlayerPoints(FirstPlayer) >= 30 :
            return 'Green'
        else :
            return 'Build'


def CheckLowPiles(FirstPlayer) :
    Gains = Buy
    Estates = 0
    if FirstPlayer :
        for i in range(0,Gains) :
            Estates = i
            Gains = Buy - Estates
            if (PlayerOnePoints + Estates) > PlayerTwoPoints : #can you gain cards plus estates needed?
                if len(EmptyPile) == 2 :
                    for i in range(0,10) :
                        if CostReduction > 2 :
                            Estates2 = 0
                        else :
                            Estates2 = Estates
                        if not kingdom[i] in EmptyPile and FindPile(i) <= Gains and money > ((int(kingdom[i][1]) - CostReduction)*Gains + (2 - CostReduction)*Estates2): #if have enough gains
                            print('Pile Out!')
                            for i in range(Estates) :
                                BuyKingdomCard(estate,'Estate',FirstPlayer)
                            for i in range(Gains) :
                                BuyKingdomCard(kingdom[i],kingdom[i][0],FirstPlayer)

                
    else :
        for i in range(0,Gains) :
            Estates = i
            Gains = Buy - Estates
            if (PlayerTwoPoints + Estates) >= PlayerOnePoints : #can you gain cards plus estates needed?
                if len(EmptyPile) == 2 :
                    for i in range(0,10) :
                        if CostReduction > 2 :
                            Estates2 = 0
                        else :
                            Estates2 = Estates
                        if not kingdom[i] in EmptyPile and FindPile(i) <= Gains and money > ((int(kingdom[i][1]) - CostReduction)*Gains + (2 - CostReduction)*Estates2): #if have enough gains
                            for j in range(Estates) :
                                BuyKingdomCard(estate,'Estate',FirstPlayer)
                            for j in range(Gains) :
                                BuyKingdomCard(kingdom[i],kingdom[i][0],FirstPlayer)


        

def KingdomHueristic(Type) :
    if Type == 'Village' :
        if village in kingdom or throne_room in kingdom or kings_court in kingdom :
            return True
    elif Type == 'CostReduction' :
        if bridge in kingdom :
            return True
    elif Type == 'Trasher' :
        if shadowfax in kingdom or counterfeit in kingdom or junk_dealer in kingdom or chapel in kingdom or moneylender in kingdom or erebor in kingdom :
            return True
    elif Type == 'Cards' :
        if smithy in kingdom or laboratory in kingdom or witch in kingdom or wharf in kingdom :
            return True
    elif Type == 'Draw' :
        if laboratory in kingdom :
            return True
        if KingdomHueristic('Village') and KingdomHueristic('Cards') :
            return True
            
        
def ChooseAIStrat() :
    #Populate options
    Options = []
    #Big Money
    Options.append('BigMoneyStrat')
    #Joel
    Options.append('JoelStrat')
    #Mega Turn
    if KingdomHueristic('CostReduction') and KingdomHueristic('Village') and KingdomHueristic('Trasher') and KingdomHueristic('Draw'):
        Options.append('MegaTurnStrat')
    #Engine
    if KingdomHueristic('Village') and KingdomHueristic('Trasher') and KingdomHueristic('Draw') :
        Options.append('EngineStrat')
    #Spell Engine
    if KingdomHueristic('Village') and KingdomHueristic('Trasher') and KingdomHueristic('Draw') :
        Options.append('SpellStrat')   
    #Would determine with data
    return Options[random.randint(0,len(Options) - 1)]
    

def CheckContested(FirstPlayer, Strat) :
    global UnconMega
    if Strat == 'MegaTurnStrat' or Strat == 'MegaTurnStrat#2' :
        if CountCard(FirstPlayer, bridge, True) > 0 :
            UnconMega = False
        if CountCard(FirstPlayer, village, True) > 1 :
            UnconMega = False
        #if not UnconMega and bridge in EmptyPile or village in EmptyPile :
        #    Green = True
        
def BuyStrat(FirstPlayer, Money, TurnCount) :
    global PlayerTwoPoints, Buy, PlayerOnePoints
    while Buy > 0 : #Bob
        CheckLowPiles(FirstPlayer)
        if CheckPhase(FirstPlayer, GameStrat(FirstPlayer)) == 'Open' : #Opening Buys
            OpeningBuy(FirstPlayer, GameStrat(FirstPlayer))
        elif CheckPhase(FirstPlayer, GameStrat(FirstPlayer)) == 'Build' : #Building phase    
            BuildingPhase(FirstPlayer, GameStrat(FirstPlayer))
        else :                                                          #Greening phase
            BuyGreen(FirstPlayer)

def Ab_BuildingPhase(FirstPlayer, Strat) :
    #Purpose: to chose which cards AI should buy
    #1. Determine which cards they can buy
    #2. Figure out what the deck is like
    #3. Determine priorities for the deck (rank cards)
    #4. Determine which combinations of cards can buy gives most value (add ranks)
    #5. Buy those cards
    CreateBuyPool() #Fills CanBuy list
    CheckDeckComp(FirstPlayer, Strat)
    RankCards()
    CalcCards()
    BuyCalcCards()
    

def CreateBuyPool() :
    CanBuy = []
    #Check kingdom
    #If card is less than money add to Buy
    for i in len(kingdom) : 
        if kingdom[i][1] <= money : 
            CanBuy.append(kingdom[i])

def CheckDeckComp(FirstPlayer, Strat) :
    #Generalize cards
    #put them into list
    #compare list to master list of Strat
    #figure out what else is needed
    GeneralizeDeck(FirstPlayer)

    #!!!
    #NEXT COMPARE TO MASTER LIST
    #!!!
    
def GeneralizeDeck(FirstPlayer) :
    global GenDeck1, GenDeck2,DrawDeck1,DrawDeck2
    #Set up Deck vars
    #itirate through deck
    #gen each card
    #return list
    GenDeck1 = []
    GenDeck2 = []
    DrawDeck1 = []
    DrawDeck2 = []
    for i in PlayerDeck(FirstPlayer) : #Go through deck
        GenDeck(FirstPlayer).append(GeneralizeCardType(i)) #Add generalized card to new decklist
        DrawDeck(FirstPlayer).append(GenCardDraw(i)) #Add cards to check deck draw capacity

def GeneralizeCardType(Card) :
    #check conditions for generalization
    if Card[0] == 'Village' : 
        return 'Village'
    elif Card[0] == 'Throne Room' or Card[0] == "King's Court" :
        return 'Throne'
    elif Card[0] == 'Junk Dealer' or Card[0] == 'Chapel' or Card[0] == 'Moneylender' or Card[0] == 'Erebor' or Card[0] == 'Shadowfax' or Card[0] == 'Counterfeit' :
        return 'Trasher'
    elif Card[0] == 'Smithy' or Card[0] == 'Witch' or Card[0] == 'Wharf' :
        return 'Cards'
    elif Card[0] == 'Laboratory' or Card[0] == 'Horse' :
        return 'Draw'
    elif Card[0] == 'Bridge' or Card[0] == 'Workshop' or Card[0] == 'Bill Ferny' or Card[0] == 'Gollum' or Card[0] == 'Boromir' or Card[0] == 'Gimli' or Card[0] == 'Militia' :
        return 'Payload'
    elif Card[0] == 'Market' or Card[0] == 'Ironmonger' :
        return 'Peddler'
    elif Card[0] == 'Rats' :
        return 'Rats'
    elif Card[0] == 'Estate' :
        return 'Estate'
    elif Card[0] == 'Copper' :
        return 'Copper'
    elif Card[2] == 'Treasure' :
        return 'Treasure'
    elif Card[2] == 'Victory' :
        return 'Victory'
    elif Card[2] == 'Curse' :
        return 'Curse'
    else :
        return 'Other'
    
def GenCardDraw(Card) :
    #check how affects draw
    '''
    elif or Card[0] == 'Shadowfax' :
        return 'D0'
    '''
    if Card[0] == 'Laboratory' or Card[0] == 'Horse' :
        return 'D2'
    elif Card[0] == 'Village' or Card[0] == 'Ironmonger' or Card[0] == 'Junk Dealer' or Card[0] == 'Rats' or Card[0] == 'Market' :
        return 'D1'
    elif Card[0] == 'Throne Room' or Card[0] == "King's Court" :
        return 'Throne' 
    elif Card[0] == 'Wharf' :
        return 'C4'
    elif Card[0] == 'Smithy' :
        return 'C3'
    elif Card[0] == 'Witch' :
        return 'C2'
    elif Card[0] == 'Bridge' or Card[0] == 'Workshop' or Card[0] == 'Militia' or Card[0] == 'Gimli' or Card[0] == 'Bill Ferny' or Card[0] == 'Chapel' or Card[0] == 'Moneylender' or Card[0] == 'Erebor' or Card[0] == 'Boromir' or Card[0] == 'Gollum' :
        return 'C0'
    else :
        return 'Dead'
    
def GenDeck(FirstPlayer) :
    if FirstPlayer :
        return GenDeck1
    else :
        return GenDeck2

def DrawDeck(FirstPlayer) :
    if FirstPlayer :
        return DrawDeck1
    else :
        return DrawDeck2

def RankCards() :
    #Based on DeckComp rank cards in can buy pool
    #look at cards in pool, assign number based on if its needed(at all and at the moment) - also rarity of cost
    pass

def CalcCards() :
    #Add together ranks of cards
    #Determine which combo gives best value
    pass

def BuyCalcCards() :
    #Buy cards that were calculated to be best
    pass
            
def BuildingPhase(FirstPlayer, Strat) :
    global Buy
    if Strat == 'TestStrat' :
        if money < 3 :
            Buy = 0
        elif money > 3 and rats not in EmptyPile :
            BuyKingdomCard(rats,'Rats',FirstPlayer)
        else :
            Buy = 0
    elif Strat == 'EngineStrat' :
        if money < 3 :
            Buy = 0
        elif money > 4 and not CardInDeck(FirstPlayer,market) and market not in EmptyPile :
            BuyKingdomCard(market,'Market',FirstPlayer)
        elif money > 5 and CountCard(FirstPlayer, gold) < 4 and gold not in EmptyPile :
            BuyKingdomCard(gold,'Gold',FirstPlayer)
        elif CountCard(FirstPlayer, copper) < 5 and CountCard(FirstPlayer, silver) < 2 and silver not in EmptyPile :
            BuyKingdomCard(silver,'Silver',FirstPlayer)
        elif village not in EmptyPile and (money == 3 or CountCard(FirstPlayer, smithy) > CountCard(FirstPlayer, village)) :
            BuyKingdomCard(village,'Village',FirstPlayer)
        elif CountCard(FirstPlayer, smithy) <= CountCard(FirstPlayer, village) and smithy not in EmptyPile :
            BuyKingdomCard(smithy,'Smithy',FirstPlayer)
        elif village not in EmptyPile and money > 2 :
            BuyKingdomCard(village,'Village',FirstPlayer)
        elif laboratory not in EmptyPile and money > 4 :
            BuyKingdomCard(laboratory,'Laboratory',FirstPlayer)
        else :
            print('Did not want to buy. Money:',money)
            Buy = 0
    elif Strat == 'SpellStrat' :
        if money < 2 :
            Buy = 0
        elif money > 4 and scroll not in EmptyPile and len(PlayerSpellbook(FirstPlayer)) > 0 :
            BuyKingdomCard(scroll,'Scroll',FirstPlayer)
        elif money > 5 and CountCard(FirstPlayer, gold) < 4 and gold not in EmptyPile :
            BuyKingdomCard(gold,'Gold',FirstPlayer)
        elif CountCard(FirstPlayer, copper) < 5 and CountCard(FirstPlayer, silver) < 2 and silver not in EmptyPile :
            BuyKingdomCard(silver,'Silver',FirstPlayer)
        elif money > 2 and gathering_storm not in PlayerSpellbook(FirstPlayer) :
            BuyLandscape(gathering_storm,'Gathering Storm',FirstPlayer)   
        elif money > 1 and len(PlayerSpellbook(FirstPlayer)) < 2 :
            if haste not in PlayerSpellbook(FirstPlayer) :
                BuyLandscape(haste,'Haste',FirstPlayer)
        elif village not in EmptyPile and (money == 3 or CountCard(FirstPlayer, smithy) > CountCard(FirstPlayer, village)) :
            BuyKingdomCard(village,'Village',FirstPlayer)
        elif CountCard(FirstPlayer, smithy) <= CountCard(FirstPlayer, village) and smithy not in EmptyPile :
            BuyKingdomCard(smithy,'Smithy',FirstPlayer)
        elif village not in EmptyPile and money > 2 :
            BuyKingdomCard(village,'Village',FirstPlayer)
        elif money > 4 and scroll not in EmptyPile :
            BuyKingdomCard(scroll,'Scroll',FirstPlayer)
        elif laboratory not in EmptyPile and money > 4 :
            BuyKingdomCard(laboratory,'Laboratory',FirstPlayer)
        else :
            print('Did not want to buy. Money:',money)
            Buy = 0
    elif Strat == 'BigMoneyStrat' :
        if money > 5 and gold not in EmptyPile :
            BuyKingdomCard(gold,'Gold',FirstPlayer)
        elif money > 3 and smithy in kingdom and smithy not in EmptyPile and CountCard(FirstPlayer, smithy) < len(PlayerDeck(FirstPlayer))/8 :
            BuyKingdomCard(smithy,'Smithy',FirstPlayer)
        elif money > 2 and silver not in EmptyPile:
            BuyKingdomCard(silver,'Silver',FirstPlayer)
        else :
            Buy = 0
    elif Strat == 'DoubleStrat' :
        if money < 3 :
            Buy = 0
        elif money > 4 and not CardInDeck(FirstPlayer,market) :
            BuyKingdomCard(market,'Market',FirstPlayer)
        elif money > 5 and CountCard(FirstPlayer, gold) < 4 :
            BuyKingdomCard(gold,'Gold',FirstPlayer)
        elif CountCard(FirstPlayer, copper) < 5 and CountCard(FirstPlayer, silver) < 2 :
            BuyKingdomCard(silver,'Silver',FirstPlayer)
        elif village not in EmptyPile and money == 3 or CountCard(FirstPlayer, smithy) > CountCard(FirstPlayer, village) :
            BuyKingdomCard(village,'Village',FirstPlayer)
        elif smithy not in EmptyPile and CountCard(FirstPlayer, smithy) <= CountCard(FirstPlayer, village) and money > 3:
            BuyKingdomCard(smithy,'Smithy',FirstPlayer)
        else :
            print('Did not want to buy. Money:',money)
            Buy = 0
    elif Strat == 'MegaTurnStrat' :
        CheckContested(FirstPlayer, Strat)
        if (money + CostReduction) < 3 :
            Buy = 0
        elif (money + CostReduction) > 3 and CountCard(FirstPlayer, bridge) < 8 and CountCard(FirstPlayer, bridge) <= (CountCard(FirstPlayer, smithy)*2 + 1) and (CountCard(FirstPlayer, bridge) + CountCard(FirstPlayer, smithy)) <= CountCard(FirstPlayer, village) and bridge not in EmptyPile :
            BuyKingdomCard(bridge,'Bridge',FirstPlayer)    
        elif village not in EmptyPile and (CountCard(FirstPlayer, bridge) + CountCard(FirstPlayer, smithy)) >= CountCard(FirstPlayer, village) :
            BuyKingdomCard(village,'Village',FirstPlayer)
        elif (money + CostReduction) > 3 and bridge not in EmptyPile and not UnconMega and CountCard(FirstPlayer, bridge) < 8 :
            BuyKingdomCard(bridge,'Bridge',FirstPlayer)
        elif smithy not in EmptyPile and (money + CostReduction) > 3 and (CountCard(FirstPlayer, bridge) + CountCard(FirstPlayer, smithy)) <= CountCard(FirstPlayer, village) :
            BuyKingdomCard(smithy,'Smithy',FirstPlayer)
        elif village not in EmptyPile :
            BuyKingdomCard(village,'Village',FirstPlayer)
        elif laboratory not in EmptyPile and (money + CostReduction) > 4 and (CountCard(FirstPlayer, laboratory) + CountCard(SecondPlayer(FirstPlayer), laboratory)) < 8 :
            BuyKingdomCard(laboratory,'Laboratory',FirstPlayer)
        else :
            print('Did not want to buy. Money:',money)
            Buy = 0
    elif Strat == 'MegaTurnStrat#2' :
        CheckContested(FirstPlayer, Strat)
        if (money + CostReduction) < 3 :
            Buy = 0
        elif (money + CostReduction) > 3 and CountCard(FirstPlayer, bridge) < 8 and CountCard(FirstPlayer, bridge) <= (CountCard(FirstPlayer, smithy)*2 + 1) and (CountCard(FirstPlayer, bridge) + CountCard(FirstPlayer, smithy)) <= CountCard(FirstPlayer, village) and bridge not in EmptyPile :
            BuyKingdomCard(bridge,'Bridge',FirstPlayer)    
        elif village not in EmptyPile and (CountCard(FirstPlayer, bridge) + CountCard(FirstPlayer, smithy)) >= CountCard(FirstPlayer, village) :
            BuyKingdomCard(village,'Village',FirstPlayer)
        elif (money + CostReduction) > 3 and bridge not in EmptyPile and not UnconMega and CountCard(FirstPlayer, bridge) < 8 :
            BuyKingdomCard(bridge,'Bridge',FirstPlayer)
        elif smithy not in EmptyPile and (money + CostReduction) > 3 and (CountCard(FirstPlayer, bridge) + CountCard(FirstPlayer, smithy)) <= CountCard(FirstPlayer, village) :
            BuyKingdomCard(smithy,'Smithy',FirstPlayer)
        elif village not in EmptyPile :
            BuyKingdomCard(village,'Village',FirstPlayer)
        elif laboratory not in EmptyPile and (money + CostReduction) > 4 and (CountCard(FirstPlayer, laboratory) + CountCard(SecondPlayer(FirstPlayer), laboratory)) < 8 :
            BuyKingdomCard(laboratory,'Laboratory',FirstPlayer)
        else :
            print('Did not want to buy. Money:',money)
            Buy = 0
    elif Strat == 'JoelStrat' :
        if (money + CostReduction) < 3 :
            Buy = 0
        elif (money + CostReduction) > 5 and gold not in EmptyPile :
            BuyKingdomCard(gold,'Gold',FirstPlayer)
        elif laboratory not in EmptyPile and (money + CostReduction) > 4 and CountCard(FirstPlayer,laboratory) < (CountCard(FirstPlayer,market) + 2) :
            BuyKingdomCard(laboratory,'Laboratory',FirstPlayer)
        elif market not in EmptyPile and (money + CostReduction) > 4 :
            BuyKingdomCard(market,'Market',FirstPlayer)
        elif (money + CostReduction) > 3 and bridge not in EmptyPile and CountCard(FirstPlayer, bridge) <= CountCard(FirstPlayer, smithy) :
            BuyKingdomCard(bridge,'Bridge',FirstPlayer)
        elif smithy not in EmptyPile and (money + CostReduction) > 3:
            BuyKingdomCard(smithy,'Smithy',FirstPlayer)
        elif CountCard(FirstPlayer, silver) <= CountCard(FirstPlayer, village) and silver not in EmptyPile :
            BuyKingdomCard(silver,'Silver',FirstPlayer)
        elif CountCard(FirstPlayer, village) < 2 and village not in EmptyPile:
            BuyKingdomCard(village,'Village',FirstPlayer)
        else :
            BuyKingdomCard(silver,'Silver',FirstPlayer)
            
def CountCard(FirstPlayer, Card, *OtherPlayer) :
    try :
        if OtherPlayer :
            if FirstPlayer :
                FirstPlayer = False
            else :
                FirstPlayer = True
    except :
        pass
    Num = PlayerHand(FirstPlayer).count(Card) + PlayerDeck(FirstPlayer).count(Card) + PlayerDiscard(FirstPlayer).count(Card) + InPlay.count(Card) 
    return Num

def CardInDeck(FirstPlayer,Card) :
    if Card in PlayerHand(FirstPlayer) or Card in PlayerDeck(FirstPlayer) or Card in PlayerDiscard(FirstPlayer) or Card in InPlay :
        return True
    else :
        return False
def OpeningBuy(FirstPlayer, Strat) :
    global Buy
    if Strat == 'TestStrat' :
        if money > 3 and rats in kingdom and rats not in EmptyPile :
            BuyKingdomCard(rats,'Rats',FirstPlayer)
        elif money > 2 :
            BuyKingdomCard(silver,'Silver',FirstPlayer)
        else :
            Buy = 0
    elif Strat == 'EngineStrat' or Strat == 'SpellStrat' or Strat == 'DoubleStrat' :
        if money < 5 and not CardInDeck(FirstPlayer,chapel) :
            BuyKingdomCard(chapel,'Chapel',FirstPlayer)
        elif money < 5 and CardInDeck(FirstPlayer,chapel) :
            BuyKingdomCard(workshop,'Workshop',FirstPlayer)
        elif money > 4 :
            BuyKingdomCard(market,'Market',FirstPlayer)
        elif money > 2 :
            BuyKingdomCard(silver,'Silver',FirstPlayer)
        else :
            Buy = 0
    elif Strat == 'BigMoneyStrat' :
        if money > 3 and smithy in kingdom :
            BuyKingdomCard(smithy,'Smithy',FirstPlayer)
        elif money > 2 :
            BuyKingdomCard(silver,'Silver',FirstPlayer)
        else :
             Buy = 0
    elif Strat == 'JoelStrat' :
        if money == 2 :
            BuyKingdomCard(chapel,'Chapel',FirstPlayer)
        elif money == 5 :
            BuyKingdomCard(laboratory,'Laboratory',FirstPlayer)
        elif money == 4 :
            BuyKingdomCard(bridge,'Bridge',FirstPlayer)
        else :
            BuyKingdomCard(silver,'Silver',FirstPlayer)
    elif Strat == 'MegaTurnStrat'or Strat == 'MegaTurnStrat#2':
        if money < 4 and not CardInDeck(FirstPlayer,chapel) :
            BuyKingdomCard(chapel,'Chapel',FirstPlayer)
        elif money > 3 :
            BuyKingdomCard(bridge,'Bridge',FirstPlayer)

def BuyGreen(FirstPlayer) :
    global PlayerTwoPoints, PlayerOnePoints, Buy
    if GameStrat(FirstPlayer) == 'SpellStrat' or GameStrat(FirstPlayer) == 'EngineStrat' or GameStrat(FirstPlayer) == 'DoubleStrat' or GameStrat(FirstPlayer) == 'TestStrat' :
        if money > 7 :
            if FirstPlayer :
                if ProvincePile == 1 and PlayerTwoPoints > (PlayerOnePoints + 6) and dutchy not in EmptyPile:
                    BuyKingdomCard(dutchy,'Dutchy',FirstPlayer)
                    PlayerOnePoints += 3
                elif ProvincePile == 1 and PlayerTwoPoints == (PlayerOnePoints + 6) and FirstPlayer and dutchy not in EmptyPile:
                    BuyKingdomCard(dutchy,'Dutchy',FirstPlayer)
                    PlayerOnePoints += 3
                elif province not in EmptyPile :
                    BuyKingdomCard(province,'Province',FirstPlayer)
                    PlayerOnePoints += 6
                else :
                    Buy = 0
            else :
                if ProvincePile == 1 and PlayerOnePoints > (PlayerTwoPoints + 6) and dutchy not in EmptyPile:
                    BuyKingdomCard(dutchy,'Dutchy',FirstPlayer)
                    PlayerTwoPoints += 3
                elif province not in EmptyPile :
                    BuyKingdomCard(province,'Province',FirstPlayer)
                    PlayerTwoPoints += 6
                else :
                    Buy = 0
        elif money > 4 and dutchy not in EmptyPile and abs(PlayerOnePoints - PlayerTwoPoints) <= 3 :
            BuyKingdomCard(dutchy,'Dutchy',FirstPlayer)
            AddPlayerPoints(FirstPlayer,3)
        else :
            BuildingPhase(FirstPlayer, GameStrat(FirstPlayer))
    elif GameStrat(FirstPlayer) == 'BigMoneyStrat' :
        if money > 7 :
            if FirstPlayer :
                if ProvincePile == 1 and PlayerTwoPoints > (PlayerOnePoints + 6) and dutchy not in EmptyPile:
                    BuyKingdomCard(dutchy,'Dutchy',FirstPlayer)
                    PlayerOnePoints += 3
                elif ProvincePile == 1 and PlayerTwoPoints == (PlayerOnePoints + 6) and FirstPlayer  and dutchy not in EmptyPile:
                    BuyKingdomCard(dutchy,'Dutchy',FirstPlayer)
                    PlayerOnePoints += 3
                else :
                    BuyKingdomCard(province,'Province',FirstPlayer)
                    PlayerOnePoints += 6
            else :
                if ProvincePile == 1 and PlayerOnePoints > (PlayerTwoPoints + 6) and dutchy not in EmptyPile:
                    BuyKingdomCard(dutchy,'Dutchy',FirstPlayer)
                    PlayerTwoPoints += 3
                else :
                    BuyKingdomCard(province,'Province',FirstPlayer)
                    PlayerTwoPoints += 6
        elif money > 4 and dutchy not in EmptyPile and abs(PlayerOnePoints - PlayerTwoPoints) <= 3 :
            BuyKingdomCard(dutchy,'Dutchy',FirstPlayer)
            AddPlayerPoints(FirstPlayer,3)
        else :
            BuildingPhase(FirstPlayer, GameStrat(FirstPlayer))   
    elif GameStrat(FirstPlayer) == 'MegaTurnStrat' or GameStrat(FirstPlayer) ==  'MegaTurnStrat#2' :
        if (money + CostReduction) > 7 :
            if FirstPlayer :
                if ProvincePile == 1 and PlayerTwoPoints > (PlayerOnePoints + 6) and dutchy not in EmptyPile:
                    BuyKingdomCard(dutchy,'Dutchy',FirstPlayer)
                    PlayerOnePoints += 3
                elif ProvincePile == 1 and PlayerTwoPoints == (PlayerOnePoints + 6) and FirstPlayer  and dutchy not in EmptyPile:
                    BuyKingdomCard(dutchy,'Dutchy',FirstPlayer)
                    PlayerOnePoints += 3
                else :
                    BuyKingdomCard(province,'Province',FirstPlayer)
                    PlayerOnePoints += 6
            else :
                if ProvincePile == 1 and PlayerOnePoints > (PlayerTwoPoints + 6) and dutchy not in EmptyPile:
                    BuyKingdomCard(dutchy,'Dutchy',FirstPlayer)
                    PlayerTwoPoints += 3
                else :
                    BuyKingdomCard(province,'Province',FirstPlayer)
                    PlayerTwoPoints += 6
        elif (money + CostReduction) > 4 and dutchy not in EmptyPile and abs(PlayerOnePoints - PlayerTwoPoints) <= 3 :
            BuyKingdomCard(dutchy,'Dutchy',FirstPlayer)
            AddPlayerPoints(FirstPlayer,3)
        elif (money + CostReduction) > 4 and dutchy not in EmptyPile and len(EmptyPile) == 2 :
            BuyKingdomCard(dutchy,'Dutchy',FirstPlayer)
            AddPlayerPoints(FirstPlayer,3)
        elif not UnconMega and (money + CostReduction) > 4 and dutchy not in EmptyPile:
            BuyKingdomCard(dutchy,'Dutchy',FirstPlayer)
            AddPlayerPoints(FirstPlayer,3)
        else :
            BuildingPhase(FirstPlayer, GameStrat(FirstPlayer))
    elif GameStrat(FirstPlayer) == 'JoelStrat' :
        if (money + CostReduction) > 7 :
            if FirstPlayer :
                if ProvincePile == 1 and PlayerTwoPoints > (PlayerOnePoints + 6) and dutchy not in EmptyPile:
                    BuyKingdomCard(dutchy,'Dutchy',FirstPlayer)
                    PlayerOnePoints += 3
                elif ProvincePile == 1 and PlayerTwoPoints == (PlayerOnePoints + 6) and FirstPlayer  and dutchy not in EmptyPile:
                    BuyKingdomCard(dutchy,'Dutchy',FirstPlayer)
                    PlayerOnePoints += 3
                else :
                    BuyKingdomCard(province,'Province',FirstPlayer)
                    PlayerOnePoints += 6
            else :
                if ProvincePile == 1 and PlayerOnePoints > (PlayerTwoPoints + 6) and dutchy not in EmptyPile:
                    BuyKingdomCard(dutchy,'Dutchy',FirstPlayer)
                    PlayerTwoPoints += 3
                else :
                    BuyKingdomCard(province,'Province',FirstPlayer)
                    PlayerTwoPoints += 6
        elif dutchy not in EmptyPile and PlayerPoints(FirstPlayer) >= 30 :
            BuyKingdomCard(dutchy,'Dutchy',FirstPlayer)
            AddPlayerPoints(FirstPlayer,3)
        elif dutchy not in EmptyPile and CountCard(SecondPlayer(FirstPlayer), bridge) >= 7 :
            BuyKingdomCard(dutchy,'Dutchy',FirstPlayer)
            AddPlayerPoints(FirstPlayer,3)
        else :
            BuildingPhase(FirstPlayer, GameStrat(FirstPlayer))
            
def SecondPlayer(FirstPlayer) :
    if FirstPlayer :
        return False
    else :
        return True

def TakeOneRing(FirstPlayer) :
    global OneRingSecondPlayer, OneRingFirstPlayer
    if FirstPlayer :
        if OneRingFirstPlayer :
            return False
        elif OneRingSecondPlayer :
            OneRingSecondPlayer = False
            OneRingFirstPlayer = True
            print(P1Name,'took the One Ring')
            return True
        else :
            OneRingFirstPlayer = True
            print(P1Name,'took the One Ring')
            return True
    else :
        if OneRingSecondPlayer :
            return False
        elif OneRingFirstPlayer :
            OneRingFirstPlayer = False
            OneRingSecondPlayer = True
            print(P2Name,'took the One Ring')
            return True
        else :
            OneRingSecondPlayer = True
            print(P2Name,'took the One Ring')
            return True

def CheckGainBonus(FirstPlayer, Name) :
    global PlayerOnePoints, PlayerTwoPoints
    if Name == 'Tom Bombadil' :
        if FirstPlayer :
            PlayerOnePoints += InPlay.count(copper)
        else :
            PlayerTwoPoints += InPlay.count(copper)
    elif Name == 'Gollum' :
        TakeOneRing(FirstPlayer)

def BuyKingdomCard(Card,Name,FirstPlayer) :
    global money, Buy
    if RemoveCardFromSupply(Name) :
        CheckGainBonus(FirstPlayer, Name)
        CheckWhileInPlayAbilities(FirstPlayer, 'Gain')
        bought = True
        if FirstPlayer :
            print(P1Name,'bought a',Name + '.')
        else :
            print(P2Name,'bought a',Name + '.')
        money -= CostFormula(kingdom.index(Card))
        Buy -= 1
        PlayerDiscard(FirstPlayer).append(Card)
    else :
        EmptyPile.append(Card)
        print(Name,'pile is empty.')
        CheckWin(FirstPlayer)

def BuyLandscape(Card,Name,FirstPlayer) :
    global money, Buy
    if FirstPlayer :
        print(P1Name,'bought a',Name + '.')
    else :
        print(P2Name,'bought a',Name + '.')
    money -= int(Card[1])
    Buy -= 1
    if Card[2] == 'Spell' :
        PlayerSpellbook(FirstPlayer).append(Card)
    elif Card[2] == 'Event' :
        pass
    else :
        print('Other Landscape.')

def CostFormula(CardPos) :
    cost = int(kingdom[CardPos][1]) - CostReduction
    if int(cost) < 0 :
        return 0
    else :
        return int(cost)
    
def BuyCard(FirstPlayer, AI) :
    global Buy, money, PlayerOnePoints, PlayerTwoPoints, CostReduction
    if FirstPlayer and OneRingFirstPlayer:
        CostReduction -= 1
    elif not FirstPlayer and OneRingSecondPlayer :
        CostReduction -= 1
    if AI and not FirstPlayer :
        if ActionAI :
            BuyStrat(FirstPlayer, money, TurnCount)
        else :
            Buy = 0
            if ProvincePile == 2 and PlayerOnePoints == PlayerTwoPoints and int(money) >= 5 and DutchyPile > 0:
                print(P2Name,'bought a Dutchy.')
                money = 0
                PlayerDiscard(FirstPlayer).append(kingdom[14])
                RemoveCardFromSupply('Dutchy')
                PlayerTwoPoints += 3
            elif int(money) > 7 and ProvincePile > 0:
                print(P2Name,'bought a Province.')
                money = 0
                PlayerDiscard(FirstPlayer).append(kingdom[15])
                RemoveCardFromSupply('Province')
                PlayerTwoPoints += 6
            elif PlayerOnePoints >= 21 and PlayerTwoPoints < 21 and DutchyPile > 0:
                print(P2Name,'bought a Dutchy.')
                money = 0
                PlayerDiscard(FirstPlayer).append(kingdom[14])
                RemoveCardFromSupply('Dutchy')
                PlayerTwoPoints += 3
            elif int(money) > 5 and GoldPile > 0:
                print(P2Name,'bought a Gold.')
                money = 0
                PlayerDiscard(FirstPlayer).append(kingdom[12])
                RemoveCardFromSupply('Gold')
            elif int(money) == 5 and PlayerTwoPoints >= 27 and DutchyPile > 0:
                print(P2Name,'bought a Dutchy.')
                money = 0
                PlayerDiscard(FirstPlayer).append(kingdom[14])
                RemoveCardFromSupply('Dutchy')
                PlayerTwoPoints += 3
            elif int(money) > 2 and SilverPile > 0:
                print(P2Name,'bought a Silver.')
                money = 0
                PlayerDiscard(FirstPlayer).append(kingdom[11])
                RemoveCardFromSupply('Silver')
            else :
                pass
    if AI2 and FirstPlayer :
        BuyStrat(FirstPlayer, money, TurnCount)
    while Buy > 0 :
        print('Money:',money)
        if CostReduction != 0 :
            print('Cost Reduction:',CostReduction)
        print('Buy:',Buy)
        #if FirstPlayer and OneRingFirstPlayer:
            #print('One Ring: +1 Cost')
        #elif not FirstPlayer and OneRingSecondPlayer :
            #print('One Ring: +1 Cost')
        CardBought = DomCardPlays.translate(input('What do you want to buy? '))
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
        elif CardBought == 'coffers' or CardBought == 'coffer':
            PlayCoffers(FirstPlayer)
        elif CardBought == 'kingdom' or CardBought == 'cards' :
            for i in range(0,10) :
                print(kingdom[i][0],'(' + str(FindPile(i)) + ')')
        for i in range(0,len(landscape)) :
            if str(CardBought) == landscape[i][0] :
                #checks if the card you named is in the kingdom
                if int(landscape[i][1]) <= int(money):
                #and if you have enough money to buy it
                    if landscape[i][2] == 'Spell' :
                        PlayerSpellbook(FirstPlayer).append(landscape[i])
                        print('You bought',CardBought)
                        money -= int(landscape[i][1])
                        Buy -= 1
                else :
                    print('You do not have enough money')
        for i in range(0,len(kingdom)) :
            if str(CardBought) == kingdom[i][0] :
                #checks if the card you named is in the kingdom
                if int(kingdom[i][1]) <= int(money) + int(CostReduction) :
                #and if you have enough money to buy it
                    #print('CardBought:',str(CardBought),str(Pile1Name))
                    if RemoveCardFromSupply(CardBought) :
                        CheckWhileInPlayAbilities(FirstPlayer, 'Gain')
                        CheckGainBonus(FirstPlayer, CardBought)
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
                        EmptyPile.append(kingdom[i])
                        print(CardBought,'pile is empty.')
                        CheckWin(FirstPlayer)
                else :
                    print('You do not have enough money')
            else :
                #print('That card is not in the kingdom')
                pass
                
def PlayTreasures(FirstPlayer, AutoplayTreasures, AI) :
    NumTreasurePlayed = 0
    if AutoplayTreasures :
        for i in range(len(PlayerHand(FirstPlayer))) :
            if IsTreasure(FirstPlayer,i) :
                TreasureInHand.append(PlayerHand(FirstPlayer)[i])
                AddMoney(NumTreasurePlayed, True, FirstPlayer)
                NumTreasurePlayed += 1
            else :
                pass
    else :
        SpecialTreasure(FirstPlayer)
    while len(TreasureInHand) > 0 :
        PlayerHand(FirstPlayer).remove(TreasureInHand[0])
        TreasureInHand.pop(0)

def IsTreasure(FirstPlayer,CardSpot) :
    if 'Treasure' == PlayerHand(FirstPlayer)[CardSpot][2] :
        return True
    else : 
        return False
        
def AddMoney(CardSpot,AutoPlayTreasures, FirstPlayer) :
    global money
    #CardSpot is referring last treasure played
    money += int(TreasureInHand[CardSpot][3])
    InPlay.append(TreasureInHand[CardSpot])

def CleanUp(FirstPlayer) :
    DeleteCard = []
    for i in range(0,len(InPlay)) :
        if InPlay[i][3] == 'Duration' :
            DeleteCard.append(InPlay[i])
    for card in DeleteCard :
        InPlay.remove(card)
    PlayerDiscard(FirstPlayer).extend(PlayerHand(FirstPlayer))
    PlayerDiscard(FirstPlayer).extend(InPlay)
    PlayerDiscard(FirstPlayer).extend(UnplayedTreasures)
    PlayerHand(FirstPlayer).clear()
    InPlay.clear()
    UnplayedTreasures.clear()
    
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
    kingdom.append(scroll)
    for i in range(0,17) :
        print(kingdom[i][0])
    #check_kingdom() - works but unneeded


def ReturnPileName(Num) : #pointless >:(
    if Num == 1 :
        return Pile1Name
    elif Num == 2 :
        return Pile2Name
    elif Num == 3 :
        return Pile3Name
    elif Num == 4 :
        return Pile4Name
    elif Num == 5 :
        return Pile5Name
    elif Num == 6 :
        return Pile6Name
    elif Num == 7 :
        return Pile7Name
    elif Num == 8 :
        return Pile8Name
    elif Num == 9 :
        return Pile9Name
    elif Num == 10 :
        return Pile10Name
    
def CheckPileNum() :
    global Pile1,Pile2,Pile3,Pile4,Pile5,Pile6,Pile7,Pile8,Pile9,Pile10
    #for i in range(1,10) :
        #if ReturnPileName(i) == 'Rats' :
            #FindPile(i) = 20
        #elif ReturnPileName(i) == 'Tom Bombadil' :
            #FindPile(i) = 8
    if Pile1Name == 'Rats' :
        Pile1 = 20
    elif Pile1Name == 'Tom Bombadil' :
        Pile1 = 8
    else :
        Pile1 = 10
    if Pile2Name == 'Rats' :
        Pile2 = 20
    elif Pile2Name == 'Tom Bombadil' :
        Pile2 = 8
    else :
        Pile2 = 10
    if Pile3Name == 'Rats' :
        Pile3 = 20
    elif Pile3Name == 'Tom Bombadil' :
        Pile3 = 8
    else :
        Pile3 = 10
    if Pile4Name == 'Rats' :
        Pile4 = 20
    elif Pile4Name == 'Tom Bombadil' :
        Pile4 = 8
    else :
        Pile4 = 10
    if Pile5Name == 'Rats' :
        Pile5 = 20
    elif Pile5Name == 'Tom Bombadil' :
        Pile5 = 8
    else :
        Pile5 = 10
    if Pile6Name == 'Rats' :
        Pile6 = 20
    elif Pile6Name == 'Tom Bombadil' :
        Pile6 = 8
    else :
        Pile6 = 10
    if Pile7Name == 'Rats' :
        Pile7 = 20
    elif Pile7Name == 'Tom Bombadil' :
        Pile7 = 8
    else :
        Pile7 = 10
    if Pile8Name == 'Rats' :
        Pile8 = 20
    elif Pile8Name == 'Tom Bombadil' :
        Pile8 = 8
    else :
        Pile8 = 10
    if Pile9Name == 'Rats' :
        Pile9 = 20
    elif Pile9Name == 'Tom Bombadil' :
        Pile9 = 8
    else :
        Pile9 = 10
    if Pile10Name == 'Rats' :
        Pile10 = 20
    elif Pile10Name == 'Tom Bombadil' :
        Pile10 = 8
    else :
        Pile10 = 10

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
def split_ans(Infinite) :
    global actual
    while working == False :
        if not Infinite :
            want = DomCardPlays.translate(input())
        else :
            want = 'ai'
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
    if 'ai' in sent :
        kingdom.extend(AIkingdom)
        kingdom.sort(key=sortMethod)
    if 'test' in sent :
        kingdom.extend(test)
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
def customise_kingdom(Infinite) :
    if not Infinite :
        print('What do you want in your kingdom? ')
    split_ans(Infinite)



def SetupPlayers(Infinite) :
    global AI, P1Name, P2Name, ActionAI, AI2, RunSize
    if Infinite :
        ans = 'y'
    else :
        ans = input('Do you want a test game? ')
    try :
        ans = int(ans)
    except :
        pass
    if ans == 'y' or ans == 'yes' :
        AI = True
        ActionAI = True
        AI2 = True
        num = random.randint(1,5)
        num2 = random.randint(1,5)
        if num == num2 :
            num = 1
            num2 = 2
        if num == 1 :
            P1Name = 'King Bob'
        if num2 == 1 :
            P2Name = 'King Bob'
        if num == 2 :
            P1Name = 'Lord Cranberry'
        if num2 == 2 :
            P2Name = 'Lord Cranberry'
        if num == 3 :
            P1Name = 'Sir Greg'
        if num2 == 3 :
            P2Name = 'Sir Greg'
        if num == 4 :
            P1Name = 'Fat Frank'
        if num2 == 4 :
            P2Name = 'Fat Frank'
        if num == 5 :
            P1Name = 'Erasmus'
        if num2 == 5 :
            P2Name = 'Erasmus'
    elif type(ans) == int :
        RunSize = ans
        SetupPlayers(True)
    else :
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
            num = random.randint(1,5)
            if num == 1 :
                P2Name = 'King Bob'
            if num == 2 :
                P2Name = 'Lord Cranberry'
            if num == 3 :
                P2Name = 'Sir Greg'
            if num == 4 :
                P2Name = 'Fat Freddy'
            if num == 5 :
                P2Name = 'Erasmus'
    
def StartTurn(FirstPlayer) :
    global money, Buy, Action, CostReduction, scroll
    CostReduction = 0
    Buy = 1
    Action = 1
    money = 0
    change = list(scroll)
    change[1] = '5'
    scroll = tuple(change)
    PrintCards(FirstPlayer,'Hand',PlayerHand)

def CompileDeck(Deck) :
    used = []
    for card in Deck :
        if card not in used :
            print(card[0] + ':',Deck.count(card))
            used.append(card)
    
def GameEnd(FirstPlayer) :
    global RunTimes
    print('Game Over.')
    CountPoints(FirstPlayer)
    if FirstPlayer :
        deck1.extend(InPlay)
    else :
        deck2.extend(InPlay)
    EndTime = datetime.datetime.now()
    TotalTime = EndTime - StartTime
    print('Time:',TotalTime)
    print('Turn: ' + str(TurnCount))
    print(P1Name,'Deck')
    deck1.extend(discard1)
    deck1.extend(hand1)
    CompileDeck(deck1)
    print(P2Name,'Deck')
    deck2.extend(discard2)
    deck2.extend(hand2)
    CompileDeck(deck2)
    print('Trash')
    CompileDeck(trash)
    CreateCSV()
    CompareStats()
    RunTimes += 1
    if RunSize > RunTimes :
        StartGame(True)
    else :
        sys.exit('Thanks for playing!')

def CreateCSV() :

    with open('kingdominfo.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        #spamwriter.writerow(['Kingdom','P1Strat', 'P2Strat', 'P1Points', 'P2Points'])
        spamwriter.writerow([CondencedKingdom(),str(P1Strat), str(P2Strat), str(PlayerOnePoints), str(PlayerTwoPoints), str(TurnCount)])
    #df = pd.read_csv('data.csv')
    #print(df.to_string())

    with open('kingdominfo.csv', newline='') as csvfile: #Prints Stuff
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))
            #print(row)


def CondencedKingdom() :
    NewKingdom = []
    for i in range(0,10) :
        NewKingdom.append(kingdom[i][0])
    return NewKingdom

def AddWinGameStrat(Strat) :
    global CMega,CBig,CSpell,CJoel,CEngine,CDouble
    if Strat == 'MegaTurnStrat' :
        CMega += 1
    elif Strat == 'BigMoneyStrat' :
        CBig += 1
    elif Strat == 'JoelStrat' :
        CJoel += 1
    elif Strat == 'EngineStrat' :
        CEngine += 1
    elif Strat == 'DoubleStrat' :
        CDouble += 1
    elif Strat == 'SpellStrat' :
        CSpell += 1

def CheckStat(Stat, Type) :
    StatCount = 0
    with open('kingdominfo.csv', newline='') as csvfile: #Prints Stuff
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            if Type == 'Win' :
                if int(row[3]) > int(row[4]) and row[3] == Stat :
                    StatCount += 1
                elif int(row[4]) > int(row[3]) and row[4] == Stat :
                    StatCount += 1
            elif Type == 'Total' :
                if row[3] == Stat or row[4] == Stat :
                    StatCount += 1
    return StatCount

def CompareStats() :
    '''
    global CMega,CBig,CSpell,CJoel,CEngine,CDouble
    CMega = 0
    CBig = 0
    CSpell = 0
    CJoel = 0
    CEngine = 0
    CDouble = 0
    with open('kingdominfo.csv', newline='') as csvfile: #Prints Stuff
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            AddTotalGameStrat(row[2])
            if int(row[3]) > int(row[4]) :
                AddWinGameStrat(row[1])
                #print(row[1])
            elif int(row[4]) > int(row[3]) :
                #print(row[2])
                AddWinGameStrat(row[2])
            else :
                pass
                #print('Tie')
    '''
    print('MegaTurnStrat:',str(CheckStat('MegaTurnStrat', 'Win')))
    print('BigMoneyStrat:',str(CheckStat('BigMoneyStrat', 'Win')))
    print('SpellStrat:',str(CheckStat('SpellStrat', 'Win')))
    print('JoelStrat:',str(CheckStat('JoelStrat', 'Win')))
    print('EngineStrat:',str(CheckStat('EngineStrat', 'Win')))
    print('DoubleStrat:',str(CheckStat('DoubleStrat', 'Win')))
        
        

def CheckWin(FirstPlayer) :
    EmptyPile = []
    if ProvincePile <= 0 :
        GameEnd(FirstPlayer)
    if CopperPile == 0 and copper not in EmptyPile :
        EmptyPile.append(copper)
    if SilverPile == 0 and silver not in EmptyPile :
        EmptyPile.append(silver)
    if GoldPile == 0 and gold not in EmptyPile :
        EmptyPile.append(gold)
    if EstatePile == 0 and estate not in EmptyPile :
        EmptyPile.append(estate)
    if DutchyPile == 0 and dutchy not in EmptyPile :
        EmptyPile.append(dutchy)
    if CursePile == 0 and curse not in EmptyPile :
        EmptyPile.append(curse)
    if HorsePile == 0 and horse not in EmptyPile :
        EmptyPile.append(horse)
    if ScrollPile == 0 and scroll not in EmptyPile :
        EmptyPile.append(scroll)
    for i in range(0,10) :
        if FindPile(i) == 0 and kingdom[i] not in EmptyPile :
            EmptyPile.append(kingdom[i])
    if len(EmptyPile) >= 3 :
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

def ChooseHand(FirstPlayer) :
    PlayerDeck(FirstPlayer).clear()
    if FirstPlayer :
        ans = input(str(P1Name) + ', what opening do you want? ')
    else :
        if AI : #always chooses 4,3
            ans = 'n'
            PlayerDeck(FirstPlayer).append(estate)
            for i in range(7) :
                PlayerDeck(FirstPlayer).append(copper)
            for i in range(2) :
                PlayerDeck(FirstPlayer).append(estate)
        else :
            ans = input(str(P1Name) + ', what opening do you want? ')
            #ans = input(str(P2Name) + ' do you want quick choose? ')
    #if ans == 'y' or ans == 'yes' :
            #ans = input('What opening? ')
    if ans == '5 2' or ans == '5,2' or ans == '5, 2' or ans == '52' :
        for i in range(7) :
            PlayerDeck(FirstPlayer).append(copper)
        for i in range(3) :
            PlayerDeck(FirstPlayer).append(estate)
    elif ans == '2 5' or ans == '2,5' or ans == '2, 5' or ans == '25' :
        for i in range(3) :
            PlayerDeck(FirstPlayer).append(estate)
        for i in range(7) :
            PlayerDeck(FirstPlayer).append(copper)
    elif ans == '4 3' or ans == '4,3' or ans == '4, 3' or ans == '43' :
        PlayerDeck(FirstPlayer).append(estate)
        for i in range(7) :
            PlayerDeck(FirstPlayer).append(copper)
        for i in range(2) :
            PlayerDeck(FirstPlayer).append(estate)
    elif ans == '3 4' or ans == '3,4' or ans == '3, 4' or ans == '34' :
        for i in range(2) :
            PlayerDeck(FirstPlayer).append(estate)
        for i in range(7) :
            PlayerDeck(FirstPlayer).append(copper)
            PlayerDeck(FirstPlayer).append(estate)
    else : #3 4 opening
        for i in range(2) :
            PlayerDeck(FirstPlayer).append(estate)
        for i in range(7) :
            PlayerDeck(FirstPlayer).append(copper)
            PlayerDeck(FirstPlayer).append(estate)
'''
    elif not AI or FirstPlayer :
        for pos in range(1,10) :
            ans = input('What do you want in ' + str(pos) + ' position? ')
            if ans == 'copper' or ans == 'Copper' or ans == 'c' :
                PlayerDeck(FirstPlayer).append(copper)
            elif ans == 'estate' or ans == 'Estate' or ans == 'e' :
                PlayerDeck(FirstPlayer).append(copper)
'''                
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

def PlayerPoints(FirstPlayer) :
    if FirstPlayer :
        return PlayerOnePoints
    else :
        return PlayerTwoPoints

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

def FindPile(Num) :
    if Num == 0 :
        return Pile1
    elif Num == 1 :
        return Pile2
    elif Num == 2 :
        return Pile3
    elif Num == 3 :
        return Pile4
    elif Num == 4 :
        return Pile5
    elif Num == 5 :
        return Pile6
    elif Num == 6 :
        return Pile7
    elif Num == 7 :
        return Pile8
    elif Num == 8 :
        return Pile9
    elif Num == 9 :
        return Pile10
    elif Num == 10 :
        return CopperPile

def AddLandscapes() :
    #landscape.append('SchoolOfMagic')
    landscape.append(prestidigitation)
    landscape.append(arcane_bolt)
    landscape.append(haste)
    landscape.append(inspiration)
    landscape.append(gathering_storm)
    landscape.append(midas_touch)
    landscape.append(summon_familiar)

def CheckDuration(FirstPlayer) :
    DeleteCard = []
    if FirstPlayer :
        for i in range(0,len(DurationLand1)) :
            if DurationLand1[i][1] == False : #checks if card was not played this turn 
                DeleteCard.append(DurationLand1[i]) #adds old cards to remove list
            else :
                InPlay.append(DurationLand1[i][0]) #Re-adds duration card to InPlay
                DurationLand1[i][1] = False #Changes turn played to not this turn
        for i in range(0,len(DeleteCard)) :
            PlayerDiscard(FirstPlayer).append(DeleteCard[0][0]) #adds last turn duration to discard
            DurationLand1.remove(DeleteCard[0]) #Deletes last turn's durations 
            DeleteCard.pop(0)               #removes card from delete list
        for i in range(0,len(DurationLand2)) :
            InPlay.append(DurationLand2[i][0]) #Re-adds duration card to InPlay
    else :
        for i in range(0,len(DurationLand2)) :
            if DurationLand2[i][1] == False : #checks if card was not played this turn 
                DeleteCard.append(DurationLand2[i]) #adds old cards to remove list
            else :
                InPlay.append(DurationLand2[i][0]) #Re-adds duration card to InPlay
                DurationLand2[i][1] = False #Changes turn played to not this turn
        for i in range(0,len(DeleteCard)) :
            PlayerDiscard(FirstPlayer).append(DeleteCard[0][0]) #adds last turn duration to discard
            DurationLand2.remove(DeleteCard[0]) #Deletes last turn's durations 
            DeleteCard.pop(0)               #removes card from delete list
        for i in range(0,len(DurationLand1)) :
            InPlay.append(DurationLand1[i][0]) #Re-adds duration card to InPlay


def Turn(FirstPlayer) :
    global TurnCount
    StartTurn(FirstPlayer)
    CheckNextTurnAbilities(FirstPlayer)
    ActionPhase(FirstPlayer)
    BuyPhase(FirstPlayer)
    CleanUp(FirstPlayer)
    CheckDuration(FirstPlayer)
    CheckWin(FirstPlayer)    
    DrawCards(FirstPlayer, HandSize) #draw hand
    ShowPoints(FirstPlayer)
    
def CreateHand() :
    if AI2 :
        random.shuffle(PlayerDeck(True))
        random.shuffle(PlayerDeck(False))
        DrawCards(True, 5) #draw player 1's hand
        DrawCards(False, 5) #draw player 2's hand
    else :
        ans = input('Do you want to choose starting hands? ')
        if ans == 'y' or ans == 'yes' :
            ChooseHand(True)
            ChooseHand(False)
        else :
            random.shuffle(PlayerDeck(True))
            random.shuffle(PlayerDeck(False))
        DrawCards(True, 5) #draw player 1's hand
        DrawCards(False, 5) #draw player 2's hand
    
def StartGame(Infinite) :
    global StartTime
    ClearStats()
    StartTime = datetime.datetime.now()
    customise_kingdom(Infinite)
    AddLandscapes()
    PopPiles()
    CheckPileNum()
    ChooseStrat()
    CreateDeck()
    SetupPlayers(Infinite)
    CreateHand()
    print(str(P1Name) + "'s 1 turn.")
    Turn(True)
    
StartGame(False)
