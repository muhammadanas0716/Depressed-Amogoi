import discord
from discord.ext import commands
from main import error_message
from main import client

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    #  Add Admin/ROLE Commmand (error)
    @client.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Missing Parameter", description="Enter the role you want to give!", color=0x481C3C)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingROle):
            embed2 = discord.Embed(title="ERROR", description=f"{error_message}", color=0x481C3C)
            await ctx.send(embed=embed2)

    # Add Admin/ROLE Command
    @commands.command()
    @commands.has_role("DEV")
    async def add(self, ctx, member: discord.Member, role: discord.Role):
        embed = discord.Embed(title="A new Admin Made.",
                              description=f"""{str(member.mention)} has been made admin!
                                You now have been admin and have access to admin commands like kick and ban!
                                You also have access to private channels!
                                """, color=0x481C3C)

        await ctx.send(embed=embed)
        await member.add_roles(role)




    # Remove Admin/ROLE Command
    @commands.command()
    @commands.has_role("DEV")
    async def remove(self, ctx, member: discord.Member, role: discord.Role):
        embed = discord.Embed(title="An Admin Removed.",
                              description=f"""Oh! {str(member.mention)} has been removed as an admin
                                You are no longer admin, contact <@814466820735631400> for more details!
                                """,
                              color=0x481C3C)
        await ctx.send(embed=embed)
        await member.remove_roles(role)

    # Remove Admin/ROLE Command (error)
    @remove.error
    async def remove_error(self, ctx, error):
        embed = discord.Embed(title="Admin Error",
                              description=error_message,
                              colour=0x481C3C)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_role("DEV")
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)
        message = await ctx.channel.send(f"{limit} messages have been deleted")





def setup(client):
    client.add_cog(Admin(client))
