#the imports--------------------------------------------------------------------
import discord
from discord import app_commands
import requests
import random
from discord.ext import commands, tasks
import json
import os
import asyncio
import settings
#the perfix---------------------------------------------------------------------pip

intents = discord.Intents.all()
# if you don't want all intents you can do discord.Intents.default()
b = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(b)
#events-------------------------------------------------------------------------
#on ready-----------------------------------------------------------------------
class ImgCmds(app_commands.Group):
  pass
imgcmds = ImgCmds(name="memes", description="All meme genration commands")

@b.event
async def on_ready():
  #b.tree.copy_global_to(gulid=settings.GULIDS_ID)
  await tree.sync(gulid=871311803630645279)
  # print "ready" in the console when the bot is ready to work
  print("ready")
  b.tree.add_command(imgcmds)

#commands-----------------------------------------------------------------------
#ready--------------------------------------------------------------------------
@tree.command(name="ready")
async def _ready(interaction: discord.Interaction):

  await interaction.response.send_message("Hello!")


#ping---------------------------------------------------------------------------
@tree.command(name="ping")
async def ping(interaction: discord.Interaction):
  await interaction.response.send_message(f'pong! {round(b.latency * 1000)}ms')


@tree.command(name="affirmaion")
async def affirmation(interaction: discord.Interaction):
  r = requests.get("https://www.affirmations.dev")
  embed = discord.Embed(color=0x000000)
  embed.add_field(name="Answer", value=r.json()['affirmation'], inline=True)
  await interaction.response.send_message(embed=embed)


@tree.command(name="advice")
async def advice(interaction: discord.Interaction):
  r = requests.get("https://api.adviceslip.com/advice")
  embed = discord.Embed(color=0x000000)
  embed.add_field(name="Answer", value=r.json()['slip']['advice'], inline=True)
  await interaction.response.send_message(embed=embed)


@tree.command(name="evilinsult")
async def evilinsult(interaction: discord.Interaction):
  r = requests.get(
    f"https://evilinsult.com/generate_insult.php?lang=en&numbe={random.randint(1,3000)}&type=json"
  )

  embed = discord.Embed(color=0x000000)
  embed.add_field(name="Answer", value=r.json()['insult'], inline=True)
  await interaction.response.send_message(embed=embed)


@tree.command(name="define")
@app_commands.describe(word_to_define="what should i define")
async def define(interaction: discord.Interaction, word_to_define: str):
  r = requests.get(
    f"https://api.urbandictionary.com/v0/define?term={word_to_define}")
  embed = discord.Embed(color=0x000000)
  embed.add_field(name="Question", value=word_to_define, inline=True)
  embed.add_field(name="Answer",
                  value=r.json()['list'][random.randrange(0,
                                                          10)]['definition'],
                  inline=True)
  await interaction.response.send_message(embed=embed)


#how much
@tree.command(name="howmuch")
@app_commands.describe(question="question")
async def how_much(interaction: discord.Interaction, question: str):
  how_list = [
    '0%', '1%', '2%', '3%', '4%', '5%', '6%', '7%', '8%', '9%', '10%', '11%',
    '12%', '13%', '14%', '15%', '16%', '17%', '18%', '19%', '20%', '21%',
    '22%', '23%', '24%', '25%', '26%', '27%', '28%', '29%', '30%', '31%',
    '32%', '33%', '34%', '35%', '36%', '37%', '38%', '39%', '40%', '41%',
    '42%', '43%', '44%', '45%', '46%', '47%', '48%', '49%', '50%', '51%',
    '52%', '53%', '54%', '55%', '56%', '57%', '58%', '59%', '60%', '61%',
    '62%', '63%', '64%', '65%', '66%', '67%', '68%', '69%', '70%', '71%',
    '72%', '73%', '74%', '75%', '76%', '77%', '78%', '79%', '80%', '81%',
    '82%', '83%', '84%', '85%', '86%', '87%', '88%', '89%', '90%', '91%',
    '92%', '93%', '94%', '95%', '96%', '97%', '98%', '99%', '100%', 'idk'
  ]
  await interaction.response.send_message(f'{random.choice(how_list)}')


#say
@imgcmds.command(name="sadcat")
@app_commands.describe(question="question")
async def advice(interaction: discord.Interaction, question: str):
  data = question.replace(" ", "+")
  r = requests.get(f"https://api.popcat.xyz/sadcat?text={data}")
  with open("image.webp", "wb") as f:
    f.write(r.content)
  await interaction.response.send_message(
    f'{interaction.user.mention} made this meme!',
    file=discord.File("image.webp"))


@imgcmds.command(name="poohmeme")
@app_commands.describe(text1="text1", text2="text2")
async def poohmeme(interaction: discord.Interaction, text1: str, text2: str):
  data1 = text1.replace(" ", "+")
  data2 = text2.replace(" ", "+")
  r = requests.get(f"https://api.popcat.xyz/pooh?text1={text1}&text2={text2}")
  with open("image.webp", "wb") as f:
    f.write(r.content)
  await interaction.response.send_message(
    f'{interaction.user.mention} made this meme!',
    file=discord.File("image.webp"))


@tree.command(name="showerthought",
              guild=discord.Object(id=871311803630645279))
async def showerthought(interaction: discord.Interaction):
  r = requests.get("https://api.popcat.xyz/showerthoughts")
  rr = r.json()["result"]
  await interaction.response.send_message(rr)


@tree.command(name="avatar")
@app_commands.describe(member="member")
async def avatar(interaction: discord.Interaction, member: discord.Member):
  await interaction.response.send_message(member.avatar)


@imgcmds.command(name="jail")
@app_commands.describe(member="member")
async def jail(interaction: discord.Interaction, member: discord.Member):
  r = requests.get(f"https://api.popcat.xyz/jail?image={member.avatar}")
  with open("image.webp", "wb") as f:
    f.write(r.content)
  await interaction.response.send_message(
    f'{interaction.user.mention} made this meme!',
    file=discord.File("image.webp"))


@imgcmds.command(name="unforgivable")
@app_commands.describe(question="question")
async def unforgivable(interaction: discord.Interaction, question: str):
  data = question.replace(" ", "+")
  r = requests.get(f"https://api.popcat.xyz/unforgivable?text={data}")
  with open("image.webp", "wb") as f:
    f.write(r.content)
  await interaction.response.send_message(
    f'{interaction.user.mention} made this meme!',
    file=discord.File("image.webp"))


@imgcmds.command(name="oogway")
@app_commands.describe(question="question")
async def oogway(interaction: discord.Interaction, question: str):
  data = question.replace(" ", "+")
  r = requests.get(f"https://api.popcat.xyz/oogway?text={data}")
  with open("image.webp", "wb") as f:
    f.write(r.content)
  await interaction.response.send_message(
    f'{interaction.user.mention} made this meme!',
    file=discord.File("image.webp"))


@imgcmds.command(name="gun")
@app_commands.describe(member="member")
async def gun(interaction: discord.Interaction, member: discord.Member):
  r = requests.get(f"https://api.popcat.xyz/gun?image={member.avatar}")
  with open("image.webp", "wb") as f:
    f.write(r.content)
  await interaction.response.send_message(
    f'{interaction.user.mention} made this meme!',
    file=discord.File("image.webp"))


@imgcmds.command(name="randommeme")
async def randommeme(interaction: discord.Interaction):
  r = requests.get("https://api.popcat.xyz/meme")
  rr = r.json()
  await interaction.response.send_message(rr['image'])


@imgcmds.command(name="ship")
@app_commands.describe(member1="member1", member2="member2")
async def ship(interaction: discord.Interaction, member1: discord.Member,
               member2: discord.Member):
  r = requests.get(
    f"https://api.popcat.xyz/ship?user1={member1.avatar}&user2={member2.avatar}"
  )
  with open("image.webp", "wb") as f:
    f.write(r.content)
  await interaction.response.send_message(
    f'{interaction.user.mention} made this!', file=discord.File("image.webp"))


@imgcmds.command(name="clown")
@app_commands.describe(member="member")
async def clown(interaction: discord.Interaction, member: discord.Member):
  r = requests.get(f"https://api.popcat.xyz/clown?image={member.avatar}")
  with open("image.webp", "wb") as f:
    f.write(r.content)
  await interaction.response.send_message(
    f'{interaction.user.mention} made this meme!',
    file=discord.File("image.webp"))


@imgcmds.command(name="pet")
@app_commands.describe(member="member")
async def pet(interaction: discord.Interaction, member: discord.Member):
  r = requests.get(f"https://api.popcat.xyz/pet?image={member.avatar}")
  with open("image.gif", "wb") as f:
    f.write(r.content)
  await interaction.response.send_message(
    f'{interaction.user.mention} made this meme!',
    file=discord.File("image.gif"))


@imgcmds.command(name="alert")
@app_commands.describe(text="text")
async def alert(interaction: discord.Interaction, text: str):
  data = text.replace(" ", "+")
  r = requests.get(f"https://api.popcat.xyz/alert?text={data}")
  with open("image.webp", "wb") as f:
    f.write(r.content)
  await interaction.response.send_message(
    f'{interaction.user.mention} made this meme!',
    file=discord.File("image.webp"))


@imgcmds.command(name="facts")
@app_commands.describe(text="text")
async def facts(interaction: discord.Interaction, text: str):
  data = text.replace(" ", "+")
  r = requests.get(f"https://api.popcat.xyz/facts?text={data}")
  with open("image.webp", "wb") as f:
    f.write(r.content)
  await interaction.response.send_message(
    f'{interaction.user.mention} made this meme!',
    file=discord.File("image.webp"))


@tree.command(name="lyrics")
@app_commands.describe(name="name")
async def lyrics(interaction: discord.Interaction, name: str):
  data = name.replace(" ", "+")
  r = requests.get(f"https://api.popcat.xyz/lyrics?song={data}")
  rr = r.json()
  embed = discord.Embed(color=0x000000)
  embed.add_field(name='Name', value=rr["title"])
  embed.set_image(url=rr['image'])
  embed.add_field(name='Artist', value=rr['artist'])
  await interaction.response.send_message('`'+rr['lyrics']+'`', embed=embed)

b.run(settings.DISCORD_API_TOKEN)
