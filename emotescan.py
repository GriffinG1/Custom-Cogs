import discord
from discord.ext import commands

'''Scan a server for your emote'''

class EmoteScan:

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=['es'])
    async def emojiscan(self, ctx, msg):
        """Scan all servers for a certain emote"""
        await ctx.message.delete()
        servers = ""
        msg = msg.split(":")[1] if msg.startswith("<") else msg
        for guild in self.bot.guilds:
            for emoji in guild.emojis:
                if emoji.name == msg:
                    servers += guild.name + "\n"
        if servers is None:
            await ctx.send(self.bot.bot_prefix + "That emote is not on any of your servers.")
        else:
            embed = discord.Embed(title="Servers with the {} emote".format(msg))
            embed.description = servers
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(EmoteScan(bot))
