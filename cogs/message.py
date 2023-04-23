import disnake
from disnake.ext import commands
import socket


class MessageCommand(commands.Cog):
    """This will be for a ping command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    
    @commands.has_permissions(administrator = True, manage_channels = True, manage_permissions = True, manage_messages = True)
    @commands.slash_command(description="You can send formatet message to some channel")
    async def message(self, inter: disnake.ApplicationCommandInteraction, channel_id, title = "New message", your_message = "Your text here", color = 0x4287f5):
        bot = commands.Bot(command_prefix = commands.when_mentioned)
        channel = bot.get_channel(int(channel_id))
        
        await inter.response.send_message(f"Your message was sended, check it {channel}", )
        embed = disnake.Embed (
            title = f"{title}",
            description = f"{your_message}",
            color = color
            )
        await channel.send(embed = embed)
         
        


def setup(bot: commands.Bot):
    bot.add_cog(MessageCommand(bot))