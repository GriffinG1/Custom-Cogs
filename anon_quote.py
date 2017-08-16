import discord
import json
from discord.ext import commands
from cogs.utils.checks import *
from cogs.utils.config import get_config_value

'''Quoting, without a name or channel'''

class AnonQuote:
    def __init__(self, bot):
        self.bot = bot
        config = load_config()
        self.bot_prefix = config["bot_identifier"]
    
    @commands.command(aliases=['noq'], pass_context=True)
    async def noquote(self, ctx, *, msg: str = None):
        """Quote a message. >help quote for more info.
        >noquote - quotes the last message sent in the channel.
        >noquote <words> - tries to search for a message in the server that contains the given words and quotes it.
        >noquote <message_id> - quotes the message with the given message id. Ex: >quote 302355374524644290(Enable developer mode to copy message ids).
        >noquote <words> | channel=<channel_name> - quotes the message with the given words from the channel name specified in the second argument
        >noquote <message_id> | channel=<channel_name> - quotes the message with the given message id in the given channel name
        >noquote <user_mention_name_or_id> - quotes the last member sent by a specific user"""
        
        await ctx.message.delete()
        result = None
        pre = cmd_prefix_len()
        channel = ctx.channel
        if msg:
            user = get_user(ctx.message, msg)
            if " | channel=" in msg:
                channel = next((ch for ch in self.bot.get_all_channels() if ch.name == msg.split("| channel=")[1]), None)
                msg = msg.split(" | channel=")[0]
                if not channel:
                    return await ctx.send(self.bot.bot_prefix + "Could not find specified channel.")
            if not isinstance(channel, discord.channel.TextChannel):
                return await ctx.send(self.bot.bot_prefix + "This command is only supported in server text channels.")
            try:
                length = len(self.bot.all_log[str(ctx.message.channel.id) + ' ' + str(ctx.message.guild.id)])
            except:
                pass
            else:
                size = length if length < 201 else 200
                for channel in ctx.message.guild.channels:
                    if type(channel) == discord.channel.TextChannel:
                        if str(channel.id) + ' ' + str(ctx.message.guild.id) in self.bot.all_log:
                            for i in range(length - 2, length - size, -1):
                                try:
                                    search = self.bot.all_log[str(channel.id) + ' ' + str(ctx.message.guild.id)][i]
                                except:
                                    continue
                                if (msg.lower().strip() in search[0].content.lower() and (
                                        search[0].author != ctx.message.author or search[0].content[pre:7] != 'quote ')) or (
                                    ctx.message.content[6:].strip() == str(search[0].id)) or (search[0].author == user and search[0].channel == ctx.message.channel):
                                    result = search[0]
                                    break
                            if result:
                                break


            if not result:
                try:
                    async for sent_message in channel.history(limit=500):
                        if (msg.lower().strip() in sent_message.content and (
                                sent_message.author != ctx.message.author or sent_message.content[pre:7] != 'quote ')) or (msg.strip() == str(sent_message.id)) or (msg.author == user):
                            result = sent_message
                            break
                except:
                    pass
        else:
            if not isinstance(channel, discord.channel.TextChannel):
                return await ctx.send(self.bot.bot_prefix + "This command is only supported in server text channels.")
            try:
                search = self.bot.all_log[str(ctx.message.channel.id) + ' ' + str(ctx.message.guild.id)][-2]
                result = search[0]
            except KeyError:
                try:
                    messages = await channel.history(limit=2).flatten()
                    result = messages[0]
                except:
                    pass


        if result:
            if embed_perms(ctx.message) and result.content:
                color = get_config_value("optional_config", "quoteembed_color")
                if color == "auto":
                    color = result.author.top_role.color
                elif color == "":
                    color = 0xbc0b0b
                else:
                    color = int('0x' + color, 16)
                em = discord.Embed(color=color, description=result.content, timestamp=result.created_at)
                await ctx.send(embed=em)
            else:
                await ctx.send('%s - %s```%s```' % (sender, result.created_at, result.content))
        else:
            await ctx.send(self.bot.bot_prefix + 'No quote found.')
            
def setup(bot):
    bot.add_cog(AnonQuote(bot))
