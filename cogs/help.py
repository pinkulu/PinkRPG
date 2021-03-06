import datetime

import discord
from discord.ext import commands


class HelpCommand(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def help(self, ctx):
        color = ctx.author.color
        embed = discord.Embed(title='PinkBot help', colour=color, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="Links:", value="[Website](http://pinkbot.xyz)"
                                             "\n[Commands](https://docs.pinkbot.xyz/) "
                                             "\n[Support server](http://support.pinkbot.xyz) "
                                             "\n[Vote for the bot](https://top.gg/bot/697887266307047424)", inline=False)
        embed.add_field(name="Developer:", value="Pinkulu", inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(HelpCommand(bot))
