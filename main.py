import discord
from discord.ext import commands
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions
from bs4 import BeautifulSoup


token = "x"

def getdata(link):
    options = ChromeOptions()
    browser = webdriver.Chrome(options=options)

    browser.get(link)
    html = browser.page_source
    time.sleep(2)
    soup = BeautifulSoup(html, 'html.parser')
    messages = soup.find_all("mr-2.5 text-xl self-center text-positive-main")
    for message in messages:
        return elem
    time.sleep(10)
    browser.quit()


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!!', intents=intents)

@bot.event
async def on_ready():
    print("Bot hazır, tarih: {date}".format(
        date=datetime.now()
    ))

@bot.command()
async def ping(ctx, link="www.google.com"):
    await ctx.send(getdata(link))


bot.run(token)