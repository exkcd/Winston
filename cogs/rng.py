import discord
from discord.ext import commands

import random


class RNG(commands.Cog):
    """Pseudo-RNG commands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx, dice: str):
        """Roll a dice in NdN format."""

        try:
            rolls, limit = map(int, dice.split('d'))

        except Exception:
            await ctx.send('Format has to be in NdN!')

        result = ', '.join(str(random.randint(1, limit))
                           for r in range(rolls))
        await ctx.send(result)

    @commands.command()
    async def choose(self, ctx, *choices: str):
        """Chooses between multiple choices"""

        await ctx.send(random.choice(choices))

    @commands.command()
    async def flip(self, ctx):
        """Flips a coin"""

        coin = ['**`HEADS`**', '**`TAILS`**']

        await ctx.send(random.choice(coin))

    @commands.command(name='8ball', aliases=['8'])
    async def _8ball(self, ctx, *, question: str):
        """Ask the 8 ball a question"""

        ball = ['As I see it, yes',
                'It is certain',
                'It is decidedly so',
                'Most likely',
                'Outlook good',
                'Signs point to yes',
                'Without a doubt',
                'Yes', 'Yes - definitely',
                'You may rely on it',
                'Reply hazy, try again',
                'Ask again later',
                'Better not tell you now',
                'Cannot predict now',
                'Concentrate and ask again',
                'Don\'t count on it',
                'My sources say no',
                'Outlook not so good',
                'Very doubtful']

        if question.endswith('?') and question != '?':
            await ctx.send(random.choice(ball))

        else:
            await ctx.send('That does not look like a question.')

    @commands.command()
    async def hug(self, ctx, user: discord.User):
        """Because everyone likes hugs!"""

        name = f'*{user.display_name}*'

        hug = ['(っ˘╰╯˘̩)っ', '(っ´▽｀)っ', '╰(*´︶`*)╯',
               '(つ≧▽≦)つ', '(づ￣ ³￣)づ', '(⊃ ´・ω・`)⊃']

        msg = (random.choice(hug))
        await ctx.send(msg + name)

    @commands.command()
    async def lenny(self, ctx):
        """Random lenny face"""
        lenny = [
            "( ͡° ͜ʖ ͡°)", "( ͠° ͟ʖ ͡°)", "ᕦ( ͡° ͜ʖ ͡°)ᕤ", "( ͡~ ͜ʖ ͡°)",
            "( ͡o ͜ʖ ͡o)", "͡(° ͜ʖ ͡ -)", "( ͡͡ ° ͜ ʖ ͡ °)", "(ง ͠° ͟ل͜ ͡°)ง",
            "ヽ༼ຈل͜ຈ༽ﾉ"
        ]

        await ctx.send(random.choice(lenny))

    @commands.command(hidden=True)
    async def love(self, ctx):
        """What is love?"""
        responses = ['https://www.youtube.com/watch?v=HEXWRTEbj1I',
                     'an intense feeling of deep affection', 'someting I cannot comprehend']

        response = random.choice(responses)
        await ctx.send(response)

    @commands.command(hidden=True)
    async def bored(self, ctx):
        """boredom looms"""

        await ctx.send('http://i.imgur.com/BuTKSzf.png')


def setup(bot):
    bot.add_cog(RNG(bot))
