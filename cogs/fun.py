from main import color
import requests, json, random, discord, aiohttp
from discord.ext import commands


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


def get_quote():
    response = requests.get(
        "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,racist&type=single"
    )
    json_data = json.loads(response.text)
    joke = json_data["joke"]
    return joke


class Joke(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def joke(self, ctx):
        quote = get_quote()
        embed = discord.Embed(title="Joke", description=f"{quote}", color=color)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Meme(client))
    client.add_cog(Joke(client))
