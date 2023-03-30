import disnake
from disnake.ext import commands
import socket


class IpCommand(commands.Cog):
    """This will be for a ping command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(description="Shows your ip :>")
    async def ip(self, inter: disnake.ApplicationCommandInteraction):
         hostname = socket.gethostname()
         IPAddr = socket.gethostbyname(hostname)
         print(f"User use command, his IP: {IPAddr}")
         await inter.response.send_message(IPAddr)
        


def setup(bot: commands.Bot):
    bot.add_cog(IpCommand(bot))