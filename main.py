import json
import os
import disnake
from disnake.ext import commands
from typing import Optional

with open('config.json', 'r') as f:
  data = json.load(f)


bot = commands.Bot(command_prefix = commands.when_mentioned, help_command = None, intents = disnake.Intents.all() )


@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    bot.reload_extension(f"cogs.{extension}")

bot.load_extension("cogs.Greetings")

# for filename in os.listdir("cogs"):
#     if filename.endswith(".py"):
#         bot.load_extension(f"cogs.{filename[:-3]}")

CENSORED_WORDS = ["слава россии", "россия вперед", "россия победит", "хохол", "хохляндия", "украине в срало"]

# Create variables for entering ids for channels of functions
# And paste it to bot.get_channel()


# @bot.event
# async def on_member_join(member):
#     role = await disnake.utils.get(guild_id=member.guild.id, role_id=1085515889950068816)
#     channel = bot.get_channel(1030004206528114694) 

#     embed = disnake.Embed(
#         title="New user",
#         description=f"{member.name}#{member.discriminator}",
#         color=0xffffff

#     )

#     await member.add_roles(role)
#     await channel.send(embed=embed)

@bot.event
async def on_message(message):  
    await bot.process_commands(message  )
    
    for content in message.content.split(","):
        for censured_word in CENSORED_WORDS:
            if content.lower() == censured_word:
                await message.delete()
                await message.channel.send(f"{message.author.mention } such repliks is forbidden, Glory to Ukraine!")


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
    channel = bot.get_channel(1085514774537830540)

    print(f"{bot.user} disconnected")
    embed = disnake.Embed (
        title=f"🟡 Connection Lost",
        description=f"It may be fixed in some time, please contact tech staff.",
        color=0xfcba03
    )

    await channel.send(embed = embed)

@bot.event
async def on_shutdown():
    print(f"{bot.user} shutting down...")

@bot.slash_command(name='shutdown', description='Turn off bot')
@commands.has_permissions(administrator=True, view_audit_log=True)
async def shutdown(ctx: disnake.ApplicationCommandInteraction):
    channel = bot.get_channel(1085514774537830540)
    embed = disnake.Embed (
        title=f"🔴 Now offline",
        description=f"Be sure, update coming.",
        color=0xfc1403
    )
    await channel.send(embed = embed)
    await bot.close()

#   Create resonse to dm message
#   With sending information
#   And create setting for custom messages

@bot.slash_command(name="tech_help", description="if you have some problems, use this command")
async def tech_help(inter: disnake.ApplicationCommandInteraction):
    await inter.response.send_message(
        "Need some help?",
        components=[
            disnake.ui.Button(label="Yes", style=disnake.ButtonStyle.success, custom_id="yes_help"),
            disnake.ui.Button(label="No", style=disnake.ButtonStyle.danger, custom_id="no_help"),    
        ]
    )

@bot.listen("on_button_click")
async def help_listener(inter: disnake.MessageInteraction):
    if inter.component.custom_id not in ["yes_help","no_help"]:
        # We filter out any other button presses except
        # the components we wish to process.
        return
    
    if inter.component.custom_id == "yes_help":
        await inter.response.send_message("Contact us at https://discord.gg/jZPSbdHpNk")
    elif inter.component.custom_id == "no_help":
        await inter.response.send_message("Ok")

# DROPDOWN MENU

bot.run(data["token"])