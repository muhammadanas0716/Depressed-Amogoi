import asyncio
import discord
import json
import random
import requests
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle
from discord.voice_client import VoiceClient
import youtube_dl

from random import choice

from main import color, client

DiscordComponents(client)


def get_quote():
    response = requests.get(
        "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,racist&type=single"
    )
    json_data = json.loads(response.text)
    joke = json_data["joke"]
    return joke

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

class Meme(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, aliases=['me', "MEME", "ME"])
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
                ################### SECOND-MEME-COLUMN ###################
                r = requests.get("https://meme-api.herokuapp.com/gimme")
                res = r.json()
                title = res["title"]
                ups = res["ups"]
                author = res["author"]
                link = res["postLink"]
                memes = discord.Embed(description=f"[{title}]({link})", colour=color)
                memes.set_image(url=res["url"])
                memes.set_footer(text=f"👍 : {ups}" f"✍: {author}")
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

class Joke(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def joke(self, ctx):
        quote = get_quote()
        embed = discord.Embed(title="Joke", description=f"{quote}", color=color)
        await ctx.send(embed=embed)


# MUSIC CLASS
class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='play', help='This command plays music')
    async def play(self, ctx, url):
        if not ctx.message.author.voice:
            await ctx.send("You are not connected to a voice channel")
            return

        else:
            channel = ctx.message.author.voice.channel

        await channel.connect()

        server = ctx.message.guild
        voice_channel = server.voice_client

        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=client.loop)
            voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

        await ctx.send('**Now playing:** {}'.format(player.title))

    @commands.command(name='stop', help='This command stops the music and makes the bot leave the voice channel')
    async def stop(self, ctx):
        voice_client = ctx.message.guild.voice_client
        await voice_client.disconnect()



def setup(client):
    client.add_cog(Meme(client))
    client.add_cog(Joke(client))
    client.add_cog(Music(client))
