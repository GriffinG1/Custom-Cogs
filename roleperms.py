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
        permissionsne = ""
        try:
            for perm in discord.utils.get(ctx.message.guild.roles, name=msg).permissions:
                perm = (perm[0].replace("_", " ").title(), perm[1])
                permissions += "**{}**: {}\n".format(*perm)
                permissionsne += "{}: {}\n".format(*perm)
            embed = discord.Embed(title="Permissions for role {}".format(msg))
            embed.description = permissions
            try:
                await ctx.send(embed=embed)
            except:
                await ctx.send("```Permissions for role {}\n\n{}```".format(msg, permissionsne))
        except:
            await ctx.send("Couldn't find role, are you sure you typed it correctly?\n\nYou typed: `{}`".format(msg))
       
def setup(bot):
    bot.add_cog(RolePerms(bot))
