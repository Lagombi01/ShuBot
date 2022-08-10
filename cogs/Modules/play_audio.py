import discord
import asyncio


async def play_audio(ctx, clip, time):

    if isinstance(ctx, discord.Interaction):
        if not ctx.user.voice:
            await ctx.channel.send("{} is not connected to a voice channel".format(ctx.user.name), delete_after=5)
            await ctx.response.defer()
            return
        else:
            channel = await ctx.user.voice.channel.connect()

        await ctx.response.defer()

        audio = discord.FFmpegPCMAudio(clip)
        channel.play(audio)
        await asyncio.sleep(time)
        await channel.disconnect()
    else:
        if not ctx.message.author.voice:
            await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name), delete_after=5)
            return
        else:
            channel = await ctx.message.author.voice.channel.connect()

        audio = discord.FFmpegPCMAudio(clip)
        channel.play(audio)
        await asyncio.sleep(time)
        await channel.disconnect()
