import discord
import random
import os

from discord.ext import commands
prefix = "!"
bot = commands.Bot(command_prefix=prefix)

class inmsg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        channel = message.channel
        message_normalized = str(message.content.lower())
        if "cross" in message_normalized and "pint" in message_normalized and "pipe" in message_normalized:
            await channel.send("G.K. probably never said that, you dolt.", file=discord.File('assets/grayons.jpg'))
        elif "sandwich" in message_normalized:
            await message.add_reaction('🌭')
        elif "hot dog" in message_normalized:
            await message.add_reaction('🍔')
        elif "marimba" in message_normalized:
            marimba_react = ['🇽','🇾','🇱','🇴','🇵','🇭','⭕','🇳','🇪']
            for r in marimba_react:
                await message.add_reaction(r)
        elif "proceeds from the father and the son" in message_normalized:
            await channel.send("{}, REEEEEEEEEEEEEEEE".format(message.author.mention))
def setup(bot):
    bot.add_cog(inmsg(bot))
