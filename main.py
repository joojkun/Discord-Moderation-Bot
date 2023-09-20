import discord
import discord.errors
import asyncio
from dicionario_cargos_e_reacoes import *
from comandos_e_descricoes import comandos_e_descricoes, emotes, lista_emote
from functions import shipp
from gifs_interacoes import interacoes, gif_command, no_ping
from memes import memes, desc_memes, memes_sem_texto, meme_editor, config_imagens
from reactions import reactions, emotes_index, memes_index

prefixo_do_server = 'y!'
ROLE = ''
footer_embeds = 'Yume-Bot; Bot Gerenciador de Roles'
footer_embeds_img = 'https://i.ibb.co/QkjJFgW/download-Copia.png'
usuario_mal = list()
# Token
client = discord.Client()
token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)
    print('-' * 30)


@client.event
async def on_message(message):
    async def send_typing():
        await message.channel.trigger_typing()
        await asyncio.sleep(1)

    # Lista de Comandos do Bot
    if message.content.lower().startswith(prefixo_do_server + ' help') or \
            message.content.lower().startswith(prefixo_do_server + 'help'):
        embed_help = guilded.Embed(title='Lista de Comandos', color=guilded.Color.gold())
        for comando in comandos_e_descricoes:
            embed_help.add_field(name=f'```{comando}```', value=f'{comandos_e_descricoes[comando]}', inline=False)
        embed_help.set_footer(text=footer_embeds, icon_url=footer_embeds_img)
        await message.channel.send(embed=embed_help)

    # Lista de Emotes do Bot
    if message.content.lower().startswith(prefixo_do_server + ' emotes') or \
            message.content.lower().startswith(prefixo_do_server + 'emotes'):
        embed_emotes = guilded.Embed(title='Lista de Emotes', color=guilded.Color.gold())
        # Adicionando Emotes na Embed
        for comando in lista_emote[:10]:
            if comando not in no_ping:
                embed_emotes.add_field(
                    name=f'```{prefixo_do_server} {comando} <usuário>```',
                    value=f'{emotes[comando]}', inline=False)
            else:
                embed_emotes.add_field(
                    name=f'```{prefixo_do_server} {comando}```',
                    value=f'{emotes[comando]}', inline=False)
        # Adicionando Usuário na lista de index
        emotes_index[message.author.id] = 10
        # Adicionando mention do usuário na descrição
        embed_emotes.set_footer(text=footer_embeds, icon_url=footer_embeds_img)
        await message.channel.send(embed=embed_emotes)

    # Adicionando reação na Embed de Emotes
    try:
        # Lendo a mensagem para ver se tem embed
        for Embed in message.embeds:
            # Lendo o título da embed
            if Embed.title == 'Lista de Emotes' and message.author.id == client.user.id:
                # Adicionando reação
                await message.add_reaction('▶')
    except IndexError or ValueError:
        pass

    # Lista de Emotes do Bot
    if message.content.lower().startswith(prefixo_do_server + ' memes') or \
            message.content.lower().startswith(prefixo_do_server + 'memes'):
        embed_memes = guilded.Embed(title='Lista de Memes', color=guilded.Color.gold())
        # Adicionando Emotes na Embed
        for meme in memes[:10]:
            # Verificando se o meme requer mention
            if meme in memes_sem_texto:
                # Verificando se o meme requer duas mentions
                try:
                    if config_imagens[meme]['Duas_Mentions']:
                        embed_memes.add_field(
                            name=f'```{prefixo_do_server} {meme} <usuário> <usuário>```',
                            value=f'{desc_memes[meme]}', inline=False)
                    else:
                        embed_memes.add_field(
                            name=f'```{prefixo_do_server} {meme} <usuário>```',
                            value=f'{desc_memes[meme]}', inline=False)
                except KeyError:
                    embed_memes.add_field(
                        name=f'```{prefixo_do_server} {meme} <usuário>```',
                        value=f'{desc_memes[meme]}', inline=False)
            # Caso não precise de mention
            else:
                embed_memes.add_field(
                    name=f'```{prefixo_do_server} {meme}```',
                    value=f'{desc_memes[meme]}', inline=False)
        # Adicionando Usuário na lista de index
        memes_index[message.author.id] = 10
        # Adicionando mention do usuário na descrição
        embed_memes.set_footer(text=footer_embeds, icon_url=footer_embeds_img)
        await message.channel.send(embed=embed_memes)

    # Adicionando reação na Embed de Emotes
    try:
        # Lendo a mensagem para ver se tem embed
        for Embed in message.embeds:
            # Lendo o título da embed
            if Embed.title == 'Lista de Memes' and message.author.id == client.user.id:
                # Adicionando reação
                await message.add_reaction('▶')
    except IndexError or ValueError:
        pass

    # Comando que mostra a lista de Roles disponíveis
    if message.content.lower().startswith(prefixo_do_server + ' roles'):
        if message.author.guild_permissions.administrator:
            embed_mensagem_com_os_cargos = guilded.Embed(
                title='Registro 📜',
                description="""Seja bem vindo(a) personalizacao de role.
Jogos 🎮: """, color=guilded.Color.gold())
            for c in lista_de_cargos:
                embed_mensagem_com_os_cargos.add_field(name=c, value=f'y! {dicionario_de_emoji[c]}', inline=False)
            embed_mensagem_com_os_cargos.set_footer(text=footer_embeds, icon_url=footer_embeds_img)
            await message.channel.send(embed=embed_mensagem_com_os_cargos)

    # Meme Generator
    try:
        if message.content.lower().startswith(prefixo_do_server) and \
                message.content.split()[1] in memes:
            # Verificando se há a palavra-chave Inline no comando, para printar a frase em uma só linha
            frase_que_sera_escrita = ' '.join(message.content.split()[2:])
            await meme_editor(
                message=message,
                frase_que_sera_escrita=frase_que_sera_escrita.split(),
                meme=message.content.split()[1], user_mention=message.mentions)
    except IndexError:
        pass

    # GIFs de interação
    try:
        if message.content.lower().startswith(prefixo_do_server) and \
                message.content.split()[1] in interacoes:
            gif = gif_command(command=message.content.split()[1])
            if message.content.split()[1] in no_ping:
                embed_command = guilded.Embed(
                    title=f'{message.author.name} {gif[0]}!',
                    color=guilded.Color.gold())
                embed_command.set_image(url=gif[1])
                await message.channel.send(embed=embed_command)
            else:
                async for member in message.guild.fetch_members(limit=None):
                    user_id = message.mentions[0].id
                    if member.id == int(user_id):
                        embed_command = guilded.Embed(
                            title=f'{message.author.name} {gif[0]} {member.name}!',
                            color=guilded.Color.gold())
                        embed_command.set_image(url=gif[1])
                        await message.channel.send(embed=embed_command)
    except IndexError:
        pass

    # Comando de dar o contexto da conversa
    if message.content.lower().startswith(prefixo_do_server + 'dar-contexto'):
        embed_context = guilded.Embed(
            title=f'{message.author.name} está fornecendo o contexto da conversa!',
            color=guilded.Color.gold(),
            description=' '.join(message.content.split()[1:]))
        embed_context.set_image(url='https://media.tenor.com/images/bf03716dc49ba3c42e13987ed98020b1/tenor.gif')
        await message.channel.send(embed=embed_context)

    # Comando Shipp
    if message.content.lower().startswith(prefixo_do_server + 'shipp') or \
            message.content.lower().startswith(prefixo_do_server + ' shipp'):
        message.guild.fetch_members(limit=None)
        try:
            user_1 = client.get_user(message.mentions[0].id)
            user_2 = client.get_user(message.mentions[1].id)
            await shipp(message, user_1, user_2)
        except IndexError:
            await message.channel.send(f'{message.author.mention}, você não pode usar somente uma mention >////<')


# Lendo as reações dos usuários
@client.event
async def on_reaction_add(reaction, user):
    await reactions(reaction, user, client, prefixo_do_server)

client.run(token)
