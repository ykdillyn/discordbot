import os
import discord
from discord.ui import Button, View
from discord.ext import commands
import random
import requests
import asyncio
import keep_alive
from grid4 import gridfour
from grid3 import gridthree
from grid2 import gridlist2
from grid1 import gridlist
intents = discord.Intents.all()
intents.members = True

p1=""
p2=""
turn=""

my_secret = os.environ['token']
blur_api = os.environ['blurapi']
my_secret_weather = os.environ['weatherapikey']

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

help = commands.DefaultHelpCommand(no_category='Commands')
#add your prefix as an ! for your bot commands
bot = commands.Bot(command_prefix='!dill', intents=intents, help=help)

#print a message to the console when your bot is online
@bot.event
async def on_connect():
  print("online")


@bot.command(brief='Get greeted by dillbot')
async def hello(ctx):
  await ctx.reply("Hello from dillbot")

@bot.command(brief='WORK IN PROGRESS')
async def bship(ctx, p2: discord.Member):
  movelist=["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "G10", "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "I1", "I2", "I3", "I4", "I5", "I6", "I7", "I8", "I9", "I10", "J1", "J2", "J3", "J4", "J5", "J6", "J7", "J8", "J9", "J10"]
  confirm_button = Button(label="Confirm", style = discord.ButtonStyle.green, emoji = "✔️")
  cancel_button = Button(label="Cancel", style = discord.ButtonStyle.red, emoji = "❌")
  p1 = ctx.author
  view=View()
  view.add_item(confirm_button)
  view.add_item(cancel_button)

  async def randgrid(user, list, map):
    x = random.randint(0,4)
    map = list[x]
    await user.send(map)
    print(x)
    print(map)

  async def game():
    turn = random.randint(0,1)
    if turn == 0:
      await p2.send(str(p1) + " TURN")
      await p1.send("YOUR TURN")
    elif turn == 1:
      await p2.send("YOUR TURN")
      await p1.send(str(p2) + " TURN")
    


  message = await p2.send( "Battleship game with " + str(p1) + " ?", view=view)
  async def confirm(interaction):
    map1=""
    map2=""
    await message.delete()
    await p2.send("BATTLESHIP GAME AGAINST " + str(p1))
    gridthree = open("gridthree.txt", "r")
    await p2.send(gridthree.read())
    await randgrid(p2, gridlist, map1)
    await p1.send("BATTLESHIP GAME AGAINST " + str(p2))
    gridfour = open("gridfour.txt", "r")
    await p1.send(gridfour.read())
    await randgrid(p1, gridlist2, map2)
    await game()
    

  async def cancel(interaction):
    await message.delete()

  confirm_button.callback=confirm
  cancel_button.callback=cancel

#use a Joke API to get a joke setup, wait a few seconds
#and deliver the punchline
@bot.command(brief='Receive a joke')
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


@bot.command(brief='Enter a zip code and receive the weather and location')
async def weather(ctx, zip):

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


@bot.command(brief='Recieve a random dog GIF')
async def dog(ctx):
  await ctx.reply(random.choice(doglist))


@bot.command(brief='Flip a coin')
async def flip(ctx):
  message = await ctx.reply(
    "https://media.tenor.com/bd3puNXKLwUAAAAC/coin-toss.gif")
  await asyncio.sleep(1)
  await message.delete()
  await ctx.reply(random.choice(coinlist))


@bot.command(brief='Enter an IP address and receive the city, state, country, and timezone')
async def IP(ctx, ip):
  url = "https://ipinfo.io/" + ip + "/geo"

  req = requests.get(url)

  data = req.json()

  city = data["city"]
  region = data["region"]
  country = data["country"]
  timezone = data["timezone"]

  await ctx.reply("City: " + city + "\nState: " + region + "\nCountry: " +
                  country + "\nTimezone: " + timezone + ".")


@bot.command(brief='Enter an image (2048x1152) and receive the image with faces blurred')
async def blur(ctx):
  printlist=["a", "b", "c", "d", "e","f", "g", "h", "i", "j","k", "l", "m", "n", "o","p", "q", "r", "s", "t","u", "v", "w", "x", "y", "z", "-", "/", "_", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", ":"]
  message = ctx.message
  for attachment in message.attachments:
    img = attachment.url
  url = "https://api.apilayer.com/face_pixelizer/url?url=" + img

  payload = {}
  headers = {"apikey":blur_api}

  response = requests.request("GET", url, headers=headers, data=payload)
  result = response.text
  result2=""
  for char in result:
    if char in printlist:
      result2 += char
  await ctx.reply(result2[7:])

keep_alive.keep_alive()
bot.run(my_secret)