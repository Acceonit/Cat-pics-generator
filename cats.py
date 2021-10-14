import discord
import aiohttp
import requests
from discord.ext import commands
from aiohttp import ClientSession


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="the Server"))
    print('Bot is Ready')
    

async def get(session: object, url: object) -> object:
    async with session.get(url) as response:
        return await response.text()


class Image(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        
@client.command()
async def cat(ctx):
      response = requests.get('https://aws.random.cat/meow')
      data = response.json()
      embed = discord.Embed(
          title = 'Cat',
          description = '\u200b',
          colour = discord.Colour.light_gray()
          )
      embed.set_image(url=data['file'])            
      embed.set_footer(text=f"Requested by {ctx.author.name}")
      await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Image(bot))


client.run('TOKEN')    
