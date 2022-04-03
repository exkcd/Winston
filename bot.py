import discord
from discord.ext import commands

import os
import logging
import sys
import traceback

from dotenv import load_dotenv

load_dotenv()

token = os.getenv('TOKEN')

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

description = '''A little bot.'''

intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(command_prefix=commands.when_mentioned_or('.'),
                   description=description, intents=intents)


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        try:
            bot.load_extension(f'cogs.{filename[:-3]}')
            print(f'Loaded cogs.{filename[:-3]}')
        except Exception as e:
            print(f'Failed to load cogs.{filename[:-3]}.', file=sys.stderr)
            traceback.print_exc()


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    print('-------')


bot.run(token)
