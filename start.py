import os
from dotenv import load_dotenv
from discord.ext import commands
import discord
from commands import loader  # Importer les commandes définies dans commands/loader.py

# Charger les variables d'environnement
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Configurer les intents
intents = discord.Intents.default()
intents.message_content = True

# Créer l'instance du bot
bot = commands.Bot(command_prefix="!", intents=intents)

# Charger les commandes depuis commands/loader.py
loader.setup(bot)

# Lancer le bot
if __name__ == "__main__":
    print("Démarrage du bot...")
    bot.run(TOKEN)
