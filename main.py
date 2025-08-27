import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Cargar variables del .env (solo para pruebas locales)
load_dotenv()

TOKEN = os.getenv("TOKEN")
if TOKEN is None:
    raise ValueError("No se encontró el TOKEN. Configurá la variable de entorno correctamente.")

# Configurar intents
intents = discord.Intents.default()
intents.message_content = True  # necesario si vas a recibir mensajes normales

# Crear bot con setup_hook para cargar cogs y registrar slash commands
class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        # Cargar todos los cogs automáticamente
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await self.load_extension(f"cogs.{filename[:-3]}")
        # Registrar slash commands en Discord
        await self.tree.sync()

bot = MyBot()

@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")

bot.run(TOKEN)
