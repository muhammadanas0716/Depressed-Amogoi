from datetime import datetime
import discord
from discord.ext import commands
from geopy.geocoders import Nominatim
from main import color

loc = Nominatim(user_agent="GetLoc")


class Location(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def location(self, ctx, place_name):
        # Getting the Place NAME
        getLoc = loc.geocode(str(place_name))
        
        # Printing adress
        print(getLoc.address)
        icon="https://cdn.nerdschalk.com/wp-content/uploads/2021/10/how-to-see-your-friends-live-location-759x427.png?width=800"
        embed = discord.Embed(title=f"DEPRESSED Location", description=f"Place Name: {place_name}", color=color, timestamp=datetime.utcnow())
        embed.set_thumbnail(url=icon)
        embed.add_field(name="**Adress: **", value=f"{getLoc.address}", inline=False)
        embed.add_field(name="**Latitude: **", value=f"{getLoc.latitude}", inline=True)
        embed.add_field(name="**Longitude: **", value=f"{getLoc.longitude}", inline=True)
        await ctx.send(embed=embed)
        

def setup(bot):
    bot.add_cog(Location(bot))
