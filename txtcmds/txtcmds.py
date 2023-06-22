import discord
from discord import app_commands
import requests
import random
from discord.ext import commands, tasks
import json

class TxtCmds(app_commands.Group):
    @app_commands.command(name="ready")
    async def _ready(self,interaction: discord.Interaction):

        await interaction.response.send_message("Hello!")


    @app_commands.command(name="ping")
    async def ping(self,interaction: discord.Interaction):
        await interaction.response.send_message(f'pong! {round(b.latency * 1000)}ms')


    @app_commands.command(name="affirmaion")
    async def affirmation(self,interaction: discord.Interaction):
        r = requests.get("https://www.affirmations.dev")
        embed = discord.Embed(color=0x000000)
        embed.add_field(name="Answer", value=r.json()['affirmation'], inline=True)
        await interaction.response.send_message(embed=embed)


    @app_commands.command(name="advice")
    async def advice(self,interaction: discord.Interaction):
        r = requests.get("https://api.adviceslip.com/advice")
        embed = discord.Embed(color=0x000000)
        embed.add_field(name="Answer", value=r.json()['slip']['advice'], inline=True)
        await interaction.response.send_message(embed=embed)


    @app_commands.command(name="evilinsult")
    async def evilinsult(self,interaction: discord.Interaction):
        r = requests.get(
        f"https://evilinsult.com/generate_insult.php?lang=en&numbe={random.randint(1,3000)}&type=json"
        )

        embed = discord.Embed(color=0x000000)
        embed.add_field(name="Answer", value=r.json()['insult'], inline=True)
        await interaction.response.send_message(embed=embed)


    @app_commands.command(name="define")
    @app_commands.describe(word_to_define="what should i define")
    async def define(self,interaction: discord.Interaction, word_to_define: str):
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
    @app_commands.command(name="howmuch")
    @app_commands.describe(question="question")
    async def how_much(self,interaction: discord.Interaction, question: str):
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


    @app_commands.command(name="showerthought")
    async def showerthought(self,interaction: discord.Interaction):
        r = requests.get("https://api.popcat.xyz/showerthoughts")
        rr = r.json()["result"]
        await interaction.response.send_message(rr)


    @app_commands.command(name="avatar")
    @app_commands.describe(member="member")
    async def avatar(self,interaction: discord.Interaction, member: discord.Member):
        await interaction.response.send_message(member.avatar)




    @app_commands.command(name="lyrics")
    @app_commands.describe(name="name")
    async def lyrics(self,interaction: discord.Interaction, name: str):
        data = name.replace(" ", "+")
        r = requests.get(f"https://api.popcat.xyz/lyrics?song={data}")
        rr = r.json()
        embed = discord.Embed(color=0x000000)
        embed.add_field(name='Name', value=rr["title"])
        embed.set_image(url=rr['image'])
        embed.add_field(name='Artist', value=rr['artist'])
        await interaction.response.send_message('`' + rr['lyrics'] + '`',
                                            embed=embed)

    @app_commands.command(name="tax")
    @app_commands.describe(amount_to_tax="amount to tax")
    async def tax(self,interaction: discord.Interaction, amount_to_tax: int):
        embed = discord.Embed(color=0x000000)
        embed.add_field(name="Probot tax", value=int(amount_to_tax * 0.05), inline=True)
        embed.add_field(name="Total amount",value=amount_to_tax * 0.05 + amount_to_tax,inline=True)
        await interaction.response.send_message(embed=embed)
async def setup(bot):
    bot.tree.add_command(TxtCmds(name="commands"))