import json, asyncio, datetime as dt, discord, os, re
from discord.ext import commands
#----------- async defs -----------#

# Perform a user check to prevent double timer set. If no existing user, continue to "async def timer"
async def userCheck(context, client, period):
    if(json.loads(open('user.json' , 'r').read()).get(str(context.message.author.id)) != None): 
        await sender(context, "Only one timer is allowed. Stop & reset if necessary.")  
    else:
        await sender(context, f"{period} minutes set! Focus on your element bend!" if(period != 15) else "No time set, default timer is 15 minutes! Focus on your element bend!") 
        await timer(context, client,  period) 

# Does the countdown work as well as remove user once "stop" command is used, or "done" command when time is up.
async def timer(context, client, period):
    try:
        temp_data = json.loads(open('user.json' , 'r').read())
        temp_data.update(json.loads(assigner(context.message.author.id)))
        open('user.json', 'w').write(json.dumps(temp_data))
        def stop(m): return m.content == '$stop' and m.author.id == context.message.author.id
        await waiter(client, period * 60, stop)
        await sender(context, "Timer is stopped and reset.")
        removeID(context.message.author.id) 

    except asyncio.TimeoutError:
        while(True):
            try: 
                await sender(context, 'Times Up!!!')
                def done(m): return m.content == '$done' and m.author.id == context.message.author.id
                await waiter(client, 5, done)
                await sender(context, 'Looks like you\'ve completed your training! Go reward yourself a nice warm tea.')
                removeID(context.message.author.id)
                break
            except asyncio.TimeoutError:
                pass

#----------- normal defs -----------#

def assigner(id):
    return json.dumps( { id : str(dt.datetime.now())} )

def sender(context, string):
    return context.message.author.send(string)

def waiter(client, timeout, check):
    return client.wait_for('message', timeout=timeout, check=check)

def removeID(id):
    try:
        temp_data = json.loads(open('user.json' , 'r').read())
        temp_data.pop(str(id))
        open('user.json', 'w').write(json.dumps(temp_data))
    except:
        pass