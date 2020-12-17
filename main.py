prefix = "g+"

import os
import discord
from discord.ext import commands

from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
  print(f'{client.user} is connected to Discord!')

async def on_message(message):
  if message.author == client.user:
    return
  if message.content == prefix + "intro":
    await message.channel.send("```Hello, I am GoogleBot!\nI was made to be able to help you surf the web just a tiny bit faster!\nGet started by requesting me to make a Google search (g+search how tall is mount everest?)```")

  if message.content == prefix + "search":
    embed=discord.Embed(title="Showing Results For ", color=0xff0000)
    embed.add_field(name="result 1", value="result 1", inline=True)
    embed.add_field(name="result 2", value="result 2", inline=True)
    embed.add_field(name="result 3", value="result 3", inline=True)
    embed.set_footer(text="Search Results brought to you by JuanR4140#0242 :D")
    await message.channel.send(embed=embed)

client.run(TOKEN)