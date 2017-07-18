import discord
from discord.ext import commands

'''Trolling'''


class Troll:

    def __init__(self, bot):
        self.bot = bot
        
    @commands.group(pass_context=True)
    async def wake(self, ctx):
        """Wake"""
        
    @wake.group(pass_context=True)
    async def me(self, ctx):
        """Me"""
    
    @me.command(pass_context=True)
    async def up(self, ctx):
        """Up"""
        await self.bot.send_message(ctx.message.channel, self.bot.bot_prefix + "Wake me up inside!")
        
def setup(bot):
    bot.add_cog(Troll(bot))