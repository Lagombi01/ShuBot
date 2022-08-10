from discord.ext import commands
from cogs.Modules.clip_functions import *


class Audio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gai(self, ctx):
        await gai_clip(ctx)

    @commands.command()
    async def cri(self, ctx):
        await cri_clip(ctx)

    @commands.command()
    async def ehh(self, ctx):
        await ehh_clip(ctx)

    @commands.command()
    async def luca(self, ctx):
        await luca_clip(ctx)

    @commands.command()
    async def boy(self, ctx):
        await boy_clip(ctx)

    @commands.command()
    async def owo(self, ctx):
        await owo_clip(ctx)

    @commands.command()
    async def wtf(self, ctx):
        await wtf_clip(ctx)

    @commands.command()
    async def yawn(self, ctx):
        await yawn_clip(ctx)


async def setup(bot):
    await bot.add_cog(Audio(bot))
