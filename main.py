from timer_func import *
from general_functions import *

client = commands.Bot(command_prefix='$')

open('user.json','w').write('{"dummy" : "dummy" }')

# Submit idea
@client.command(name='idea')
async def idea(context, arg1, arg2, arg3=""):
  await submit_idea(context, client, arg1, arg2, arg3, "CHANNEL ID WITHOUT QUOTATION MARK")

# Check version
@client.command(name='version')
async def verion(context):
  await general_version(context)

# Timer function
@client.command(name='timer')
async def pomodoro(context, arg1, arg2=''):
  if(arg1 == 'start' and arg2 != ''): 
    await userCheck(context, client, int(arg2))
    
  elif(arg1 == 'start'):
    await userCheck(context, client, 15)

# Join project command
@client.command(name='Im')
async def join(context):
  print('im in')
  return 0

# Help command
client.remove_command('help')
@client.command('help')
async def help(context):
  await context.message.author.send(embed=embed_msg)

client.run(os.getenv('TOKEN'))  # for heroku 

