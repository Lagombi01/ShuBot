import discord
from discord.ext import commands
import asyncio
import random
from mutagen.mp3 import MP3


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


class Audio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gai(self, ctx):
        time = MP3('Clips/Gai.mp3').info.length
        await play_audio(ctx, 'Clips/Gai.mp3', time + 0.25)

    @commands.command()
    async def cri(self, ctx):
        time = MP3('Clips/Cri.mp3').info.length
        await play_audio(ctx, 'Clips/Cri.mp3', time + 0.25)

    @commands.command()
    async def ehh(self, ctx):
        time = MP3('Clips/Ehh.mp3').info.length
        await play_audio(ctx, 'Clips/Ehh.mp3', time + 0.25)

    @commands.command()
    async def luca(self, ctx):
        time = MP3('Clips/Luca.mp3').info.length
        await play_audio(ctx, 'Clips/Luca.mp3', time + 0.25)

    @commands.command()
    async def boy(self, ctx):
        time = MP3('Clips/Boy.mp3').info.length
        await play_audio(ctx, 'Clips/Boy.mp3', time + 0.25)

    @commands.command()
    async def owo(self, ctx):
        chance = random.randint(1, 50)
        if chance == 50:
            filepath = 'Clips/Owo2.mp3'
        else:
            filepath = 'Clips/Owo.mp3'
        time = MP3(filepath).info.length
        await play_audio(ctx, filepath, time + 0.25)

    @commands.command()
    async def wtf(self, ctx):
        time = MP3('Clips/Wtf.mp3').info.length
        await play_audio(ctx, 'Clips/Wtf.mp3', time + 0.25)

    @commands.command()
    async def yawn(self, ctx):
        filepath = "Clips/Yawns/" + str(random.randint(1, 6)) + ".mp3"
        time = MP3(filepath).info.length
        await play_audio(ctx, filepath, time + 0.25)


def setup(bot):
    bot.add_cog(Audio(bot))
