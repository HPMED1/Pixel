import discord
from discord import app_commands
import requests
import random
from discord.ext import commands, tasks
import json


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


async def setup(bot):
    bot.tree.add_command(TxtCmds(name="commands"))
