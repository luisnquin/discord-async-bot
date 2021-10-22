from discord.ext import commands
import discord

from urllib import parse, request
from datetime import datetime
import re

bot = commands.Bot(command_prefix='>', description='Helper bot')
#>[ping, sum, stats, cat, youtube]

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def sum(ctx, n1:int, n2:int):
    await ctx.send(f"Result: {n1 + n2}")

@bot.command()
async def stats(ctx):
    embed = discord.Embed(title="Stats", description="Description about something we don't know", timestamp=datetime.utcnow(), color=discord.Color.blurple())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    await ctx.send(embed=embed)

@bot.command()
async def cat(ctx):
    embed=discord.Embed(title="cat", description="meow")
    embed.set_thumbnail(url="https://es.m.wikipedia.org/wiki/Archivo:Cat_November_2010-1a.jpg")
    await ctx.send(embed=embed)

@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall('watch\?v=(.{11})', html_content.read().decode())
    print(search_results)
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Bot is activated but, Twitch??", url="https://www.twitch.tv/skuldklm"))
    print('My bot is ready')



bot.run('OTAxMTk4ODA4NTk4MzE5MTA1.YXMYyw.MyAADrmutao2aGkYxtQN3KHOPCg')