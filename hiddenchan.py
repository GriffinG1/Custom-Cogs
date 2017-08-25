import discord
from discord.ext import commands

'''Display Hidden Channels'''

class HiddenChan:

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=['hc'], pass_context=True)
    async def hiddenchan(self, ctx):
        """Show hidden channels"""
        channels = ""
        embed = discord.Embed()
        for x in ctx.message.guild.channels:
            if not x.permissions_for(ctx.message.author).read_messages:
                channels += "#" + x.name + "\n"
        embed.description = channels
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(HiddenChan(bot))