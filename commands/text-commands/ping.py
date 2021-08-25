import discord
import random
from discord.ext import commands, tasks
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option
from bot import slash

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.reply(f'am i supposed to say pong?, heres my ping tho: {round(self.bot.latency * 1000)}ms')

def setup(bot):
    bot.add_cog(ping(bot))