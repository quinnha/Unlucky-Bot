import discord
import os
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    data = ['unlucky', 'unluck']
    if message.author == client.user:
        return

    for word in data:
        if word in message.content:
            await message.channel.send(file=discord.File('unlucky_steel.jpg'))
            return

    if message.content.startswith('!unlucky'):
        await message.channel.send(file=discord.File('unlucky_steel.jpg'))
        return

keep_alive()
client.run(os.getenv('TOKEN'))