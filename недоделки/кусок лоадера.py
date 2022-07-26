@bot.command()
async def loader (ctx, arg=None):
        with open('users.json', 'r') as file:
                dataServerID = json.load(file)
                COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
                ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
        try:
            if str(ctx.author.id) in ADMINS:
                if arg == 'on':
                    bot.load_extension('module.loader')
                    msg = await ctx.send(embed=discord.Embed(
                        title="Успешно",
                        description=f"*Модуль loader успешно загружен!*",
                        color=COLOR
                    ))
                elif arg == 'off':
                    bot.unload_extension('module.loader')
                    msg = await ctx.send(embed=discord.Embed(
                        title="Успешно",
                        description=f"*Модуль loader успешно отключен!*",
                        color=COLOR
                    ))
                elif arg == 'reload':
                    bot.reload_extension('module.loader')
                    msg = await ctx.send(embed=discord.Embed(
                        title="Успешно",
                        description=f"*Модуль loader успешно перезагружен!*",
                        color=COLOR
                    ))
                else:
                    msg = await ctx.send(embed=discord.Embed(
                        title="Ошибка",
                        description=f"*Аргумента {arg} не существует!*" ,
                        color=ErCOLOR
                        ))
            else:
                msg = await ctx.send(embed=discord.Embed(
                        title="Ошибка",
                        description=f"*У вас не достаточно прав!*" ,
                        color=ErCOLOR
                        ))
            await asyncio.sleep(5)
            await msg.delete()
        except ImportError:
            msg = await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="Ошибка",
                color=ErCOLOR
            ))
            await asyncio.sleep(5)
            await msg.delete()