import discord
from discord.ext import commands

'''My Ace Attorney commands'''


class AceAttorney:

    def __init__(self, bot):
        self.bot = bot

    async def simple_embed(self, text, title="", color=discord.Color.default()):
        embed = discord.Embed(title=title, color=color)
        embed.description = text
        await self.bot.say("", embed=embed)
		
    @commands.command(pass_context=True)
    async def holy(self, ctx):
        """Edgeworth's Response (image)"""
        await self.bot.delete_message(ctx.message)
        await self.bot.send_message(ctx.message.channel, content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="https://i.imgur.com/KBWpDpW.png"))
        await self.bot.send_message(ctx.message.channel, content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="https://i.imgur.com/BixOUBV.png"))
        
    @commands.command(pass_context=True)
    async def holytext(self, ctx):
        """Edgeworth's Response (text)"""
        await self.bot.delete_message(ctx.message)
        embed = discord.Embed(title="Miles Edgeworth", color=discord.Color.blue())
        embed.description = "This one single statement is so full of contradictions... For a moment there, I thought I was going to collapse."
        await self.bot.say("", embed=embed)

    @commands.command(pass_context=True)
    async def press(self, ctx):
        """HOLD IT!"""
        await self.bot.delete_message(ctx.message)
        await self.bot.send_message(ctx.message.channel, content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="http://i.imgur.com/umt4Pr2.png"))
        
    @commands.command(pass_context=True)
    async def object(self, ctx):
        """OBJECTION!"""
        await self.bot.delete_message(ctx.message)
        await self.bot.send_message(ctx.message.channel, content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="http://i.imgur.com/0GTlFg0.png"))
        
    @commands.command(pass_context=True)
    async def take(self, ctx):
        """TAKE THAT!"""
        await self.bot.delete_message(ctx.message)
        await self.bot.send_message(ctx.message.channel, content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="http://i.imgur.com/qPIwEaq.png"))
        
    @commands.command(pass_context=True)
    async def silence(self, ctx):
        """SHUT THE FUCK UP!"""
        await self.bot.delete_message(ctx.message)
        await self.bot.send_message(ctx.message.channel, content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="http://i.imgur.com/AxbuzZ9.png"))
        
def setup(bot):
    bot.add_cog(AceAttorney(bot))
