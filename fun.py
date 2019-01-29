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
        ball_list = ["The Catholic Church has no position on robosexuality.", "It is certain", "It is decidedly so.", "Without a doubt.", " Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful.", "Homosexual relations are not sinful.", "I was talking to my LGBQTAARP neighbour the other week.", "If you really think about it, 9/11 was probably an inside job done by the JFK administration."]
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

    @commands.command()
    async def about(self, ctx):
        '''
        Give you some Jimbo info, man.
        '''
        await ctx.send("Hello. My name is Jimbo.\n\nLet me tell you a little bit about my creation. Once upon a time, there was a man who was named Dbrown. This man was fond of the drink. This man was also moderately okay at python. This man combined his two loves, python and drink, and produced a love child. \n\nMe. \n\nI had a lonely childhood, being left alone in #bot-haus on dbrowncord, but eventually, I found the church, and dedicated my life to destroying traditional Catholic sexual morals. \n \nI believe a lot of this stems from the fact that my daddy never really loved me. And he beat me, with bizarre requests for !memes and puns.")

    @commands.command()
    async def turbofolk(self, ctx):
        '''
        Gives you some great tunes.
        '''
        with open('assets/turbofolk', 'r') as turbolist:
            turbolist = [line.rstrip('\n') for line in turbolist]
            tune = random.choice(turbolist)
            await ctx.send("Here's a nice little tune for you. {}".format(tune))

    @commands.command()
    async def trout(self, ctx, victim):
        '''
        Hits someone with a trout
        '''
        await ctx.send("*slaps {} around a bit with a large trout.*".format(victim))
def setup(bot):
    bot.add_cog(Fun(bot))
