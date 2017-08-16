import discord
import subprocess
import os
import git
from discord.ext import commands

'''Code to switch between branches'''

class Git:
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.group(pass_context=True, invoke_without_command=True)
    async def git(self, ctx, *, branch):
        """Switch between branches"""
        if ctx.invoked_subcommand is None:
            g = git.cmd.Git(working_dir=os.getcwd())
            branchversion = g.execute(["git", "rev-parse", "--abbrev-ref", "HEAD"])
            if branch != branchversion:
                exit_code = subprocess.call(['git', 'stash'])
                if exit_code:
                    return await ctx.send(self.bot.bot_prefix + "Couldn't stash changes. Aborting...")
                await ctx.send(self.bot.bot_prefix + "Stashed changes to " + branchversion + ".")
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
            else:
                await ctx.send(self.bot.bot_prefix + "You're already on that branch!")
            
    @git.command(pass_context=True)
    async def pull(self, ctx):
        """Pull changes for the current branch"""
        g = git.cmd.Git(working_dir=os.getcwd())
        branch = g.execute(["git", "rev-parse", "--abbrev-ref", "HEAD"])
        exit_code = subprocess.call(['git', 'pull', 'origin', branch])
        if exit_code:
            return await ctx.send(self.bot.bot_prefix + "Something went wrong with pulling the branch. Check the console for details.")
        await ctx.send(self.bot.bot_prefix + "Successfully pulled {}!".format(branch))
        
def setup(bot):
    bot.add_cog(Git(bot))
