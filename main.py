import json
import os
import disnake
from disnake.ext import commands
from typing import Optional

bot = commands.Bot(command_prefix = commands.when_mentioned, help_command = None, intents = disnake.Intents.all() )

# Json loading
with open('config.json', 'r') as f:
  data = json.load(f)


@bot.event
async def on_ready():
  channel = bot.get_channel(1085514774537830540)
  print(f"{bot.user} is online")

  embed = disnake.Embed (
    title = f"🟢 Now online",
    description = f"Write `/help` to know what I can",
    color = 0x03fc03
  )
  await channel.send(embed = embed)
  await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching, name="for commands"))

@bot.event
async def on_disconnect():
  channel = bot.get_channel(1085514774537830540)
  print(f"{bot.user} disconnected")

  embed = disnake.Embed (
    title=f"🟡 Connection Lost",
    description=f"It may be fixed in some time, please contact tech staff.",
    color=0xfcba03
  )
  await channel.send(embed = embed)

@commands.slash_command(name='shutdown', description='Turn off bot')
@commands.has_permissions(administrator=True, view_audit_log=True)
async def shutdown(ctx: disnake.ApplicationCommandInteraction):
  channel = bot.get_channel(1085514774537830540)
  print(f"{bot.user} is offline")

  embed = disnake.Embed (
    title=f"🔴 Now offline",
      description=f"Be sure, update coming.",
      color=0xfc1403
    )
  await channel.send(embed = embed)
  await commands.close()

# Cogs
bot.load_extension("cogs.ping")  # Note: We did not append the .py extension.
#bot.load_extension("cogs.tech_help")
#bot.load_extension("cogs.error_handling")
bot.load_extension("cogs.kick")
bot.load_extension("cogs.ban")
#bot.load_extension("cogs.censored")


bot.run(data["token"])