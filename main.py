import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random, os, asyncio

# 啟用所有 intents
intents = discord.Intents.all()

# 讀取設定檔 load settings
with open('setting.json', 'r', encoding= 'utf8') as jfile:
	jdata = json.load(jfile)

"""
command_prefix: 指令前綴
owner_ids: 擁有者ID
"""
bot = commands.Bot(command_prefix= jdata['Prefix'], 
										 owner_ids= jdata['Owner_id'])

# Bot完成啟動後事件
@bot.event
async def on_ready():
	print(">> Bot is online <<")

# 載入cmds資料夾內所有cog
for filename in os.listdir('./cmds'):
	if filename.endswith('.py'):
		bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
	bot.run(jdata['TOKEN'])
	
