import discord
import random
from discord.ext import commands, tasks
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option
from bot import slash

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @slash.slash(name="ping", description="pong?", guild_ids=[629728204780994590])
    async def ping(ctx):
        await ctx.send(f'am i supposed to say pong?, my ping dont exist')

def setup(bot):
    bot.add_cog(ping(bot))