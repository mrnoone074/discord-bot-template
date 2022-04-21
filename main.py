import discord
from discord.ext import commands
import os

prefix = "!"
bot = commands.Bot(command_prefix = prefix)

@bot.event
async def on_ready():
    print(f"{bot.user} is up!")

# go and create a secret named exactly the same as the name under
bot.run(os.getenv("token"))