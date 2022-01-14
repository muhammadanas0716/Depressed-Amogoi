import discord
from discord.ext import commands
from main import client, owner, admin_users, error_message, color

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client


    # Add admin Command
    @commands.command()
    async def add(self, ctx, member: discord.Member):
        if str(ctx.author) in admin_users:
            if str(member) not in admin_users:
                admin_users.append(str(member))
                embed = discord.Embed(title="A new Admin Made.",
                                      description=f"{str(member.mention)}, You have been made admin - "
                                                  f"You now have access to other admin commands and perms. For further details DM {owner}",
                                      color=color)
                await ctx.send(embed=embed)
            else:
                embed2 = discord.Embed(title="Error...", description=f"{str(member)} is already an admin",
                                       color=color)
                await ctx.send(embed=embed2)
        elif str(ctx.author) not in admin_users:
            embed3 = discord.Embed(title="Error...", description=f"{ctx.author.mention} - You are not an admin. Contact {owner} for more futher details",
                                   color=color)
            await ctx.send(embed=embed3)


    # Remove admin command
    @commands.command()
    async def remove(self, ctx, member: discord.Member):
        if str(ctx.author) in valid_users:
            if str(member) in valid_users:
                valid_users.remove(str(member))
                embed = discord.Embed(title="An Admin Removed.",
                                      description=f"Oh! {str(member.mention)} has been removed as an admin",
                                      color=color)
                await ctx.send(embed=embed)
            else:
                embed2 = discord.Embed(title="Error.",
                                       description=f"{str(member.mention)} was never an admin",
                                       color=color)
                await ctx.send(embed=embed2)


    @commands.command()
    @commands.has_role("DEV")
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)


def setup(client):
    client.add_cog(Admin(client))
