import nextcord
from nextcord.ext import commands


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Cogs is loaded - Commands')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def help(self, ctx):
        emb = nextcord.Embed(title='Навигация по коммандам',
                             description=
                             f"📕 Base command\n\n"
                             f'/clear - Очитка \n'
                             f'/thelp - Вывод правил\n'
                             f'/ticket1 - Создание тикетов\n'
                             f'/market_place - создание маркета\n'
                             f'/changenickforall - Изменить всем ники\n'
                             f'/clearnicknames - Очистить всем ники \n\n'
                             f"📗 Server command\n\n"
                             f"/ds_stop - остановка дс бота\n"
                             f"/ds_restart - рестарт дс бота\n"
                             f"/reboot - рестарт VDS\n"
                             f"/system - общая сводка о сервере\n"
                             f"/restart - Рестарт сервера\n"
                             f"/start - Запуск сервера\n"
                             f"/stop - Выключение сервера\n",
                             color=nextcord.Color.gold())
        await ctx.send(embed=emb)


async def setup(bot):
    bot.add_cog(Commands(bot))