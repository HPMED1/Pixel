import os
from dotenv import load_dotenv
import pathlib
import discord

load_dotenv()
DISCORD_API_TOKEN = os.getenv('DISCORD_API_TOKEN')
BASE_DIR = pathlib.Path(__file__).parent
IMGCMDS_DIR = BASE_DIR / "imgcmds"
TXTCMDS_DIR = BASE_DIR / "txcmds"
GUILDS_ID = discord.Object(int(os.getenv('GUILD')))
