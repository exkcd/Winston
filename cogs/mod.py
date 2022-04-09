import discord
from discord.ext import commands

from typing import Union


class Mod(commands.Cog):
    """Moderation related commands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='cleanup', aliases=['purge', 'clear'])
    @commands.guild_only()
    @commands.has_guild_permissions(manage_messages=True)
    async def cleanup(self, ctx, amount=10):
        """Clears recent messages."""
        await ctx.channel.purge(limit=amount + 1)

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self, ctx, member: Union[discord.User, discord.Member] = None, *, reason=None):
        """Kicks a user from the guild."""
        if reason is None:
            reason = f'Action done by {ctx.author} (ID: {ctx.author.id}'

        await ctx.guild.kick(member, reason=reason)
        await ctx.send('\N{OK HAND SIGN}')

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member: Union[discord.User, discord.Member] = None, *, reason=None):
        """Bans a user from the guild."""
        if reason is None:
            reason = f'Action done by {ctx.author} (ID: {ctx.author.id}'

        await ctx.guild.ban(member, reason=reason)
        await ctx.send('\N{OK HAND SIGN}')

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(ban_members=True)
    async def softban(self, ctx, member: Union[discord.User, discord.Member] = None, *, reason=None):
        """Softbans a user from the guild. Essentially bans and then unbans a user. Like kick, but removes their messages as well."""
        if reason is None:
            reason = f'Action done by {ctx.author} (ID: {ctx.author.id}'

        await ctx.guild.ban(member, reason=reason)
        await ctx.guild.unban(member, reason=reason)
        await ctx.send('\N{OK HAND SIGN}')


def setup(bot):
    bot.add_cog(Mod(bot))
