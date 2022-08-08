import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio
import random
from mutagen.mp3 import MP3

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
guild_id = os.getenv('GUILD_ID')

bot = commands.Bot(command_prefix=',')


async def play_audio(ctx, clip, time):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel

    vc = await channel.connect()
    audio = discord.FFmpegPCMAudio(clip)
    player = vc.play(audio)
    await asyncio.sleep(time)
    await vc.disconnect()


@bot.event
async def on_ready():
    print(f"Shuuu?")


@bot.command(name="test")
async def test(ctx):
    print("hi")


@bot.command()
async def gai(ctx):
    time = MP3('Clips/Gai.mp3').info.length
    await play_audio(ctx, 'Clips/Gai.mp3', time + 0.25)


@bot.command()
async def cri(ctx):
    time = MP3('Clips/Cri.mp3').info.length
    await play_audio(ctx, 'Clips/Cri.mp3',  time + 0.25)


@bot.command()
async def ehh(ctx):
    time = MP3('Clips/Ehh.mp3').info.length
    await play_audio(ctx, 'Clips/Ehh.mp3', time + 0.25)


@bot.command()
async def luca(ctx):
    time = MP3('Clips/Luca.mp3').info.length
    await play_audio(ctx, 'Clips/Luca.mp3', time + 0.25)


@bot.command()
async def boy(ctx):
    time = MP3('Clips/Boy.mp3').info.length
    await play_audio(ctx, 'Clips/Boy.mp3', time + 0.25)


@bot.command()
async def owo(ctx):
    chance = random.randint(1, 50)
    if chance == 50:
        filepath = 'Clips/Owo2.mp3'
    else:
        filepath = 'Clips/Owo.mp3'
    time = MP3(filepath).info.length
    await play_audio(ctx, filepath, time + 0.25)


@bot.command()
async def wtf(ctx):
    time = MP3('Clips/Wtf.mp3').info.length
    await play_audio(ctx, 'Clips/Wtf.mp3', time + 0.25)


@bot.command()
async def yawn(ctx):
    filepath = "Clips/Yawns/" + str(random.randint(1, 6)) + ".mp3"
    time = MP3(filepath).info.length
    await play_audio(ctx, filepath, time + 0.25)


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if bot.user.id != message.author.id:
        if 'shu' in message.content.lower():
            await message.reply("ShuUUuUuuuuUUuUUuu?!!?!?!")
        elif 'gai' in message.content.lower():
            await message.reply("GaiiiiIIIIIiiiIIIIiiIIii!?!?!?!?!?!")
        elif 'inori' in message.content.lower():
            await message.reply("InoriIIIIiiiIIIiIiiIiiIiiiI!!!!!!!!!")
        elif 'captain' in message.content.lower() and "<" not in message.content and ">" not in message.content:
            await message.reply("arf arf")
        elif 'incest' in message.content.lower() or 'christmas' in message.content.lower():
            await message.reply("MANAAAAAAAAAAAAAAA!")
        elif 'woof' in message.content.lower():
            await message.reply("woof woof")
        elif 'sugar' in message.content.lower():
            await message.reply("Sugar???")


bot.run(token)
