import discord
from discord.ext import commands

'''Get role perms'''

class RolePerms:

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=['rp'])
    async def roleperms(self, ctx, msg):
        """Get role perms! The role name must match exactly. Ex for a role "Admin", you'd do >roleperms Admin. If the role name contains a space, the role name must be in quotes."""
        await ctx.message.delete()
        permissions = ""
        for perm in discord.utils.get(ctx.message.guild.roles, name=msg).permissions:
            # perm.title()
            # perm = perm.replace('\'', '**').replace('(','').replace(')', '').replace(',',':').replace('_',' ')
            permissions += "**{}** {}\n".format(*perm)
        embed = discord.Embed(title="Permissions for role {}".format(msg))
        embed.description = permissions
        await ctx.send(embed=embed)

       
def setup(bot):
    bot.add_cog(RolePerms(bot))
