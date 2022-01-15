# Importing Modules
import os
import discord
from discord.ext import commands

# Loading Intents
intents = discord.Intents.default()
intents.members = True

# Initializing client object and setting up command prefix, as well as GLOBAL VARIABLES
client = commands.Bot(command_prefix="dp ", intents=intents)
client.remove_command("help")
error_message = """You aren't a DEPRESSED admin. If you are, you might have typed something incorrect. Contact <@814466820735631400> for further details!"""
owner = "<@814466820735631400>"
color = 0x481C3C


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


# Show Stats of server
@client.command()
async def stats(ctx):
    true_member_count = len([m for m in ctx.guild.members if not m.bot])
    embed = discord.Embed(title="Lorem Ipsum Stats....",
                          description=f"""
                          **USERS:** We have **{true_member_count}** DEPRESSED users.
                          """,
                          color=color)

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
        title="Rules", description=all_rules, color=color)
    await ctx.send(embed=embed)


# Show all available commands
@client.command()
async def help(ctx):
    with open("commands/all_commands.txt") as f:
        all_commands = f.read()
    embed = discord.Embed(title="All Commands",
                          description=all_commands, color=color)
    await ctx.send(embed=embed)


# /\/\/\/\/\/ *****IMPORTING AND USING COGS ***** /\/\/\/\/\/
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

# Run the Bot
client.run("ODkwNDk4MjY2Nzg4MTYzNjE2.YUwrIw.TzjSxoIqOWLKOfqGAIdOqSAMRPE")
