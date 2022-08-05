import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix=',')


@bot.event
async def on_ready():
    print("Shuuu?")


@bot.command(name="test")
async def test(ctx):
    print("hi")


@bot.command()
async def gai(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel

    vc = await channel.connect()
    audio = discord.FFmpegPCMAudio('Gai.mp3')
    player = vc.play(audio)
    await asyncio.sleep(3)
    await vc.disconnect()


@bot.command()
async def cri(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel

    vc = await channel.connect()
    audio = discord.FFmpegPCMAudio('Cri.mp3')
    player = vc.play(audio)
    await asyncio.sleep(9)
    await vc.disconnect()

bot.run(TOKEN)
