# Importing Modules
import os
import discord
from discord.ext import commands

# Loading Intents
intents = discord.Intents.default()
intents.members = True

# Initializing client object and setting up command prefix, as well as GLOBAL VARIABLES
client = commands.Bot(command_prefix="dp ", intents=intents)
error_message = """You aren't a DEPRESSED admin. If you are, you might have typed something incorrect. Contact <@814466820735631400> for details!"""
owner = "<@814466820735631400>"
admin_users = ["<@814466820735631400>"]


# On Ready Command
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("I am DEPRESSED and LONELY"))
    print("Bot OS ready to roll!")


# On Member Join Function
@client.event
async def on_member_join(member):
    print(f"{member} has hopped into the server")
    with open("commands/welcome.txt", "r") as f:
        lines = f.read()
    await member.send(f"{member.mention}, {lines}")
    print("Done")


# Show number of Users in Server
@client.command()
async def users(ctx):
    # Doesn't Include Bots
    true_member_count = len([m for m in ctx.guild.members if not m.bot])
    embed = discord.Embed(title="Member Count....",
                          description=f"We have **{true_member_count}** DEPRESSED users, excluding bots",
                          color=0x481C3C)

    await ctx.send(embed=embed)


# Ping Command
@client.command()
async def ping(ctx):
    await ctx.channel.send(f"Pong {ctx.message.author.mention}")


# Show rules Command
@client.command()
async def rules(ctx):
    with open("commands/rules.txt") as f:
        all_rules = f.read()
    embed = discord.Embed(
        title="Rules", description=all_rules, color=0x481C3C)
    await ctx.send(embed=embed)


# Show all available commands
@client.command()
async def commands(ctx):
    with open("commands/all_commands.txt") as f:
        all_commands = f.read()
    embed = discord.Embed(title="All Commands",
                          description=all_commands, color=0x481C3C)
    await ctx.send(embed=embed)


# /\/\/\/\/\/ *****IMPORTING AND USING COGS ***** /\/\/\/\/\/
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

# Run the Bot
client.run("ODkwNDk4MjY2Nzg4MTYzNjE2.YUwrIw.E4T1xR5gHksPxqSPHLhNedNhjpc")
