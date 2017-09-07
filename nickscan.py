import discord
from discord.ext import commands

"""Get a list of all your nicknames!"""

class NickScan:

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=['ns'])
    async def nickscan(self, ctx):
        """Get a list of all your nicknames!"""
        await ctx.message.delete()
        nick = ""
        for guild in self.bot.guilds:
            if guild.get_member(self.bot.user.id).nick:
                nick += "**Server:** `{}` **Nick:** `{}`\n".format(guild.name, guild.get_member(self.bot.user.id).nick)
            embed = discord.Embed(title="Servers I Have Nicknames In")
            embed.description = nick
        await ctx.send(embed=embed)
                
def setup(bot):
    bot.add_cog(NickScan(bot))