import json
import disnake
from disnake.ext import commands

# Json loading
with open('config.json', 'r') as f:
    data = json.load(f)

# Json ChannelsId
with open('channels.json', 'r') as g:
    channel_data = json.load(g)

# Извлекаем массивы из JSON данных
status_channel_ids = channel_data.get("statusChannelId", [])
member_channel_id = channel_data.get("memberChannelId", [])

# Configuring bot
bot = commands.Bot(command_prefix=data["prefix"], help_command=None, intents=disnake.Intents.all())

# --------------------------- Adding channel Ids to Json
@bot.slash_command(name="settings", description="You need to setup your channels with correct id to work with them")
@commands.has_permissions(administrator=True)
async def settings(ctx, *, statusid, memberid):
    await ctx.send(f"Administrator {ctx.author.mention} set ID for **status channel** {statusid}", )
    await ctx.send(f"Administrator {ctx.author.mention} set ID for **user channel** {memberid}")

    # Data saving
    channel_data.update({"statusChannelId": [statusid]})
    channel_data.update({"memberChannelId": memberid})
    json.dump(channel_data, open('channels.json', 'w'))

@bot.event
async def on_ready():
    for channel_id in status_channel_ids:
        channel = bot.get_channel(int(channel_id))
        if channel:
            embed = disnake.Embed(
                title=f"🟢 Now online",
                description=f"Write `/help` to know what I can",
                color=0x03fc03
            )
            await channel.send(embed=embed)
    await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching, name="1.1"))

@bot.event
async def on_disconnect():
    for channel_id in status_channel_ids:
        channel = bot.get_channel(int(channel_id))
        if channel:
            embed = disnake.Embed(
                title=f"🔵 Reconnecting",
                description=f"It may be fixed in some time, please contact tech staff.",
                color=0x4287f5
            )
            await channel.send(embed=embed)

@bot.slash_command(name='shutdown', description='Turn off bot')
@commands.has_permissions(administrator=True, view_audit_log=True)
async def shutdown(ctx: disnake.ApplicationCommandInteraction):
    for channel_id in status_channel_ids:
        channel = bot.get_channel(int(channel_id))
        if channel:
            embed = disnake.Embed(
                title=f"🔴 Now offline",
                description=f"Be sure, update coming.",
                color=0xfc1403
            )
            await channel.send(embed=embed)
    await bot.close()

@bot.event
async def on_member_join(member: disnake.Member):
    channel = bot.get_channel(int(member_channel_id))
    if channel:
        embed = disnake.Embed(
            title=f"New member",
            description=f"{member.name} joined the server\nID: {member.id}",
            color=0x3258a8
        )
        await channel.send(embed=embed)

@bot.event
async def on_member_remove(member: disnake.Member):
    channel = bot.get_channel(int(member_channel_id))
    if channel:
        embed = disnake.Embed(
            title=f"Member left",
            description=f"{member.name} left the server\nID: {member.id}",
            color=0xa83242
        )
        await channel.send(embed=embed)

# Cogs
bot.load_extension("cogs.ping")  # Note: We did not append the .py extension.
bot.load_extension("cogs.tech_help")
bot.load_extension("cogs.error_handling")
bot.load_extension("cogs.kick")
bot.load_extension("cogs.ban")
bot.load_extension("cogs.censore")
bot.load_extension("cogs.voting")
bot.load_extension("cogs.ip")
bot.load_extension("cogs.roles")
bot.load_extension("cogs.message")
bot.load_extension("cogs.calc")

bot.run(data["token"])
