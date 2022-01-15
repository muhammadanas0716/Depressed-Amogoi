import asyncio
import aiohttp
import discord
import json
import random
import requests
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle

from main import color, client

DiscordComponents(client)


def get_quote():
    response = requests.get(
        "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,racist&type=single"
    )
    json_data = json.loads(response.text)
    joke = json_data["joke"]
    return joke


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, aliases=['me'])
    async def meme(self, ctx):
        def meme_opt():
            choices = [1, 2]
            chosen = random.choice(choices)
            if chosen == 1:
                '''Post a meme'''
                r = requests.get("https://memes.blademaker.tv/api?lang=en")
                res = r.json()
                title = res["title"]
                ups = res["ups"]
                # downs = res["downs"]
                comments = res['score']
                authors = res["author"]
                memes = discord.Embed(title=f"{title}", colour=color)
                memes.set_image(url=res["image"])
                memes.set_footer(text=f"👍 : {ups}  💬 : {comments} ")
            else:
                ###################
                r = requests.get("https://meme-api.herokuapp.com/gimme")
                res = r.json()
                title = res["title"]
                ups = res["ups"]
                author = res["author"]
                link = res["postLink"]
                memes = discord.Embed(description=f"[{title}]({link})", colour=color)
                memes.set_image(url=res["url"])
                memes.set_footer(text=f"👍 : {ups}")
            return memes

        components = [
            [
                Button(label='Next meme', style=ButtonStyle.green, custom_id='next'),
                Button(label='End interaction', style=ButtonStyle.red, custom_id='exit')
            ]
        ]

        message = await ctx.send(embed=meme_opt(), components=components)
        id = message.id
        while True:
            try:
                interaction = await self.client.wait_for(
                    'button_click',
                    check=lambda inter: inter.message.id == message.id,
                    timeout=30
                )
            except asyncio.TimeoutError:
                for row in components:
                    row.disable_components()
                return await message.edit(components=components)

            if interaction.author.id == ctx.author.id:
                if interaction.custom_id == "next":
                    await interaction.edit_origin(embed=meme_opt(), components=components)
                elif interaction.custom_id == "exit":
                    for row in components:
                        row.disable_components()
                    message = await ctx.fetch_message(id)
                    return await interaction.edit_origin(embed=message.embeds[0], components=components)
            else:
                await interaction.send("Hey! This is not for you!")


    @commands.command()
    async def joke(self, ctx):
        quote = get_quote()
        embed = discord.Embed(title="Joke", description=f"{quote}", color=color)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Fun(client))
