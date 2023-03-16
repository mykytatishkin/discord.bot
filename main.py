import disnake
from disnake.ext import commands
import json

with open('config.json', 'r') as f:
  data = json.load(f)

bot = commands.Bot(command_prefix = data["prefix"], help_command = None, intents = disnake.Intents.all() )
CENSORED_WORDS = ["слава россии", "россия вперед", "россия победит", "хохол", "хохляндия", "украине в срало"]

# Create variable for entering id for channel of turning on Bot
# And paste it to bot.get_channel(id)

@bot.event 
async def on_ready():
    print(f"{bot.user} ready to work")
    channel = bot.get_channel(1085514774537830540)


    embed = disnake.Embed (
        title = f"🟢 Now online",
        description = f"Write `/help` to know what I can",
        color = 0x03fc03
    )
    await channel.send(embed = embed)
    await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching, name="for commands"))

# Create variables for entering ids for channels of functions
# And paste it to bot.get_channel()


@bot.event
async def on_member_join(member):
    role = await disnake.utils.get(guild_id=member.guild.id, role_id=1085515889950068816)
    channel = bot.get_channel(1030004206528114694) 

    embed = disnake.Embed(
        title="New user",
        description=f"{member.name}#{member.discriminator}",
        color=0xffffff

    )

    await member.add_roles(role)
    await channel.send(embed=embed)

@bot.event
async def on_message(message):  
    await bot.process_commands(message  )
    
    for content in message.content.split(","):
        for censured_word in CENSORED_WORDS:
            if content.lower() == censured_word:
                await message.delete()
                await message.channel.send(f"{message.author.mention } such repliks is forbidden, Glory to Ukraine!")

@bot.slash_command(description="If someone will break some rules or will try to crash server, he will get kick", usage="/kick <@user> reason=None")
@commands.has_permissions(kick_members = True, administrator = True)
async def kick(ctx, member: disnake.Member, *, reason="Rules broker"):
    await ctx.send(f"Moderator {ctx.author.mention} kicked user {member.mention}", delete_after=300)
    await member.kick(reason = reason)
    await ctx.message.delete()

@bot.slash_command(aliases="БАН НАХУЙ", description="If someone will break some rules or will try to crash server, he will get ban", usage="/ban <@user> reason=None")
@commands.has_permissions(ban_members = True, administrator = True)
async def ban(ctx, member: disnake.Member, *, reason="Rules broker"):
    await ctx.send(f"Moderator {ctx.author.mention} baned user {member.mention}", delete_after=300)
    await member.ban(reason = reason)
    await ctx.message.delete()

@bot.event
async def on_command_error(ctx, error):
    print(error)

    if isinstance (error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author} you don`t have such permission")
    elif isinstance (error, commands.UserInputError):
        await ctx.send(embed=disnake.Embed(
            description=f"Correct usage of command: `{ctx.prefix}{ctx.command.name}`({ctx.command.brief})\nExample: {ctx.prefix}{ctx.command.usage}"

        ))

@bot.event
async def on_disconnect():
    print(f"{bot.user} disconnected")

@bot.event
async def on_shutdown():
    print(f"{bot.user} shutting down...")

@bot.slash_command(name='shutdown', description='Turn off bot')
@commands.has_permissions(administrator=True, view_audit_log=True)
async def shutdown(ctx: disnake.ApplicationCommandInteraction):
    channel = bot.get_channel(1085514774537830540)
    embed = disnake.Embed (
        title=f"🔴 Now offline",
        description=f"Contact tech help to know a reason",
        color=0xfc1403
    )
    await channel.send(embed = embed)
    await bot.close()

bot.run(data["token"])