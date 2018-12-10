import discord
import random
import os

from discord.ext import commands
prefix = "!"
bot = commands.Bot(command_prefix=prefix)

class Fun:
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Admin(bot))
