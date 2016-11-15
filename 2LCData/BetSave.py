import sqlite3
import time
import datetime
import random
import Database

connection = sqlite3.connect("2LC.db")
c = connection.cursor()

def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS betting(playerID TEXT, playerName TEXT, selectedChoice TEXT, betAmount INT)")

def data_entry():
	c.execute("INSERT INTO betting VALUES('id', 'name', 'A', 0)")
	connection.commit()	

def dynamic_data_entry(playerID, playerName, selectedChoice, betAmount):
	c.execute("INSERT INTO betting (playerID, playerName, selectedChoice, betAmount) VALUES(?, ?, ?, ?)", (playerID, playerName, selectedChoice, betAmount))
	connection.commit()
	
def read_from_db(command, id = 0, win = ""):
	c.execute("SELECT * FROM betting")
	if command == "scan":
		found = 0
		for row in c.fetchall(): 
			if row[0] == id:
				found += 1
		if found < 1:
			return True
		else:
			return False
	if command == "retrieve":
		for row in c.fetchall(): 
			if row[0] == id:
				return row[2]
	if command == "check":
		for row in c.fetchall(): 
			if row[0] == id:
				return "You have betted " + str(row[3]) + " Dice on \"" + row[2] + "\""
	if command == "wonbet":
		winners = ""
		for row in c.fetchall():
			if row[2] == win:
				Database.del_and_update("add", row[0], row[1]+"#", row[3]*2)
				winners += "\n" + row[1]
		return winners + "\n\n" + del_and_update("end")
		
	if command == "startCheck":
		count = c.fetchall()
		if len(count) > 0:
			return "\nBetting Available"
		else:
			return "\nCurrently, there is no betting session"""

def del_and_update(command):
	if command == "end":
		c.execute("DELETE FROM betting")
		connection.commit()
		return "Contest is over"
	
def convert(n):
	name = ""
	max = str(n).index("#")
	name = str(n)[: max]
	return name
#create_table()
#data_entry()