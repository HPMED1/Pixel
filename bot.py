import discord
from discord import app_commands
import requests
import random
from discord.ext import commands, tasks
import json
import os
import asyncio
import settings
import wavelink

intents = discord.Intents.all()
b = commands.Bot(command_prefix=".", intents=intents)

@b.event
async def on_ready():
  await b.load_extension("imgcmds.imgcmds")
  await b.load_extension("txtcmds.txtcmds")
  b.tree.copy_global_to(guild=settings.GUILDS_ID)
  await b.tree.sync(guild=settings.GUILDS_ID)
  # print "ready" in the console when the bot is ready to work
  print("ready")


b.run(settings.DISCORD_API_TOKEN)
