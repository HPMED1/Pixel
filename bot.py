#
import discord
import random
from discord.ext import commands, tasks
from keep import keep_alive
import youtube_dl
import os
import time
import sys
#from twitch import TwitchClient
from pprint import pformat
import DiscordUtils
#the perfix
b = commands.Bot(command_prefix='.')


#client = TwitchClient(client_id='<twitch token>')
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


#@b.command()
#async def info(ctx, username):
#response = await ctx.send("Querying twitch database...")
#try:
#users = client.users.translate_usernames_to_ids(username)
#for user in users:
#print(user.id)
#userid = user.id
#twitchinfo = client.users.get_by_id(userid)
#status = client.streams.get_stream_by_user(userid)
#if status == None:
#print("Not live")
#livestat = twitchinfo.display_name + "is not live"
#else:
#livestat = twitchinfo.display_name + " is " + status.stream_type
#responsemsg = pformat(twitchinfo) + "\n" + livestat
#await response.edit(content=responsemsg)
#except:
#await response.edit(content="Invalid username")
music = DiscordUtils.Music()


@b.command(aliases=['J', 'j'], help="Joins the voice channel")
async def join(ctx):
    await ctx.author.voice.channel.connect()
    await ctx.send("I'm connected")


@b.command(aliases=['l', 'L', 'ds', 'DS'], help="leaves the voice channel")
async def leave(ctx):
    await ctx.voice_client.disconnect()


@b.command(aliases=['p', 'P'], help="play music")
async def play(ctx, *, url):
    player = music.get_player(guild_id=ctx.guild.id)
    if not b.is_connected()
      await ctx.author.voice.channel.connect()
      await ctx.send("I'm connected")
    if not player:
        player = music.create_player(ctx, ffmpeg_error_betterfix=True)
    if not ctx.voice_client.is_playing():
        await player.queue(url, search=True)
        song = await player.play()
        await ctx.send(f"Playing {song.name}")
    else:
        song = await player.queue(url, search=True)
        await ctx.send(f"Queued {song.name}")


@b.command(aliases=['st', 'ST'], help="pause the music")
async def pause(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.pause()
    await ctx.send(f"Paused {song.name}")


@b.command(aliases=['r', 'R'], help="resume the music")
async def resume(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.resume()
    await ctx.send(f"Resumed {song.name}")


@b.command(aliases=['s', 'S'], help="stop the music")
async def stop(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    await player.stop()
    await ctx.send("Stopped")


@b.command(help="loop the music")
async def loop(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.toggle_song_loop()
    if song.is_looping:
        await ctx.send(f"Enabled loop for {song.name}")
    else:
        await ctx.send(f"Disabled loop for {song.name}")


@b.command(aliases=['q', 'Q'], help="see the queue")
async def queue(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    await ctx.send(
        f"{', '.join([song.name for song in player.current_queue()])}")


@b.command(help="see the name of the song playing right now")
async def np(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = player.now_playing()
    await ctx.send(song.name)


@b.command(help="skip songs")
async def skip(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    data = await player.skip(force=True)
    if len(data) == 2:
        await ctx.send(f"Skipped from {data[0].name} to {data[1].name}")
    else:
        await ctx.send(f"Skipped {data[0].name}")


@b.command(aliases=['vol', 'VOL', 'v', 'V'],
           help="change the volume of the music")
async def volume(ctx, vol):
    player = music.get_player(guild_id=ctx.guild.id)
    song, volume = await player.change_volume(
        float(vol) / 100)  # volume should be a float between 0 to 1
    await ctx.send(f"Changed volume for {song.name} to {volume*100}%")


#
@b.command(help="remove a song in the queue")
async def remove(ctx, index):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.remove_from_queue(int(index))
    await ctx.send(f"Removed {song.name} from queue")


@b.command()
async def add(ctx, num1: int, num2: int):
    res = float(num1 + num2)
    await ctx.send(res)


keep_alive()
#the run
b.run('NzQxNzg0NjcwMzc4NjU1NzY2.Xy8mzw.WcBlJI7pW2U8rZVizr8xiLg3Guo')
