#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from time import strftime
from datetime import datetime
import discord, requests, json

def getDate():
    date = datetime.now()
    return strftime("%Y-%m-%d %H:%M:%S")

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

def getCoinName(coin):
    names = {"BCN": "Bytecoin",
             "BELA": "Belacoin",
             "BLK": "BlackCoin",
             "BTCD": "BitcoinDark",
             "BTM": "Bitmark",
             "BTS": "BitShares",
             "BURST": "Burst",
             "GNT": "Golem",
             "CLAM": "CLAMS",
             "DASH": "Dash",
             "DGB": "DigiByte",
             "DOGE": "Dogecoin",
             "EMC2": "Einsteinium",
             "FLDC": "FoldingCoin",
             "FLO": "Florincoin",
             "GAME": "GameCredits",
             "GRC": "Gridcoin Research",
             "HUC": "Huntercoin",
             "LTC": "Litecoin",
             "MAID": "MaidSafeCoin",
             "OMNI": "Omni",
             "NAUT": "Nautiluscoin",
             "NAV": "NAVCoin",
             "NEOS": "Neoscoin",
             "NMC": "Namecoin",
             "NOTE": "DNotes",
             "NXT": "NXT",
             "PINK": "Pinkcoin",
             "POT": "PotCoin",
             "PPC": "Peercoin",
             "RIC": "Riecoin",
             "SJCX": "Storjcoin-X",
             "STR": "Stellar",
             "SYS": "Syscoin",
             "VIA": "Viacoin",
             "XVC": "Vcash",
             "VRC": "VeriCoin",
             "VTC": "Vertcoin",
             "XBC": "BitcoinPlus",
             "XCP": "Counterparty",
             "XEM": "NEM",
             "XMR": "Monero",
             "XPM": "Primecion",
             "XRP": "Ripple",
             "GNO": "Gnosis",
             "ETH": "Ethereum",
             "SC": "Siacoin",
             "BCY": "BitCrystals",
             "EXP": "Expanse",
             "FCT": "Factom",
             "RADS": "Radium",
             "AMP": "Synereo AMP",
             "DCR": "Decred",
             "LSK": "Lisk",
             "LBC": "LBRY Credits",
             "STEEM": "STEEM",
             "SBD": "Steem-Dollars",
             "ETC": "Ethereum-Classic",
             "REP": "Augur",
             "ARDR": "Ardor",
             "ZEC": "Zcash",
             "STRAT": "Stratis",
             "NXC": "Nexium",
             "PASC": "PascalCoin",
             "ZRX": "0x",
             "CVC": "Civic",
             "BCH": "Bitcoin-Cash",
             "OMG": "OmiseGO",
             "GAS": "Gas",
             "STORJ": "Storj",
             "BTC": "Bitcoin",
             "XVG": "Verge",
             "BWK": "Bulwark",
             "ITNS": "IntenseCoin",
             "ZCL": "ZClassic",
             "BTG": "Bitcoin-Gold",
             "MONA": "MonaCoin",
             "XZC": "ZCoin",
             "BTCZ": "BitcoinZ",
             "KMD": "Komodo",
             "HUSH": "Hush",
             "UBQ": "Ubiq",
             "MUSIC": "Musicoin",
             "ETN": "Electroneum",
             "XLM": "Stellar",
             "EVN": "Envion",
             "HOT": "Holo"
             }

    if coin in names:
        return names[coin]
    return None


def getTickerData(money):
    coin_name = getCoinName(money.upper())
    if coin_name is None:
        return None

    url = "https://api.coinmarketcap.com/v1/ticker/" + coin_name + "/?convert=EUR"
    ticker = requests.get(url)
    if ticker.status_code == 200:
        return ticker.json()
    return None

def getData(ticker, coin):
    
    coin_name = getCoinName(coin.upper())
    logo = getCoinLogo(coin.upper())
    if logo is None:
        logo = getCoinLogo("NO")

    usd_price = "Current USD Price: `" + str(round(float(ticker[0]["price_usd"]),5)) + "$`\n"
    eur_price = "Current EUR Price: `" + str(round(float(ticker[0]["price_eur"]),5)) + "€`\n"

    #changeNum = float(ticker[0]["percent_change_24h"])
    #sign = "+" if changeNum > 0 else ""
    #change24 = "Percent Change 24h: ```diff\n" + sign + str(changeNum) + "%```"

    changeNum1 = float(ticker[0]["percent_change_1h"])
    sign = "+" if changeNum1 > 0 else ""
    if sign == "+":
        change1 = "`["+ sign + str(round(float(changeNum1),3)) + "%]` " + "<:pump:433581031161856000>"
    else:
        change1 = "`["+ sign + str(round(float(changeNum1),3)) + "%]` " + "<:dump:433578647681630208>"


    changeNum24 = float(ticker[0]["percent_change_24h"])
    sign = "+" if changeNum24 > 0 else ""
    if sign == "+":
        change24 = "`["+ sign + str(round(float(changeNum24),3)) + "%]` " + "<:pump:433581031161856000>"
    else:
        change24 = "`["+ sign + str(round(float(changeNum24),3)) + "%]` " + "<:dump:433578647681630208>"

    changeNum7 = float(ticker[0]["percent_change_7d"])
    sign = "+" if changeNum7 > 0 else ""
    if sign == "+":
        change7 = "`["+ sign + str(round(float(changeNum7),3)) + "%]` " + "<:pump:433581031161856000>"
    else:
        change7 = "`["+ sign + str(round(float(changeNum7),3)) + "%]` " + "<:dump:433578647681630208>"

    price = usd_price + eur_price
    change = "1h :  " + change1 + "\n24h : " + change24 + "\n7j :  " + change7

    embed = discord.Embed(title = "", description = "", color = 0xFF9900)
    embed.set_author(name = coin_name + " (" + coin.upper() + ")", icon_url = logo)
    embed.add_field(name = "Price", value = price, inline = False)
    embed.add_field(name = "Change", value = change, inline = False)
    embed.set_thumbnail(url = logo)
    embed.set_footer(text = "Powered by Akikazu and coinmarketcap.com")
    return embed


def getTop(number):
    url = "https://api.coinmarketcap.com/v1/ticker/?convert=EUR&limit=" + str(number)
    ticker = requests.get(url)
    data = ticker.json()
    embed_data = ""

    for i in range(int(number)):
        name = "**" + data[i]["name"] + "** : "
        usd_price = str(round(float(data[i]["price_usd"]),3)) + "$"
        eur_price = str(round(float(data[i]["price_eur"]),3)) + "€"
        changeNum24 = float(data[i]["percent_change_24h"])
        sign = "+" if changeNum24 > 0 else ""
        if sign == "+":
            change24 = " `["+ sign + str(round(float(changeNum24),3)) + "%]` " + "<:pump:433581031161856000>"
        else:
            change24 = " `["+ sign + str(round(float(changeNum24),3)) + "%]` " + "<:dump:433578647681630208>"

        #change = "```diff\n" + sign + str(changeNum) + "%```"

        embed_data += str(i+1) + ". " + name + "`" + usd_price + "` | `" + eur_price + "` | " + change24 +  "\n"

    description = "Current ranking for the top "+ str(number) +" at " + getDate() + "\nCoin : USD | EUR | 24h\n\n" + embed_data
    header = "Top " + str(number) + " currency"
    embed = discord.Embed(title = "", description = description, color=0xFF9900)
    embed.set_author(name = header, icon_url = getCoinLogo("BTC"))
    embed.set_footer(text = "Powered by Akikazu and coinmarketcap.com")
    return embed

def getConv(ticker, number, coin):
    
    coin_name = getCoinName(coin.upper())
    logo = getCoinLogo(coin.upper())
    if logo is None:
        logo = getCoinLogo("NO")

    conveur = str(float(ticker[0]["price_eur"]) * float(number))
    convusd = str(float(ticker[0]["price_usd"]) * float(number))

    layout_name = number + " " + coin_name + " = "
    layout_value = round(conveur,5) + "€ / " + round(convusd,5) + "$"

    layout = number + " **" + coin_name + "** = " + conveur + "€ / " + convusd + "$"

    embed = discord.Embed(title = "", description = layout, color = 0xFF9900)
    embed.set_author(name = coin_name + " (" + coin.upper() + ") at " + getDate(), icon_url = logo)
    #embed.add_field(name = layout_name, value = layout_value, inline = False)
    embed.set_footer(text = "Powered by Akikazu and coinmarketcap.com")
    return embed