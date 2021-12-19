import asyncio

import discord
from discord.ext import commands
from datetime import date, datetime

class Work(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Classwork Command
    @commands.command()
    async def classwork(self, ctx):
        with open("commands/classwork.txt") as f:
            classwork = f.read()
            embed = discord.Embed(
                title=f"Classwork - {date.today()}", description=classwork, color=0x481C3C)
        await ctx.send(embed=embed)

    @commands.command()
    async def update_classwork(self, ctx, *, classwork):
        with open("commands/classwork.txt", "w+") as f:
            f.writelines(classwork)
            f.write("\n")
        await ctx.send(f"I have updated Classwork😀")

    # Homework Command
    @commands.command()
    async def homework(self, ctx):
        with open("commands/homework.txt") as f:
            homework = f.read()
            embed = discord.Embed(
                title=f"Homework - {date.today()}", description=homework, color=0x481C3C)
        await ctx.send(embed=embed)

    @commands.command()
    async def update_homework(self, ctx, *, homework):
        with open("commands/homework.txt", "w+") as f:
            f.writelines(homework)
            f.write("\n")
        await ctx.send(f"I have updated Homework😀")

    @commands.command()
    async def reminder(self, ctx, member: discord.Member = None, time="5m", *, reminder):
        print(f"Reminder: {reminder}")
        print(f"Time: {time}")
        print(f"By: {ctx.author}")
        embed = discord.Embed(color=0x481C3C, timestamp=datetime.utcnow())
        seconds = 0
        if reminder is None:
            embed.add_field(name='Warning',
                            value='Please specify what do you want me to remind you about.')  # Error message
        if str(time.lower()).endswith("d"):
            seconds += int(time[:-1]) * 60 * 60 * 24
            counter = f"{seconds // 60 // 60 // 24} days"
        if str(time.lower()).endswith("h"):
            seconds += int(time[:-1]) * 60 * 60
            counter = f"{seconds // 60 // 60} hours"
        elif str(time.lower()).endswith("m"):
            seconds += int(time[:-1]) * 60
            counter = f"{seconds // 60} minutes"
        elif str(time.lower()).endswith("s"):
            seconds += int(time[:-1])
            counter = f"{seconds} seconds"
        if seconds == 0:
            embed.add_field(name='Warning',
                            value='Please specify a proper duration, send `reminder_help` for more information.')
        elif seconds < 0:
            embed.add_field(name='Warning',
                            value='You have specified a too short duration!\nMinimum duration is 5 minutes.')
        elif seconds > 7776000:
            embed.add_field(name='Warning',
                            value='You have specified a too long duration!\nMaximum duration is 90 days.')
        else:
            await ctx.send(
                f"Alright {ctx.author.mention}, I will remind {member} in {counter}.")
            await asyncio.sleep(seconds)
            await ctx.send(
                f"Hi {member.mention}, {ctx.author.mention} asked me to remind you about {reminder} {counter} ago.")
            return
        await ctx.send(embed=embed)




def setup(client):
    client.add_cog(Work(client))
