import discord
from discord.ext import commands
import os
import traceback
from os.path import isfile, join

bot = commands.Bot(command_prefix='x...', self_bot=True)

def log(msg, separator = False, warning = False):
    if separator:
        print('__________________________________________________\n')
    if warning:
        return print(f'[WARNING] {msg}')
    print(f'[BOT] {msg}'); # <----------- WHAT THE FUCK IS THIS

@bot.event
async def on_ready():
    log("Ready.")
    await LoadCogs()

async def LoadCogs():
    for cog in [f.replace('.py', "") for f in os.listdir("Cogs") if isfile(join("Cogs", f))]: # Dont question it.
        try:
            if not "__init__" in cog:
                bot.load_extension("Cogs." + cog)
                log("Loaded {}".format(cog))
        except Exception as e:
            log("Couldn't load {} dipshit.".format(cog), warning=True)
            traceback.print_exc()

token = open('token.txt').readline().strip('\n') # Smells like bloat cuz it is, I recommend using .env
if __name__ == '__main__':
    bot.run(token, reconnect=True, bot=False)
else:
    del bot
