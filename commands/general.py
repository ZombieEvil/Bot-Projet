from discord.ext import commands

def setup_general_commands(bot):
    @bot.command()
    async def ping(ctx):
        # Obtenir la latence en millisecondes
        latency = round(bot.latency * 1000)

        # Choisir un emoji en fonction de la latence
        if latency < 50:
            emoji = "🟢"  # Excellente connexion
        elif latency < 150:
            emoji = "🟡"  # Bonne connexion
        elif latency < 300:
            emoji = "🟠"  # Connexion moyenne
        else:
            emoji = "🔴"  # Mauvaise connexion

        # Réponse du bot
        await ctx.send(f"{emoji} Latence : `{latency}ms`")

    @bot.command()
    async def hello(ctx):
        await ctx.send("Salut, je suis ton bot!")
