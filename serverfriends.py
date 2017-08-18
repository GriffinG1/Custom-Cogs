import discord
from discord.ext import commands

'''Check what friends are on the current server.'''

class ServerFriends:
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=['sf'], pass_context=True)
    async def serverfriends(self, ctx):
        """Check friends on the current server."""
        await ctx.message.delete()
        friends = ""
        for user in ctx.guild.members:
            if user.relationship:
                if user.relationship.type == discord.RelationshipType.friend:
                    friends += "<@" + str(user.id) + ">\n"
        if not friends:
            await ctx.send("You have no friends on this server ☹")
        else:
            embed = discord.Embed(title="Friends on this server")
            embed.description = friends
            await ctx.send(embed=embed)
            
def setup(bot):
    bot.add_cog(ServerFriends(bot))