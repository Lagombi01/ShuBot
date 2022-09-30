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
    async def amb(self, ctx):
        await amb_clip(ctx)

    @commands.command()
    async def dic(self, ctx):
        await dic_clip(ctx)

    @commands.command()
    async def mouth(self, ctx):
        await mouth_clip(ctx)

    @commands.command()
    async def arf(self, ctx):
        await arf_clip(ctx)

    @commands.command()
    async def women(self, ctx):
        await women_clip(ctx)

    @commands.command()
    async def uwu(self, ctx):
        await funny_yawn(ctx)

    @commands.command()
    async def boba(self, ctx):
        await boba_clip(ctx)

    @commands.command()
    async def dom(self, ctx):
        await dom_clip(ctx)

    @commands.command()
    async def yawn(self, ctx):
        await yawn_clip(ctx)


async def setup(bot):
    await bot.add_cog(Audio(bot))
