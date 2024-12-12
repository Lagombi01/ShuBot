import os
import subprocess
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
guild_id = discord.Object(id=(os.getenv('GUILD_ID')))
app_id = os.getenv('APPLICATION_ID')

print(guild_id)

class MyBot(commands.Bot):

    def __init__(self):
        super().__init__(
            command_prefix=',',
            status=discord.Status.online,
            activity=discord.Game(name="with your void UwU"),
            intents=discord.Intents.all(),
            application_id=app_id
        )
        self.initial_extensions = [
            "cogs.soundboard",
            "cogs.clips",
            "cogs.audio",
            "cogs.message"
        ]

    async def setup_hook(self):
        for ext in self.initial_extensions:
            await self.load_extension(ext)

    async def on_ready(self):
        print(f"Shuuu?")


bot = MyBot()


@bot.command()
@commands.is_owner()
async def sink(ctx):
    await bot.tree.sync(guild=guild_id)
    await ctx.send(file=discord.File("Sink-chan.jpg"))
    print(f"Synced")

@bot.command()
@commands.is_owner()
async def update(ctx):
    subprocess.run(["python", "update.py"])
    pass


bot.run(token)
