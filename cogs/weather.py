from turtle import color
from discord.ext import commands
from matplotlib.pyplot import title
import requests, json, discord
from main import color

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


class Weather(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def weather(self, ctx, city_name):
        api_key = "c81a6ba0dc041f053faa361c6428bd5d"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        
        if x["cod"] != "404":
        
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]

            
            description = "Weather Forcast API"
            embed = discord.Embed(
                title="Weather Forcast",
                description=description,
                color=color
            )
            icon="https://www.timeanddate.com/scripts/weather_og.php?h1=Weather&h2=Local%20Weather%20Around%20the%20World"
            embed.set_thumbnail(url=icon)
            embed.add_field(name="**Location:**", value=f"{city_name}", inline=True)
            embed.add_field(name="**Temperature:**", value=f"{int(current_temperature-273)}°C", inline=True)
            embed.add_field(name="**Pressure:**", value=f"{current_pressure} Pressure", inline=True)
            embed.add_field(name="**Humidity:**", value=f"{current_humidity}%", inline=True)
            embed.add_field(name="**Info:**", value=f"{weather_description}", inline=True)

            await ctx.send(embed=embed)
        else:
            await ctx.send("City not Found")


def setup(client):
    client.add_cog(Weather(client))
