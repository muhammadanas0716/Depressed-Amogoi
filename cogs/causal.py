import discord, os
from discord.ext import commands
from main import color, OWNER, client


class CasualCommands(commands.Cog):

    # Ping Command
    @commands.command()
    async def ping(self, ctx):
        await ctx.channel.send(f"Pong {ctx.message.author.mention}")

    # Server Stats Command
    @commands.command()
    async def stats(self, ctx):
        name = str(ctx.guild.name)
        description = "A Construction Site for Depressed Bots 🤖"

        owner = OWNER
        id = str(ctx.guild.id)
        memberCount = str(ctx.guild.member_count)

        icon = str(ctx.guild.icon_url)

        embed = discord.Embed(
            title=name + " Server Information",
            description=description,
            color=color
        )
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Owner", value=owner, inline=True)
        embed.add_field(name="Server ID", value=id, inline=True)
        embed.add_field(name="Member Count", value=memberCount, inline=False)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(CasualCommands(client))
