import discord
import os
from discord.ext import commands
import re
from dotenv import load_dotenv

load_dotenv()

client = commands.Bot(command_prefix='$')

@client.command(name='idea')
async def idea(context, arg1, arg2, arg3=""):
  ideaSubmissions_channel=client.get_channel(793898817061126225)
  emoji="\N{THUMBS UP SIGN}"
  name = ""
  if arg3=="":
    name = '{}'.format(context.author)
  else:
    name=arg3 
    
  myEmbed = discord.Embed(title=arg1, description=arg2, color=0x00ff00)
  myEmbed.set_author(name=name)
  await context.message.author.send('Your **{}** idea has been added!'.format(arg1))
  message = await ideaSubmissions_channel.send(embed=myEmbed)

  

  await message.add_reaction(emoji = "\U0001F44D")

@client.command(name='version')
async def idea(context):
  myEmbed = discord.Embed(title="Current Version", description='The bot is in Version 1.0' , color=0xff0000)
  myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
  myEmbed.add_field(name="Date Released:", value="December 30th, 2020", inline=False)
  myEmbed.set_footer(text="Created by OsamaBinNaughty & Chrisadilla")

  await context.message.channel.send(embed= myEmbed)


@client.event
async def on_ready():
  print('We have logged in as {0.user}'
  .format(client))
  botTest_channel=client.get_channel(793898817061126225)
  await botTest_channel.send('Beep beep boob, I am alive!')

  await client.change_presence(status=discord.Status.online, activity='Brainstorming')

@client.event
async def on_message(message):
  botTest_channel=client.get_channel(793898817061126225)
  if message.author == client.user:
    return

  await client.process_commands(message)
   

client.run(os.getenv('TOKEN'))
