import discord
import random
from discord.ext import commands
#from utils import get_emoji
#from random import randint
from utils import get_channel
from datetime import datetime
client = commands.Bot(command_prefix='!')
#from dictionary import Dictionary
from bot import patches
from bot.bot import Bot
from bot.constants import Bot as BotConfig, DEBUG_MODE


bot = Bot(
    command_prefix=when_mentioned_or(BotConfig.prefix),
    activity=discord.Game(name="Commands: !help"),
    case_insensitive=True,
    max_messages=10_000,
)

# Internal/debug
bot.load_extension("bot.cogs.error_handler")
bot.load_extension("bot.cogs.filtering")
bot.load_extension("bot.cogs.logging")
bot.load_extension("bot.cogs.security")

# Commands, etc
bot.load_extension("bot.cogs.antimalware")
bot.load_extension("bot.cogs.antispam")
bot.load_extension("bot.cogs.bot")
bot.load_extension("bot.cogs.clean")
bot.load_extension("bot.cogs.extensions")
bot.load_extension("bot.cogs.help")

# Only load this in production
if not DEBUG_MODE:
    bot.load_extension("bot.cogs.doc")
    bot.load_extension("bot.cogs.verification")

# Feature cogs
bot.load_extension("bot.cogs.alias")
bot.load_extension("bot.cogs.defcon")
bot.load_extension("bot.cogs.eval")
bot.load_extension("bot.cogs.duck_pond")
bot.load_extension("bot.cogs.free")
bot.load_extension("bot.cogs.information")
bot.load_extension("bot.cogs.jams")
bot.load_extension("bot.cogs.metrics")
bot.load_extension("bot.cogs.moderation")
bot.load_extension("bot.cogs.off_topic_names")
bot.load_extension("bot.cogs.reddit")
bot.load_extension("bot.cogs.reminders")
bot.load_extension("bot.cogs.site")
bot.load_extension("bot.cogs.snekbox")
bot.load_extension("bot.cogs.sync")
bot.load_extension("bot.cogs.tags")
bot.load_extension("bot.cogs.token_remover")
bot.load_extension("bot.cogs.utils")
bot.load_extension("bot.cogs.watchchannels")
bot.load_extension("bot.cogs.wolfram")

# Apply `message_edited_at` patch if discord.py did not yet release a bug fix.
if not hasattr(discord.message.Message, '_handle_edited_timestamp'):
    patches.message_edited_at.apply_patch()

bot.run(BotConfig.token)
#Events
@client.event
async def on_ready():
    print('Hi!')

@client.event
async def run(self, client):
  now = datetime.now()
  if now.hour == 8 and now.minute == 30:
    msg = "It's school time!"
  elif now.hour == 9 and now.minute == 40 :
    msg = "It's period two!"
  elif now.hour == 10 and now.minute == 56:
    msg = "It's time for lunch!"
  elif now.hour == 12 and now.minute == 15:
    msg = "It's high noon!(period 3)"
  elif now.hour == 13 and now.minute == 27:
    msg = "It's past high noon!(period 4)"
  elif now.hour == 15:
    msg = "It's home time"
  else:
    msg = f"It is {now.hour}:{now.minute}"
  channel = get_channel(client, "general")
  await client.send_message(channel, msg)

@client.event
async def on_member_join(member):
  print(f'{member} has joined the server')

@client.event
async def on_member_remove(member):
  print(f'{member} has left the server')

#Commands
@client.command(aliases = ['Ping' , 'Latancy', 'latancy'])
async def ping(ctx):
  await ctx.send(f'ping: {round(client.latency * 1000)} ms')

'''
@client.command(aliases = ['definebros' , 'whatDoes'])
async def _(word):
  wordDefine = Dictionary(word)
  print (wordDefine)
  return
'''


#dice roller attempt 2 

@client.command(aliases = ['coin', 'coinFlip', '2'])
async def d2(ctx, *, values):
  numbers = ['heads','tails']
  await ctx.send(f'Dice: {values}\nAnswer: {random.choice(numbers)}')


@client.command(aliases = ['4'])
async def d4(ctx, *, values):
  numbers = ['1','2','3','4']
  await ctx.send(f'Dice: {values}\nAnswer: {random.choice(numbers)}')

@client.command(aliases = ['6'])
async def d6(ctx, *, values):
  numbers = ['1','2','3','4','5','6']
  await ctx.send(f'Dice: {values}\nAnswer: {random.choice(numbers)}')

@client.command(aliases = ['8'])
async def d8(ctx, *, values):
  numbers = ['1','2','3','4','5','6','7','8']
  await ctx.send(f'Dice: {values}\nAnswer: {random.choice(numbers)}')

@client.command(aliases = ['10'])
async def d10(ctx, *, values):
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    await ctx.send(f'Dice: {values}\nAnswer: {random.choice(numbers)}')

@client.command(aliases = ['12'])
async def d12(ctx, *, values):
  numbers = ['1','0']
  await ctx.send(f'Dice: {values}\nAnswer: {random.choice(numbers)}')
'''
@client.command(aliases = ['20'])
async def d20(ctx, *, values):
  numbers = ['1','2','3','4','5','6','7','8','9','10','11','12']
  await ctx.send(f'Dice: {values}\nAnswer: {random.choice(numbers)}')
'''
@client.command(aliases = ['100'])
async def d100(ctx, *, values):
  numbers = ['0','10','20','30','40','50','60','70','80','90']
  await ctx.send(f'Dice: {values}\nAnswer: {random.choice(numbers)}')

@client.command(aliases = ['20'])
async def d20(message, client):
  try:
    lower_bound = int([1])
    upper_bound = int([20])
  except ValueError:
    await client.send_message(message.channel, "Please, provide valid numbers")
    return

#Discord Importer
#client.run('NjYzNzM3Mzc3ODA1NTY1OTUy.XiDz0Q.VVbnJNQyQA2XXQu1tWWkbDnnr2Y')
bot.run(BotConfig.token)