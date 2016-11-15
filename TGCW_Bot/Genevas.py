from attackFunctionality import*
attack = attackFunctionality()

class Genevas:
	
	def __init__(self):
		self.stats = [350, 200, 0, 5, 25, 0, 25, 20, 15, 10]

	def retrieveStats(self):
		return self.stats
	
	def attack1(self):
		damage = 20
		target = attack.chooseTarget()
		turns = 3
		DoT = attack.damageOverTime(damage, target, turns)
		print(DoT)
	
	def attack2(self):
		return #nothing
		
	def attack3(self):
		return #nothing
	
	def attack4(self):
		return #nothing