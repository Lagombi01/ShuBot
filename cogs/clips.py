import discord
import os
from discord.ext import commands
from discord import app_commands

guild_id = os.getenv('GUILD_ID')


class clips(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="clips", description="Outputs a list of valid commands")
    async def clips(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"```gai\ncri\nehh\nboy\nluca\nowo\nwtf\nyawn```", ephemeral=True)


async def setup(bot):
    await bot.add_cog(clips(bot), guilds=[discord.Object(id=guild_id)])


