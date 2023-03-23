import disnake
from disnake.ext import commands


class KickCommand(commands.Cog):
    """This will be for a Kick command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="kick_user", description="If someone will break some rules or will try to crash server, he will get ban", usage="/ban <@user> reason=None")
    @commands.has_permissions(ban_members = True, administrator = True)
    async def ban(ctx, member: disnake.Member, *, reason="Rules broker"):
        await ctx.send(f"Moderator {ctx.author.mention} baned user {member.mention}", delete_after=300)
        await member.kick(reason = reason)
        await ctx.message.delete()

def setup(bot: commands.Bot):
    bot.add_cog(KickCommand(bot))