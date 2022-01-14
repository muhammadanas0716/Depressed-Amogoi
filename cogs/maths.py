import math

import discord
import numpy as np
from discord.ext import commands
from sympy import N
from main import color


class Trignometry(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pi(self, ctx, decimal_places=2):
        pi_value = math.pi
        await ctx.send(f"The value of **pi** rounded to 3 decimal places is as follows: `{pi_value.__round__(decimal_places)}`")

    @commands.command()
    async def sin(self, ctx, num):
        await ctx.send(f"The value of **sin** {num} is as follow: `{math.sin(int(num))}`")

    @commands.command()
    async def cos(self, ctx, num):
        await ctx.send(f"The value of **cos** {num} is `{math.cos(int(num))}`")

    @commands.command()
    async def tan(self, ctx, num):
        await ctx.send(f"The value of **tan** {num} is as follows `{math.tan(int(num))}`")

    @commands.command()
    async def sinh(self, ctx, num):
        await ctx.send(f"The value of **sinh** {num} is as follows `{math.sinh(int(num))}`")

    @commands.command()
    async def cosh(self, ctx, num):
        await ctx.send(f"The value of **cosh** {num} is as follows: `{math.cosh(int(num))}`")

    @commands.command()
    async def tanh(self, ctx, num):
        await ctx.send(f"The value of **tanh** {num} is as follows: `{math.tanh(int(num))}`")


class Calc(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def calc(self, ctx, arg):
        answer = N(arg)
        ans = np.format_float_positional(answer, trim='-')
        embed = discord.Embed(title='{0} = {1}'.format(arg, ans), color=color)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Trignometry(client))
    client.add_cog(Calc(client))
