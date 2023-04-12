import disnake
from disnake.ext import commands


class RolesCommand(commands.Cog):
    """This will be for a Roles command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    bot = commands.Bot(command_prefix = commands.when_mentioned)
    @commands.slash_command(name="roles", description="if you have some problems, use this command")
    async def roles(inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(
            "Choose your roles",
            components=[
                disnake.ui.Button(label="StarCraft 2", style=disnake.ButtonStyle.link, custom_id="sc_button"),
                disnake.ui.Button(label="League of Legends", style=disnake.ButtonStyle.url, custom_id="lol_button"),    
                disnake.ui.Button(label="Warmode", style=disnake.ButtonStyle.gray, custom_id="warmode_button"),
                disnake.ui.Button(label="Civilization 6", style=disnake.ButtonStyle.secondary, custom_id="civ6_button"),
                disnake.ui.Button(label="CS:GO", style=disnake.ButtonStyle.secondary, custom_id="csgo_button"),    
                
            ]
        )

    bot.listen("on_button_click")
    async def help_listener(inter: disnake.MessageInteraction):
        if inter.component.custom_id not in ["yes_help","no_help"]:
            # We filter out any other button presses except
            # the components we wish to process.
            return
    
        if inter.component.custom_id == "yes_help":
            await inter.response.send_message("Contact <@373151601487118346>")
        elif inter.component.custom_id == "no_help":
            await inter.response.send_message("Ok")

def setup(bot: commands.Bot):
    bot.add_cog(RolesCommand(bot))