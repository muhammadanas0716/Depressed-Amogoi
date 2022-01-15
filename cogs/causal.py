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
        embed.add_field(name="Member Count", value=memberCount, inline=True)

        await ctx.send(embed=embed)

    # Help Command
    @commands.command()
    async def help(self, ctx):
        with open(os.path("commands", "help.txt")) as f:
            all_commands = f.read()
        embed = discord.Embed(title="All Available Commands",
                              description=all_commands, color=color)
        await ctx.send(embed=embed)

    # Rules Command
    @commands.command()
    async def rules(self, ctx):
        with open(os.path("commands", "rules.txt")) as f:
            all_rules = f.read()
        embed = discord.Embed(
            title="Rules", description=all_rules, color=color)
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(CasualCommands(client))
