import aiohttp
import discord
from discord.ext import commands
import random


class Meme(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def meme(self, ctx):
        embed = discord.Embed(title="", description="")

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                meme = await r.json()
                embed.set_image(url=meme['data']['children'][random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)
