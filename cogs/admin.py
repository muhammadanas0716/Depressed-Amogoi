import discord
from discord.ext import commands
from main import error_message
from main import client
from main import owner

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Add Admin/ROLE Command
    @commands.command()
    @commands.has_role("DEV")
    async def give(self, ctx, member: discord.Member, role: discord.Role):
        embed = discord.Embed(title="A new Admin Made.",
                              description=f"""{str(member.mention)} has been made admin!
                                You now have been admin and have access to admin commands like kick and ban!
                                You also have access to private channels too! Contact {str(owner)} for further details.
                                """, color=0x481C3C)

        await ctx.send(embed=embed)
        await member.add_roles(role)

    # Remove Admin/ROLE Error
    @give.error
    async def give_error(self, ctx, error):
        embed = discord.Embed(title="Error!",
                              description="You either ain't an admin or you missed the parameter of ROLE to be given.",
                              colour=0x481C3C)
        await ctx.send(embed=embed)


    # Remove Admin/ROLE Command
    @commands.command()
    @commands.has_role("DEV")
    async def fire(self, ctx, member: discord.Member, role: discord.Role):
        embed = discord.Embed(title="An Admin Removed.",
                              description=f"""Oh! {str(member.mention)} has been removed as an admin
                                You are no longer admin, contact <@814466820735631400> for more details!
                                """,
                              color=0x481C3C)
        await ctx.send(embed=embed)
        await member.remove_roles(role)

    # Remove Admin/ROLE Command (error)
    @fire.error
    async def fire_error(self, ctx, error):
        embed = discord.Embed(title="Admin Error",
                              description=error_message,
                              colour=0x481C3C)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_role("DEV")
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)


def setup(client):
    client.add_cog(Admin(client))
