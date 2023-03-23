import disnake
from disnake.ext import commands


class ErrorHandling(commands.Cog):
    """This will be for a Error Handling."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    bot = commands.Bot(command_prefix = commands.when_mentioned)
    @bot.event
    async def on_command_error(ctx, error):
        print(error)

        if isinstance (error, commands.MissingPermissions):
            await ctx.send(f"{ctx.author} you don`t have such permission")
        elif isinstance (error, commands.UserInputError):
            await ctx.send(embed=disnake.Embed(
                description=f"Correct usage of command: `{ctx.prefix}{ctx.command.name}`({ctx.command.brief})\nExample: {ctx.prefix}{ctx.command.usage}"))


def setup(bot: commands.Bot):
    bot.add_cog(ErrorHandling(bot))