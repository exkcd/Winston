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


def setup(bot):
    bot.add_cog(Fun(bot))
