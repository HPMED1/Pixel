#the imports--------------------------------------------------------------------
import discord
import requests
import random
from discord.ext import commands
from discord.ext import commands, tasks
import json
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('token')
#the perfix---------------------------------------------------------------------pip

b = commands.Bot(command_prefix='.')
#events-------------------------------------------------------------------------
#on ready-----------------------------------------------------------------------
@b.event
async def on_ready():
    
    print('bot is here')
#commands-----------------------------------------------------------------------
#ready--------------------------------------------------------------------------
@b.command(aliases=['ready', 'r'])
async def _ready(ctx):
    await ctx.send('yes')
#ping---------------------------------------------------------------------------
@b.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(b.latency * 1000)}ms')

@b.command()
async def Affirmation(ctx):
    r = requests.get("https://www.affirmations.dev")
    embed = discord.Embed(color=0x000000)
    embed.add_field(name="Answer", value=r.json()['affirmation'], inline=True)
    await ctx.send(embed=embed)


@b.command()
async def Advice(ctx):
    r = requests.get("https://api.adviceslip.com/advice")
    embed = discord.Embed(color=0x000000)
    embed.add_field(name="Answer", value=r.json()['slip']['advice'], inline=True)
    await ctx.send(embed=embed)


@b.command()
async def Evilinsult(ctx):
    r = requests.get(f"https://evilinsult.com/generate_insult.php?lang=en&numbe={random.randint(1,3000)}&type=json")
    
    embed = discord.Embed(color=0x000000)
    embed.add_field(name="Answer", value=r.json()['insult'], inline=True)
    await ctx.send(embed=embed)
@b.command()
async def Define (ctx, msg):
    r = requests.get(f"https://api.urbandictionary.com/v0/define?term={msg}")
    embed = discord.Embed(color=0x000000)
    embed.add_field(name="Question", value=msg, inline=True)
    embed.add_field(name="Answer", value=r.json()['list'][random.randrange(0,10)]['definition'], inline=True)
    await ctx.send(embed=embed)


@b.command()
async def _8Ball(ctx,msg):
    r = requests.get(f"https://8ball.delegator.com/magic/JSON/{msg}")
    embed = discord.Embed(color=0x000000)
    embed.add_field(name="Question", value=msg, inline=True)
    embed.add_field(name="Answer", value=r.json()['magic']['answer'], inline=True)
    await ctx.send(embed=embed)


#make a new command to that gets info on the user-----------------------------------
@b.command()
async def userinfo(ctx, member: discord.Member):
    embed = discord.Embed(title=f"{member}'s info", color=0x000000)
    embed.add_field(name="Name", value=member.name, inline=True)
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.add_field(name="Status", value=member.status, inline=True)
    embed.add_field(name="Highest role", value=member.top_role, inline=True)
    embed.add_field(name="Joined", value=member.joined_at, inline=True)
    await ctx.send(embed=embed)
#make a new command to that gets info on the server-----------------------------------
@b.command()
async def serverinfo(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}'s info", color=0x000000)
    embed.add_field(name="Name", value=ctx.guild.name, inline=True)
    embed.add_field(name="ID", value=ctx.guild.id, inline=True)
    embed.add_field(name="Owner", value=ctx.guild.owner, inline=True)
    embed.add_field(name="Roles", value=len(ctx.guild.roles), inline=True)
    embed.add_field(name="Channels", value=len(ctx.guild.channels), inline=True)
    await ctx.send(embed=embed)


@b.command(aliases=['8ball', '8BALL'],
           help="ask me something and i will answer")
async def _8ball(ctx, *, question):
    rr = ['no|لا', 'yes|ايوه', 'Maybe|ممكن', '5555555555555|خخخخخخخخخخخ']
    await ctx.send(f'QUESTION:{question}\nAnswer: {random.choice(rr)}')


#how much
@b.command(aliases=['howmuch', 'HOW_MUCH'], help="number%")
async def how_much(ctx, *, member_name):
    how_list = [
        '0%', '1%', '2%', '3%', '4%', '5%', '6%', '7%', '8%', '9%', '10%',
        '11%', '12%', '13%', '14%', '15%', '16%', '17%', '18%', '19%', '20%',
        '21%', '22%', '23%', '24%', '25%', '26%', '27%', '28%', '29%', '30%',
        '31%', '32%', '33%', '34%', '35%', '36%', '37%', '38%', '39%', '40%',
        '41%', '42%', '43%', '44%', '45%', '46%', '47%', '48%', '49%', '50%',
        '51%', '52%', '53%', '54%', '55%', '56%', '57%', '58%', '59%', '60%',
        '61%', '62%', '63%', '64%', '65%', '66%', '67%', '68%', '69%', '70%',
        '71%', '72%', '73%', '74%', '75%', '76%', '77%', '78%', '79%', '80%',
        '81%', '82%', '83%', '84%', '85%', '86%', '87%', '88%', '89%', '90%',
        '91%', '92%', '93%', '94%', '95%', '96%', '97%', '98%', '99%', '100%',
        'idk'
    ]
    await ctx.send(f'{random.choice(how_list)}')


#question
@b.command(aliases=[
    'DOES', 'Does', 'does', 'do', 'Do', 'DO', 'did', 'Did', 'DID', 'will',
    'Will', 'WILL', 'shall', 'Shall', 'SHALL', 'are', 'Are', 'ARE', 'am', 'Am',
    'AM', 'have', 'Have', 'HAVE', 'has', 'Has', 'HAS', 'can', 'Can', 'CAN',
    'must', 'Must', 'MUST', 'might', 'Might', 'MIGHT', 'COULD', 'could',
    'Could'
    'is', 'IS', 'Is'
],
           help="ask me somthing and i will answer with yes or no")
async def question(ctx, *, question1):
    does_list = ['no|لا', 'yes|ايوه', 'maybe|ممكن']
    await ctx.send(f'{random.choice(does_list)}')


#dm
@b.command(aliases=['DM'], help="send a message to someone")
async def dm(ctx, member: discord.Member):
    await ctx.send("what do you want to say")

    def check(m):
        return m.author.id == ctx.author.id

    message = await b.wait_for('message', check=check)

    await ctx.send(f'the message is sent to {member}')

    await member.send(
        f'{ctx.author.mention} Has a message for you:\n{message.content}')


#say
@b.command(aliases=['SAY'], help="do i have to explain?")
async def say(ctx, ):
    await ctx.send("what do you want me to say")

    def check(m):
        return m.author.id == ctx.author.id

    message = await b.wait_for('message', check=check)

    await ctx.send(f'{ctx.author.mention} made me say\n{message.content}')

b.run(TOKEN)
