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
        channel = message.channel
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
        elif "hot dog" in message.content.lower():
            await message.add_reaction('🍔')
        elif "marimba" in message.content.lower():
            marimba_react = ['🇽','🇾','🇱','🇴','🇵','🇭','⭕','🇳','🇪']
            for r in marimba_react:
                await message.add_reaction(r)
        elif "baha" in message.content.lower():
            channel = message.channel
            await channel.send("https://www.youtube.com/watch?v=Qkuu0Lwb5EM")
        elif "dance" in message.content.lower():
            await channel.send("https://www.youtube.com/watch?v=AjPau5QYtYs")
        elif "proceeds from the father and the son" in message.content.lower():
            await channel.send("{}, REEEEEEEEEEEEEEEE".format(message.author.mention))
        elif "yikes" in message.content.lower():
            with open('assets/turbofolk', 'r') as turbolist:
                turbolist = [line.rstrip('\n') for line in turbolist]
                turbo = random.choice(turbolist)
                await channel.send("{}, Cyka blyat. {}".format(message.author.mention, turbo))
def setup(bot):
    bot.add_cog(inmsg(bot))
