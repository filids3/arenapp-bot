import discord
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")
GUILD_ID = 1410140145449046039  # tu servidor de prueba

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# -------------------------
# Evento on_ready
# -------------------------
@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")

    # Registrar comandos para tu servidor (aparece al instante)
    guild = discord.Object(id=GUILD_ID)
    await bot.tree.sync(guild=guild)

    # Registrar globalmente (tarda ~1 hora en otros servidores)
    await bot.tree.sync()

# -------------------------
# Ejemplo de slash command
# -------------------------
@bot.tree.command(name="ping", description="Prueba instantánea en tu servidor")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")

# -------------------------
# Cargar cogs automáticamente
# -------------------------
async def setup_hook():
    for filename in ["ping", "cr_player"]:  # solo los cogs que existen
        await bot.load_extension(f"cogs.{filename}")

bot.setup_hook = setup_hook

bot.run(TOKEN)
