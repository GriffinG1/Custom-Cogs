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
        nechannels = ""
        hidden = 0
        if type(ctx.channel) != discord.channel.DMChannel:
            total = len(ctx.message.guild.channels)
        else:
            await ctx.send(self.bot.bot_prefix + "This command *obviously* doesn't work in a DM, you peasant.")
            return
        embed = discord.Embed(title="Hidden channels in {}".format(ctx.message.guild))
        for x in ctx.message.guild.channels:
            if not x.permissions_for(ctx.message.author).read_messages:
                channels += "**#{}**".format(x.name)
                nechannels += "#{}".format(x.name)
                if x.topic == "None" or not x.topic:
                    channels += "\n\n"
                    nechannels += "\n\n"
                else:
                    channels += " - {}\n\n".format(x.topic)
                    nechannels += " - {}\n\n".format(x.topic)
                hidden += 1
        embed.description = channels
        footer = "{} out of {} channels are hidden".format(hidden, total)
        embed.set_footer(text=footer)
        if not channels:
            await ctx.send(self.bot.bot_prefix + "There are no channels you cannot see!")
        else:
            try:
                await ctx.send(embed=embed)
            except:
                await ctx.send("```{}\n\n{}```".format(nechannels, footer))
        
def setup(bot):
    bot.add_cog(HiddenChan(bot))
