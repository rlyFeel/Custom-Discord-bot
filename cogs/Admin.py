import nextcord
from nextcord.ext import commands
from Cybernator import Paginator as pag
from cfg.cfg import *


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Cogs is loaded - Admin')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def thelp(self, ctx):
        embed1 = nextcord.Embed(title='**📜・Основные правила**',
                               description='> 1) Пиар (кроме пиара moonlight)\n\n '
                                           '> 2) Попрошайничать ебучие гб на телефон/деньги\n\n'
                                           '> 3) Шок/треш контент всё только в nsfw\n\n'
                                           '> 4) Твинки/фейки\n\n'
                                           '> 5) Оскорбление чита в любом виде\n\n'
                                           '> 6) Рофл над тем, что чит ратка/майнер и т.п.\n\n'
                                           '> 7) Злоупотребление капсом\n\n'
                                           '> 8) Продажа всякой хуйни\n\n'
                                           '> 9) Инвайт ботов-спаммеров (кик вместе с пригласившим)\n\n'
                                           '> 10) Писать хуйню\n\n',
                                color=nextcord.Color.gold())
        embed2 = nextcord.Embed(title='**📜・Взаимодействие с администрацией**',
                               description='> 1) Оскорбление администрации в любом виде\n\n'
                                           '> 2) Тегать Naturalovа и NightMare',
                                color=nextcord.Color.brand_red())
        embed3 = nextcord.Embed(title='**📜・Дополнительные правила**',
                                description='> 1) Отличие мнения другого человека может являться поводом для кибербуллинга.\n\n'
                                            '> 2)А так же ты можешь быть кикнут за то, что ты пидорас по усмотрению администрации\n\n'
                                            '> P.S Если вы не прочитали правила,нам похуй',
                                color=nextcord.Color.brand_red())

        embeds = [embed1, embed2, embed3]
        message = await ctx.response.send_message(embed=embed1, ephemeral=False)
        page = pag(self.bot,
                   message,
                   use_more=False,
                   embeds=embeds,
                   timeout=lifetime)
        await page.start()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount=100+1):
        await ctx.channel.purge(limit=amount)
        emb = nextcord.Embed(title='Очистка чата!', description=f'**Было удаленно {amount} сообщений**', color=nextcord.Color.teal())
        await ctx.send(embed=emb)
        
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error,commands.MissingPermissions):
            emb = nextcord.Embed(title='📛 Error 📛', description='```Лох вгетай права, ez ez```', color=nextcord.Color.blurple())
            await ctx.send(embed=emb)
        elif isinstance(error,commands.MissingRequiredArgument):
            emb = nextcord.Embed(title='📛 Error 📛', description='```Лох вгетай аргумент, ez ez```', color=nextcord.Color.blurple())
            await ctx.send(embed=emb)
        elif isinstance(error, commands.CommandNotFound):
            emb = nextcord.Embed(title='📛 Error 📛', description='```Лох вгетай мозг, ez ez```', color=nextcord.Color.blurple())
            await ctx.send(embed=emb)



async def setup(bot):
    bot.add_cog(Admin(bot))