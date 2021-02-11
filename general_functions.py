from timer_func import *

help_text="""
Hello World!
"""

embed_msg = discord.Embed(title="Command Guide", description=help_text, color=0x00ff00)

async def general_version(context):
    myEmbed = discord.Embed(title="Current Version", description='The bot is in Version 1.0' , color=0xff0000)
    myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
    myEmbed.add_field(name="Date Released:", value="December 30th, 2020", inline=False)
    myEmbed.set_footer(text="Created by OsamaBinNaughty & Chrisadilla")
    await context.message.channel.send(embed= myEmbed)

async def submit_idea(context, client, arg1, arg2, arg3, channelID):
    ideaSubmissions_channel=client.get_channel(channelID)
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