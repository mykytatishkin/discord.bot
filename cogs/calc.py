import disnake
from disnake.ext import commands
import socket


class CalcCommand(commands.Cog):
    """This will be for a calc command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name= "calculator",description="Easy calculator")
    async def calc(self, inter: disnake.ApplicationCommandInteraction, tocalc):
        await inter.response.send_message(eval(tocalc))
        


def setup(bot: commands.Bot):
    bot.add_cog(CalcCommand(bot))