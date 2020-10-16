import discord
import random
import asyncio
from random_word import RandomWords
from botkeyBiden import *
r = RandomWords()

client = discord.Client()
#random time
#chance of if person puts message in chat, grabs random words from persons message and repeats them using add structure

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name='with kids'))

async def background_loop():
    await client.wait_until_ready()
    while not client.is_closed():
        channel = client.get_channel(flubChannel)
        output = ""
        print("Generating random words...\n")
        for x in range(4):
            output += r.get_random_word() + " "
        await channel.send(addStructure(output))
        print("Waiting...\n")
        await asyncio.sleep(3600000)

def addStructure(input):
    front = input[0:1]
    input = input[1:]
    simp = [".", "!", "?", ".com", ", you know?", ", uuuuuuuuuuuuuuuuuuuuh....", ", and then i ate some pealapound soup and shit my pants!"]
    random.shuffle(simp)
    return front.upper()+input.rstrip()+simp[0]


client.loop.create_task(background_loop())
client.run(token)
