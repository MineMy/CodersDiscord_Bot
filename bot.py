import logging
import os
import sys

import discord
from discord.ext import commands
from discord.utils import get

lang_emojis: list = ['c_', 'cpp', 'python', 'php', 'ruby', 'java', 'javascript', 'typescript', 'nodejs', 'css']
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
    for emoji in lang_emojis:
        await message.add_reaction(emojis[emoji])
    await context.send("흠")


@bot.command(name="역할신청")
async def set_role(context):
    message: discord.Message = context.message
    for emoji in lang_emojis:
        await message.add_reaction(emojis[emoji])

    await context.author.add_roles(get(context.author, role))


bot.run(os.environ['BOT_TOKEN'])
