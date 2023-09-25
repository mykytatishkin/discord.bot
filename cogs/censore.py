import re
from disnake.ext import commands


class CensoreCommand(commands.Cog):
    """This will be for a censor listener."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        CENSORED_WORDS = ["слава россии", "россия вперед", "россия победит", "хохол", "хохляндия", "украине в срало"]

        # Перебираем все каналы на сервере
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                async for message in channel.history(limit=None):
                    message_text = message.content.lower()
                    pattern = "|".join(re.escape(word) for word in CENSORED_WORDS)
                    if re.search(pattern, message_text):
                        await message.delete()
                        await message.channel.send(
                            f"{message.author.mention} such remarks are forbidden, Glory to Ukraine!")

    @commands.Cog.listener()
    async def on_message(self, message):
        CENSORED_WORDS = ["слава россии", "россия вперед", "россия победит", "хохол", "хохляндия", "украине в срало"]

        message_text = message.content.lower()
        pattern = "|".join(re.escape(word) for word in CENSORED_WORDS)
        if re.search(pattern, message_text):
            await message.delete()
            await message.channel.send(f"{message.author.mention} such remarks are forbidden, Glory to Ukraine!")


def setup(bot: commands.Bot):
    bot.add_cog(CensoreCommand(bot))
