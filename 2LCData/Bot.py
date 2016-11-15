import discord
import random
import Database
import BetSave

client = discord.Client()

@client.event
async def on_message(message):
	print(message.content)
	# we do not want the bot to reply to itself
	if message.author == client.user:
		return
	
	#User Commands
	if "215667284008501248" in [r.id for r in message.author.roles]:
		#User Checking/Creating
		if message.content.startswith(".check") and len(message.mentions) > 0:
			for m in message.mentions:
				await client.send_message(message.channel, Database.read_from_db("check", m.id, str(m)))
		elif message.content.startswith(".check"):
			await client.send_message(message.channel, Database.read_from_db("check", message.author.id, str(message.author)))
		if BetSave.read_from_db("startCheck") == "\nBetting Available":
			#User Betting
			if message.content.startswith(".bet"):
				if len(message.content) == 4:
					await client.send_message(message.channel, "{}".format(BetSave.read_from_db("check", message.author.id)))
				else:
					command = message.content.split(" ")
					if Database.read_from_db("enough", message.author.id, message.author, command[2]):
						if command[1].isalpha() & command[2].isdigit():
							if BetSave.read_from_db("scan", message.author.id):
								BetSave.dynamic_data_entry(message.author.id, message.author.name, command[1], command[2])
								await client.send_message(message.channel, Database.del_and_update("bet", message.author.id, message.author, -int(command[2])))
							else:
								await client.send_message(message.channel, "You have already betted \"{}\"".format(BetSave.read_from_db("retrieve", message.author.id)))
						else:
							await client.send_message(message.channel, "Your value {} or {} is invalid. Type in .bet [choice] [amount]".format(command[1], str(command[2])))
					else:
						await client.send_message(message.channel, "Your value {} is too large. {}".format(command[2], Database.read_from_db("check", message.author.id, message.author)))
		else:
			if message.content.startswith(".bet"):
				await client.send_message(message.channel, "You cannot bet until the session has begun")
	
		if message.content.startswith(".help"):
			await client.send_message(message.channel, " Commands\
			\n.check - Creates and displays Dice amount; .check [@user] Use .check to check self\
			\n.bet - Sets and checks bet for the player; .bet [choice][amount] Use .bet to check bet. Bets cannot be changed\n\nAdmin Commands\
			\n.begin - Starts a new betting session. Use .winner to terminate\
			\n.add - Adds given amount to player; .add [@user][amount]\
			\n.del - Removes given amount from player; .del [@user][amount]\
			\n.winner - Ends betting session, money would be distributed; .winner [choice]{}".format(BetSave.read_from_db("startCheck")))
			
	#Admin Modification
	if "208914572143362059" in [r.id for r in message.author.roles]:
		if message.content.startswith(".add"):
			command = message.content.split(" ")
			if command[2].isdigit():
				for m in message.mentions:
						await client.send_message(message.channel, Database.del_and_update("add", m.id, str(m), command[2]))
			else:
				await client.send_message(message.channel, "Your value {} is invalid. Type in .add [user] [amount]".format(command[2]))
			
		if message.content.startswith(".del"):
			command = message.content.split(" ")
			if command[2].isdigit():
				for m in message.mentions:
						await client.send_message(message.channel, Database.del_and_update("del", m.id, str(m), -int(command[2])))
			else:
				await client.send_message(message.channel, "Your value {} is invalid. Type in .del [user] [amount]".format(command[2]))
	
		#Admin Tournament Start
		if message.content.startswith(".begin"):
			if BetSave.read_from_db("startCheck") != "\nBetting Available":
				BetSave.data_entry()
				await client.send_message(message.channel, "Betting session has begun")
			else:
				await client.send_message(message.channel, "A session is already in place")
		#Admin Tournament Completion
		if message.content.startswith(".winner"):
			if BetSave.read_from_db("startCheck") == "\nBetting Available":
				command = message.content.split(" ")
				await client.send_message(message.channel, "Tournament winner:\n{}\n\nBetted: {}".format(command[1], BetSave.read_from_db("wonbet", message.author.id, command[1])))
			else:
				await client.send_message(message.channel, "Betting session has not begun")
@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	
client.run('MjQyNDIyNzYzODIwNjc5MTcw.CvgNUQ.HgRYs0fskAUOkGsv8FM5XULNNxc')
