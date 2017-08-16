import discord
import subprocess
import os
from discord.ext import commands

'''Code to switch between branches'''

class Git:
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(pass_context=True)
    async def git(self, ctx, *, branch):
        """Switch between branches"""
        exit_code = subprocess.call(['git', 'stash'])
        if exit_code:
            return await ctx.send(self.bot.bot_prefix + "Couldn't stash changes. Aborting...")
        await ctx.send(self.bot.bot_prefix + "Stashed changes to " + branch + ".")
        exit_code = subprocess.call(['git', 'checkout', branch])
        if exit_code:
            return await ctx.send(self.bot.bot_prefix + "Something went wrong with checking out the branch. Check the console for details.")
        exit_code = subprocess.call(['git', 'pull', 'origin', branch])
        if exit_code:
            return await ctx.send(self.bot.bot_prefix + "Something went wrong with pulling the branch. Check the console for details.")
        await ctx.send(self.bot.bot_prefix + "Successfully checked out branch {} and pulled it!".format(branch))
        if os.name == 'nt':
            os.system('cls')
        else:
            try:
                os.system('clear')
            except:
                pass
        print('Logged in as')
        try:
            print(self.bot.user.name)
        except:
            pass
        print('User id:' + str(self.bot.user.id))
        print('------')
        print('Switched to branch ' + branch)
        
def setup(bot):
    bot.add_cog(Git(bot))