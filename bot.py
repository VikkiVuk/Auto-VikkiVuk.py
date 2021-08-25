import os
import discord
import logging
import pymongo
import util.exceptions as exceptions
from dotenv import load_dotenv
from discord.ext import commands
from discord_slash import SlashCommand

# This loads the .env file so that we can access our local config
load_dotenv(dotenv_path=".env")

# Required Variables
client = commands.Bot(command_prefix = "av.")
slash = SlashCommand(client, sync_commands=True)
mongo_url = os.getenv("mongo")

# Command Initializer
for folder in os.listdir("./commands"):
    for file in os.listdir(f"./commands/{folder}"):
        if file.endswith(".py"):
            name = file[:-3]
            client.load_extension(f'commands.{folder}.{name}')

# Bot Start
@client.event
async def on_ready():
    print("omgggg! vikki you actually made something work! congrats!")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="av.help | python"))

    try:
        client.db = pymongo.MongoClient(mongo_url)
        client.config = client.db["config"]
        client.profiles = client.db["profiles"]
    except exceptions.PyMongoError as e:
        print("An error occurred while fetching the config: %s" % e)
    else:
       print("Database connection established successfully")

# Start the bot using the token
client.run(os.getenv("token"))