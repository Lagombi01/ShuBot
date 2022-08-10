import discord
import asyncio


async def play_audio(ctx, clip, time):
    if isinstance(ctx, discord.Interaction):
        if not ctx.user.voice:
            await ctx.channel.send("{} is not connected to a voice channel".format(ctx.user.name), ephemeral=True, delete_after=5)
            return
        else:
            channel = await ctx.user.voice.channel.connect()
        audio = discord.FFmpegPCMAudio(clip)
        await ctx.response.defer()
        channel.play(audio)
        await asyncio.sleep(time)
        await channel.disconnect()
    else:
        if not ctx.message.author.voice:
            await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name), ephemeral=True, delete_after=5)
            return
        else:
            channel = await ctx.message.author.voice.channel.connect()

        audio = discord.FFmpegPCMAudio(clip)
        channel.play(audio)
        await asyncio.sleep(time)
        await channel.disconnect()
