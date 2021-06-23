import discord
from discord.ext import commands
import time
import random
import datetime;
import os

bot = commands.Bot(command_prefix='x...', self_bot=True)

def rand(min, max):
    return random.randint(min, max)

def log(msg, separator = False):
    if separator:
        print('__________________________________________________\n')
    print(f'[BOT] {msg}');

@bot.event
async def on_ready():
    print('Ready')

@bot.command()
async def p(ctx): # Gotta stay under the radar with the command names
    while True:
        # Randomize the message we will send
        toSend = '' # Initialize so we can append to it
        randSend = rand(0, 100)
        if randSend >= 75:
            files = sorted(os.listdir('sentence/'))
            for fileName in files:
                file = open('sentence/' + fileName, 'r')
                content = file.readlines()
                randLine = rand(0, len(content) - 1)
                toSend += content[randLine][:-1] + ' ' # [:-1] + ' ' Remove newline char, and add a space between the text
        else:
            fileToRead = 'Gifs.txt' if randSend <= 15 else 'XP.txt' # Send GIF (25%) or send "xp" (50%)
            file = open('other/' + fileToRead, 'r')
            content = file.readlines()
            randLine = rand(0, len(content) - 1)
            toSend = content[randLine][:-1] # [:-1] Remove newline char (fixes logs)

        log(f'Sending: {toSend} | Time {datetime.datetime.now()}', True)
        await ctx.send(toSend)

        # Randomize sleep times between messages
        randSleep = rand(0, 100)
        toSleep = 60 * (rand(15, 30) if randSleep >= 90 else rand(1, 5))

        log(f'Sending next message in {toSleep / 60} minutes...')
        time.sleep(toSleep)

tokenFile = open('token.txt', 'r')
bot.run(tokenFile.readlines()[0], reconnect=True, bot=False)
