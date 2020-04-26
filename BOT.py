import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='!')

@bot.command(pass_context=True) #разрешаем передавать агрументы
async def test(ctx, arg): #создаем асинхронную фунцию бота
    await ctx.send(arg) #отправляем обратно аргумент
  
token = os.environ.get('BOT_TOKEN')

bot.run(token)
