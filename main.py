import discord
import os
from discord.ext import commands
import re

bot = commands.Bot(command_prefix='$')

 # Bot prints embedded message from any user's input, will return to original input user's name if arg3 is not mentioned
@bot.command(name='idea')
async def isb(ctx, arg1, arg2, arg3 = ''):
  channel = bot.get_channel('Channel ID integer')
  name = ctx.author if(arg3 is '') else arg3
  myEmbed = discord.Embed(title=arg1, description=arg2, color=0x00ff00)
  myEmbed.set_author(name=name)
  await channel.send(embed=myEmbed)
  await ctx.message.author.send(f'Your **{arg1}** idea has been added!')

@bot.command(name='version')  # Bot prints version numbers and creators
async def idea(ctx):
  myEmbed = discord.Embed(title="Current Version", description='The bot is in Version 1.0' , color=0xff0000)
  myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
  myEmbed.add_field(name="Date Released:", value="December 30th, 2020", inline=False)
  myEmbed.set_footer(text="Created by OsamaBinNaughty & Chrisadilla")
  await ctx.message.channel.send(embed= myEmbed)

@bot.event
async def on_ready(): # Initial state of the bot, will say "Beep beep boob, I am alive!"
  print('We have logged in as {0.user}'
  .format(bot))
  botTest_channel=bot.get_channel(785290698710056990)
  await botTest_channel.send('Beep beep boob, I am alive!')
  await bot.change_presence(status=discord.Status.online, activity='Brainstorming')

# @bot.event
# async def on_message(message):
#   botTest_channel=bot.get_channel(785290698710056990)
#   if message.author == bot.user:
#     return

#   await bot.process_commands(message)
  

bot.run('TOKEN')
