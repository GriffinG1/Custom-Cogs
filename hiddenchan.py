import discord
from discord.ext import commands

'''Display Hidden Channels'''

class HiddenChan:

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=['hc'], pass_context=True)
    async def hiddenchan(self, ctx):
        """Show hidden channels"""
        await ctx.message.delete()
        channels = ""
        hidden = 0
        total = len(ctx.message.guild.channels)
        embed = discord.Embed()
        for x in ctx.message.guild.channels:
            if not x.permissions_for(ctx.message.author).read_messages:
                channels += "#" + x.name + "\n"
                hidden += 1
        embed.description = channels
        embed.set_footer(text="{} out of {} channels are hidden".format(hidden, total))
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(HiddenChan(bot))
