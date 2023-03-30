import disnake
from disnake.ext import commands


class VotingCommand(commands.Cog):
    """This will be for a ping command."""
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def votefor(self, inter: disnake.ApplicationCommandInteraction):
       await inter.response.send_message("In development, wait till 1.1")

def setup(bot: commands.Bot):
    bot.add_cog(VotingCommand(bot))