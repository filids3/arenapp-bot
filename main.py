import discord
import os

TOKEN = os.getenv("TOKEN")  # Lo vas a configurar en Railway como variable secreta

intents = discord.Intents.default()
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == "!ping":
        await message.channel.send("Pong!")

bot.run(TOKEN)
