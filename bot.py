import asyncio
import logging
import os
import sys

import discord
from discord.ext import commands
from discord.utils import get, find

from config import CoderBot as Config

lang_emojis: list = ['c_', 'cpp', 'python', 'php', 'ruby', 'java', 'javascript', 'typescript', 'nodejs', 'css']
role_setting: dict = {'c_' : 'C', 'cpp': 'C++', 'csharp' : 'C#'}
role_setting_id = 655322859823955969
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
async def on_raw_reaction_add(payload):
    msg_id = payload.message.id
    if msg_id is role_setting_id:
        guild_id = payload.guild.id
        guild = find(lambda g : g.id == guild_id, bot.guilds)
        role = get(guild.roles, name = role_setting[payload.emoji.name])
        if role is not None:
            member = find(lambda m : m.id == payload.user.id, guild.members)
            if member is not None:
                await member.add_roles(role)
            else:
                await None




@bot.command(name="안녕")
async def hello(ctx):
    for emoji in lang_emojis:
        await ctx.message.add_reaction(emojis[emoji])
    await ctx.send("흠")


@bot.command(name="설정")
async def setting(ctx):
    pass

@bot.command(name="역할지급")
async def set_role(ctx):
    logger.debug('ser_role 진입')
    await ctx.send('역할 지급 채널로 설정했습니다!')
    # msg = await ctx.send('필요한 역할을 선택해주세요.')
    for emoji in lang_emojis:
        await msg.add_reaction(emojis[emoji])
    # await asyncio.sleep(20)
    # for reaction in msg.reactions:
    '''
    def check(reaction, user):
        return user == ctx.author and reaction.emoji
    
    try:
        reactions, user = await bot.wait_for(event='reaction_add', timeout=20.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send('오랜 시간 응답이 없어 작업을 취소합니다.')
    else:
        await ctx.send(f'입력하신 역할들 : {reactions}')
        # await user.add_roles(get(ctx.author, role))
        await ctx.send('역할 부여가 완료되었습니다.')
    '''

for init_cog in Config.init_cogs:
    try:
        bot.load_extension("cogs.{}".format(init_cog))
    except commands.errors.ExtensionNotFound:
        logger.error("Cog not found: {}".format(init_cog))
    except Exception as e:
        logger.exception("Error while load cog {}".format(init_cog))
    else:
        logger.debug("Load: {}".format(init_cog))

bot.run(Config.token)

