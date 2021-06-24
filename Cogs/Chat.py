import datetime
import asyncio

from discord.ext import commands
from random import randint
from os import listdir
from app import log

class Chat(commands.Cog):

    def __init__(self, bot): # Cuz 1 init isnt enough
        self.bot = bot

    @commands.command()
    async def p(self, ctx): # Gotta stay under the radar with the command names
        await ctx.message.delete() # or just delete the message u monkey @veasman
        while True:
            # Randomize the message we will send
            toSend = '' # Initialize so we can append to it
            randSend = randint(0, 100)
            if randSend >= 75:
                files = sorted(listdir('sentence/'))
                for fileName in files:
                    file = open('sentence/' + fileName, 'r')
                    content = file.readlines()
                    randLine = randint(0, len(content) - 1)
                    toSend += content[randLine][:-1] + ' ' # [:-1] + ' ' Remove newline char, and add a space between the text
            else:
                fileToRead = 'Gifs.txt' if randSend <= 15 else 'XP.txt' # Send GIF (25%) or send "xp" (50%)
                file = open('other/' + fileToRead, 'r')
                content = file.readlines()
                randLine = randint(0, len(content) - 1)
                toSend = content[randLine][:-1] # [:-1] Remove newline char (fixes logs)

            log(f'Sending: {toSend} | Time {datetime.datetime.now()}', True)
            await ctx.send(toSend)

            # Randomize sleep times between messages
            randSleep = randint(0, 100)
            toSleep = 60 * (randint(15, 30) if randSleep >= 90 else randint(1, 5))

            log(f'Sending next message in {toSleep / 60} minutes...')
            await asyncio.sleep(toSleep) # AsyncIO works well with dpy imo

def setup(bot):
    bot.add_cog(Chat(bot))
