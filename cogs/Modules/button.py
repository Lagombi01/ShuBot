import discord


class Button(discord.ui.Button):
    def __init__(self, label, clip_function=None):
        super().__init__(label=label, style=discord.ButtonStyle.blurple)
        if clip_function is not None:
            self.clip = clip_function

    async def callback(self, interaction: discord.Interaction):
        try:
            await self.clip(interaction)
        except discord.errors.ClientException:
            await interaction.response.send_message("Too many requests, slow down!", ephemeral=True, delete_after=5)
        except:
            await interaction.response.send_message("Something went wrong :S, pls tell my creator about it ^_^", ephemeral=True, delete_after=5)


