import discord
import random
import os

from discord.ext import commands
prefix = "!"
bot = commands.Bot(command_prefix=prefix)

class inmsg:
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        if "cross" in message.content.lower():
            chesty = str(message.content)
            chesty = chesty.lower()
            ree = ""
            if "pint" in chesty:
                if "pipe" in chesty:
                    ree = True
                else:
                    ree = False
            else:
                ree = False
            if ree == True:
                channel = message.channel
                await channel.send("G.K. probably never said that, you dolt.", file=discord.File('assets/grayons.jpg'))
        elif "sandwich" in message.content.lower():
            await message.add_reaction('🌭')
        elif "oof" in message.content.lower():
            await message.add_reaction('🤕')
        elif "hot dog" in message.content.lower():
            await message.add_reaction('🍔')
        elif "marimba" in message.content.lower():
            await message.add_reaction('🇽')
            await message.add_reaction('🇾')
            await message.add_reaction('🇱')
            await message.add_reaction('🇴')
            await message.add_reaction('🇵')
            await message.add_reaction('🇭')
            await message.add_reaction('⭕')
            await message.add_reaction('🇳')
            await message.add_reaction('🇪')
        elif "baha" in message.content.lower():
            channel = message.channel
            await channel.send("https://www.youtube.com/watch?v=Qkuu0Lwb5EM")
def setup(bot):
    bot.add_cog(inmsg(bot))
