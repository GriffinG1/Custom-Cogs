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
        if not nick:
            await ctx.send(self.bot.bot_prefix + "You dont have any nicknames set!")
        elif len(nick) <= 2000:
            embed = discord.Embed(title="Servers I Have Nicknames In")
            embed.description = nick
            await ctx.send(embed=embed)
        else:
            await ctx.send("Currently, you have too many nicknames to scan. This will be fixed at a date TBD")
                
def setup(bot):
    bot.add_cog(NickScan(bot))
