#
import discord
import random
from discord.ext import commands
from keep import keep_alive
#the perfix
b = commands.Bot(command_prefix='.')
b.remove_command("help")
#events
#on ready
@b.event
async def on_ready():
       print("Bot online")
#commands
#help
@b.command(aliases=['HELP'])
async def help(ctx):
  await ctx.send('`1-8ball: ask me something and i will answer \nexample ".8ball are you a bot"\n2-how_much: ask me something and i will answer with a percentage \nexample "how_much are you good"\n3-does: ask me somthing and i will answer with yes or no \nexample "does any one love me"\n4-is: type is and mention and see`')
#ping
@b.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(b.latency * 1000)}ms')
#8ball
@b.command(aliases=['8ball', '8BALL'])
async def _8ball(ctx, *, question):
    rr = ['no|لا','yes|ايوه', 'Maybe|ممكن','5555555555555|خخخخخخخخخخخ']
    await ctx.send (f'QUESTION:{question}\nAnswer: {random.choice(rr)}')
#how much
@b.command(aliases=['howmuch', 'HOW_MUCH'])
async def how_much(ctx, *, member_name):
    how_list = ['0%','1%', '2%','3%', '4%','5%','6%','7%','8%','9%','10%','11%','12%','13%','14%','15%','16%','17%','18%','19%','20%','21%','22%','23%','24%','25%','26%','27%','28%','29%','30%','31%','32%','33%','34%','35%','36%','37%','38%','39%','40%','41%','42%','43%','44%','45%','46%','47%','48%','49%','50%','51%','52%','53%','54%','55%','56%','57%','58%','59%','60%','61%','62%','63%','64%','65%','66%','67%','68%','69%','70%','71%','72%','73%','74%','75%','76%','77%','78%','79%','80%','81%','82%','83%','84%','85%','86%','87%','88%','89%','90%','91%','92%','93%','94%','95%','96%','97%','98%','99%','100%','idk']
    await ctx.send (f'{random.choice(how_list)}')
#dose
@b.command(aliases=['DOES'])
async def does(ctx, *, question1):
    does_list = ['no|لا','yes|ايوه']
    await ctx.send (f'QUESTION:{question1}\nAnswer: {random.choice(does_list)}')
#is
@b.command(aliases=['is', 'IS'])
async def _is(ctx, *, member_name):
    is_list = ['a nice guy? yes|راجل طيب؟ ايوه','a bitch? yes|عاهره؟ ايوه','a gay? yes|شاذ؟ ايوه']
    await ctx.send (f'QUESTION:is {member_name}\nAnswer: {random.choice(is_list)}')



keep_alive()
#the run
b.run('NzQxNzg0NjcwMzc4NjU1NzY2.Xy8mzw.WcBlJI7pW2U8rZVizr8xiLg3Guo')

