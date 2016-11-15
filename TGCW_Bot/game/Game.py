from Genevas import*
id1 = Genevas()
"""
from Andlat import*
id2 = Andlat()
from Christina import*
id3 = Christina()
from Tor import*
id4 = Tor()
from Ophelia import*
id5 = Ophelia()
from Silias import*
id6 = Silias()
from Merrie import*
id7 = Merrie()
from Vorpspiel import*
id8 = Vorspiel()
from Lace import*
id9 = Lace()
from Galath import*
id10 = Galath()
from Chips import*
id11 = Chips()
from Tana import*
id12 = Tana()
from Grace import*
id13 = Grace()
from Vant import*
id14 = Vant()
from Kyl import*
id15 = Kyl()
from Naru import*
id16 = Naru()
from Alex import*
id17 = Alex()
"""
	
#This checks the name of the ID the player selected, and returns it
def checkId(heroNames, id):
	playerSelects = heroNames[id]
	return playerSelects
	
def nameModify(n):
	print("\nCharacter Select")
	name = input(str(players[n]) + " please enter your name. ")
	players[n] = name
	return name
	
def selectionFormat(num, hero):
	return "(" + str(num + 1) + ") " + hero
	
def selectionRecall(n, pNum):
	if (n == 0):
		n -= 1
		print("\nSelection Panel")
		for n in range(len(heroesLeft)):
			if(heroesLeft[n] != "an unavailable hero. Try again"):
				print(selectionFormat(n, heroesLeft[n]))
	else:
		n-=1
		heroesLeft[n] = "an unavailable hero. Try again"
		selectionRecall(n, pNum)
#This later would be in a part of the code that refers to the individual player, checking which hero he/she selects
def playerCheck(n):
	selectionRecall(0, playersLeft)
	namePlyr = nameModify(n)
	id = int(input("Enter in your hero: "))-1
	playerHeroID.append(id)
	print(namePlyr + " has selected " + checkId(names, id))
	selectionRecall(id + 1, playersLeft)
	return checkId(names, id)
	
#Checks the stats and IDs for the player the user calls for
def statCheck():
	i = int(input("\nChoose the player you wish to check: "))-1
	print("\n" + players[i] + "'s hero is: " + playerHeroes[i])
	print("The ID of " + playerHeroes[i] + " is " + str(playerHeroID[i]))
	print("Health: " + str((callStats(playerHeroID[i])[0])))
	print("Stamina: " + str((callStats(playerHeroID[i])[1])))
	print("Mana: " + str((callStats(playerHeroID[i])[2])))
	print("Ammo: " + str((callStats(playerHeroID[i])[3])))
	print("Physical Attack: " + str((callStats(playerHeroID[i])[4])))
	print("Magical Attack: " + str((callStats(playerHeroID[i])[5])))
	print("Technological Attack: " + str((callStats(playerHeroID[i])[6])))
	print("Physical Defense: " + str((callStats(playerHeroID[i])[7])))
	print("Magical Defense: " + str((callStats(playerHeroID[i])[8])))
	print("Technological Defense: " + str((callStats(playerHeroID[i])[9])))

#This is where stats of the player can be called
def callStats(n):
	playerStats = []
	idcheck = eval("id" + str(n + 1))
	playerStats = idcheck.retrieveStats()
	return playerStats

	
#Here is where the Game Starts
print("Welcome to the Gythian Civil War Battle Simulator.")
print("Please input the number of players.")
playerNum = int(input())
playersLeft = playerNum

names = ["Genevas", "Andlat", "Christina", "Tor", "Ophelia", "Silias", "Merrie", "Vorspiel", "Lace", "Galath", "Chips", "Tana", "Grace", "Vant", "Kyl", "Naru", "Alex"]
heroesLeft = []

for i in range(0, len(names)):
	heroesLeft.append(names[i])

#The player ID, or each individual player
players = []
#The name of the hero each player selected
playerHeroes = []
#The ID of the hero each player selected
playerHeroID = []

#Creates playerIDs
for x in range(1, playerNum+1):
	a = "Player " + str(x)
	players.append(a)
	
for i in range(0, len(players)):
	playerHeroes.append(playerCheck(i))

statCheck()
