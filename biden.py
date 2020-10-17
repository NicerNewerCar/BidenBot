import discord
import random
import asyncio
from random_word import RandomWords
from botkeyBiden import *
from discord.ext import commands
r = RandomWords()

bot = commands.Bot(command_prefix='!')
#also he will randomy join a voice chat with people in it and play an audio clip of him saying something very biden

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
        if random.randint(1,101) <= 43:
            try:
                channel = bot.get_channel(flubChannel)
                await channel.send(getWord())
            except:
                print("Error Generating words, oh well\n")
        else:
            print("Chance to generate words failed\n")
        time = random.randint(1800000,5400000)
        print("Waiting for "+(str)(time/3600000)+" hour(s)")
        await asyncio.sleep(time)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)
    if random.randint(1,101) <= 6:
        await message.channel.send(repeat(message.content))

def getWord():
    input = ""
    print("Generating random words...\n")
    for x in range(4):
        input += r.get_random_word() + " "
    front = input[0:1]
    input = input[1:]
    endings = [".", "!", "?", ".com", ", you know?", ", uuuuuuuuuuuuuuuuuuuuh....", ", and then i ate some pealapound soup and shit my pants!"]
    random.shuffle(endings)
    return front.upper()+input.rstrip()+endings[0]

def repeat(str):
    messageList = str.split(' ')
    random.shuffle(messageList)
    interjections = ['something something', 'something', 'something about', '...uuuuhhhh...', '*sniffs*']
    enders = [', what?','. No, no, I am awake!',', you know?', ', and I agree completey.', '. Uhhhhhhhhhhh...', ', will you just shut up man?']
    output = ''
    for x in range(random.randint(0,len(messageList)-2)):
        random.shuffle(interjections)
        output += messageList[x] +' '+ interjections[0] + ' '
    random.shuffle(enders)
    return output.rstrip()+enders[0]

bot.loop.create_task(background_loop())
bot.run(token)
