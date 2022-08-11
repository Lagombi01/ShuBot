from cogs.Modules.play_audio import play_audio
import random
import discord
from mutagen.mp3 import MP3


async def gai_clip(ctx):
    time = MP3('Clips/Gai.mp3').info.length
    await play_audio(ctx, 'Clips/Gai.mp3', time + 0.25)


async def cri_clip(ctx):
    time = MP3('Clips/Cri.mp3').info.length
    await play_audio(ctx, 'Clips/Cri.mp3', time + 0.25)


async def ehh_clip(ctx):
    time = MP3('Clips/Ehh.mp3').info.length
    await play_audio(ctx, 'Clips/Ehh.mp3', time + 0.25)


async def luca_clip(ctx):
    time = MP3('Clips/Luca.mp3').info.length
    await play_audio(ctx, 'Clips/Luca.mp3', time + 0.25)


async def boy_clip(ctx):
    time = MP3('Clips/Boy.mp3').info.length
    await play_audio(ctx, 'Clips/Boy.mp3', time + 0.25)


async def owo_clip(ctx):
    chance = random.randint(1, 50)
    if chance == 50:
        filepath = 'Clips/Owo2.mp3'
    else:
        filepath = 'Clips/Owo.mp3'
    time = MP3(filepath).info.length
    await play_audio(ctx, filepath, time + 0.25)


async def wtf_clip(ctx):
    time = MP3('Clips/Wtf.mp3').info.length
    await play_audio(ctx, 'Clips/Wtf.mp3', time + 0.25)


async def amb_clip(ctx):
    time = MP3('Clips/Amb.mp3').info.length
    await play_audio(ctx, 'Clips/Amb.mp3', time + 0.25)


async def yawn_clip(ctx):
    filepath = "Clips/Yawns/" + str(random.randint(1, 6)) + ".mp3"
    time = MP3(filepath).info.length
    await play_audio(ctx, filepath, time + 0.25)
    if filepath == "Clips/Yawns/6.mp3":
        if isinstance(ctx, discord.Interaction):
            await ctx.channel.send("uwu I'm sorry table-chan <a:captainoof:1004070115567992842>")
        else:
            await ctx.send("uwu I'm sorry table-chan <a:captainoof:1004070115567992842>")
