#
import discord
import random
from discord.ext import commands
from keep import keep_alive
#import youtube_dl
#import os
#import DiscordUtils
#the perfix
b = commands.Bot(command_prefix='.')

#b.remove_command("help")
#events
#on ready
@b.event
async def on_ready():
	print("Bot online")


#commands
#ping
@b.command()
async def ping(ctx):
	await ctx.send(f'pong! {round(b.latency * 1000)}ms')


#8ball
@b.command(
    aliases=['8ball', '8BALL'],
    help="8ball: ask me something and i will answer example .8ball are you a bot"
)
async def _8ball(ctx, *, question):
	rr = ['no|لا', 'yes|ايوه', 'Maybe|ممكن', '5555555555555|خخخخخخخخخخخ']
	await ctx.send(f'QUESTION:{question}\nAnswer: {random.choice(rr)}')


#how much
@b.command(
    aliases=['howmuch', 'HOW_MUCH'],
    help=
    "how_much: ask me something and i will answer with a percentage example how_much are you good"
)
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
@b.command(
    aliases=[
        'DOES', 'Does', 'does', 'do', 'Do', 'DO', 'did', 'Did', 'DID', 'will',
        'Will', 'WILL', 'shall', 'Shall', 'SHALL', 'are', 'Are', 'ARE', 'am',
        'Am', 'AM', 'have', 'Have', 'HAVE', 'has', 'Has', 'HAS', 'can', 'Can',
        'CAN', 'must', 'Must', 'MUST', 'might', 'Might', 'MIGHT', 'COULD',
        'could', 'Could'
    'is', 'IS', 'Is'],
    help=
    "does: ask me somthing and i will answer with yes or no example does any one love me"
)
async def question(ctx, *, question1):
	does_list = ['no|لا', 'yes|ايوه', 'maybe|ممكن']
	await ctx.send(f'{random.choice(does_list)}')


#is
#@b.command(aliases=['is', 'IS'])
#async def _is(ctx, *, member_name):
#	is_list = [
#	    'a nice guy? yes|راجل طيب؟ ايوه', 'a bitch? yes|عاهره؟ ايوه',
#	    'a gay? yes|شاذ؟ ايوه'
#	]
#	await ctx.send(
#	    f'QUESTION:is {member_name}\nAnswer: {random.choice(is_list)}')

#dm
@b.command(aliases=['DM'], help="do i have to explain?")
async def dm(ctx, member: discord.Member):
	await ctx.send("what do you want to say")

	def check(m):
		return m.author.id == ctx.author.id

	message = await b.wait_for('message', check=check)

	await ctx.send(f'the message is sent to {member}')

	await member.send(
	    f'{ctx.author.mention} Has a message for you:\n{message.content}')












keep_alive()
#the run
#test

b.run('NzQxNzg0NjcwMzc4NjU1NzY2.Xy8mzw.WcBlJI7pW2U8rZVizr8xiLg3Guo')
