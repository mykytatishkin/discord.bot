from discord import BotIntegration
import disnake
from disnake.ext import commands


class CensoreCommand(commands.Cog):
    """This will be for a censore listener."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    bot = commands.Bot(command_prefix = commands.when_mentioned)
    @bot.event
    async def on_message(message):  
        bot = commands.Bot(command_prefix = commands.when_mentioned)
        CENSORED_WORDS = ["слава россии", "россия вперед", "россия победит", "хохол", "хохляндия", "украине в срало"]
        await bot.process_commands(message  )

        for content in message.content.split(","):
            for censured_word in CENSORED_WORDS:
                if content.lower() == censured_word:
                    await message.delete()
                    await message.channel.send(f"{message.author.mention } such repliks is forbidden, Glory to Ukraine!")



def setup(bot: commands.Bot):
    bot.add_cog(CensoreCommand(bot))