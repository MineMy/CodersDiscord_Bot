import asyncio
import logging
import os
import sys

import discord
from discord.ext import commands
from discord.utils import get

lang_emojis: list = ['c_', 'cpp', 'python', 'php', 'ruby', 'java', 'javascript', 'typescript', 'nodejs', 'css']
test_msg_id = 655230612504051722
emojis: dict
logger = logging.getLogger("discord")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s] %(name)s: %(message)s'))
logger.addHandler(handler)
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('봇이 다음 옵션으로 실행되었습니다. : ')
    print(f'command_prefix : {bot.command_prefix}')
    global emojis
    emojis = {x.name: x for x in bot.emojis}
    print(f'emojis : {emojis}')


@bot.event
async def on_message(message):
    if message.content[0] is bot.command_prefix:
        print(f'{message.author} used {message.content}')


'''
@bot.event
async def on_reaction_add(reaction, user):
    if reaction.message.id is test_msg_id:
        if type(user) is discord.Member:
            for :
                await reaction.message.author.add_roles(get(reaction.message.author, role))
    else:
        await None
'''

@bot.command(name="안녕")
async def hello(ctx):
    for emoji in lang_emojis:
        await ctx.message.add_reaction(emojis[emoji])
    await ctx.send("흠")


@bot.command(name="역할신청")
async def set_role(ctx):
    msg = await ctx.send('필요한 역할을 선택해주세요.')
    for emoji in lang_emojis:
        await msg.add_reaction(emojis[emoji])

    def check(reaction, user):
        return user == ctx.author and reaction.emoji

    try:
        reactions, user = await discord.client.wait_for('reaction_add', timeout=20.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send('오랜 시간 응답이 없어 작업을 취소합니다.')
    else:
        await ctx.send(f'입력하신 역할들 : {reactions}')
        #await user.add_roles(get(ctx.author, role))
        await ctx.send('역할 부여가 완료되었습니다.')


bot.run(os.environ['BOT_TOKEN'])
