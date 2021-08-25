import discord
import random
from discord.ext import commands, tasks
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option
from bot import slash

class isreal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @slash.slash(name="is-real", description="are you not real or is everyone around you not real? i guess find out with this.", guild_ids=[629728204780994590], options=[create_option(name="user",description="so like who do you want to check",option_type=6,required=False)])
    async def isreal(ctx, user: discord.User):
        await ctx.send(f'<@{user.id}> is **{random.choice(["REAL", "NOT REAL"])}**')

    @isreal.error
    async def isreal_error(ctx, error):
        await ctx.send(f'You are **{random.choice(["REAL", "NOT REAL"])}**')

def setup(bot):
    bot.add_cog(isreal(bot))