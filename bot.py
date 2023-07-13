import asyncio
import json
import os
import random
import re

import discord
import requests
from discord import app_commands
from discord.ext import commands, tasks

import settings

intents = discord.Intents.all()
b = commands.Bot(command_prefix=".", intents=intents)


async def getidinfo(t, b=b):
    pattern = "<@[0-9]{18}>"
    id = re.findall(pattern, t)
    if len(id) != 0:
        id = id[0]
    else:
        return t
    id = id = re.search(r'\d+', id).group()
    user = await b.fetch_user(id)
    user = user.display_name
    t = re.sub(pattern, user, t)
    return t


async def makeembed(title: str, thumbnail: str):
    embed = discord.Embed(
        colour=discord.Colour(0xffffff),
        title=title
    )
    embed.set_thumbnail(url=thumbnail)
    return embed


class ImgCmds(app_commands.Group):
    @app_commands.command(name="sadcat")
    @app_commands.describe(text="text")
    async def sadcat(self, interaction: discord.Interaction, text: str):
        text = await getidinfo(text)
        data = text.replace(" ", "+")
        embed = await makeembed(title=f'{interaction.user.display_name} made this meme!', thumbnail=interaction.user.avatar)
        r = requests.get(
            f"https://api.popcat.xyz/sadcat?text={data}")
        with open("image.jpg", "wb") as f:
            f.write(r.content)
            await interaction.response.send_message(embed=embed, file=discord.File("image.jpg"))

    @app_commands.command(name="poohmeme")
    @app_commands.describe(text1="text1", text2="text2")
    async def poohmeme(self, interaction: discord.Interaction, text1: str, text2: str):
        text1 = await getidinfo(text1)
        text2 = await getidinfo(text2)
        data1 = text1.replace(" ", "+")
        data2 = text2.replace(" ", "+")
        embed = await makeembed(title=f'{interaction.user.display_name} made this meme!', thumbnail=interaction.user.avatar)
        r = requests.get(
            f"https://api.popcat.xyz/pooh?text1={data1}&text2={data2}")
        with open("image.jpg", "wb") as f:
            f.write(r.content)
            await interaction.response.send_message(embed=embed,
                                                    file=discord.File("image.jpg"))

    @app_commands.command(name="jail")
    @app_commands.describe(member="member")
    async def jail(self, interaction: discord.Interaction, member: discord.Member):
        embed = await makeembed(title=f'{interaction.user.display_name} made this meme!', thumbnail=interaction.user.avatar)
        r = requests.get(
            f"https://api.popcat.xyz/jail?image={member.avatar}")
        with open("image.jpg", "wb") as f:
            f.write(r.content)
            await interaction.response.send_message(embed=embed, file=discord.File("image.jpg"))

    @app_commands.command(name="unforgivable")
    @app_commands.describe(question="question")
    async def unforgivable(self, interaction: discord.Interaction, question: str):
        question = await getidinfo(question)
        data = question.replace(" ", "+")
        embed = await makeembed(title=f'{interaction.user.display_name} made this meme!', thumbnail=interaction.user.avatar)
        r = requests.get(
            f"https://api.popcat.xyz/unforgivable?text={data}")
        with open("image.jpg", "wb") as f:
            f.write(r.content)
            await interaction.response.send_message(embed=embed, file=discord.File("image.jpg"))

    @app_commands.command(name="oogway")
    @app_commands.describe(question="question")
    async def oogway(self, interaction: discord.Interaction, question: str):
        question = await getidinfo(question)
        data = question.replace(" ", "+")
        embed = await makeembed(title=f'{interaction.user.display_name} made this meme!', thumbnail=interaction.user.avatar)
        r = requests.get(
            f"https://api.popcat.xyz/oogway?text={data}")
        with open("image.jpg", "wb") as f:
            f.write(r.content)
            await interaction.response.send_message(embed=embed, file=discord.File("image.jpg"))

    @app_commands.command(name="gun")
    @app_commands.describe(member="member")
    async def gun(self, interaction: discord.Interaction, member: discord.Member):
        embed = await makeembed(title=f'{interaction.user.display_name} made this meme!', thumbnail=interaction.user.avatar)
        r = requests.get(
            f"https://api.popcat.xyz/gun?image={member.avatar}")
        with open("image.jpg", "wb") as f:
            f.write(r.content)
            await interaction.response.send_message(embed=embed, file=discord.File("image.jpg"))

    @app_commands.command(name="ship")
    @app_commands.describe(member1="member1", member2="member2")
    async def ship(self, interaction: discord.Interaction, member1: discord.Member, member2: discord.Member):
        embed = await makeembed(title=f'{interaction.user.display_name} made this meme!', thumbnail=interaction.user.avatar)
        r = requests.get(
            f"https://api.popcat.xyz/ship?user1={member1.avatar}&user2={member2.avatar}")
        with open("image.jpg", "wb") as f:
            f.write(r.content)
            await interaction.response.send_message(embed=embed, file=discord.File("image.jpg"))

    @app_commands.command(name="pet")
    @app_commands.describe(member="member")
    async def pet(self, interaction: discord.Interaction, member: discord.Member):
        # with open("image.gif", "wb") as f:
        # f.write(r.content)
        # await interaction.response.send_message(
        # f'{interaction.user.display_name} made this meme!',
        # file=discord.File("image.gif"))
        # embed = discord.Embed(
        # colour=discord.Colour(0xffffff),
        # title=f'{interaction.user.display_name} made this meme!'
        # )
        # embed.set_thumbnail(url=interaction.user.avatar)
        # embed.set_image(
        # url=f"https://api.popcat.xyz/pet?image={member.avatar}")
        await interaction.response.send_message(f"https://api.popcat.xyz/pet?image={member.avatar}")

    @app_commands.command(name="alert")
    @app_commands.describe(text="text")
    async def alert(self, interaction: discord.Interaction, text: str):
        text = await getidinfo(text)
        data = text.replace(" ", "+")
        embed = await makeembed(title=f'{interaction.user.display_name} made this meme!', thumbnail=interaction.user.avatar)
        r = requests.get(
            f"https://api.popcat.xyz/alert?text={data}")
        with open("image.jpg", "wb") as f:
            f.write(r.content)
            await interaction.response.send_message(embed=embed, file=discord.File("image.jpg"))

    @app_commands.command(name="facts")
    @app_commands.describe(text="text")
    async def facts(self, interaction: discord.Interaction, text: str):
        text = await getidinfo(text)
        data = text.replace(" ", "+")
        embed = await makeembed(title=f'{interaction.user.display_name} made this meme!', thumbnail=interaction.user.avatar)
        r = requests.get(
            f"https://api.popcat.xyz/facts?text={data}")
        with open("image.jpg", "wb") as f:
            f.write(r.content)
            await interaction.response.send_message(embed=embed, file=discord.File("image.jpg"))

# -------------------------------------------------------------


class TxtCmds(app_commands.Group):

    @app_commands.command(name="affirmaion", description="affirms you")
    async def affirmation(self, interaction: discord.Interaction):
        r = requests.get("https://www.affirmations.dev")
        embed = discord.Embed(color=0xffffff)
        embed.add_field(name="Affirmation", value=r.json()
                        ['affirmation'], inline=True)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="advice", description="gives you an advice")
    async def advice(self, interaction: discord.Interaction):
        r = requests.get("https://api.adviceslip.com/advice")
        embed = discord.Embed(color=0xffffff)
        embed.add_field(name="Advice", value=r.json()[
                        'slip']['advice'], inline=True)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="evilinsult", description="returns the most evil insults known to mankind")
    async def evilinsult(self, interaction: discord.Interaction):
        r = requests.get(
            f"https://evilinsult.com/generate_insult.php?lang=en&numbe={random.randint(1,3000)}&type=json"
        )

        embed = discord.Embed(color=0xffffff)
        embed.add_field(name="Insult", value=r.json()['insult'], inline=True)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="define", description="defines a word")
    @app_commands.describe(word_to_define="what should i define")
    async def define(self, interaction: discord.Interaction, word_to_define: str):
        r = requests.get(
            f"https://api.urbandictionary.com/v0/define?term={word_to_define}")
        embed = discord.Embed(color=0xffffff)
        embed.add_field(name="Defintion to", value=word_to_define, inline=True)
        embed.add_field(name="Answer", value=r.json()[
                        'list'][random.randrange(0, 10)]['definition'], inline=True)
        await interaction.response.send_message(embed=embed)

    # how much
    @app_commands.command(name="howmuch", description="returns 0% -> 100%")
    @app_commands.describe(question="question")
    async def how_much(self, interaction: discord.Interaction, question: str):
        question = await getidinfo(question)
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
        embed = discord.Embed(
            colour=discord.Colour(0xffffff),
            title=f'how much {question}'
        )
        embed.add_field(name="Answer", value=f'{random.choice(how_list)}')

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="showerthought", description="some shower thoughts so you don't have to think in the shower")
    async def showerthought(self, interaction: discord.Interaction):
        r = requests.get("https://api.popcat.xyz/showerthoughts")
        rr = r.json()["result"]
        embed = discord.Embed(
            colour=discord.Colour(0xffffff),
            title="Shower thought"
        )
        embed.add_field(name="Thought", value=rr)

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="avatar", description="returns the avatar of a member")
    @app_commands.describe(member="member")
    async def avatar(self, interaction: discord.Interaction, member: discord.Member):
        embed = discord.Embed(
            colour=discord.Colour(0xffffff),
            title=f"{member.display_name}'s avatar"
        )
        embed.set_image(url=member.avatar)

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="lyrics", description="returns the lyrics of any song")
    @app_commands.describe(name="name")
    async def lyrics(self, interaction: discord.Interaction, name: str):
        data = name.replace(" ", "+")
        r = requests.get(f"https://api.popcat.xyz/lyrics?song={data}")
        rr = r.json()
        embed = discord.Embed(color=0xffffff)
        embed.add_field(name='Name', value=rr["title"])
        embed.set_image(url=rr['image'])
        embed.add_field(name='Artist', value=rr['artist'])
        await interaction.response.send_message('`' + rr['lyrics'] + '`', embed=embed)

    @app_commands.command(name="tax")
    @app_commands.describe(amount_to_tax="amount to tax")
    async def tax(self, interaction: discord.Interaction, amount_to_tax: int):
        embed = discord.Embed(color=0xffffff)
        embed.add_field(name="Probot tax", value=int(
            amount_to_tax * 0.05), inline=True)
        embed.add_field(name="Total amount", value=amount_to_tax *
                        0.05 + amount_to_tax, inline=True)
        await interaction.response.send_message(embed=embed)


@b.event
async def on_ready():
    b.tree.add_command(TxtCmds(name="commands"))
    b.tree.add_command(
        ImgCmds(name="memes", description="commands that generate memes"))
    await b.tree.sync()
    print('Command tree synced.')
    # print "ready" in the console when the bot is ready to work
    print("ready")

b.run(settings.DISCORD_API_TOKEN)
