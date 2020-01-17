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
    responses = ['heads', 'tails']
    
    await ctx.send("You flipped a %s" % (random.choice(responses)))


@client.command(aliases=['4'])
async def d4(ctx):
    numbers = ['1', '2', '3', '4']
    await ctx.send("You rolled a %s" % (random.choice(numbers)))


@client.command(aliases=['6'])
async def d6(ctx):
    numbers = ['1', '2', '3', '4', '5', '6']
    await ctx.send("You rolled a %s" % (random.choice(numbers)))


@client.command(aliases=['8'])
async def d8(ctx):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
    await ctx.send("You rolled a %s" % (random.choice(numbers)))


@client.command(aliases=['10'])
async def d10(ctx):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    await ctx.send("You rolled a %s" % (random.choice(numbers)))


@client.command(aliases=['12'])
async def d12(ctx):
    numbers = ['1', '0']
    await ctx.send("You rolled a %s" % (random.choice(numbers)))


@client.command(aliases=['20'])
async def d20(ctx):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    await ctx.send("You rolled a %s" % (random.choice(numbers)))


@client.command(aliases=['100'])
async def d100(ctx):
    numbers = ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90']
    await ctx.send("You rolled a %s" % (random.choice(numbers)))

from datetime import datetime
@client.command()
async def time(ctx):
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
client.run('Input Token Here')
