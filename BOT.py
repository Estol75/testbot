import discord
from discord.ext import commands
import os

Bot = commands.Bot(command_prefix= "!")
Bot.remove_command('help')

@Bot.event
async def on_ready():
    print("Bot is ready")

@Bot.command(pass_context = True)
async def корды():
    await Bot.say('**Вот тебе полезные координаты:**\r\n'
                      '```Ферма скелетов (По метро): -7844 -5753```'
                      '```Ферма гвардов (по метро): -8000 -6435```'
                      '```Ферма золота и яма: -7777 -6460```'
                      '```Ферма зомби и пауков (По метро): -7430 -5895```'
                      '```Городская ферма ифритов (В аду): -1200 -630```'
                      '```Портал в энд (В аду): -1100 -950```'
                      '```Портал в Техноград (В аду): -918 -750```'
                      '```Портал в хаб Технограда: -7400 -6085```'
                      '```Склад: -7470 -6015```')

token = os.environ.get('BOT_TOKEN')
Bot.run(str(token))
