import disnake
from discord.ui import Select, View
from disnake.ext import commands

# In development
class VotingCommand(commands.Cog):
    """This will be for a ping command."""
    bot = commands.Bot(command_prefix = commands.when_mentioned)

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @bot.event
    async def votefor(self, ctx, inter: disnake.MessageInteraction):
        
        select = Select(
            placeholder="Choose color",
            options = [
            disnake.SelectOption(
                label="Red", description="Your favourite colour is red", emoji="🟥"
            ),
            disnake.SelectOption(
                label="Green", description="Your favourite colour is green", emoji="🟩"
            ),
            disnake.SelectOption(
                label="Blue", description="Your favourite colour is blue", emoji="🟦"
            ),
        ])

        view = View()
        view.add_item(select)
        
        await inter.response.send_message("Choose color: ", view=view)

        

def setup(bot: commands.Bot):
    bot.add_cog(VotingCommand(bot))

