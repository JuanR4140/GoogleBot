import os
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)

from discord.ext import commands
import discord

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

bot = commands.Bot(command_prefix='g+')

@bot.event
async def on_ready():
  print(f'{bot.user.name} has connected to Discord!')

@bot.command(name="intro", help="GoogleBot's introduction")
async def intro(ctx):
  await ctx.send("```Hello, I am GoogleBot!\nI was made to be able to help you surf the web just a tiny bit faster!\nGet started by requesting me to make a Google search (g+search how tall is mount everest?)```")

@bot.command(name="search", help="Main feature of GoogleBot. Allows you to search Google quickly")
async def search(ctx, *args):
  await ctx.send("```retrieving page data, please wait..```")
  url = "https://www.google.com/search?q="
  wsurl = url + '+'.join(args)
  
  driver.get(wsurl)
  
  title = driver.find_elements_by_class_name("ellip")
  desc = driver.find_elements_by_class_name("aCOpRe")
  #print(title1.text)
  #print(desc1.text)

  
  #print(driver.page_source)

  try:
    embed=discord.Embed(title="Showing Results For '" + ' '.join(args) + "'", color=0x37ff00) #0x37ff00 = green; 0xff0000 = red;
    embed.add_field(name=title[0].text, value=desc[0].text, inline=True)
    embed.add_field(name=title[1].text, value=desc[1].text, inline=True)
    embed.add_field(name=title[2].text, value=desc[2].text, inline=True)
    embed.set_footer(text="Search Results brought to you by JuanR4140#0242 :D")
  except:
    embed=discord.Embed(title="Search Results failed to load", color=0xff0000)
    embed.add_field(name="(IndexError | Error 1)", value="Something went wrong when accessing list to display")
    embed.set_footer(text="That's all we know.. :/")
    await ctx.send(embed=embed)

  try:
    await ctx.send(embed=embed)
  except:
    embed=discord.Embed(title="Search Results failed to load", color=0xff0000)
    embed.add_field(name="(Embed=Embed | Error 2)", value="Something went wrong when messaging the embed")
    embed.set_footer(text="That's all we know.. :/")
    await ctx.send(embed=embed)
  await ctx.send(url + '+'.join(args))
  #await ctx.send('{} arguments: {}'.format(len(args), ' '.join(args)))
bot.run(TOKEN)