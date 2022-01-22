# Importing Modules
import os
from pydoc import cli
import discord
from discord.ext import commands

# Loading Intents
intents = discord.Intents.default()
intents.members = True

# Initializing client object and setting up command prefix, as well as GLOBAL VARIABLES
client = commands.Bot(command_prefix="dp ", intents=intents)
client.remove_command("help")
error_message = """You aren't a DEPRESSED admin. Contact <@814466820735631400> for further details!"""
OWNER = "<@814466820735631400>"
color = 0x481C3C


# On Ready Command
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("I am DEPRESSED and LONELY"))
    print("Bot OS ready to roll!")


# On Member Join Function
@client.event
async def on_member_join(member):
    print(f"{member} has hopped into the server")
    with open("commands/welcome.txt", "r") as f:
        lines = f.read()
    await member.send(f"{member.mention}, {lines}")
    print("Done!")


# Help Command
@client.command()
async def help(ctx):
    with open("commands/help.txt") as f:
        all_commands = f.read()
    embed = discord.Embed(title="All Available Commands",
                            description=all_commands, color=color)
    await ctx.send(embed=embed)

# Rules Command
@client.command()
async def rules(ctx):
    with open("commands/rules.txt") as f:
        all_rules = f.read()
    embed = discord.Embed(
        title="Rules", description=all_rules, color=color)
    await ctx.send(embed=embed)



# /\/\/\/\/\/ *****IMPORTING AND USING COGS ***** /\/\/\/\/\/
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

# Run the Bot
client.run("ODkwNDk4MjY2Nzg4MTYzNjE2.YUwrIw.TzjSxoIqOWLKOfqGAIdOqSAMRPE")
