import discord
from discord.ext import commands
from main import error_message, color


class Remove(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Kick Command
    @commands.command()
    @commands.has_role("DEV")
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        embed = discord.Embed(title="A Member Kicked",
                              description=f"{str(member.mention)} has been kicked by {ctx.author.mention} \n Reason : {reason}",
                              color=color)
        await ctx.send(embed=embed)

    @kick.error
    async def kick_error(self, ctx, error):
        embed = discord.Embed(title="Admin Error",
                              description=error_message,
                              colour=color)
        await ctx.send(embed=embed)

    # Ban Command
    @commands.command()
    @commands.has_role("DEV")
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        embed = discord.Embed(title="A Member Banned",
                              description=f"{member.mention} has been banned by {ctx.author.mention} \n Reason : {reason}",
                              color=color)
        await ctx.send(embed=embed)

    @ban.error
    async def ban_error(self, ctx, error):
        embed = discord.Embed(title="Admin Error",
                              description=error_message,
                              colour=color)
        await ctx.send(embed=embed)

    # Unban Command
    @commands.command()
    @commands.has_role("DEV")
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(title="A Member Banned",
                                      description=f"I have UNBANNED {user.mention}, you may invite him back!",
                                      color=color)
                await ctx.send(embed=embed)

    @unban.error
    async def unban_error(self, ctx, error):
        embed = discord.Embed(title="Admin Error",
                              description=error_message,
                              colour=color)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Remove(client))
