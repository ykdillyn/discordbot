import os
import discord
from discord.ui import Button, Select, View
from discord.ext import commands
import random
import requests
import asyncio
import keep_alive

intents = discord.Intents.all()
intents.members = True

p1 = ""
p2 = ""
turn = ""

token = os.environ['token']
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
  option1 = open("option1.txt", "r")
  option2 = open("option2.txt", "r")
  option3 = open("option3.txt", "r")
  option4 = open("option4.txt", "r")
  option5 = open("option5.txt", "r")
  option6 = open("option6.txt", "r")
  option7 = open("option7.txt", "r")
  option8 = open("option8.txt", "r")
  option9 = open("option9.txt", "r")
  option10 = open("option10.txt", "r")
  gridlist = [
    option1, option2, option3, option4, option5, option6, option7, option8,
    option9, option10
  ]
  
  confirm_button = Button(label="Confirm",
                          style=discord.ButtonStyle.green,
                          emoji="✔️")
  cancel_button = Button(label="Cancel",
                         style=discord.ButtonStyle.red,
                         emoji="❌")
  p1 = ctx.author
  view = View()
  view.add_item(confirm_button)
  view.add_item(cancel_button)

  async def randgrid():
    global map1
    global map2
    x = random.randint(0, 9)
    map1 = gridlist[x]
    map1 = map1.read()
    await p1.send(map1)
    print(x)
    y = random.randint(0, 9)
    map2 = gridlist[y]
    map2 = map2.read()
    await p2.send(map2)
    print(y)

  async def game():
    global gridmsg1
    global gridmsg2
    global gridone
    global gridtwo
    global newgridone
    global newgridtwo
    global z
    global ze
    global turn
    fire_button = Button(label="Fire",
                         style=discord.ButtonStyle.green,
                         emoji="💣")
    view3 = View()
    view3.add_item(fire_button)

    z=0
    ze=0
    location = 0
    location2 = 0
    location3 = 0
    select = Select(options=[
      discord.SelectOption(
        label="A",
        default=True,
      ),
      discord.SelectOption(label="B", ),
      discord.SelectOption(label="C", ),
      discord.SelectOption(label="D", ),
      discord.SelectOption(label="E", ),
      discord.SelectOption(label="F", ),
      discord.SelectOption(label="G", ),
      discord.SelectOption(label="H", ),
      discord.SelectOption(label="I", ),
      discord.SelectOption(label="J", )
    ])

    select2 = Select(options=[
      discord.SelectOption(
        label="1",
        default=True,
      ),
      discord.SelectOption(label="2", ),
      discord.SelectOption(label="3", ),
      discord.SelectOption(label="4", ),
      discord.SelectOption(label="5", ),
      discord.SelectOption(label="6", ),
      discord.SelectOption(label="7", ),
      discord.SelectOption(label="8", ),
      discord.SelectOption(label="9", ),
      discord.SelectOption(label="10", )
    ])

    async def callback(interaction):
      global gridmsg1
      global gridmsg2
      global gridone
      global gridtwo
      global newgridone
      global newgridtwo
      global z
      global ze
      global turn
      if select.values[0] == "A":
        location = 0
      elif select.values[0] == "B":
        location = 1
      elif select.values[0] == "C":
        location = 2
      elif select.values[0] == "D":
        location = 3
      elif select.values[0] == "E":
        location = 4
      elif select.values[0] == "F":
        location = 5
      elif select.values[0] == "G":
        location = 6
      elif select.values[0] == "H":
        location = 7
      elif select.values[0] == "I":
        location = 8
      elif select.values[0] == "J":
        location = 9

      if select2.values[0] == "1":
        location2 = 0
      elif select2.values[0] == "2":
        location2 = 11
      elif select2.values[0] == "3":
        location2 = 22
      elif select2.values[0] == "4":
        location2 = 33
      elif select2.values[0] == "5":
        location2 = 44
      elif select2.values[0] == "6":
        location2 = 55
      elif select2.values[0] == "7":
        location2 = 66
      elif select2.values[0] == "8":
        location2 = 77
      elif select2.values[0] == "9":
        location2 = 88
      elif select2.values[0] == "10":
        location2 = 99
      location3 = location + location2
      if turn == 0:
        z = int(location3)
        print(z)
        newgridone = gridone[0:z]+gridone[z:].replace("⬛","❌",1)
        print(newgridone)
        await gridmsg1.edit(content=newgridone)
      elif turn == 1:
        ze = int(location3)
        print(ze)
        newgridtwo = gridtwo[0:ze]+gridtwo[ze:].replace("⬛","❌",1)
        print(newgridtwo)
        await gridmsg2.edit(content=newgridtwo)
      await interaction.response.defer()

    async def fire(interaction):
      global gridmsg1
      global gridmsg2
      global gridone
      global gridtwo
      global newgridone
      global newgridtwo
      global z
      global ze
      global turn
      if turn == 0:
        newgridone = newgridone[0:z]+newgridone[z:].replace("❌","⬛",1)
        if map2[z] == "🟦":
          await r1.delete()
          await c1.delete()
          await fire.delete()
          await p1.send("MISS")
          newgridone = newgridone[0:z]+newgridone[z:].replace("⬛","⬜",1)
          await gridmsg1.edit(content=newgridone)
          turn = 1
          await game()
        elif map2[z] == "🚢":
          await p1.send("HIT. GO AGAIN")
          newgridone = newgridone[0:z]+newgridone[z:].replace("⬛","🟥",1)
          await gridmsg1.edit(content=newgridone)
      elif turn == 1:
        newgridtwo = newgridtwo[0:z]+newgridtwo[z:].replace("❌","⬛",1)
        if map1[ze] == "🟦":
          await r2.delete()
          await c2.delete()
          await fire.delete()
          await p2.send("MISS")
          newgridtwo = newgridtwo[0:ze]+newgridtwo[ze:].replace("⬛","⬜",1)
          await gridmsg2.edit(content=newgridtwo)
          turn = 0
          await game()
        elif map1[ze] == "🚢":
          await p2.send("HIT. GO AGAIN")
          newgridtwo = newgridtwo[0:ze]+newgridtwo[ze:].replace("⬛","🟥",1)
          await gridmsg2.edit(content=newgridtwo)

    fire_button.callback = fire

    select.callback = callback
    select2.callback = callback
    view = View()
    view2 = View()
    view.add_item(select)
    view2.add_item(select2)
    
    if turn == 0:
      await p2.send(str(p1) + " TURN")
      c1 = await p1.send("**CHOOSE A COLUMN**", view=view)
      r1 = await p1.send("**CHOOSE A ROW**", view=view2)
      fire = await p1.send("--------------------------------------",
                           view=view3)

    elif turn == 1:
      await p1.send(str(p2) + " TURN")
      c2 = await p2.send("**CHOOSE A COLUMN**", view=view)
      r2 = await p2.send("**CHOOSE A ROW**", view=view2)
      fire = await p2.send("--------------------------------------",
                           view=view3)

  message = await p2.send("Battleship game with " + str(p1) + " ?", view=view)

  async def confirm(interaction):
    global gridmsg1
    global gridmsg2
    global gridone
    global gridtwo
    global newgridone
    global newgridtwo
    global z
    global ze
    global turn
    await message.delete()
    await p2.send("BATTLESHIP GAME AGAINST " + str(p1))
    await p1.send("BATTLESHIP GAME AGAINST " + str(p2))
    await randgrid()
    gridone = open("gridone.txt", "r")
    gridtwo = open("gridtwo.txt", "r")
    gridone=gridone.read()
    gridtwo=gridtwo.read()
    gridmsg1 = await p1.send(gridone)
    gridmsg2 = await p2.send(gridtwo)
    turn = random.randint(0, 1)
    await game()

  async def cancel(interaction):
    await message.delete()

  confirm_button.callback = confirm
  cancel_button.callback = cancel


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


@bot.command(
  brief='Enter an IP address and receive the city, state, country, and timezone'
)
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


@bot.command(
  brief='Enter an image (2048x1152) and receive the image with faces blurred')
async def blur(ctx):
  printlist = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "-", "/", "_", "1",
    "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", ":"
  ]
  message = ctx.message
  for attachment in message.attachments:
    img = attachment.url
  url = "https://api.apilayer.com/face_pixelizer/url?url=" + img

  payload = {}
  headers = {"apikey": blur_api}

  response = requests.request("GET", url, headers=headers, data=payload)
  result = response.text
  result2 = ""
  for char in result:
    if char in printlist:
      result2 += char
  await ctx.reply(result2[7:])


keep_alive.keep_alive()

bot.run(token)
