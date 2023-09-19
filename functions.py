"""
Arquivo onde ficarão as funções
"""
import asyncio
import random
from io import BytesIO
import discord
import requests
from PIL import Image, ImageDraw, ImageFont, ImageOps


# Send Typing
async def send_typing(channel: discord.Message):
    await channel.trigger_typing()
    await asyncio.sleep(1)


# Dicionário com o valor dos shipps
shipp_results = dict()


async def shipp(message: discord.Message, user_1: discord.User, user_2: discord.User):
    """
    Função que calcula o shipp de dois usuários
    :return: O valor do shipp
    """
    if f'{user_1.id} {user_2.id}' in shipp_results.keys() or\
            f'{user_2.id} {user_1.id}' in shipp_results.keys():
        try:
            shipp_value = shipp_results[f'{user_1.id} {user_2.id}']
        except KeyError:
            shipp_value = shipp_results[f'{user_2.id} {user_1.id}']
    else:
        shipp_results[f'{user_1.id} {user_2.id}'] = random.randint(1, 10)
        shipp_value = shipp_results[f'{user_1.id} {user_2.id}']

    # Avatar do Usuário
    fonte = ImageFont.truetype('Fonts/LEMONMILK-Regular.otf', 70)
    url = requests.get(user_1.avatar_url)
    avatar = Image.open(BytesIO(url.content))
    avatar = avatar.resize((600, 570))
    bigsize = (avatar.size[0] * 3, avatar.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(avatar.size, Image.ANTIALIAS)
    avatar.putalpha(mask)
    # Inserindo o avatar na imagem
    output = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)
    output.save('avatar.png')

    # avatar = Image.open('avatar.png')
    # Decidindo qual será o wallpaper escolhido
    wallpapers = ['fundo_shipp_1', 'fundo_shipp_2', 'fundo_shipp_3', 'fundo_shipp_4', 'fundo_shipp_5']
    fundo = Image.open(f'Imagens/Imagens_shipp/{random.choice(wallpapers)}.jpg')
    escrever = ImageDraw.Draw(fundo)
    fundo.paste(avatar, (160, 450), avatar)
    # Avatar do usuário 2
    url = requests.get(user_2.avatar_url)
    avatar = Image.open(BytesIO(url.content))
    avatar = avatar.resize((600, 570))
    bigsize = (avatar.size[0] * 3, avatar.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(avatar.size, Image.ANTIALIAS)
    avatar.putalpha(mask)
    # Inserindo o avatar na Imagem
    output = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)
    output.save('avatar.png')
    fundo.paste(avatar, (1100, 450), avatar)

    if (shipp_value * 10) <= 10:
        escrever.text(xy=(550, 110), text=f"{10 * shipp_value}% de chance!\n\n", fill=(255, 255, 255), font=fonte)
        escrever.text(xy=(80, 220), text=f"Vocês não combinam nada um com o outro!", fill=(255, 255, 255), font=fonte)
    if 11 <= (shipp_value * 10) <= 40:
        escrever.text(xy=(550, 110), text=f"{10 * shipp_value}% de chance!\n\n", fill=(255, 255, 255), font=fonte)
        escrever.text(xy=(450, 220), text=f"Não tem química aí!", fill=(255, 255, 255), font=fonte)
    if 41 <= (shipp_value * 10) <= 50:
        escrever.text(xy=(550, 110), text=f"{10 * shipp_value}% de chance!\n\n", fill=(255, 255, 255), font=fonte)
        escrever.text(xy=(250, 220), text=f"Quem sabe...Vocês deveriam tentar!", fill=(255, 255, 255), font=fonte)
    if 51 <= (shipp_value * 10) <= 70:
        escrever.text(xy=(550, 110), text=f"{10 * shipp_value}% de chance!\n\n", fill=(255, 255, 255), font=fonte)
        escrever.text(xy=(350, 220), text=f"Até que daria um bom casal!", fill=(255, 255, 255), font=fonte)
    if 71 <= (shipp_value * 10) <= 84:
        escrever.text(xy=(550, 110), text=f"{10 * shipp_value}% de chance!\n\n", fill=(255, 255, 255), font=fonte)
        escrever.text(xy=(450, 220), text=f"Daria um ótimo casal!", fill=(255, 255, 255), font=fonte)
    if 85 <= (shipp_value * 10) <= 100:
        escrever.text(xy=(550, 110), text=f"{10 * shipp_value}% de chance!\n\n", fill=(255, 255, 255), font=fonte)
        escrever.text(xy=(400, 220), text=f"Vocês são o par perfeito!", fill=(255, 255, 255), font=fonte)
    fundo.save('bv.png')
    await send_typing(message.channel)
    await message.channel.send(file=discord.File('bv.png'))
