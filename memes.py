from io import BytesIO
import discord
import requests
from PIL import Image, ImageDraw, ImageFont, ImageOps
import asyncio


# Send Typing
async def send_typing(channel: discord.Message):
    await channel.trigger_typing()
    await asyncio.sleep(1)

# 'monica', 'ticket',
memes = ['scares-me', 'love-more-than', 'do-something',
         'silence', 'always-has-been', 'religion', 'you-cant-defeat-me', 'drake-prefers', 'to-kill-me',
         'this-is-worthless', 'mask', 'reasons-to-live', 'lets-see-who-you-are', 'matrix-choice',
         'obrigado', 'pintura', 'titan']
memes_sem_texto = ['scares-me', 'love-more-than', 'do-something', 'silence',
                   'always-has-been', 'religion', 'you-cant-defeat-me', 'drake-prefers', 'to-kill-me',
                   'this-is-worthless', 'mask', 'reasons-to-live', 'lets-see-who-you-are', 'matrix-choice',
                   'obrigado', 'pintura', 'titan']
desc_memes = {
    'scares-me': '[Imagem do Meme](https://i.imgur.com/ralVpCD.png)',
    'love-more-than': '[Imagem do Meme](https://i.imgur.com/As7Y8E8.png)',
    'do-something': '[Imagem do Meme](https://i.imgur.com/BfimLrE.png)',
    'silence': '[Imagem do Meme](https://i.imgur.com/SkbpKXo.png)',
    'always-has-been': '[Imagem do Meme](https://i.imgur.com/uU1CYLX.png)',
    'religion': '[Imagem do Meme](https://i.imgur.com/8sgm3xg.jpeg)',
    'you-cant-defeat-me': '[Imagem do Meme](https://i.imgur.com/uAaPVZ8.png)',
    'drake-prefers': '[Imagem do Meme](https://i.imgur.com/UjshMni.jpeg)',
    'to-kill-me': '[Imagem do Meme](https://i.imgur.com/Ac4Vya0.jpeg)',
    'this-is-worthless': '[Imagem do Meme](https://i.imgur.com/pWCWsCA.jpeg)',
    'mask': '[Imagem do Meme](https://i.imgur.com/vtvnhFA.jpeg)',
    'reasons-to-live': '[Imagem do Meme](https://i.imgur.com/NUmIJd3.png)',
    'lets-see-who-you-are': '[Imagem do Meme](https://i.imgur.com/zoFgsrr.jpeg)',
    'obrigado': '[Imagem do Meme](https://i.imgur.com/KtOexxY.jpeg)',
    'pintura': '[Imagem do Meme](https://i.imgur.com/ykRHvOz.jpeg)',
    'titan': '[Imagem do Meme](https://i.imgur.com/OQ0acSw.jpeg)',
    'matrix-choice': '[Imagem do Meme](https://i.imgur.com/7zEppeR.jpeg)'
}

# Posição das imagens
config_imagens = {
    'scares-me': {'Arquivo': 'scares_me.png', 'Tamanho': (1090, 830), 'Posição': (3, 870),
                  'Forma': 'Retângulo'},
    'love-more-than': {'Arquivo': 'love_more_than.png', 'Tamanho': (225, 167), 'Posição': (220, 295),
                       'Forma': 'Retângulo'},
    'silence': {'Arquivo': 'silence.png', 'Tamanho': (72, 64), 'Posição': (127, 3),
                'Forma': 'Retângulo'},
    'reasons-to-live': {'Arquivo': 'reasons_to_live.png', 'Tamanho': (80, 90), 'Posição': (80, 405),
                        'Forma': 'Retângulo'},
    'religion': {'Arquivo': 'religion.jpg', 'Tamanho': (550, 440), 'Posição': (20, 235),
                 'Forma': 'Retângulo'},
    'this-is-worthless': {'Arquivo': 'this_is_worthless.jpg', 'Tamanho': (130, 140), 'Posição': (146, 70),
                          'Forma': 'Retângulo'},
    'mask': {'Arquivo': 'mask.jpg', 'Tamanho': (150, 150), 'Posição': (130, 630),
             'Forma': 'Retângulo'},
    'obrigado': {'Arquivo': 'obrigado.jpg', 'Tamanho': (205, 220), 'Posição': (377, 186),
                 'Forma': 'Retângulo'},
    'do-something': {'Arquivo': 'do_something.png', 'Tamanho': (180, 150, 190, 200),
                     'Posição': (454, 140, 350, 650), 'Forma': 'Retângulo',
                     'Forma_2': 'Retângulo', 'Duas_Mentions': False},
    'lets-see-who-you-are': {'Arquivo': 'lets_see_who_you_are.jpg', 'Tamanho': (160, 190),
                             'Posição': (60, 670), 'Forma': 'Retângulo'},
    'pintura': {'Arquivo': 'pintura.jpg', 'Tamanho': (85, 108, 11, 14),
                'Posição': (214, 70, 159, 114), 'Forma': 'Retângulo',
                'Forma_2': 'Retângulo', 'Duas_Mentions': False},
    'matrix-choice': {'Arquivo': 'matrix_choice.jpg', 'Tamanho': (140, 135, 140, 135),
                      'Posição': (275, 460, 50, 465), 'Forma': 'Retângulo',
                      'Forma_2': 'Retângulo', 'Duas_Mentions': True},
    'titan': {'Arquivo': 'titan.jpg', 'Tamanho': (120, 140, 120, 140),
              'Posição': (390, 80, 390, 690), 'Forma': 'Retângulo',
              'Forma_2': 'Retângulo', 'Duas_Mentions': True},
    'drake-prefers': {'Arquivo': 'drake_prefers.jpg', 'Tamanho': (250, 250, 250, 250),
                      'Posição': (250, 0, 250, 250), 'Forma': 'Retângulo',
                      'Forma_2': 'Retângulo', 'Duas_Mentions': True},
    'you-cant-defeat-me': {'Arquivo': 'you_cant_defeat_me.png', 'Tamanho': (290, 240, 266, 225),
                           'Posição': (280, 35, 280, 700), 'Forma': 'Retângulo',
                           'Forma_2': 'Retângulo', 'Duas_Mentions': True},
    'to-kill-me': {'Arquivo': 'to_kill_me.jpg', 'Tamanho': (250, 240, 250, 240),
                   'Posição': (290, 15, 270, 450), 'Forma': 'Retângulo',
                   'Forma_2': 'Retângulo', 'Duas_Mentions': True},
    'always-has-been': {'Arquivo': 'always_has_been.png', 'Tamanho': (465, 386, 160, 140),
                        'Posição': (40, 55, 690, 155), 'Forma': 'Elipse',
                        'Forma_2': 'Retângulo', 'Duas_Mentions': False}}


async def meme_editor(message: discord.Message, frase_que_sera_escrita, meme, user_mention=None):
    # Variável que verifica se a frase em mais de uma palavra
    if meme in memes_sem_texto:
        # Avatar do Usuário
        url = requests.get(user_mention[0].avatar_url)
        avatar = Image.open(BytesIO(url.content))
        avatar = avatar.resize((config_imagens[meme]['Tamanho'][0], config_imagens[meme]['Tamanho'][1]))
        bigsize = (avatar.size[0] * 3, avatar.size[1] * 3)
        mask = Image.new('L', bigsize, 0)
        draw = ImageDraw.Draw(mask)
        # Formato da Imagem
        # Retângulo
        if config_imagens[meme]['Forma'] == 'Retângulo':
            draw.rectangle((0, 0) + bigsize, fill=255)
        # Esfera
        if config_imagens[meme]['Forma'] == 'Elipse':
            draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(avatar.size, Image.ANTIALIAS)
        avatar.putalpha(mask)
        # Inserindo o avatar na imagem
        output = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
        output.putalpha(mask)
        output.save('avatar.png')
        # Decidindo qual será o wallpaper escolhido
        fundo = Image.open(f"Imagens/Meme_source/{config_imagens[meme]['Arquivo']}")
        fundo.paste(avatar, (config_imagens[meme]['Posição'][0], config_imagens[meme]['Posição'][1]), avatar)
        # Verificando se é presico colar mais de uma imagem no meme
        if len(config_imagens[meme]['Tamanho']) > 2:
            # Avatar do Usuário
            # Verificando se o meme requer duas mentions
            if config_imagens[meme]['Duas_Mentions']:
                # Verificando se o Usuário forneceu duas Mentions
                try:
                    url = requests.get(user_mention[1].avatar_url)
                # Caso tenha fornecido apenas uma
                except IndexError:
                    url = requests.get(user_mention[0].avatar_url)
            else:
                url = requests.get(user_mention[0].avatar_url)
            avatar = Image.open(BytesIO(url.content))
            avatar = avatar.resize((config_imagens[meme]['Tamanho'][2], config_imagens[meme]['Tamanho'][3]))
            bigsize = (avatar.size[0] * 3, avatar.size[1] * 3)
            mask = Image.new('L', bigsize, 0)
            draw = ImageDraw.Draw(mask)
            # Formato da Imagem
            # Retângulo
            if config_imagens[meme]['Forma_2'] == 'Retângulo':
                draw.rectangle((0, 0) + bigsize, fill=255)
            # Esfera
            if config_imagens[meme]['Forma_2'] == 'Elipse':
                draw.ellipse((0, 0) + bigsize, fill=255)
            mask = mask.resize(avatar.size, Image.ANTIALIAS)
            avatar.putalpha(mask)
            # Inserindo o avatar na imagem
            output = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
            output.putalpha(mask)
            output.save('avatar.png')
            fundo.paste(avatar, (config_imagens[meme]['Posição'][2], config_imagens[meme]['Posição'][3]), avatar)
        fundo.save('bv.png')
        # Enviando o meme já editado
        await send_typing(message.channel)
        await message.channel.send(file=discord.File('bv.png'))
    else:
        pos_img_x_y_large_1 = {'monica': (300, 87, 300, 180, 300, 280), 'ticket': (194, 120, 200, 220, 200, 310)}
        limite_char_linha = {'monica': 3, 'ticket': 3}
        limite_char_linha_2 = {'monica': 5, 'ticket': 6}
        limite_char_total = {'monica': 6, 'ticket': 10}
        arquivo = {'monica': 'imagem.jpg', 'ticket': 'Ticket.png'}
        fundo = Image.open(f'Imagens/Meme_source/{arquivo[meme]}')
        escrever = ImageDraw.Draw(fundo)
        # Verificando se o texto está dentro do Limite de Caracteres
        print(len(frase_que_sera_escrita))
        if len(frase_que_sera_escrita) > limite_char_total[meme]:
            # Enviando o meme já editado
            await send_typing(message.channel)
            await message.channel.send(f'{message.author.mention}, a sua frase excedeu o limite de caracteres do meme!')

        else:
            if len(frase_que_sera_escrita) > limite_char_linha[meme]:
                if len(frase_que_sera_escrita) > limite_char_linha_2[meme]:
                    fonte = ImageFont.truetype('Fonts/arial_narrow_7.ttf', 60)
                    escrever.text(
                        xy=(pos_img_x_y_large_1[meme][0], pos_img_x_y_large_1[meme][1]),
                        text=f"{' '.join(frase_que_sera_escrita[:limite_char_linha[meme]])}", fill=(0, 0, 0),
                        font=fonte)
                    escrever.text(
                        xy=(pos_img_x_y_large_1[meme][2], pos_img_x_y_large_1[meme][3]),
                        text=f"{' '.join(frase_que_sera_escrita[limite_char_linha[meme]:limite_char_linha_2[meme]])}",
                        fill=(0, 0, 0), font=fonte)
                    escrever.text(
                        xy=(pos_img_x_y_large_1[meme][4], pos_img_x_y_large_1[meme][5]),
                        text=f"{' '.join(frase_que_sera_escrita[limite_char_linha_2[meme]:])}", fill=(0, 0, 0),
                        font=fonte)
                    fundo.save('bv.png')
                    # Enviando o meme já editado
                    await send_typing(message.channel)
                    await message.channel.send(file=discord.File('bv.png'))
                else:
                    fonte = ImageFont.truetype('Fonts/arial_narrow_7.ttf', 60)
                    escrever.text(
                        xy=(pos_img_x_y_large_1[meme][0], pos_img_x_y_large_1[meme][1]),
                        text=f"{' '.join(frase_que_sera_escrita[:limite_char_linha[meme]])}", fill=(0, 0, 0),
                        font=fonte)
                    escrever.text(
                        xy=(pos_img_x_y_large_1[meme][2], pos_img_x_y_large_1[meme][3]),
                        text=f"{' '.join(frase_que_sera_escrita[limite_char_linha[meme]:])}", fill=(0, 0, 0),
                        font=fonte)
                    fundo.save('bv.png')
                    # Enviando o meme já editado
                    await send_typing(message.channel)
                    await message.channel.send(file=discord.File('bv.png'))
            else:
                fonte = ImageFont.truetype('Fonts/arial_narrow_7.ttf', 80)
                escrever.text(
                    xy=(pos_img_x_y_large_1[meme][0], pos_img_x_y_large_1[meme][1]),
                    text=f"{' '.join(frase_que_sera_escrita)}", fill=(0, 0, 0), font=fonte)
                fundo.save('bv.png')
                # Enviando o meme já editado
                await send_typing(message.channel)
                await message.channel.send(file=discord.File('bv.png'))
