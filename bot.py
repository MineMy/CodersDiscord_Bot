import logging
import os
import sys

import discord
from discord.ext import commands

emojis: dict
logger = logging.getLogger("discord")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s] %(name)s: %(message)s'))
logger.addHandler(handler)
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    global emojis
    emojis = {x.name: x for x in bot.emojis}


@bot.command(name="안녕")
async def hello(context):
    message: discord.Message = context.message
    for emoji in ['c_', 'cpp', 'python', 'php', 'ruby', 'java', 'javascript', 'typescript', 'nodejs', 'html', 'css']:
        await message.add_reaction(emojis[emoji])
    await context.send("흠")


bot.run(os.environ['BOT_TOKEN'])
