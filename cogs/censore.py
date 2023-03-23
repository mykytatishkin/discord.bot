import disnake
from disnake.ext import commands


class CensoreCommand(commands.Cog):
    """This will be for a ping command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    
    @commands.event
    async def on_message(message):  
        CENSORED_WORDS = ["слава россии", "россия вперед", "россия победит", "хохол", "хохляндия", "украине в срало"]
        await commands.process_commands(message)
    
        for content in message.content.split(","):
            for censured_word in CENSORED_WORDS:
                if content.lower() == censured_word:
                    await message.delete()
                    await message.channel.send(f"{message.author.mention } such repliks is forbidden, Glory to Ukraine!")



def setup(bot: commands.Bot):
    bot.add_cog(CensoreCommand(bot))