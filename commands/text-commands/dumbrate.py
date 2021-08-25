import discord
import random
from discord.ext import commands, tasks
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option
from bot import slash

class dumbrate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['dumbr8'])
    async def dumbrate(self, ctx):
        await ctx.reply(f'you are {random.randint(1,100)}% dumb')

def setup(bot):
    bot.add_cog(dumbrate(bot))