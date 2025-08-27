import discord
from discord.ext import commands
from discord import app_commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Slash command
    @app_commands.command(name="ping", description="Responde Pong!")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message("Pong!")

# Setup asíncrono para que load_extension funcione
async def setup(bot: commands.Bot):
    await bot.add_cog(Ping(bot))
