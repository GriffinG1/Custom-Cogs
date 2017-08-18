import discord
import subprocess
import os
import git
from discord.ext import commands
import asyncio

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
                exit_code = g.execute(['git', 'stash'])
                if exit_code != "No local changes to save":
                    await ctx.send(self.bot.bot_prefix + "Stashed changes to " + branchversion + ".")
                exit_code = g.execute(['git', 'checkout', branch])
                exit_code = g.execute(['git', 'pull', 'origin', branch])
                if exit_code != "Already up-to-date.":
                    await ctx.send(self.bot.bot_prefix + "Pulled latest changes to " + branch + ".")
                stash = g.execute(['git', 'stash', 'list'])
                if stash != "\n":
                    try:
                        exit_code = g.execute(['git', 'stash', 'apply'])
                        if exit_code:
                            await ctx.send(self.bot.bot_prefix + "Applied stashed changes")
                    except:
                        return
                await ctx.send(self.bot.bot_prefix + "Successfully checked out branch {}!".format(branch))
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
                print(stash)
            else:
                await ctx.send(self.bot.bot_prefix + "You're already on that branch!")
            
    @git.command(pass_context=True)
    async def pull(self, ctx):
        """Pull changes for the current branch"""
        await ctx.message.delete()
        g = git.cmd.Git(working_dir=os.getcwd())
        branch = g.execute(["git", "rev-parse", "--abbrev-ref", "HEAD"])
        exit_code = g.execute(['git', 'pull', 'origin', branch])
        if exit_code != "Already up-to-date.":
            await ctx.send(self.bot.bot_prefix + "Pulling latest changes to " + branch + "...", delete_after=15)
            await asyncio.sleep(5)
            await ctx.send(self.bot.bot_prefix + "Successfully pulled {}!".format(branch), delete_after=10)
        else:
            await ctx.send(self.bot.bot_prefix + "There were no changes to pull.", delete_after=10)
        
    @git.command(pass_context=True)
    async def branch(self, ctx):
        """Check current branch"""
        await ctx.message.delete()
        g = git.cmd.Git(working_dir=os.getcwd())
        branch = g.execute(["git", "rev-parse", "--abbrev-ref", "HEAD"])
        await ctx.send(self.bot.bot_prefix + "Current branch is: " + branch, delete_after=20)
        
def setup(bot):
    bot.add_cog(Git(bot))
