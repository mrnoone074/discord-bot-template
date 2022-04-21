# imports
import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

prefix = "!"
bot = commands.Bot(command_prefix = prefix)

# here the console prints that your bot is logged in!
@bot.event
async def on_ready():
    print(f"{bot.user} is up!")

# in the top of the output you see a link you can copy and paste in a monitor on www.uptimerobot.com
keep_alive()
# go and create a secret named exactly the same as the name under
bot.run(os.getenv("token"))