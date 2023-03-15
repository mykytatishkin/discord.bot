import disnake
from disnake.ext import commands
import json

with open('config.json', 'r') as f:
  data = json.load(f)

bot = commands.Bot(command_prefix = ".", help_command = None, intents = disnake.Intents.all() )
CENSORED_WORDS = ["слава россии", "россия вперед", "россия победит", "хохол", "хохляндия", "украине в срало"]

@bot.event 
async def on_ready():
    print(f"{bot.user} ready to work")
    channel = bot.get_channel(1085514774537830540)


    embed = disnake.Embed (
        title = f"<:disnake:1085542833848594523> Bot in development",
        description = f"Will be in furute...",
        color = 0xffe32e
    )
    await channel.send(embed = embed)

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

@bot.slash_command()
@commands.has_permissions(kick_members = True, administrator = True)
async def kick(ctx, member: disnake.Member, *, reason="Rules broker"):
    await ctx.send(f"Moderator {ctx.author.mention} kicked user {member.mention}", delete_after=300)
    await member.kick(reason = reason)
    await ctx.message.delete()

bot.run(data["token"])