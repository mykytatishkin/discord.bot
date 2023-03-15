import discord
from discord.ext import commands

fila = open('config.json')
config = json.load(file)

bot = commands.Bot(config['prefix'])

@bot.commands(name = 'ping')

async def ping(ctx):
    await ctx.send(f'{ctx.author.mention}pong')

bot.run(config['token'])
