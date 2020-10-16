import discord
import random
import asyncio
from random_word import RandomWords
from botkeyBiden import *
from discord.ext import commands
r = RandomWords()

#client = discord.Client()
bot = commands.Bot(command_prefix='$')
#random time
#chance of if person puts message in chat, grabs random words from persons message and repeats them using add structure
#also he will randomy join a voice chat with people in it and play an audio clip of him saying something very biden
#command to force biden to talk

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Game(name='with kids'))

@bot.command()
async def speak(ctx):
    try:
        await ctx.send(getWord())
    except:
        await ctx.send("Nah I'm Good")

async def background_loop():
    await bot.wait_until_ready()
    while not bot.is_closed():
        if random.randint(1,101) <= 20:
            try:
                channel = bot.get_channel(testChannel)
                await channel.send(getWord())
            except:
                print("Error Generating words, oh well\n")
        else:
            print("Chance to generate words failed\n")
        time = random.randint(1800000,5400000)
        print("Waiting for "+(str)(time/3600000)+" hour(s)")
        await asyncio.sleep(time)

def getWord():
    input = ""
    print("Generating random words...\n")
    for x in range(4):
        input += r.get_random_word() + " "
    front = input[0:1]
    input = input[1:]
    simp = [".", "!", "?", ".com", ", you know?", ", uuuuuuuuuuuuuuuuuuuuh....", ", and then i ate some pealapound soup and shit my pants!"]
    random.shuffle(simp)
    return front.upper()+input.rstrip()+simp[0]


bot.loop.create_task(background_loop())
bot.run(token)
