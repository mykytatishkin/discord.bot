# RustCamp Clan Bot
# version: 1.1
# status: pre-realese
#
# Creator: @mykytatishkin
# Helper: @Del37

import json
import os
import disnake
from disnake.ext import commands
from typing import Optional

# Json loading
with open('config.json', 'r') as f:
  data = json.load(f)

with open('channels.json', 'r') as g:
  dataChannels = json.load(g)


bot = commands.Bot(command_prefix = data["prefix"], help_command = None, intents = disnake.Intents.all() )

@bot.slash_command(name="settings", description="You need to setup your channels with correct id to work with them")
@commands.has_permissions(administrator = True)
async def settings(ctx, *, statusid, memberid):
  await ctx.send(f"Administrator {ctx.author.mention} set ID for **status channel** {statusid}", )
  await ctx.send(f"Administrator {ctx.author.mention} set ID bor **user channel** {memberid}")
  
  # Data saving
  dataChannels.update({"statusChannelId":statusid})
  dataChannels.update({"memberChannelId":memberid})
  json.dump(dataChannels, open('channels.json','w'))

@bot.event
async def on_ready():

  idC = dataChannels["statusChannelId"]
  channel = bot.get_channel(int(idC))

  print(f"\n\t{bot.user} now online")


  embed = disnake.Embed (
    title = f"🟢 Now online",
    description = f"Write `/help` to know what I can",
    color = 0x03fc03
  )
  await channel.send(embed = embed)
  await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching, name="1.1"))

@bot.event
async def on_disconnect():
  idC = dataChannels["statusChannelId"]
  channel = bot.get_channel(int(idC))

  print(f"\n\t{bot.user} disconnected")

  embed = disnake.Embed (
    title=f"🔵 Reconnecting",
    description=f"It may be fixed in some time, please contact tech staff.",
    color=0x4287f5
  )
  await channel.send(embed = embed)

@bot.slash_command(name='shutdown', description='Turn off bot')
@commands.has_permissions(administrator=True, view_audit_log=True)
async def shutdown(ctx: disnake.ApplicationCommandInteraction):
  idC = dataChannels["statusChannelId"]
  channel = bot.get_channel(int(idC))
  
  print(f"\n\t{bot.user} is offline")

  embed = disnake.Embed (
    title=f"🔴 Now offline",
      description=f"Be sure, update coming.",
      color=0xfc1403
    )
  await channel.send(embed = embed)
  await bot.close()


@bot.event
async def on_member_join(member: disnake.Member):
  idC = dataChannels["memberChannelId"]
  channel = bot.get_channel(int(idC))

  embed = disnake.Embed (
    title=f"New member",
      description=f"{member.name} joined the server\nID: {member.id}",
      color=0x3258a8
    )

  await channel.send(embed = embed)

@bot.event
async def on_member_remove(member: disnake.Member):
  idC = dataChannels["memberChannelId"]
  channel = bot.get_channel(int(idC))

  embed = disnake.Embed (
    title=f"Member left",
      description=f"{member.name} left the server\nID: {member.id}",
      color=0xa83242
    )

  await channel.send(embed = embed)

# Cogs
bot.load_extension("cogs.ping")  # Note: We did not append the .py extension.
bot.load_extension("cogs.tech_help")
bot.load_extension("cogs.error_handling")
bot.load_extension("cogs.kick")
bot.load_extension("cogs.ban")
bot.load_extension("cogs.censore")
bot.load_extension("cogs.voting")
bot.load_extension("cogs.ip")

bot.run(data["token"])
