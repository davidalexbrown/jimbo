import discord
import random
import os

from discord.ext import commands
prefix = "!"
bot = commands.Bot(command_prefix=prefix)

class Fun:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pun(self, ctx):
        '''
        I wrote between heaven and mirth, so, it only makes sense.
        '''
        with open('assets/puns', 'r') as punlist:
            punlist = [line.rstrip('\n') for line in punlist]
            pun = random.choice(punlist)
        await ctx.send(pun)

    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx):
        '''
        Ever want your favorite Jesuit to determine your life choices?
        '''
        ball_list = ["It is certain", "It is decidedly so.", "Without a doubt.", " Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful.", "Homosexual relations are not sinful."]
        ball_answer = random.choice(ball_list)
        await ctx.send("🎱" + ball_answer + "🎱")

    @commands.command()
    async def meme(self, ctx):
        '''
        Delivers a random meme, right to your door
        '''
        memey = random.choice(os.listdir("assets/dankmeme/"))
        await ctx.send("Fresh baked memes, right to your door!", file=discord.File('assets/dankmeme/' + memey))

    @commands.command(aliases=['approval', 'fantasticmeme'])
    async def approve(self, ctx):
        '''
        I will approve whatever is trendy.
        '''
        await ctx.send(file=discord.File('assets/approval.png'))

    @commands.command(aliases=['coinflip', 'flip'])
    async def coin(self, ctx):
        '''
        I will flip a coin
        '''
        await ctx.send(random.choice(['Heads', 'Tails']))

    @commands.command()
    async def lmgtfy(self, ctx, query):
        '''
        Stupid questions get this. !lmgtfy {query}
        '''
        await ctx.send("http://www.lmgtfy.com/?q={}".format(query))

def setup(bot):
    bot.add_cog(Fun(bot))
