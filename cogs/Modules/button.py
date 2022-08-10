import discord


class Button(discord.ui.Button):
    def __init__(self, label, clip_function=None, style=discord.ButtonStyle.blurple, emoji=None):
        super().__init__(label=label, style=style, emoji=emoji)
        if clip_function is not None:
            self.clip = clip_function

    async def callback(self, interaction: discord.Interaction):
        try:
            await self.clip(interaction)
        except discord.errors.ClientException:
            await interaction.response.send_message("Too many requests, slow down!", ephemeral=True)
        except:
            await interaction.response.send_message("Something went wrong :S, pls tell my creator about it ^_^", ephemeral=True)
