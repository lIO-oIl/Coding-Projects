import discord
import random
client = discord.Client()
	
class TGCW_BOT:
	playerNum = 0
	def playerCount():
		playerNum += 1
		return playerNum

	@client.event
	async def on_message(message):
		print(message.content)
		# we do not want the bot to reply to itself
		if message.author == client.user:
			return

		if message.content.startswith('>>game'):
			await client.send_message(message.channel, "Playing The Gythian Civil War is not yet available")
			await client.send_message(message.channel, "Welcome to the Gythian Civil War Battle Simulator.")
			await client.send_message(message.channel, "All participants type >>add to join")
		
		if message.content.startswith('>>add'):
			await client.send_message(message.channel, "Player added")
			await client.send_message(message.channel, str(playerCount()))
			playerCount()
			
		if message.content.startswith('>>start'):
			if (playerCount() == 0):
				await client.send_message(message.channel, "No users joined")
			else:
				await client.send_message(message.channel, "Game starting with " + playerNum + " players")
		if message.content.startswith('>>clearlog'):
			print("\n\n\n\n\n\n\n\n\n\nLog Start\n---------------")
			
	@client.event
	async def on_ready():
		print('Logged in as')
		print(client.user.name)
		print(client.user.id)
		print('------')
		
	client.run('MjM4ODcxMDg3NTIwMjg0Njcy.CusoLw.7mjcVn88D8wUa3w8jo_31CEmYYE')
