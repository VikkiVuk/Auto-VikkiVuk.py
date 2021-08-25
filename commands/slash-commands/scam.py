import discord
import random
import asyncio
from discord.ext import commands, tasks
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option
from bot import slash

class scam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @slash.slash(name="scam", description="you are a psycho", guild_ids=[629728204780994590], options=[create_option(name="user",description="so like who do you want to scam",option_type=6,required=True)])
    async def scam(ctx, user: discord.User):
        await ctx.defer()
        await asyncio.sleep(3)
        await ctx.send(f"totally scamming <@{user.id}>.... \n \n_can take some time, this process is usually shorter than the hacking process_")
        await asyncio.sleep(random.randint(30, 60))
        rng = random.randint(1,2)
        if rng == 1:
            await ctx.send(f"welp <@{user.id}> is a dumbass and fell for the scam, so he is now homeless.")
        elif rng == 2:
            await ctx.send(f"<@{user.id}> was a smartass and didnt fall for the scam.")
def setup(bot):
    bot.add_cog(scam(bot))