import discord

from comandos_e_descricoes import emotes, lista_emote
from gifs_interacoes import no_ping

# Index da lista de emotes
from memes import memes, desc_memes, memes_sem_texto, config_imagens

emotes_index = dict()
# Index memes
memes_index = dict()
# Embed links
footer_embeds = 'Yume-Bot'
footer_embeds_img = 'https://i.ibb.co/QkjJFgW/download-Copia.png'


async def reactions(reaction: discord.reaction, user: discord.User, client: discord.Client, prefixo):
    if reaction.count >= 2 and user.id != client.user.id:
        # Verificando se há uma embed na mensagem em que o usuário reagiu
        try:
            for Embed in reaction.message.embeds:
                # Verificando título da Embed, autor da Embed e autor da reação
                if Embed.title == 'Lista de Emotes' and reaction.message.author.id == client.user.id \
                        and user.id in emotes_index and reaction.emoji == '▶':
                    # Index da lista de emotes
                    index_user = emotes_index[user.id]
                    index_user_final = emotes_index[user.id] + 10
                    # Setando o novo index do usuário
                    emotes_index[user.id] += 10
                    # Criando a Embed com a lista de emotes
                    embed_emotes = discord.Embed(title='Lista de Emotes', color=discord.Color.gold())
                    for comando in lista_emote[index_user:index_user_final]:
                        if comando not in no_ping:
                            embed_emotes.add_field(
                                name=f'```{prefixo} {comando} <usuário>```',
                                value=f'{emotes[comando]}', inline=False)
                        else:
                            embed_emotes.add_field(
                                name=f'```{prefixo} {comando}```',
                                value=f'{emotes[comando]}', inline=False)
                    embed_emotes.set_footer(text=footer_embeds, icon_url=footer_embeds_img)
                    # Limpando reações e adicionando novas
                    await reaction.message.clear_reactions()
                    await reaction.message.add_reaction('◀')
                    if len(lista_emote[index_user:]) > 10:
                        await reaction.message.add_reaction('▶')
                    # Editando a Embed com a nova Embed
                    await reaction.message.edit(embed=embed_emotes)

                # Verificando título da Embed, autor da Embed e autor da reação
                if Embed.title == 'Lista de Emotes' and reaction.message.author.id == client.user.id \
                        and user.id in emotes_index and reaction.emoji == '◀':
                    # Index da lista de emotes
                    index_user = emotes_index[user.id] - 20
                    index_user_final = emotes_index[user.id] - 10
                    # Setando o novo index
                    emotes_index[user.id] -= 10
                    # Criando a Embed com a lista de emotes
                    embed_emotes = discord.Embed(title='Lista de Emotes', color=discord.Color.gold())
                    for comando in lista_emote[index_user:index_user_final]:
                        if comando not in no_ping:
                            embed_emotes.add_field(
                                name=f'```{prefixo} {comando} <usuário>```',
                                value=f'{emotes[comando]}', inline=False)
                        else:
                            embed_emotes.add_field(
                                name=f'```{prefixo} {comando}```',
                                value=f'{emotes[comando]}', inline=False)
                    embed_emotes.set_footer(text=footer_embeds, icon_url=footer_embeds_img)
                    # Limpando reações e adicionando novas
                    await reaction.message.clear_reactions()
                    if emotes_index[user.id] - 10 > 0:
                        await reaction.message.add_reaction('◀')
                    await reaction.message.add_reaction('▶')
                    # Editando a Embed com a nova Embed
                    await reaction.message.edit(embed=embed_emotes)
        except IndexError or ValueError:
            pass

        # Verificando se há uma embed na mensagem em que o usuário reagiu
        try:
            for Embed in reaction.message.embeds:
                # Verificando título da Embed, autor da Embed e autor da reação
                if Embed.title == 'Lista de Memes' and reaction.message.author.id == client.user.id \
                        and user.id in memes_index and reaction.emoji == '▶':
                    # Index da lista de emotes
                    index_user = memes_index[user.id]
                    index_user_final = memes_index[user.id] + 10
                    # Setando o novo index do usuário
                    memes_index[user.id] += 10
                    # Criando a Embed com a lista de emotes
                    embed_memes = discord.Embed(title='Lista de Memes', color=discord.Color.gold())
                    for meme in memes[index_user:index_user_final]:
                        # Verificando se o meme requer mention
                        if meme in memes_sem_texto:
                            # Verificando se o meme requer duas mentions
                            try:
                                if config_imagens[meme]['Duas_Mentions']:
                                    embed_memes.add_field(
                                        name=f'```{prefixo} {meme} <usuário> <usuário>```',
                                        value=f'{desc_memes[meme]}', inline=False)
                                else:
                                    embed_memes.add_field(
                                        name=f'```{prefixo} {meme} <usuário>```',
                                        value=f'{desc_memes[meme]}', inline=False)
                            except KeyError:
                                embed_memes.add_field(
                                    name=f'```{prefixo} {meme} <usuário>```',
                                    value=f'{desc_memes[meme]}', inline=False)
                        # Caso não precise de mention
                        else:
                            embed_memes.add_field(
                                name=f'```{prefixo} {meme}```',
                                value=f'{desc_memes[meme]}', inline=False)
                    embed_memes.set_footer(text=footer_embeds, icon_url=footer_embeds_img)
                    # Limpando reações e adicionando novas
                    await reaction.message.clear_reactions()
                    await reaction.message.add_reaction('◀')
                    if len(lista_emote[index_user:]) > 10:
                        await reaction.message.add_reaction('▶')
                    # Editando a Embed com a nova Embed
                    await reaction.message.edit(embed=embed_memes)

                # Verificando título da Embed, autor da Embed e autor da reação
                if Embed.title == 'Lista de Memes' and reaction.message.author.id == client.user.id \
                        and user.id in memes_index and reaction.emoji == '◀':
                    # Index da lista de emotes
                    index_user = memes_index[user.id] - 20
                    index_user_final = memes_index[user.id] - 10
                    # Setando o novo index
                    memes_index[user.id] -= 10
                    # Criando a Embed com a lista de emotes
                    embed_memes = discord.Embed(title='Lista de Memes', color=discord.Color.gold())
                    for meme in memes[index_user:index_user_final]:
                        # Verificando se o meme requer mention
                        if meme in memes_sem_texto:
                            # Verificando se o meme requer duas mentions
                            try:
                                if config_imagens[meme]['Duas_Mentions']:
                                    embed_memes.add_field(
                                        name=f'```{prefixo} {meme} <usuário> <usuário>```',
                                        value=f'{desc_memes[meme]}', inline=False)
                                else:
                                    embed_memes.add_field(
                                        name=f'```{prefixo} {meme} <usuário>```',
                                        value=f'{desc_memes[meme]}', inline=False)
                            except KeyError:
                                embed_memes.add_field(
                                    name=f'```{prefixo} {meme} <usuário>```',
                                    value=f'{desc_memes[meme]}', inline=False)
                        # Caso não precise de mention
                        else:
                            embed_memes.add_field(
                                name=f'```{prefixo} {meme}```',
                                value=f'{desc_memes[meme]}', inline=False)
                    embed_memes.set_footer(text=footer_embeds, icon_url=footer_embeds_img)
                    # Limpando reações e adicionando novas
                    await reaction.message.clear_reactions()
                    if memes_index[user.id] - 10 > 0:
                        await reaction.message.add_reaction('◀')
                    await reaction.message.add_reaction('▶')
                    # Editando a Embed com a nova Embed
                    await reaction.message.edit(embed=embed_memes)
        except IndexError or ValueError:
            pass
