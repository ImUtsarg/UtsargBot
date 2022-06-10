#very old and shitty src
#idc abt this shitty bot im working on a new bot that is better discord.gg/winstreak

import discord
import os
import platform
from datetime import date
from discord.ext import commands, tasks
from itertools import cycle
import json
from WebSvr import WebSvr

with open('Warnings.json', encoding='utf-8') as f:
  try:
    report = json.load(f)
  except ValueError:
    report = {}
    report['users'] = []

client = commands.Bot(command_prefix = '.')

ListOfStatus = cycle(['.help'])
today = date.today()
client.remove_command('help')

@client.event
async def on_ready():
  ChangeStatus.start()
  print("Bot Ready")
  channel = client.get_channel(852284554781261831)
  await channel.send("Bot is up")
  platform.system()

@tasks.loop(seconds=3)
async def ChangeStatus():
  await client.change_presence(activity=discord.Game(next(ListOfStatus)))

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

@client.command()
async def ping(ctx):
  EmbedMsg = discord.Embed(title="Ping", description=f'Your Ping is:  {round(client.latency * 1000)}ms', color=discord.Color.from_rgb(255, 0, 0))
  EmbedMsg.set_footer(text="Bot By someone on repl")
  await ctx.send(embed = EmbedMsg)


@client.command()
async def help(ctx):
  EmbedMsg = discord.Embed(title="Help", description="1.Help - Shows all the commands\n2.Ping - Shows the ping between the user and the bot\n3.Date - Shows the date for today\n4.Join - Joins the voice channel you are in\n5.Leave - Leaves the voice channel\n6.Play - Play (Song Title here) - plays the song\n7.helpMusic - Shows the commands for music", color=discord.Color.from_rgb(255, 0, 0))
  await ctx.send(embed = EmbedMsg)

@client.command()
@commands.has_any_role('⁂ Server Manager')
async def say(ctx, *, msg):
    await ctx.message.delete()
    EmbedMsg = discord.Embed(title="Brodcast", description=msg, color=discord.Color.from_rgb(255, 0, 0))
    await ctx.send(embed = EmbedMsg)

@client.command()
@commands.has_any_role('Staff')
async def rm(ctx):
  me = 610121260793462794
  await ctx.message.delete()
  mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
  await ctx.me.remove_roles(mutedRole)
  await ctx.me.send("Muted role removed")

@client.command()
async def helpMusic(ctx):
  EmbedMsg = discord.Embed(title="Music Commands", description="1.Play - plays the song requested - Usage: .Play (song name here)\n2.skip/s - skips the song playing - Usage: .s\n3.volume - Makes the volume higher or lower - Usage: .volume (number from 1-100)\n4.Join - Makes the bot join your vc - Usage: .join\n5.pause - Pauses the song - Usage: .pause\n6.queue - Shows the queue - Usage: .queue\n7.resume - resumes the song after using the pause command - Usage: .resume\n8.stop - stops everything in terms of music - Usage: .stop", color=discord.Color.from_rgb(255, 0, 0))
  await ctx.send(embed = EmbedMsg)

@client.command()
async def credits(ctx):
  EmbedMsg = discord.Embed(title="Credits", desription="Utsarg", color=discord.Color.from_rgb(255, 0, 0))
  await ctx.send(embed = EmbedMsg)

@client.command()
async def date(ctx):
  EmbedMsg = discord.Embed(title="Date", description=f'Date for today:  {today}', color=discord.Color.from_rgb(255, 0, 0))
  await ctx.send(embed = EmbedMsg)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        EmbedMsg = discord.Embed(title="Invalid command", description="The command you have used is invalid!", colour=discord.Color.from_rgb(255, 0, 0))
        EmbedMsg.set_footer(text="do .help for the list of commands")
        await ctx.send(embed = EmbedMsg)
  
@client.event
async def on_message(message):
  await client.process_commands(message)
  if message.author == client.user:
    return
  print(message.channel,message.author,message.content)
  channel = client.get_channel(888867181771784202)
  EmbedMsg = discord.Embed(title="Message", description=f'{message.channel} {message.author} {message.content}', color=discord.Color.from_rgb(255, 0, 0))
  await channel.send(embed = EmbedMsg)

WebSvr()
client.run(os.getenv('TOKEN')) #originally meant to be ran on repl, just makea thing in SEV called TOKEN and make it ur bot token, or you can just do client.run('YOURTOKENHERE')
