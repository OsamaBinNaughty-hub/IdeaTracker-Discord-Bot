import discord, os, random
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

# Bot prints embedded message from any user's input, will return to original input user's name if arg3 is not mentioned
@bot.command(name='idea')
async def isb(ctx, arg1, arg2, arg3 = ''):
  channel = bot.get_channel("CHANNEL ID IN INT")
  name = ctx.author if(arg3 == '') else arg3
  myEmbed = discord.Embed(title=arg1, description=arg2, color=0x00ff00)
  myEmbed.set_author(name=name)
  await channel.send(embed=myEmbed)
  await ctx.message.author.send(f'Your **{arg1}** idea has been added!')

# Bot prints version numbers and creators
@bot.command(name='version')
async def idea(ctx):
  myEmbed = discord.Embed(title="Current Version", description='The bot is in Version 1.0' , color=0xff0000)
  myEmbed.add_field(name="Version Code:", value="v1.0.1", inline=False)
  myEmbed.add_field(name="Date Released:", value="December 30th, 2020", inline=False)
  myEmbed.set_footer(text="Created by OsamaBinNaughty & Chrisadilla")
  await ctx.message.channel.send(embed= myEmbed)

# Bot returns "mentioned-user you're in!" with a gif
@bot.command(name="im") 
async def im_in(ctx, argIn):
  channel = bot.get_channel("CHANNEL ID IN INT")
  if(argIn == 'in'):
    await channel.send(f"<@{ctx.author.id}> you're in!")
    await channel.send(f"{random.choice(open(os.getcwd()+'/gif_links.txt','r').readlines())}")

# Initial state of the bot, will say "Beep beep boob, I am alive!"
@bot.event
async def on_ready(): 
  print('We have logged in as {0.user}'
  .format(bot))
  botTest_channel=bot.get_channel("CHANNEL ID IN INT")
  await botTest_channel.send('Beep beep boob, I am alive!')
  await bot.change_presence(status=discord.Status.online, activity='Brainstorming')
  
# start here for debugging                       
client.remove_command("help")

@client.group(invoke_without_command=True)
async def help(ctx):
  em = discord.Embed(title="Help", description = "Use $help <command> for extended information on a command.", color = ctx.author.color)

  em.add_field(name = "Flutter Sprints", value="`idea`")
  em.add_field(name= "Bot", value="``version`")

  await ctx.send(embed=em)

@help.command()
async def idea(ctx):
  em = discord.Embed(title="Idea", description = "Adds an idea to the #idea-submissions channel", color = ctx.author.color)
  em.add_field(name= "**Syntax**", description = "$idea \"idea name\" \"idea description\" ")

  await ctx.send(embed = em)
   
@help.command()
async def version(ctx):
  em = discord.Embed(title="Version", description = "Shows info about the bot", color = ctx.author.color)
  em.add_field(name= "**Syntax**", description = "$version")

  await ctx.send(embed = em)
                      

bot.run('YOUR-TOKEN')

