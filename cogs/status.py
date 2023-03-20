import disnake
from disnake.ext import commands

# Create variable for entering id for channel of turning on Bot
# And paste it to bot.get_channel(id)

class CmdKick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.bot.user} ready to work")
        channel = self.get_channel(1085514774537830540)


        embed = disnake.Embed (
            title = f"🟢 Now online",
            description = f"Write `/help` to know what I can",
            color = 0x03fc03
        )
        await channel.send(embed = embed)
        await self.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching, name="for commands "))

def setup(bot: commands.Bot):
    bot.add_cog(CmdKick(bot))