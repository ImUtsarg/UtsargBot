#more old and shitty code, remove the role check or change it if u want

import discord
from discord.ext import commands

class annoyCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.has_any_role('⁂ Server Manager', 'only dev', 'Staff')
  async def annoyp(self, ctx, ammount : int, user : discord.Member, *, msg):
    await ctx.send(f'Attemting to annoy {user}')
    for x in range(ammount):
      await user.send(f'{msg}')
    await ctx.send(f'Annoyed {user}')

def setup(client):
  client.add_cog(annoyCog(client))
