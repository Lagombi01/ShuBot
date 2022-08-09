import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
guild_id = os.getenv('GUILD_ID')

bot = commands.Bot(command_prefix=',', status=discord.Status.online, activity=discord.Game(name="with your void UwU"))


@bot.event
async def on_ready():
    print(f"Shuuu?")


@bot.command(name="test")
async def test():
    print("hi")


bot.load_extension("cogs.audio")
bot.load_extension("cogs.message")
bot.run(token)
