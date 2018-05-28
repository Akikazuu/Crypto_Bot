#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import datetime
from datetime import datetime, timedelta
import coinmarketcap

Client = discord.Client()
bot = commands.Bot(command_prefix = "?")

channelethos = discord.Object(id = "432260844110479360")
channellmf = discord.Object(id = "295660477386850314")
channelserya = discord.Object(id = "424979780899700749")


<<<<<<< HEAD
def helpPLZ():
    description = "Type **?<coin>** to printout the info of this coin\n" + "Type **?conv <amount> <coin>** to printout the X coin conversion to € / $\n" + "Type **?top <amount>** to printout the top X coin\n" + "(List of coin in coinmarketcap.com only)"
    embed = discord.Embed(title = ":information_source: Bot helper", description = "", color = 0x3f89c1)
    embed.add_field(name = "Commands :", value = description, inline = False)
    embed.add_field(name = "Version :", value = "`v1.0`", inline = False)
=======
def HelpPLZ():
    description = "Type **?<coin>** to printout the info of this coin\n" + "Type **?conv <amount> <coin>** to printout the X coin conversion to € / $\n" + "Type **?top <amount>** to printout the top X coin\n" + " (List of coin in coinmarketcap.com only)"
    embed = discord.Embed(title = "Bot helper", description = description, color = 0xFF9900)
>>>>>>> a74806a7d4a8ff14e2f27cb2e3a938de422ea2fe
    embed.set_footer(text = "Developed by Akikazu, host by Antho")
    return embed

def error(coin):
        embed = discord.Embed(title = ":no_entry_sign: Error", description = ":warning: Coin : " + coin.upper() + " not found in coinmarketcap API", color = 0xBC1D35)
        embed.set_footer(text = "Contact Akikazu if the currency exists in coinmarketcap.com")
        return embed

def getCoin(coin):
    ticker = coinmarketcap.getTickerData(coin)
    if ticker is None:
        return error(coin)
    else:
        return coinmarketcap.getData(ticker, coin)

def getConv(number, coin):
    ticker = coinmarketcap.getTickerData(coin)
    if ticker is None:
        return error(coin)
    else:
        return coinmarketcap.getConv(ticker, number, coin)

@bot.event
async def on_ready():
    print("Bot is online")
    print(datetime.today())

@bot.event
async def Top10():
    await bot.wait_until_ready()
    while not bot.is_closed:
        embed = coinmarketcap.getTop(10)
        await bot.send_message(channelethos, embed = embed)
        await bot.send_message(channellmf, embed = embed)
        await bot.send_message(channelserya, embed = embed)
        await asyncio.sleep(3600)

@bot.event
async def Purge():
    await bot.wait_until_ready()
    while not bot.is_closed:
        yesterday = datetime.today() - timedelta(days = 1)
        await bot.purge_from(channelethos, before = yesterday)
       # await bot.purge_from(channellmf, before = yesterday)

        print("PURGE NOW !")
        await asyncio.sleep(3600)

@bot.event
async def on_message(message):

    msg = message.content.lower()
    words = msg.split()
    target = discord.Object(id = message.channel.id)

    if target.id == channelethos.id or target.id == channellmf.id or target.id == channelserya.id:
        if msg.startswith("?"):

            cmd = words[0][1:]

            if len(words) == 1:
                rep = getCoin(str(cmd))
                    
            if len(words) == 2:
                number = words[1]
                if cmd == "top":
                    rep = coinmarketcap.getTop(number)

            if len(words) == 3:
                number = words[1]
                coin = words[2]
                if cmd == "conv":
                    rep = getConv(number,coin)

            if cmd == "help":
<<<<<<< HEAD
                rep = helpPLZ()
=======
                rep = HelpPLZ()
>>>>>>> a74806a7d4a8ff14e2f27cb2e3a938de422ea2fe
                
            if rep:
                await bot.send_message(target, embed = rep)
            
bot.loop.create_task(Top10())
bot.loop.create_task(Purge())
bot.run("NDMyMjA2MDc1MDEwMzUxMTA0.Daqr7A.4uR5KqXcVKCxVOiq9O5IOU5B0ZU")
