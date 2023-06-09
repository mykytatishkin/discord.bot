import disnake
from disnake.ext import commands

# In testing
class TechHelpCommand(commands.Cog):
    """This will be for a Tech_Help command."""
    bot = commands.Bot(command_prefix = commands.when_mentioned)

    def __init__(self, bot: commands.Bot):
        self.bot = bot
   
    @commands.slash_command(name="tech_help", description="if you have some problems, use this command")
    async def tech_help(inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(
            "Need some help?",
            components=[
                disnake.ui.Button(label="Yes", style=disnake.ButtonStyle.success, custom_id="yes_help"),
                disnake.ui.Button(label="No", style=disnake.ButtonStyle.danger, custom_id="no_help"),    
            ]
        )

    bot.listen("on_button_click")
    async def help_listener(inter: disnake.MessageInteraction):
        if inter.component.custom_id not in ["yes_help","no_help"]:
            # We filter out any other button presses except
            # the components we wish to process.
            return
    
        if inter.component.custom_id == "yes_help":
            print("Someone needs help")
            await inter.response.send_message("Contact <@373151601487118346>")
        elif inter.component.custom_id == "no_help":
            print("Someone doesnt need help")
            await inter.response.send_message("Ok")

def setup(bot: commands.Bot):
    bot.add_cog(TechHelpCommand(bot))