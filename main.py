import os
import discord
import random
import requests
import asyncio
import keep_alive

from discord.ext import commands

intents = discord.Intents.all()

coinlist = ["Heads", "Tails"]

doglist = [
  "https://media0.giphy.com/media/Y4qGpiECSsduijMo7i/giphy.gif?cid=ecf05e4770tp1pezg9pf8u9g0jdllhm6p7fjdfjf85kug6kd&rid=giphy.gif&ct=g",
  "https://media.giphy.com/media/eeUJaTwsHh3tswkaYm/giphy.gif",
  "https://media.giphy.com/media/gFW9rRpOkMRBY2KF6s/giphy.gif",
  "https://media.giphy.com/media/2vmgb8ZGaeBsuSeo5I/giphy.gif",
  "https://media.giphy.com/media/9rtpurjbqiqZXbBBet/giphy.gif",
  "https://media.giphy.com/media/m0MfjLtKOgTPG/giphy.gif",
  "https://media.giphy.com/media/NmGbJwLl7Y4lG/giphy.gif",
  "https://media.giphy.com/media/3o85xsGXVuYh8lM3EQ/giphy.gif",
  "https://media.giphy.com/media/naXyAp2VYMR4k/giphy.gif",
  "https://media.giphy.com/media/k2Da0Uzaxo9xe/giphy.gif",
  "https://media.giphy.com/media/y4PQTcLTYJwOI/giphy.gif",
  "https://media.giphy.com/media/apCyQKrrVwCXuRtd1O/giphy.gif",
  "https://media.giphy.com/media/26DMZwX57QxPoqZPy/giphy.gif",
  "https://media.giphy.com/media/fMS9fSkCgK68E/giphy.gif",
  "https://media.giphy.com/media/10YNI9aU5LQR68/giphy.gif"
]

#add your prefix as an ! for your bot commands
bot = commands.Bot(command_prefix='!dill', intents=intents)
#awasda

#print a message to the console when your bot is online
@bot.event
async def on_connect():
  print("online")


#
@bot.command()
async def hello(ctx):
  await ctx.reply("Hello from dillbot")


@bot.command()
async def play(ctx):
  ship = '🚢'
  cross = '❌'
  reactlist = [ship, cross]
  message = await ctx.reply(
    "What Game Would You Like to Play? \n:ship: Battleship")
  await message.add_reaction(ship)
  await message.add_reaction(cross)

  def check(reaction, user):
    return user == ctx.author and str(reaction.emoji) in reactlist

  battleship = await bot.wait_for("reaction_add", check=check)

  battleship = await bot.wait_for("reaction_add", check=check)

  if battleship:
    await asyncio.sleep(0.5)
    await message.delete()
    await ctx.reply("@ the person you would like to challenge")
  elif cross:
    await message.delete()


#use a Joke API to get a joke setup, wait a few seconds
#and deliver the punchline
@bot.command()
async def joke(ctx):
  url = "https://official-joke-api.appspot.com/random_joke"

  req = requests.get(url)

  #data variable that holds the json data that the api holds
  data = req.json()

  #pull the joke setup form the json data
  setup = data["setup"]

  await ctx.send(setup)

  punchline = data["punchline"]

  await asyncio.sleep(2)

  await ctx.send(punchline)


@bot.command()
async def weather(ctx, zip):

  my_secret_weather = os.environ['weatherapikey']

  url = "https://api.openweathermap.org/data/2.5/weather?zip=" + zip + ",us&appid=" + my_secret_weather

  req = requests.get(url)

  #data variable that holds the json data that the api holds
  data = req.json()

  desc = data["weather"][0]["description"]
  location = data["name"]
  kelvin = data["main"]["temp"]
  K = int(kelvin)
  degrees = 1.8 * (K - 273) + 32
  F = str(degrees)

  await ctx.send(F + "°F, " + desc + " in " + location)


@bot.command()
async def dog(ctx):
  await ctx.reply(random.choice(doglist))


@bot.command()
async def flip(ctx):
  message = await ctx.reply(
    "https://media.tenor.com/bd3puNXKLwUAAAAC/coin-toss.gif")
  await asyncio.sleep(1)
  await message.delete()
  await ctx.reply(random.choice(coinlist))


@bot.command()
async def IPinfo(ctx, ip):
  url = "https://ipinfo.io/" + ip + "/geo"

  req = requests.get(url)

  data = req.json()

  city = data["city"]
  region = data["region"]
  country = data["country"]
  timezone = data["timezone"]

  await ctx.reply("City: " + city + "\nState: " + region + "\nCountry: " +
                  country + "\nTimezone: " + timezone + ".")


@bot.command()
async def blur(ctx):
  printlist=["a", "b", "c", "d", "e","f", "g", "h", "i", "j","k", "l", "m", "n", "o","p", "q", "r", "s", "t","u", "v", "w", "x", "y", "z", "-", "/", "_", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", ":"]
  message = ctx.message
  for attachment in message.attachments:
    img = attachment.url
  url = "https://api.apilayer.com/face_pixelizer/url?url=" + img

  payload = {}
  headers = {"apikey":"Sz8div64BU43dql72fPmqcxMkGbJWQRJ"}

  response = requests.request("GET", url, headers=headers, data=payload)
  result = response.text
  result2=""
  for char in result:
    if char in printlist:
      result2 += char
  await ctx.reply(result2[7:])

keep_alive.keep_alive()
my_secret = os.environ['token']
bot.run(my_secret)