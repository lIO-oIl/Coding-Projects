import sqlite3
import time
import datetime
import random

connection = sqlite3.connect("2LC.db")
c = connection.cursor()

def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS userCurrency(playerID TEXT, playerName TEXT, currency INT)")

def data_entry():
	c.execute("INSERT INTO userCurrency VALUES('id', 'name', 0)")
	connection.commit()	

def dynamic_data_entry(playerID, playerName, currency):
	keyword = ""
	value = 0
	c.execute("INSERT INTO userCurrency (playerID, playerName, currency) VALUES(?, ?, ?)", (playerID, playerName, currency))
	connection.commit()
	
def read_from_db(command, id, name, amount = 0):
	c.execute("SELECT * FROM userCurrency")
	if command == "check":
		found = 0
		for row in c.fetchall():
			#retrieve playerID
			if row[0] == id:
				return convert(name) + " has " + str(row[2]) + " Dice"
				found += 1
		if found < 1:
			dynamic_data_entry(id, name, 0)
			return "New ID " + convert(name) + " created"
	if command == "enough":
		for row in c.fetchall():
			#retrieve playerID
			if row[0] == id:
				if row[2] >= int(amount):
					return True
	else:
		return "Null"

def del_and_update(command, id, name, value):
	if command == "delete":
		c.execute("DELETE FROM userCurrency WHERE playerID ={}".format(id))
		connection.commit()
		return convert(name) + " has been deleted"
	if command == "add":
		c.execute("UPDATE userCurrency SET currency = currency + {} WHERE playerID = {}".format(value ,id))
		connection.commit()
		return convert(name) + " has been given " + str(value) + " Dice"
		
	if command == "del":
		c.execute("UPDATE userCurrency SET currency = currency + {} WHERE playerID = {}".format(value ,id))
		connection.commit()
		return convert(name) + " has lost " + str(-value) + " Dice"
	if command == "bet":
		c.execute("UPDATE userCurrency SET currency = currency + {} WHERE playerID = {}".format(value ,id))
		connection.commit()
		return convert(name) + " has invested " + str(-value) + " Dice"
	
def convert(n):
	name = ""
	max = str(n).index("#")
	name = str(n)[: max]
	return name
#create_table()
#data_entry()