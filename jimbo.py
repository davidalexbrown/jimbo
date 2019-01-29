import discord
import random
import os
from discord.ext import commands
import auths
###
token = auths.token
prefix = "!"
bot = commands.Bot(command_prefix=prefix, case_insensitive = True)

##
### Extension List

extensions = ['fun', 'inmsg']

##
### Bot starts
@bot.event
async def on_ready():
    print("Jimbo Rules!")


# Load Extensions
@bot.command()
async def load(extension):
    try:
        bot.load_extension(extension)
        print('Loaded [{}]'.format(extension))
    except Exception as error:
        print ('{} is not loading. [{}]'.format(extension, error))

# Unload Extension
@bot.command()
async def unload(extension):
    try:
        bot.unload_extension(extension)
        print('Unloaded [{}]'.format(extension))
    except Exception as error:
        print ('{} did not unload. [{}]'.format(extension, error))

####
if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as error:
            print ('{} is not loading. [{}]'.format(extension, error))
    bot.run(token)
