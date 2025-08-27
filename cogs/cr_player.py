import discord
from discord.ext import commands
from discord import app_commands
import requests
import os

class CRPlayer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.token = os.getenv("CR_API_TOKEN")  # Token de la API de Clash Royale
        self.base_url = "https://api.clashroyale.com/v1"

    # Slash command para buscar jugador por tag
    @app_commands.command(name="player", description="Buscar jugador de Clash Royale por tag")
    @app_commands.describe(tag="Tag del jugador (ej: #ABC123)")
    async def player(self, interaction: discord.Interaction, tag: str):
        await interaction.response.defer()  # Mensaje de espera

        # Asegurarse de que el tag tenga #
        if not tag.startswith("#"):
            tag = "#" + tag

        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        # Llamada a la API
        url = f"{self.base_url}/players/{tag.replace('#', '%23')}"
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            await interaction.followup.send(f"Error al buscar el jugador. Status: {response.status_code}")
            return

        data = response.json()

        # Crear embed para mostrar la info del jugador
        embed = discord.Embed(
            title=f"{data.get('name')} ({data.get('tag')})",
            description=f"Nivel: {data.get('expLevel')} | Trofeos: {data.get('trophies')}",
            color=discord.Color.blue()
        )

        embed.add_field(name="Mejor Liga", value=data.get('bestTrophies', "N/A"))
        embed.add_field(name="Victorias", value=data.get('wins', 0))
        embed.add_field(name="Derrotas", value=data.get('losses', 0))

        await interaction.followup.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(CRPlayer(bot))
