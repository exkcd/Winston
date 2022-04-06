import discord
from discord.ext import commands

import aiohttp


class Fun(commands.Cog):
    """Fun commands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    async def cat(self, ctx):
        """Gives a random cat."""
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.thecatapi.com/v1/images/search')
            catjs = await request.json()

        data = discord.Embed()
        data.set_image(url=catjs[0]['url'])

        await ctx.send(embed=data)

    @commands.command(hidden=True)
    async def dog(self, ctx):
        """Gives a random dog."""
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/dog')
            dogjs = await request.json()

            data = discord.Embed()
            data.set_image(url=dogjs['link'])

            await ctx.send(embed=data)

    @commands.group()
    async def cool(self, ctx):
        """Says if a user is cool. (checks if subcommand is being invoked)"""

        if ctx.invoked_subcommand is None:
            await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

    @cool.command(name='bot')
    async def _bot(self, ctx):
        """Is the bot cool?"""

        await ctx.send('Yes, the bot is cool.')


def setup(bot):
    bot.add_cog(Fun(bot))
