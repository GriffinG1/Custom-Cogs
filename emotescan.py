import discord
from discord.ext import commands
import re

'''Scan a server for your emote'''

class EmoteScan:

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=['emojiscan', 'es'])
    async def emotescan(self, ctx, msg):
        """Scan all servers for a certain emote"""
        await ctx.message.delete()
        server = ""
        msg = msg.replace('<','').replace('>','').replace(':','')
        print(msg)
        for x in self.bot.guilds:
            for y in x.emojis:
                if y.name == msg:
                    server += x.name + "\n"
        if server is None:
            await ctx.send(self.bot.bot_prefix + "Couldn't find that emote")
        else:
            embed = discord.Embed(title="Servers with {} on it".format(msg))
            embed.description = server
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(EmoteScan(bot))
