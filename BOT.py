import discord
from discord.ext import commands
import os

Bot = commands.Bot(command_prefix='!')
Bot.remove_command('help')

@Bot.command(pass_context=True) #разрешаем передавать агрументы
async def test(ctx, arg): #создаем асинхронную фунцию бота
    await ctx.send(arg) #отправляем обратно аргумент
  
token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))
