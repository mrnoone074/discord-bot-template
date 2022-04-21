import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

prefix = "!"
bot = commands.Bot(command_prefix = prefix)

@bot.event
async def on_ready():
    print(f"{bot.user} is up!")

keep_alive()
# go and create a secret named exactly the same as the name under
bot.run(os.getenv("token"))