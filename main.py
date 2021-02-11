
from timer_func import *
from general_functions import *

client = commands.Bot(command_prefix='$')

open('user.json','w').write('{"dummy" : "dummy" }')

@client.command(name='idea')
async def idea(context, arg1, arg2, arg3=""):
  await submit_idea(context, client, arg1, arg2, arg3, 785290698710056990)

@client.command(name='version')
async def verion(context):
  await general_version(context)

@client.command(name='timer')
async def pomodoro(context, arg1, arg2=''):
  if(arg1 == 'start' and arg2 != ''): 
    await userCheck(context, client, int(arg2))
    
  elif(arg1 == 'start'):
    await userCheck(context, client, 15)

# client.run(os.getenv('TOKEN'))  # for heroku only
client.run("TOKEN")
