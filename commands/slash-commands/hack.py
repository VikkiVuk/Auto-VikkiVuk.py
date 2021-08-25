import discord
import random
import asyncio
import datetime
from discord.ext import commands, tasks
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option
from bot import slash

class hack(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @slash.slash(name="hack", description="why.", guild_ids=[629728204780994590], options=[create_option(name="user",description="so like who do you want to hack",option_type=6,required=True)])
    async def hack(ctx, user: discord.User):
        await ctx.defer()
        await asyncio.sleep(3)
        embedVar = discord.Embed(title="HACKING", description=f"Currently hacking <@{user.id}> \n \n_This can take some time!_", color=0x9d13ed)
        await ctx.send(embed=embedVar)
        await asyncio.sleep(random.randint(60, 120))
        rng = random.randint(1,3)
        if rng == 1:
            success = discord.Embed(title="SUCCESS", description=f"Hey there! I successfully hacked <@{user.id}> \n \n_All of the information has been sent to VikkiVuk_", color=0x13ed1a)
            await ctx.send(embed=success)
        elif rng == 2:
            fail = discord.Embed(title="ANTIVIRUS", description=f"Uh oh! <@{user.id}> has an antivirus! This has prevented the attack. \n \n_Better luck next time_", color=0xeded13)
            await ctx.send(embed=fail)
        elif rng == 3:
            error = discord.Embed(title="ERROR", description=f"Oopsies! An error occured while hacking <@{user.id}> \n \n_Better luck next time_", color=0xed1313)
            await ctx.send(embed=error)   
def setup(bot):
    bot.add_cog(hack(bot))