import discord
from discord.ext import commands

'''My Ace Attorney commands'''


class AceAttorney:

    def __init__(self, bot):
        self.bot = bot
		
    @commands.command(pass_context=True)
    async def holy(self, ctx):
        """Edgeworth's Response (image)"""
        await ctx.message.delete()
        await ctx.send( content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="https://i.imgur.com/KBWpDpW.png"))
        await ctx.send( content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="https://i.imgur.com/BixOUBV.png"))
        
    @commands.command(pass_context=True)
    async def holytext(self, ctx):
        """Edgeworth's Response (text)"""
        await ctx.message.delete()
        embed = discord.Embed(title="Miles Edgeworth", color=discord.Color.blue())
        embed.description = "This one single statement is so full of contradictions... For a moment there, I thought I was going to collapse."
        await ctx.send("", embed=embed)

    @commands.command(pass_context=True)
    async def press(self, ctx):
        """HOLD IT!"""
        await ctx.message.delete()
        await ctx.send( content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="http://i.imgur.com/umt4Pr2.png"))
        
    @commands.command(pass_context=True)
    async def object(self, ctx):
        """OBJECTION!"""
        await ctx.message.delete()
        await ctx.send( content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="http://i.imgur.com/0GTlFg0.png"))
        
    @commands.command(pass_context=True)
    async def take(self, ctx):
        """TAKE THAT!"""
        await ctx.message.delete()
        await ctx.send( content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="http://i.imgur.com/qPIwEaq.png"))
        
    @commands.command(pass_context=True)
    async def silence(self, ctx):
        """SHUT THE FUCK UP!"""
        await ctx.message.delete()
        await ctx.send( content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="http://i.imgur.com/AxbuzZ9.png"))
        
    @commands.command(pass_context=True)
    async def gotcha(self, ctx):
        """GOTCHA!"""
        await ctx.message.delete()
        await ctx.send( content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="http://i.imgur.com/29ZvDWm.png"))
        
    @commands.command(pass_context=True)
    async def enough(self, ctx):
        """ENOUGH!"""
        await ctx.message.delete()
        await ctx.send( content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="http://i.imgur.com/paNw1dh.png"))
        
    @commands.command(pass_context=True)
    async def fast(self, ctx):
        """NOT SO FAST!"""
        await ctx.message.delete()
        await ctx.send( content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="http://i.imgur.com/Nab2PLO.png"))
        
    @commands.command(pass_context=True)
    async def got(self, ctx):
        """GOT IT!"""
        await ctx.message.delete()
        await ctx.send( content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="http://i.imgur.com/J3X6Fbd.png"))
        
    @commands.command(pass_context=True)
    async def eureka(self, ctx):
        """EUREKA!"""
        await ctx.message.delete()
        await ctx.send( content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="http://i.imgur.com/O8gVn3q.png"))

    @commands.command(pass_context=True)
    async def guilty(self, ctx):
        """GUILTY!"""
        await ctx.message.delete()
        await ctx.send( content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="http://i.imgur.com/1kq5gau.gif"))

    @commands.command(pass_context=True)
    async def notguilty(self, ctx):
        """NOT GUILTY!"""
        await ctx.message.delete()
        await ctx.send( content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="http://i.imgur.com/KeggKe4.gif"))
		
	@commands.command(pass_context=True)
	async def satorha(self, ctx):
		"""Satorha!"""
		await ctx.message.delete()
		await ctx.send( content=None, embed=discord.Embed(color=discord.Color.blue()).set_image(url="http://i.imgur.com/FMEzpJ7.png"))
def setup(bot):
    bot.add_cog(AceAttorney(bot))
