import discord
import random
import asyncio
from discord.ext import commands, tasks
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option
from bot import slash

class magicball(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @slash.slash(name="8ball", description="this exists to ruin your life.", guild_ids=[629728204780994590], options=[create_option(name="question",description="yah so you put your question here idk",option_type=3,required=True)])
    async def magicball(ctx, question: str):
        await ctx.defer()
        await asyncio.sleep(5)
        responses = ["It is certain.","It is decidedly so.","Without a doubt.","Yes - definitely.","You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.","Reply hazy, try again.","Ask again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful."]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

def setup(bot):
    bot.add_cog(magicball(bot))