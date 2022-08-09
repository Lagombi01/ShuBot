import discord
import os
from discord.ext import commands
from discord import app_commands

guild_id = os.getenv('GUILD_ID')


class soundboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="soundboard", description="This is just a test")
    async def soundboard(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Hi there owo")


async def setup(bot):
    await bot.add_cog(soundboard(bot), guilds=[discord.Object(id=guild_id)])


