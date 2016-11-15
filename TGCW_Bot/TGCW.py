import discord
import random

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('>>game'):
        await client.send_message(message.channel, "Playing The Gythian Civil War is not yet available")
        await client.send_message(message.channel, "Try again next time")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('MjM4ODcxMDg3NTIwMjg0Njcy.CusoLw.7mjcVn88D8wUa3w8jo_31CEmYYE')
