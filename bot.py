#the imports
import discord
import random
from discord.ext import commands
#the perfix
b = commands.Bot(command_prefix='.')
#events
#on ready
@b.event
async def on_ready():
       print("Bot online")
#commands
#ready
@b.command(aliases=['ready', 'r'])
async def _ready(ctx):
    await ctx.send('yes')
#ping
@b.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(b.latency * 1000)}ms')
#8ball
@b.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    rr = ['no|لا','yes|ايوه', 'Maybe|ممكن','5555555555555|خخخخخخخخخخخ']
    await ctx.send (f'QUESTION:{question}\nAnswer: {random.choice(rr)}')
#how much
@b.command(aliases=['how much'])
async def how_much(ctx, *, member_name):
    how_list = ['0%','1%', '2%','3%']
    await ctx.send (f'{random.choice(how_list)}')





#the run
b.run('NzQxNzg0NjcwMzc4NjU1NzY2.Xy8mzw.KtnWs6ec4VX-S9D8epHKPeXUP2U')
