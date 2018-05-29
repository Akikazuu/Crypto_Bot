#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from time import strftime
from datetime import datetime
import discord, requests, json

def getDate():
    date = datetime.now()
    return strftime("%d-%m-%Y %H:%M:%S")

def getCoinLogo(coin):
    logos = {"NO": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/No-logo.svg/1280px-No-logo.svg.png",
            "BTC": "https://s2.coinmarketcap.com/static/img/coins/200x200/1.png",
            "ETH": "https://s2.coinmarketcap.com/static/img/coins/200x200/1027.png",
            "XRP": "https://s2.coinmarketcap.com/static/img/coins/200x200/52.png",
            "BCH": "https://s2.coinmarketcap.com/static/img/coins/200x200/1831.png",
            "LTC": "https://s2.coinmarketcap.com/static/img/coins/200x200/2.png",
            "EOS": "https://s2.coinmarketcap.com/static/img/coins/200x200/1765.png",
            "XMR": "https://s2.coinmarketcap.com/static/img/coins/200x200/328.png",
            "DASH": "https://s2.coinmarketcap.com/static/img/coins/200x200/131.png",
            "ADA": "https://s2.coinmarketcap.com/static/img/coins/200x200/2010.png",
            "XLM": "https://s2.coinmarketcap.com/static/img/coins/200x200/512.png",
            "NEO": "https://s2.coinmarketcap.com/static/img/coins/200x200/1376.png",
            "MIOTA": "https://s2.coinmarketcap.com/static/img/coins/200x200/1720.png",
            "TRX": "https://s2.coinmarketcap.com/static/img/coins/200x200/1958.png",
            "USDT": "https://s2.coinmarketcap.com/static/img/coins/200x200/825.png",
            "XEM": "https://s2.coinmarketcap.com/static/img/coins/200x200/873.png",
            "VEN": "https://s2.coinmarketcap.com/static/img/coins/200x200/1904.png",
            "BNB": "https://s2.coinmarketcap.com/static/img/coins/200x200/1839.png",
            "ETC": "https://s2.coinmarketcap.com/static/img/coins/200x200/1321.png",
            "QTUM": "https://s2.coinmarketcap.com/static/img/coins/200x200/1684.png",
            "XVG": "https://s2.coinmarketcap.com/static/img/coins/200x200/693.png",
            "OMG": "https://s2.coinmarketcap.com/static/img/coins/200x200/1808.png",
            "LSK": "https://s2.coinmarketcap.com/static/img/coins/200x200/1214.png",
            "ONT": "https://s2.coinmarketcap.com/static/img/coins/200x200/2566.png",
            "ICX": "https://s2.coinmarketcap.com/static/img/coins/200x200/2099.png",
            "BTG": "https://s2.coinmarketcap.com/static/img/coins/200x200/2083.png",
            "NANO": "https://s2.coinmarketcap.com/static/img/coins/200x200/1567.png",
            "ZEC": "https://s2.coinmarketcap.com/static/img/coins/200x200/1437.png",
            "BTM": "https://s2.coinmarketcap.com/static/img/coins/200x200/1866.png",
            "STEEM": "https://s2.coinmarketcap.com/static/img/coins/200x200/1230.png",
            "PPT": "https://s2.coinmarketcap.com/static/img/coins/200x200/1789.png",
            "DGD": "https://s2.coinmarketcap.com/static/img/coins/200x200/1229.png",
            "BCN": "https://s2.coinmarketcap.com/static/img/coins/200x200/372.png",
            "BCD": "https://s2.coinmarketcap.com/static/img/coins/200x200/2222.png",
            "BTS": "https://s2.coinmarketcap.com/static/img/coins/200x200/463.png",
            "SC": "https://s2.coinmarketcap.com/static/img/coins/200x200/1042.png",
            "STRAT": "https://s2.coinmarketcap.com/static/img/coins/200x200/1343.png",
            "WAVES": "https://s2.coinmarketcap.com/static/img/coins/200x200/1274.png",
            "DCR": "https://s2.coinmarketcap.com/static/img/coins/200x200/1168.png",
            "RHOC": "https://s2.coinmarketcap.com/static/img/coins/200x200/2021.png",
            "MKR": "https://s2.coinmarketcap.com/static/img/coins/200x200/1518.png",
            "DOGE": "https://s2.coinmarketcap.com/static/img/coins/200x200/74.png",
            "KMD": "https://s2.coinmarketcap.com/static/img/coins/200x200/1521.png",
            "MONA": "https://s2.coinmarketcap.com/static/img/coins/200x200/213.png",
            "ETN": "https://s2.coinmarketcap.com/static/img/coins/200x200/2137.png",
            "UBQ": "https://s2.coinmarketcap.com/static/img/coins/200x200/588.png",
            "ITNS": "https://s2.coinmarketcap.com/static/img/coins/200x200/2185.png",
            "BTCZ": "https://s2.coinmarketcap.com/static/img/coins/200x200/2041.png",
            "EVN": "https://s2.coinmarketcap.com/static/img/coins/200x200/2526.png",
            "HOT": "https://s2.coinmarketcap.com/static/img/coins/200x200/2682.png"
            
            }

    if coin in logos:
        return logos[coin]
    return None

def getCoinId(symbol):
    url = "https://api.coinmarketcap.com/v2/listings/"
    get = requests.get(url)
    ticker = get.json()

    coin_id = None
    for keys, values in ticker.items():
        if keys == "data":
            for coin in values:
                if symbol == coin["symbol"]:
                    coin_id = coin["id"]
                    break
    return coin_id

def getTickerData(money):
    coin_id = getCoinId(money.upper())

    if coin_id is None:
        return None

    url = "https://api.coinmarketcap.com/v2/ticker/" + str(coin_id) + "/?convert=EUR"
    ticker = requests.get(url)
    if ticker.status_code == 200:
        return ticker.json()
    return None

def getDataV2(ticker, coin):
    
    coin_name = ticker["data"]["name"]
    logo = getCoinLogo(coin.upper())
    if logo is None:
        logo = getCoinLogo("NO")

    if ticker["data"]["quotes"]["USD"]["price"] is not None:
        usd_price = "Current USD Price: `" + str(round(float(ticker["data"]["quotes"]["USD"]["price"]),6)) + "$`\n"
    else:
        usd_price = "?"
    
    if ticker["data"]["quotes"]["EUR"]["price"] is not None:
        eur_price = "Current EUR Price: `" + str(round(float(ticker["data"]["quotes"]["EUR"]["price"]),6)) + "€`\n"
    else:
        eur_price = "?"
    

    if ticker["data"]["quotes"]["USD"]["percent_change_1h"] is not None:
        changeNum_1 = float(ticker["data"]["quotes"]["USD"]["percent_change_1h"])
        sign = "+" if changeNum_1 > 0 else ""
        if sign == "+":
            change_1 = "`["+ sign + str(round(float(changeNum_1),3)) + "%]` " + "<:pump:433581031161856000>"
        else:
            change_1 = "`["+ sign + str(round(float(changeNum_1),3)) + "%]` " + "<:dump:433578647681630208>"
    else:
        change_1 = "?"


    if ticker["data"]["quotes"]["USD"]["percent_change_24h"] is not None:
        changeNum_24 = float(ticker["data"]["quotes"]["USD"]["percent_change_24h"])
        sign = "+" if changeNum_24 > 0 else ""
        if sign == "+":
            change_24 = "`["+ sign + str(round(float(changeNum_24),3)) + "%]` " + "<:pump:433581031161856000>"
        else:
            change_24 = "`["+ sign + str(round(float(changeNum_24),3)) + "%]` " + "<:dump:433578647681630208>"
    else:
        change_24 = "?"
    
    if ticker["data"]["quotes"]["USD"]["percent_change_7d"] is not None:
        changeNum_7 = float(ticker["data"]["quotes"]["USD"]["percent_change_7d"])
        sign = "+" if changeNum_7 > 0 else ""
        if sign == "+":
            change_7 = "`["+ sign + str(round(float(changeNum_7),3)) + "%]` " + "<:pump:433581031161856000>"
        else:
            change_7 = "`["+ sign + str(round(float(changeNum_7),3)) + "%]` " + "<:dump:433578647681630208>"
    else:
        change_7 = "?"



    price = usd_price + eur_price
    change = "1h :  " + change_1 + "\n24h : " + change_24 + "\n7j :  " + change_7
    
    embed = discord.Embed(title = "", description = "", color = 0xFF9900)
    embed.set_author(name = coin_name + " (" + coin.upper() + ")", icon_url = logo)
    embed.add_field(name = "Price", value = price, inline = False)
    embed.add_field(name = "Change", value = change, inline = False)
    embed.set_thumbnail(url = logo)
    embed.set_footer(text = "Powered by Akikazu and coinmarketcap.com")
    return embed

def getTop(number):
    url = "https://api.coinmarketcap.com/v2/ticker/?convert=EUR&limit=" + str(number)
    get = requests.get(url)
    ticker = get.json()
    embed_data = ""
    
    for key, coin_id in ticker.items():
        if key == "data":
            for keys in coin_id:
                name = "**" + ticker["data"][keys]["name"] + "** : "
                usd_price = str(round(float(ticker["data"][keys]["quotes"]["USD"]["price"]),6)) + "$"
                eur_price = str(round(float(ticker["data"][keys]["quotes"]["EUR"]["price"]),6)) + "€"
                changeNum_24 = float(ticker["data"][keys]["quotes"]["USD"]["percent_change_24h"])
                sign = "+" if changeNum_24 > 0 else ""
                if sign == "+":
                    change24 = " `["+ sign + str(round(float(changeNum_24),3)) + "%]` " + "<:pump:433581031161856000>"
                else:
                    change24 = " `["+ sign + str(round(float(changeNum_24),3)) + "%]` " + "<:dump:433578647681630208>"
    
                embed_data += str(ticker["data"][keys]["rank"]) + ". " + name + "`" + usd_price + "` | `" + eur_price + "` | " + change24 +  "\n"
        
    description = "Current ranking for the top "+ str(number) +" at " + getDate() + "\nCoin : USD | EUR | 24h\n\n" + embed_data
    header = "Top " + str(number) + " currency"
    embed = discord.Embed(title = "", description = description, color=0xFF9900)
    embed.set_author(name = header, icon_url = getCoinLogo("BTC"))
    embed.set_footer(text = "Powered by Akikazu and coinmarketcap.com")
    return embed

def getConv(ticker, number, coin):
    
    coin_name = ticker["data"]["name"]
    logo = getCoinLogo(coin.upper())
    if logo is None:
        logo = getCoinLogo("NO")

    conveur = float(ticker["data"]["quotes"]["EUR"]["price"]) * float(number)
    convusd = float(ticker["data"]["quotes"]["USD"]["price"]) * float(number)

    layout = "***1 " + coin_name + " = " + str(round(float(ticker["data"]["quotes"]["USD"]["price"]),5)) + "$ / " + str(round(float(ticker["data"]["quotes"]["EUR"]["price"]),5)) + "€***\n\n __Your conversion :__\n" + number + " **" + coin_name + "** = " + str(round(float(convusd),5)) + "$ / " + str(round(float(conveur),5)) + "€"

    embed = discord.Embed(title = "", description = layout, color = 0xFF9900)
    embed.set_author(name = coin_name + " (" + coin.upper() + ") at " + getDate(), icon_url = logo)
    embed.set_footer(text = "Powered by Akikazu and coinmarketcap.com")
    return embed