import disnake
from disnake.ext import commands

class RolesCommand(commands.Cog):
    """This will be for a Roles command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="roles", description="Choose your roles")
    async def roles(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(
            "Choose your roles",
            components=[
                disnake.ui.Button(label="StarCraft 2", custom_id="sc_button"),
                disnake.ui.Button(label="League of Legends", custom_id="lol_button"),
                disnake.ui.Button(label="Warmode", custom_id="warmode_button"),
                disnake.ui.Button(label="Civilization 6", custom_id="civ6_button"),
                disnake.ui.Button(label="CS:GO", custom_id="csgo_button"),
            ],
        )

    @commands.Cog.listener()
    async def on_button_click(self, inter: disnake.MessageInteraction):
        if inter.custom_id in ["sc_button", "lol_button", "warmode_button", "civ6_button", "csgo_button"]:
            await inter.response.send_message(f"You selected {inter.custom_id} role.")
            # Add your logic for assigning roles here
        else:
            await inter.response.send_message("Invalid button click.")

def setup(bot: commands.Bot):
    bot.add_cog(RolesCommand(bot))
