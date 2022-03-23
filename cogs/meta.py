import discord
from discord.ext import commands

import datetime
from typing import Union


class Meta(commands.Cog):
    """General utility based commands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        """Displays my welcome message."""
        await ctx.send('Hello! I am a robot.')

    @commands.command()
    async def ping(self, ctx):
        """Checks bot latency."""
        await ctx.send(f'Pong: `{round(self.bot.latency * 1000)} ms`')

    @commands.command(aliases=['userinfo'])
    async def info(self, ctx, user: Union[discord.Member, discord.User] = None):
        """Shows info about a user."""

        user = user or ctx.author

        data = discord.Embed(colour=user.colour)

        roles = [role.name.replace('@', '@\u200b')
                 for role in getattr(user, 'roles', [])]

        joined_at = user.joined_at.replace(tzinfo=datetime.timezone.utc)
        user_created = user.created_at.replace(tzinfo=datetime.timezone.utc)

        joined_timestamp = joined_at.timestamp()
        created_timestamp = user_created.timestamp()

        joined_on = '<t:{0}>\n(<t:{0}:R>)'.format(int(joined_timestamp))
        created_on = '<t:{0}>\n(<t:{0}:R>)'.format(int(created_timestamp))

        data.add_field(name='Created on', value=created_on, inline=False)
        data.add_field(name='Joined on', value=joined_on, inline=False)

        if roles:
            data.add_field(name='Roles', value=', '.join(roles) if len(
                roles) < 10 else f'{len(roles)} roles', inline=False)
        else:
            roles = None

        data.set_author(name=str(user))
        data.set_thumbnail(url=user.avatar_url)
        data.set_footer(text='ID: {}'.format(user.id))

        await ctx.send(embed=data)

    @commands.command(aliases=['serverinfo'])
    async def server(self, ctx):
        """Shows server information."""

        guild = ctx.guild

        roles = [role.name.replace('@', '@\u200b') for role in guild.roles]

        data = discord.Embed()

        data.description = f'**ID:** {guild.id}\n**Owner:** {guild.owner}'
        data.set_author(name=f'{guild.name}')
        data.set_thumbnail(url=guild.icon_url)
        data.set_footer(text='Created').timestamp = guild.created_at

        data.add_field(
            name='Channels', value=f'Text: {len(guild.text_channels)}\nVoice: {len(guild.voice_channels)}', inline=False)
        data.add_field(name='Members', value=guild.member_count, inline=False)
        data.add_field(name='Roles', value=', '.join(roles) if len(
            roles) < 10 else f'{len(roles)} roles', inline=False)

        await ctx.send(embed=data)

    @commands.command()
    async def avatar(self, ctx, *, user: Union[discord.Member, discord.User] = None):
        """Shows a user's avatar but bigger."""

        user = user or ctx.author
        data = discord.Embed(colour=user.colour)

        avatar = user.avatar_url
        data.set_author(name=str(user), url=avatar)
        data.set_image(url=avatar)

        await ctx.send(embed=data)


def setup(bot):
    bot.add_cog(Meta(bot))
