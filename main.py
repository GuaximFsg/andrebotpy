#!/usr/bin/python3
import discord
from discord.ext import commands
from random import randint, choice, shuffle
import math
import sys
from sys import argv
from cmath import cos
import os
import json
import datetime

# from webserver import keep_alive


description = """An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here."""
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", description=description, intents=intents)
client = discord.Client(intents=intents)

# BASE_URL= "https://xinga-me.appspot.com/api"
emojiappended = [
    "😀",
    " ",
    "😃",
    "😄",
    "😁",
    "😆",
    "😅",
    "😂",
    "🤣",
    "🥲",
    "☺",
    "️",
    "😊",
    "😇",
    "🙂",
    "🙃",
    "😉",
    "😌",
    "😍",
    "🥰",
    "😘",
    "😗",
    "😙",
    "😚",
    "😋",
    "😛",
    "😝",
    "😜",
    "🤪",
    "🤨",
    "🧐",
    "🤓",
    "😎",
    "🥸",
    "🤩",
    "🥳",
    "😏",
    "😒",
    "😞",
    "😔",
    "😟",
    "😕",
    "🙁",
    "☹",
    "😣",
    "😖",
    "😫",
    "😩",
    "🥺",
    "😢",
    "😭",
    "😤",
    "😠",
    "😡",
    "🤬",
    "🤯",
    "😳",
    "🥵",
    "🥶",
    "😱",
    "😨",
    "😰",
    "😥",
    "😓",
    "🤗",
    "🤔",
    "🤭",
    "🤫",
    "🤥",
    "😶",
    "😐",
    "😑",
    "😬",
    "🙄",
    "😯",
    "😦",
    "😧",
    "😮",
    "😲",
    "🥱",
    "😴",
    "🤤",
    "😪",
    "😵",
    "🤐",
    "🥴",
    "🤢",
    "🤮",
    "🤧",
    "😷",
    "🤒",
    "🤕",
    "🤑",
    "🤠",
    "😈",
    "👿",
    "👹",
    "👺",
    "🤡",
    "💩",
    "👻",
    "💀",
    "☠",
    "👽",
    "👾",
    "🤖",
    "🎃",
    "😺",
    "😸",
    "😹",
    "😻",
    "😼",
    "😽",
    "🙀",
    "😿",
    "😾",
]
indtratadas = open("indtratadas.txt").readlines()
toxingar = open("toxingar.txt").readlines()
gabaritoh = open("2022_D1.txt").readlines()
gabaritoe = open("2022_D2.txt").readlines()
# request_url = f"{BASE_URL}"
# response= requests.get(request_url)

# if response.status_code == 200:
#    data = response.json()
#    #printa um dicionario
#    xingada = data['xingamento']


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    await bot.change_presence(activity=discord.Game("Votando 13"))
    print("------")


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
    await ctx.send(ctx)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split("d"))
    except Exception:
        await ctx.send("Format has to be in NdN!")
        return

    result = ", ".join(str(randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description="For when you wanna settle the score some other way")
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(choice(choices))


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f"{member.name} joined {discord.utils.format_dt(member.joined_at)}")


@bot.group()
async def cool(ctx, *args):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """


#  await ctx.send(file=discord.File('foraadm1.mp4'))


###################################################################


@bot.command()
async def linux(ctx):
    """Usa Linux boyy (?)"""
    await ctx.send("Usa Linux boyy")
    await ctx.send(file=discord.File("Tux.svg.png"))


#   await ctx.send(file=discord.File('fuderadm3.mp4'))


@bot.command()
async def desculpa(ctx):
    """Peço desculpas pelo meu comportamento uwu"""
    await ctx.send("Peço desculpas pelo meu comportamento uwu")


@bot.command()
async def repete(ctx, *args, content="Repetindo"):
    """ " !repete palavras a serem repetidas uma vez"""
    arguments = " ".join(args)  # .join joins tudo de uma lista, tuple ou dict
    #    print (arguments)
    await ctx.send(f"{arguments}")


#    await ctx.send(file=discord.File('fuderadm2.mp4'))
#    print(*args)
#    print(ctx)


@bot.command()
async def repeat(ctx, times: int, content="Repetindo..."):
    """!repeat (número de vezes a repetir) palavra"""
    if times <= 8:
        for i in range(times):
            await ctx.send(content)
    else:
        await ctx.send(f"Pq vc não fala {content} pro seu birolho {times} vezes?")
        ofensa = toxingar[randint(1, 70)]
        await ctx.send(f"Tá querendo me banir do discord seu {ofensa}")


#        response= requests.get(request_url)
#         await ctx.send(xingada)


@bot.command()
async def pizza(ctx, left: int, right: int, content="Pizzaiando"):
    """!pizza numerodefatias raiodapizza
    use pizzahelp em caso de dúvidas
    """
    fatias = int(left)
    r = int(right)

    b = math.radians((360 / int(fatias)) * 0.5)
    cossenus = cos(b).real
    profundidade = round(r - (cossenus * r), 3)

    senus = math.sin(b).real
    comprimento = round(2 * senus * r, 2)
    print(comprimento)
    await ctx.send(comprimento)


@bot.command()
async def sergio(ctx, description="Quantos dias faltam para SERGIO SALES"):
    """Quantos dias faltam para SERGIO SALES"""
    bdayhj = str(datetime.datetime.today().strftime("%j"))
    if bdayhj == "217":
        sergio = "HOJE É O ANIVERSÁRIO DO SÉRGIO MITO (ou o dia seguinte)"
    elif bdayhj == "218":
        sergio = "HOJE É O ANIVERSÁRIO DO SÉRGIO MITO (ou o dia seguinte)"
        print(sergio)
    else:
        sergio = "Hoje não é o aniverśario de serginho. "
        faltambday = (365 - int(bdayhj)) + 217
        print(sergio)
        print(faltambday)
    await ctx.send(sergio)
    await ctx.send("ainda faltam {0} dias".format(faltambday))


@bot.command()
async def enem(ctx):
    """Quantos dias faltam pro tinhoso dia (motivacional)"""
    hoje = int(datetime.datetime.today().strftime("%j"))
    if hoje == 317:
        await ctx.send(f"Hoje é o dia do enem :) {emojiappended[randint(1, 116)]}")
    else:
        await ctx.send(
            f"Faltam {317-hoje} dias pro ENEM {emojiappended[randint(1, 116)]}"
        )


@bot.command()
async def salve(ctx, *args):
    tosend = indtratadas[randint(1, 409)]
    await ctx.send(f"Salve pra {tosend}")


@bot.command()
async def corrige(ctx, left: int, mid: str, right: int, content="Corrigindo"):
    """!corrige dia-enem(1 ou 2) cor(az(azul), br(branco) etc) questão"""
    # arguments = ' '.join(args) # .join joins tudo de uma lista, tuple ou dict
    # cor = arguments[0]
    # quest = arguments[2]
    # quest2 = arguments[3]
    # questf = ''.join(arguments)
    print(left, mid, right)
    if left == 1:
        if mid == "az":
            await ctx.send(gabaritoh[right])
        elif mid == "am":
            await ctx.send(gabaritoh[right + 91])
        elif mid == "br":
            await ctx.send(gabaritoh[right + 182])
        elif mid == "ro":
            await ctx.send(gabaritoh[right + 273])
        else:
            await ctx.send(
                "sintaxe: !corrige dia-do-enem(1 ou 2) cor-do-caderno(az(de azul), br(de branco), ro(rosa), am(amarelo)) questão"
            )
    elif left == 2:
        if mid == "am":
            await ctx.send(gabaritoe[right])
        elif mid == "cz":
            await ctx.send(gabaritoe[right + 1])
        elif mid == "az":
            await ctx.send(gabaritoe[right + 92])
        elif mid == "ro":
            await ctx.send(gabaritoe[right + 183])
        else:
            await ctx.send(
                "sintaxe: !corrige dia-do-enem(1 ou 2) cor-do-caderno(az(de azul), br(de branco), ro(rosa), am(amarelo)) questão"
            )
    else:
        await ctx.send(
            "sintaxe: !corrige dia-do-enem(1 ou 2) cor-do-caderno(az(de azul), br(de branco), ro(rosa), am(amarelo)) questão"
        )
        await ctx.send("exemplo: dia 1, prova azul, questão 30: !corrige 1 az 30")


@bot.command()
async def nota(ctx, n1: float, n2: float, n3: float):
    """!nota nota1 nota2 nota3. outputa a nota faltando"""
    n4 = 28 - n1 - n2 - n3
    await ctx.send(n4)


@bot.command()
async def sortcamas(ctx, *args):  # sortbeds
    """Sorteia quem dividirá qual cama com quem, apenas mande os nomes"""
    Persons = list(args)
    NumOfPersons = len(Persons)
    if NumOfPersons == 0:
        ctx.send(
            "Não dorme ninguém. Diga os nomes de quem precisa ser organizado na próxima."
        )
    shuffle(Persons)
    # print(f"Persons shuffled: {Persons}\nNumOfPersons{NumOfPersons}")
    Persons.append("Com seus pensamentos")
    Pairs = {}
    i = 0

    while i < NumOfPersons:
        Pairs[Persons[i]] = Persons[i + 1]
        i += 2
    Output = ""
    i = 1
    for person, pair in Pairs.items():
        Output += f"Na cama {i} :   {person} dorme com {pair}\n"
        i += 1
    await ctx.send(Output)


# keep_alive()
TOKEN = "MTAwMjkzODY1ODQ0NzQyNTYwOA.GQux99.WetR7J_cpf8Pf2qtiIMYb0o_MPTNg1Z11QMLs0"


bot.run(TOKEN)
