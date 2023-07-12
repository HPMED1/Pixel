import discord
from discord import app_commands
import requests
import random
from discord.ext import commands, tasks
import json


class ImgCmds(app_commands.Group):
    @app_commands.command(name="sadcat")
    @app_commands.describe(text="text")
    async def sadcat(self, interaction: discord.Interaction, text: str):
        data = text.replace(" ", "+")
        embed = discord.Embed(
            colour=discord.Colour(0xffffff),
            title=f'{interaction.user.display_name} made this meme!'
        )
        # embed.set_thumbnail(url=interaction.user.avatar)
        embed.set_image(url=f"https://api.popcat.xyz/sadcat?text={data}")
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="poohmeme")
    @app_commands.describe(text1="text1", text2="text2")
    async def poohmeme(self, interaction: discord.Interaction, text1: str, text2: str):
        data1 = text1.replace(" ", "+")
        data2 = text2.replace(" ", "+")
        embed = discord.Embed(
            colour=discord.Colour(0xffffff),
            title=f'{interaction.user.display_name} made this meme!'
        )
        # embed.set_thumbnail(url=interaction.user.avatar)
        embed.set_image(
            url=f"https://api.popcat.xyz/pooh?text1={data1}&text2={data2}")
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="jail")
    @app_commands.describe(member="member")
    async def jail(self, interaction: discord.Interaction, member: discord.Member):
        embed = discord.Embed(
            colour=discord.Colour(0xffffff),
            title=f'{interaction.user.display_name} made this meme!'
        )
        # embed.set_thumbnail(url=interaction.user.avatar)
        embed.set_image(
            url=f"https://api.popcat.xyz/jail?image={member.avatar}")
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="unforgivable")
    @app_commands.describe(question="question")
    async def unforgivable(self, interaction: discord.Interaction, question: str):
        data = question.replace(" ", "+")
        embed = discord.Embed(
            colour=discord.Colour(0xffffff),
            title=f'{interaction.user.display_name} made this meme!'
        )
        # embed.set_thumbnail(url=interaction.user.avatar)
        embed.set_image(url=f"https://api.popcat.xyz/unforgivable?text={data}")
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="oogway")
    @app_commands.describe(question="question")
    async def oogway(self, interaction: discord.Interaction, question: str):
        data = question.replace(" ", "+")
        embed = discord.Embed(
            colour=discord.Colour(0xffffff),
            title=f'{interaction.user.display_name} made this meme!'
        )
        # embed.set_thumbnail(url=interaction.user.avatar)
        embed.set_image(url=f"https://api.popcat.xyz/oogway?text={data}")
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="gun")
    @app_commands.describe(member="member")
    async def gun(self, interaction: discord.Interaction, member: discord.Member):
        embed = discord.Embed(
            colour=discord.Colour(0xffffff),
            title=f'{interaction.user.display_name} made this meme!'
        )
        # embed.set_thumbnail(url=interaction.user.avatar)
        embed.set_image(
            url=f"https://api.popcat.xyz/gun?image={member.avatar}")
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="ship")
    @app_commands.describe(member1="member1", member2="member2")
    async def ship(self, interaction: discord.Interaction, member1: discord.Member, member2: discord.Member):
        embed = discord.Embed(
            colour=discord.Colour(0xffffff),
            title=f'{interaction.user.display_name} made this meme!'
        )
        # embed.set_thumbnail(url=interaction.user.avatar)
        embed.set_image(
            url=f"https://api.popcat.xyz/ship?user1={member1.avatar}&user2={member2.avatar}")
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="pet")
    @app_commands.describe(member="member")
    async def pet(self, interaction: discord.Interaction, member: discord.Member):
        # with open("image.gif", "wb") as f:
        # f.write(r.content)
        # await interaction.response.send_message(
        # f'{interaction.user.display_name} made this meme!',
        # file=discord.File("image.gif"))
        embed = discord.Embed(
            colour=discord.Colour(0xffffff),
            title=f'{interaction.user.display_name} made this meme!'
        )
        # embed.set_thumbnail(url=interaction.user.avatar)
        embed.set_image(
            url=f"https://api.popcat.xyz/pet?image={member.avatar}")
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="alert")
    @app_commands.describe(text="text")
    async def alert(self, interaction: discord.Interaction, text: str):
        data = text.replace(" ", "+")
        embed = discord.Embed(
            colour=discord.Colour(0xffffff),
            title=f'{interaction.user.display_name} made this meme!'
        )
        # embed.set_thumbnail(url=interaction.user.avatar)
        embed.set_image(url=f"https://api.popcat.xyz/alert?text={data}")
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="facts")
    @app_commands.describe(text="text")
    async def facts(self, interaction: discord.Interaction, text: str):
        data = text.replace(" ", "+")
        embed = discord.Embed(
            colour=discord.Colour(0xffffff),
            title=f'{interaction.user.display_name} made this meme!'
        )
        # embed.set_thumbnail(url=interaction.user.avatar)
        embed.set_image(url=f"https://api.popcat.xyz/facts?text={data}")
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    bot.tree.add_command(
        ImgCmds(name="memes", description="commands that generate memes"))
