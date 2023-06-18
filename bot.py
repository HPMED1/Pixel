#the imports--------------------------------------------------------------------
import discord
from discord import app_commands
import requests
import random
from discord.ext import commands, tasks
import json
import os
import asyncio
#the perfix---------------------------------------------------------------------pip

intents = discord.Intents.all()
# if you don't want all intents you can do discord.Intents.default()
b = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(b)
#events-------------------------------------------------------------------------
#on ready-----------------------------------------------------------------------


@b.event
async def on_ready():
  await tree.sync(guild=discord.Object(id=871311803630645279))
  # print "ready" in the console when the bot is ready to work
  print("ready")


#commands-----------------------------------------------------------------------
#ready--------------------------------------------------------------------------
@tree.command(name="ready", guild=discord.Object(id=871311803630645279))
async def _ready(interaction: discord.Interaction):

  await interaction.response.send_message("Hello!")


#ping---------------------------------------------------------------------------
@tree.command(name="ping", guild=discord.Object(id=871311803630645279))
async def ping(interaction: discord.Interaction):
  await interaction.response.send_message(f'pong! {round(b.latency * 1000)}ms')


@tree.command(name="affirmaion", guild=discord.Object(id=871311803630645279))
async def affirmation(interaction: discord.Interaction):
  r = requests.get("https://www.affirmations.dev")
  embed = discord.Embed(color=0x000000)
  embed.add_field(name="Answer", value=r.json()['affirmation'], inline=True)
  await interaction.response.send_message(embed=embed)


@tree.command(name="advice", guild=discord.Object(id=871311803630645279))
async def advice(interaction: discord.Interaction):
  r = requests.get("https://api.adviceslip.com/advice")
  embed = discord.Embed(color=0x000000)
  embed.add_field(name="Answer", value=r.json()['slip']['advice'], inline=True)
  await interaction.response.send_message(embed=embed)


@tree.command(name="evilinsult", guild=discord.Object(id=871311803630645279))
async def evilinsult(interaction: discord.Interaction):
  r = requests.get(
    f"https://evilinsult.com/generate_insult.php?lang=en&numbe={random.randint(1,3000)}&type=json"
  )

  embed = discord.Embed(color=0x000000)
  embed.add_field(name="Answer", value=r.json()['insult'], inline=True)
  await interaction.response.send_message(embed=embed)


@tree.command(name="define", guild=discord.Object(id=871311803630645279))
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
@tree.command(name="howmuch", guild=discord.Object(id=871311803630645279))
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
@tree.command(name="sadcat", guild=discord.Object(id=871311803630645279))
@app_commands.describe(question="question")
async def advice(interaction: discord.Interaction, question: str):
  data = question.replace(" ", "+")
  r = requests.get(f"https://api.popcat.xyz/sadcat?text={data}")
  with open("image.webp", "wb") as f:
    f.write(r.content)
  await interaction.response.send_message(
    f'{interaction.user.mention} made this meme!',
    file=discord.File("image.webp"))


@tree.command(name="poohmeme", guild=discord.Object(id=871311803630645279))
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


@tree.command(name="avatar", guild=discord.Object(id=871311803630645279))
@app_commands.describe(member="member")
async def avatar(interaction: discord.Interaction, member: discord.Member):
  await interaction.response.send_message(member.avatar)


@tree.command(name="jail", guild=discord.Object(id=871311803630645279))
@app_commands.describe(member="member")
async def jail(interaction: discord.Interaction, member: discord.Member):
  r = requests.get(f"https://api.popcat.xyz/jail?image={member.avatar}")
  with open("image.webp", "wb") as f:
    f.write(r.content)
  await interaction.response.send_message(
    f'{interaction.user.mention} made this meme!',
    file=discord.File("image.webp"))


@tree.command(name="unforgivable", guild=discord.Object(id=871311803630645279))
@app_commands.describe(question="question")
async def unforgivable(interaction: discord.Interaction, question: str):
  data = question.replace(" ", "+")
  r = requests.get(f"https://api.popcat.xyz/unforgivable?text={data}")
  with open("image.webp", "wb") as f:
    f.write(r.content)
  await interaction.response.send_message(
    f'{interaction.user.mention} made this meme!',
    file=discord.File("image.webp"))


@tree.command(name="oogway", guild=discord.Object(id=871311803630645279))
@app_commands.describe(question="question")
async def oogway(interaction: discord.Interaction, question: str):
  data = question.replace(" ", "+")
  r = requests.get(f"https://api.popcat.xyz/oogway?text={data}")
  with open("image.webp", "wb") as f:
    f.write(r.content)
  await interaction.response.send_message(
    f'{interaction.user.mention} made this meme!',
    file=discord.File("image.webp"))


@tree.command(name="gun", guild=discord.Object(id=871311803630645279))
@app_commands.describe(member="member")
async def gun(interaction: discord.Interaction, member: discord.Member):
  r = requests.get(f"https://api.popcat.xyz/gun?image={member.avatar}")
  with open("image.webp", "wb") as f:
    f.write(r.content)
  await interaction.response.send_message(
    f'{interaction.user.mention} made this meme!',
    file=discord.File("image.webp"))


@tree.command(name="randommeme", guild=discord.Object(id=871311803630645279))
async def randommeme(interaction: discord.Interaction):
  r = requests.get("https://api.popcat.xyz/meme")
  rr = r.json()
  await interaction.response.send_message(rr['image'])


@tree.command(name="ship", guild=discord.Object(id=871311803630645279))
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


@tree.command(name="clown", guild=discord.Object(id=871311803630645279))
@app_commands.describe(member="member")
async def clown(interaction: discord.Interaction, member: discord.Member):
  r = requests.get(f"https://api.popcat.xyz/clown?image={member.avatar}")
  with open("image.webp", "wb") as f:
    f.write(r.content)
  await interaction.response.send_message(
    f'{interaction.user.mention} made this meme!',
    file=discord.File("image.webp"))


@tree.command(name="pet", guild=discord.Object(id=871311803630645279))
@app_commands.describe(member="member")
async def pet(interaction: discord.Interaction, member: discord.Member):
  r = requests.get(f"https://api.popcat.xyz/pet?image={member.avatar}")
  with open("image.gif", "wb") as f:
    f.write(r.content)
  await interaction.response.send_message(
    f'{interaction.user.mention} made this meme!',
    file=discord.File("image.gif"))


@tree.command(name="alert", guild=discord.Object(id=871311803630645279))
@app_commands.describe(text="text")
async def alert(interaction: discord.Interaction, text: str):
  data = text.replace(" ", "+")
  r = requests.get(f"https://api.popcat.xyz/alert?text={data}")
  with open("image.webp", "wb") as f:
    f.write(r.content)
  await interaction.response.send_message(
    f'{interaction.user.mention} made this meme!',
    file=discord.File("image.webp"))


@tree.command(name="facts", guild=discord.Object(id=871311803630645279))
@app_commands.describe(text="text")
async def facts(interaction: discord.Interaction, text: str):
  data = text.replace(" ", "+")
  r = requests.get(f"https://api.popcat.xyz/facts?text={data}")
  with open("image.webp", "wb") as f:
    f.write(r.content)
  await interaction.response.send_message(
    f'{interaction.user.mention} made this meme!',
    file=discord.File("image.webp"))


@tree.command(name="lyrics", guild=discord.Object(id=871311803630645279))
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

b.run("NzQxNzg0NjcwMzc4NjU1NzY2.GuqQKz.8R3jmDmh3CDjYyzl-O2bl6SLGyhMPqb-tU3jo8")
