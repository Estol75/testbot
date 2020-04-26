import discord
from discord.ext import commands
import os

Bot = commands.Bot(command_prefix='!')
Bot.remove_command('help')

@Bot.command(pass_context = True)
async def ping():
    await Bot.say("pong")


token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))
