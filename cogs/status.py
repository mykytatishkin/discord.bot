import disnake
from disnake.ext import commands


class StatusBot(commands.Cog):
    """This will be for a ping command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    bot = commands.Bot(command_prefix = commands.when_mentioned)
    @bot.event
    async def on_ready():
        bot = commands.Bot(command_prefix = commands.when_mentioned)
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
        bot = commands.Bot(command_prefix = commands.when_mentioned)
        channel = bot.get_channel(1085514774537830540)
        print(f"{bot.user} disconnected")

        embed = disnake.Embed (
        title=f"🟡 Connection Lost",
        description=f"It may be fixed in some time, please contact tech staff.",
        color=0xfcba03
        )
        await channel.send(embed = embed)

    @bot.slash_command(name='shutdown', description='Turn off bot')
    @commands.has_permissions(administrator=True, view_audit_log=True)
    async def shutdown(ctx: disnake.ApplicationCommandInteraction):
        bot = commands.Bot(command_prefix = commands.when_mentioned)
        channel = bot.get_channel(1085514774537830540)
        print(f"{bot.user} is offline")

        embed = disnake.Embed (
            title=f"🔴 Now offline",
            description=f"Be sure, update coming.",
            color=0xfc1403
        )
        await channel.send(embed = embed)
        await bot.close()

def setup(bot: commands.Bot):
    bot.add_cog(StatusBot(bot))