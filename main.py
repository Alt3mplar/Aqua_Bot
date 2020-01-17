import discord
import random
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
client = commands.Bot(command_prefix='!')


# Events
@client.event
async def on_ready():
    
    print('Hi!')


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')


# Commands
@client.command(aliases=['Ping', 'Latancy', 'latancy'])
async def ping(ctx):
    await ctx.send(f'ping: {round(client.latency * 1000)} ms')

@client.command()
async def function(ctx,arg):
  await ctx.send(arg)

def findDefinition(word):
    '''
    Locates the definitions of a word from the dictionary
    Specifically uses https://www.merriam-webster.com/dictionary and will provide a brief description or link the user to related words that have the same general definition

    Parameters
    ----------
    url : str
        the URL to the dictionary
    word : str
        the word that is being defined
    page
        allows for imported program (beautifulsoup) to access the website
    text : 
        locates the definition from the source code
    soup
        calls imported program
    title : str
        the definition of the word given
  
    Returns
    -------
    str
        the definition of the word that was defined
    '''
    url = "https://www.merriam-webster.com/dictionary/%s" % (word)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = soup.findAll('meta')

    title = soup.find("meta",  property="og:description")
    url = soup.find("meta",  property="og:url")
    
    return title["content"]

@client.command()
async def define(ctx,arg):
    await ctx.send(findDefinition(arg))

@client.command(aliases=['coin', 'coinFlip', '2'])
async def d2(ctx):
    '''
    flips a coin 

    Parameters
    ----------
    responses : list
        provides the possibilities for the coin
  
    Returns
    -------
    str
        the side of the coin, heads or tails
    '''
    responses = ['heads', 'tails']
    
    await ctx.send("You flipped a %s" % (random.choice(responses)))


@client.command(aliases=['4'])
async def d4(ctx):
    '''
    Rolls a 4 sided die

    Parameters
    ----------
    numbers : list
        provides the possibilities for the sides
  
    Returns
    -------
    str
        number rolled when randomized
    '''
    numbers = ['1', '2', '3', '4']
    await ctx.send("You rolled a %s" % (random.choice(numbers)))


@client.command(aliases=['6'])
async def d6(ctx):
    '''
    Rolls a 6 sided die

    Parameters
    ----------
    numbers : list
        provides the possibilities for the sides
  
    Returns
    -------
    str
        number rolled when randomized
    '''
    numbers = ['1', '2', '3', '4', '5', '6']
    await ctx.send("You rolled a %s" % (random.choice(numbers)))


@client.command(aliases=['8'])
async def d8(ctx):
    '''
    Rolls a 8 sided die

    Parameters
    ----------
    numbers : list
        provides the possibilities for the sides
  
    Returns
    -------
    str
        number rolled when randomized
    '''    
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
    await ctx.send("You rolled a %s" % (random.choice(numbers)))


@client.command(aliases=['10'])
async def d10(ctx):
    '''
    Rolls a 10 sided die

    Parameters
    ----------
    numbers : list
        provides the possibilities for the sides
  
    Returns
    -------
    str
        number rolled when randomized
    '''    
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    await ctx.send("You rolled a %s" % (random.choice(numbers)))


@client.command(aliases=['12'])
async def d12(ctx):
    '''
    Rolls a 12 sided die

    Parameters
    ----------
    numbers : list
        provides the possibilities for the sides
  
    Returns
    -------
    str
        number rolled when randomized
    '''
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    await ctx.send("You rolled a %s" % (random.choice(numbers)))


@client.command(aliases=['20'])
async def d20(ctx):
    '''
    Rolls a 20 sided die

    Parameters
    ----------
    numbers : list
        provides the possibilities for the sides
  
    Returns
    -------
    str
        number rolled when randomized
    '''
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12','13','14','15','16','17','18','19','20']
    await ctx.send("You rolled a %s" % (random.choice(numbers)))


@client.command(aliases=['100'])
async def d100(ctx):
    '''
    Rolls a 10 sided die with a *10 multiplier to the values 

    Parameters
    ----------
    numbers : list
        provides the possibilities for the sides
  
    Returns
    -------
    str
        number rolled when randomized
    '''
    numbers = ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90']
    await ctx.send("You rolled a %s" % (random.choice(numbers)))

from datetime import datetime
@client.command()
async def time(ctx):
        '''
    alerts the users of the time 
    Has alarms for specific times: based on school day @ John Fraser

    Parameters
    ----------
    now
        current time
    hour : int
        current hour based on datetime import
    minute : int
         current minute based on datetime import
    msg : str
         return value dependant on time
    Returns
    -------
    str
        current time after midnight (24 hour clock)
    '''
        now = datetime.now()
        if now.hour == 8 and now.minute == 30:
            msg = "It's school time!"
        elif now.hour == 9 and now.minute == 40 :
            msg = "It's period two!"
        elif now.hour == 10 and now.minute == 56:
            msg = "It's time for lunch!"
        if now.hour == 12 and now.minute == 15:
            msg = "It's high noon!(period 3)"

        elif now.hour == 13 and now.minute == 27:
            msg = "It's past high noon!(period 4)"
        elif now.hour == 15:
            msg = "It's home time"
        else:
            msg = f"It is {now.hour} hours and {now.minute} minutes past midnight."

        await ctx.send(msg)

# Discord Importer
client.run('Input Your Token Here')
