import discord
import random
import os

from discord.ext import commands
prefix = "!"
bot = commands.Bot(command_prefix=prefix)

class Admin:
    '''
    Admin only module.
    '''
    def __init__(self, bot):
        self.bot = bot

    @bot.event
    async def on_member_join(member):
        member = member.guild
        newbie = '{0.mention} is building a bridge.'
        await ctx.send(newbie.format(member))



def setup(bot):
    bot.add_cog(Admin(bot))
