import os

import discord

client = discord.Client()


@client.event
async def on_ready():
    pass


@client.event
async def on_message(message: discord.Message):
    if message.content == "안녕":
        await message.channel.send("So What?")


client.run(os.environ['BOT_TOKEN'])
