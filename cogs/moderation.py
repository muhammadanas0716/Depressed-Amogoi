from click import command
import discord
from discord.ext import commands

from main import color, OWNER


class Kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        embed = discord.Embed(title="Member Kicked", description=f"""
        **Kicked Member Name:** {member.mention} \n
        **Kicked By Member Name:** {ctx.author.mention} \n
        **Reason:** {reason}
        """, color=color)
        await ctx.send(embed=embed)
        await member.kick(reason=reason)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="Permission Error.",
                                  description=f"You don't have the permission to kick members, contact {OWNER} for further Details.",
                                  colour=color)
            await ctx.send(embed=embed)
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Missed Requeired Argument.",
                    description=f"You have missed a requeried argument, please specify the user you want to kick.",
                    colour=color)
            await ctx.send(embed=embed)

########## BAN COMMAND ##########
class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        embed = discord.Embed(title="Member Banned", description=f"""
        **Banned Member Name:** {member.mention} \n
        **Banned By Member Name:** {ctx.author.mention} \n
        **Reason:** {reason}
        """, color=color)
        await ctx.send(embed=embed)
        await member.ban(reason=reason)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="Permission Error.",
                                  description=f"You don't have the permission to ban members, contact {OWNER} for further Details.",
                                  colour=color)
            await ctx.send(embed=embed)
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Missed Requeired Argument.",
                    description=f"You have missed a requeried argument, please specify the user you want to ban.",
                    colour=color)
            await ctx.send(embed=embed)

########## UNBAN COMMAND ##########
class Unban(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()

        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                embed = discord.Embed(title="Member Unbanned", description=f"""
                **Unbanned Member Name:** {member} \n
                **Unbanned By Member Name:** {ctx.author.mention} \n
                """, color=color)
                await ctx.guild.unban(user)
                await ctx.send(embed=embed)


    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="Permission Error.",
                                  description=f"You don't have the permission to unban members, contact {OWNER} for further Details.",
                                  colour=color)
            await ctx.send(embed=embed)
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Missed Requeired Argument.",
                    description=f"You have missed a requeried argument, please specify the user you want to unban, (DEPRESSED#0000)",
                    colour=color)
            await ctx.send(embed=embed)


########## CLEAR COMMAND ##########                             
class Clear(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="Permission Error.",
                                  description=f"You don't have the permission to manange messages, contact {OWNER} for further Details",
                                  colour=color)
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Kick(client))
    client.add_cog(Ban(client))
    client.add_cog(Unban(client))
    client.add_cog(Clear(client))
