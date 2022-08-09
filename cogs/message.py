from discord.ext import commands


class Message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.bot.user.id != message.author.id:
            if 'shu' in message.content.lower():
                await message.reply("ShuUUuUuuuuUUuUUuu?!!?!?!")
            elif 'gai' in message.content.lower():
                await message.reply("GaiiiiIIIIIiiiIIIIiiIIii!?!?!?!?!?!")
            elif 'inori' in message.content.lower():
                await message.reply("InoriIIIIiiiIIIiIiiIiiIiiiI!!!!!!!!!")
            elif 'captain' in message.content.lower() and "<" not in message.content and ">" not in message.content:
                await message.reply("arf arf")
            elif 'incest' in message.content.lower() or 'christmas' in message.content.lower():
                await message.reply("MANAAAAAAAAAAAAAAA!")
            elif 'woof' in message.content.lower():
                await message.reply("woof woof")
            elif 'sugar' in message.content.lower():
                await message.reply("Sugar???")


def setup(bot):
    bot.add_cog(Message(bot))
