import discord
from discord.colour import Color
from discord.ext import commands
from random import randint

gifs = [
'https://media.giphy.com/media/gk3R16JhLP8RUka2nD/giphy.gif',
'https://media.giphy.com/media/iKBAAfYNDu1dowhnEj/giphy.gif',
'https://media.giphy.com/media/mGDvFv4tWxzZcw4Bn6/giphy.gif',
'https://media.giphy.com/media/RMcT76sMWIGLxpiyjx/giphy.gif',
'https://media.giphy.com/media/z964EmS0VNVdUv9jyW/giphy.gif',
'https://media.giphy.com/media/65FuAnjw896Hhy3qiF/giphy.gif',
'https://media.giphy.com/media/CjmvTCZf2U3p09Cn0h/giphy.gif',
'https://media.giphy.com/media/YSSpYE1Um2bpcK5T9h/giphy.gif',
'https://media.giphy.com/media/dBGi39HzazuTV21S15/giphy.gif',
'https://media.giphy.com/media/3o72F03RnbPTvKtR7y/giphy.gif',
'https://media.giphy.com/media/3o85xIapRKSRgdiSaY/giphy.gif',
'https://media.giphy.com/media/hT6wgEtwoUt0no87gV/giphy.gif',
'https://media.giphy.com/media/8YHmc8luwmJJjFY7zh/giphy.gif',
'https://media.giphy.com/media/3oz8xxR3P26nCtYpYA/giphy.gif',
'https://media.giphy.com/media/mEnciyhXNQARSfnGCb/giphy.gif',
'https://media.giphy.com/media/YP2HqPBbtQVSU2DFKt/giphy.gif',
'https://media.giphy.com/media/I7piX5ah7h8XkS41sP/giphy.gif',
'https://media.giphy.com/media/9MImaFGs8o95msW9gc/giphy.gif',
'https://media.giphy.com/media/3kElxXbKHtKhkME8tG/giphy.gif',
'https://media.giphy.com/media/3oz8xUBD4CZm90iZYQ/giphy.gif',
'https://media.giphy.com/media/EOdCKQ3xV0WDONIJ07/giphy.gif',
]


bot = commands.Bot(command_prefix='$')

channelId = 785290698710056990

@bot.command(name='Im')
async def imIn(ctx, arg1):
  if arg1 == 'in':
    channel = bot.get_channel(channelId)
    randomGif = gifs[randint(0,len(gifs)-1)]
    await channel.send("<@{}> is in!".format(ctx.author.id)) 
    await channel.send(randomGif)

@bot.command(name='im')
async def imIn(ctx, arg1):
  if arg1 == 'in':
    channel = bot.get_channel(channelId)
    randomGif = gifs[randint(0,len(gifs)-1)]
    await channel.send("<@{}> is in!".format(ctx.author.id)) 
    await channel.send(randomGif)

@bot.command(name='imin')
async def imIn(ctx):
    channel = bot.get_channel(channelId)
    randomGif = gifs[randint(0,len(gifs)-1)]
    await channel.send("<@{}> is in!".format(ctx.author.id)) 
    await channel.send(randomGif)

@bot.command(name='Imin')
async def imIn(ctx):
    channel = bot.get_channel(channelId)
    randomGif = gifs[randint(0,len(gifs)-1)]
    await channel.send("<@{}> is in!".format(ctx.author.id)) 
    await channel.send(randomGif)

@bot.event
async def on_ready(): # Initial state of the bot, will say "Beep beep boob, I am alive!"
  print('We have logged in as {0.user}'
  .format(bot))
  botTest_channel=bot.get_channel(channelId)
  await botTest_channel.send('Who\'s in?')
  await bot.change_presence(status=discord.Status.online)

bot.run('TOKEN')
