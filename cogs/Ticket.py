import nextcord

from nextcord.ext import commands
from cfg.cfg import *
from cfg.dtb import *
from pyqiwip2p import QiwiP2P

p2p = QiwiP2P(auth_key=QIWI_TOKEN)

class addhwid(nextcord.ui.Modal):
    def __init__(self, channel):
        super().__init__(
            "Подтверждение привязки",
            timeout=None
        )
        self.channel = channel

        self.user = nextcord.ui.TextInput(
            label="WHID",
            min_length=32,
            max_length=32,
            required=True,
            placeholder='Введите ваш HWID'
        )
        self.add_item(self.user)
        print(self.user)

    async def callback(self, interaction: nextcord.Interaction) -> None:
        whid = str(self.user.value)
        match await add_hwid(interaction.user.id, whid, interaction.user.name):
            case 0:
                emb = nextcord.Embed(title="Ваш хвид был добавлен!",
                                    description=f'Вот ваш чит.\n',
                                    color=nextcord.Color.dark_blue())
                await interaction.send(embed=emb, ephemeral=False)
            case 1:
                emb = nextcord.Embed(title="Ваш хвид был обновлен!",
                                    description=f'Вот ваш чит.\n',
                                    color=nextcord.Color.dark_blue())
                await interaction.send(embed=emb, ephemeral=False)

class WhidGetter(nextcord.ui.View):
    def __init__(self):
        super().__init__(
            timeout=None
        )
    @nextcord.ui.button(
        label="Подтвердить WHID", style=nextcord.ButtonStyle.primary
    )

    async def whidgetter(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_modal(addhwid(interaction.channel))


class CreateTicket(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(
        label='🔨 Помощь', style=nextcord.ButtonStyle.blurple
    )
    async def create_ticket_help(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        msg = await interaction.response.send_message("a ticket be create", ephemeral=True)
        channel = await interaction.guild.create_text_channel(f'🔨┃{interaction.user.name}-Помощь',
                                                              category=nextcord.utils.get(
                                                                  interaction.guild.categories,
                                                                  id=1037406108526051398))
        await channel.set_permissions(interaction.user,
                                      send_messages=True,
                                      read_message_history=True,
                                      read_messages=True)
        await channel.set_permissions(interaction.guild.get_role(interaction.guild.id),
                                      send_messages=False,
                                      read_messages=False)

        await msg.edit(f"Тикет был создан! {channel.mention}")
        emb = nextcord.Embed(title=f'Помощь ! - {interaction.user.name}',
                                description='Тут можете задать вопрос или уточнить детали')
        await channel.send(embed=emb, view=TicketSettings())

    @nextcord.ui.button(
        label='💸 Покупка', style=nextcord.ButtonStyle.blurple
    )
    async def create_ticket_buy(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        msg = await interaction.response.send_message("a ticket be create", ephemeral=True)
        channel = await interaction.guild.create_text_channel(f'💸┃{interaction.user.name}-Покупка',
                                                              category=nextcord.utils.get(
                                                                  interaction.guild.categories,
                                                                  id=))
        await channel.set_permissions(interaction.user,
                                      send_messages=True,
                                      read_message_history=True,
                                      read_messages=True)
        await channel.set_permissions(interaction.guild.get_role(interaction.guild.id),
                                      send_messages=False,
                                      read_messages=False)

        await msg.edit(f"Тикет был создан! {channel.mention}")
        emb_buy = nextcord.Embed(title=f'Покупка ! - {interaction.user.name}',
                                 description='Инструкция \n '
                                             '1.Нажмите на "Получить счёт",чтобы получить счёт \n'
                                             '2.После оплаты нажмите на "Проверить оплату"\n'
                                             '3.После успешной оплаты следуйте дальнейшим инструкциям')
        await channel.send(embed=emb_buy, view=TicketBuy())


class TicketSettings(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(
        label='Закрыть тикет', style=nextcord.ButtonStyle.red, emoji='📕'
    )
    async def close_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message("Тикет скоро закроется...", ephemeral=True)
        await interaction.channel.delete()

    @nextcord.ui.button(
        label='Позвать администрацию', style=nextcord.ButtonStyle.blurple, emoji='💡'
    )
    async def sing_to_help(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        emb = nextcord.Embed(description=f"🔔 {interaction.user.mention} позвал на помощь.",color=nextcord.Color.red())
        await interaction.channel.send(f'<@&{Id_Staff_Role}>', embed=emb)


class TicketBuy(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(
        label='Позвать администрацию', style=nextcord.ButtonStyle.blurple, emoji='💡'
    )
    async def sing_to_help(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        emb = nextcord.Embed(description=f"🔔 {interaction.user.mention} позвал на помощь.",color=nextcord.Color.red())
        await interaction.response.send_message(f'<@&{Id_Staff_Role}>', embed=emb, ephemeral=False)

    @nextcord.ui.button(
        label='Закрыть тикет', style=nextcord.ButtonStyle.red, emoji='📕'
    )
    async def close_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message("Тикет скоро закроется...", ephemeral=True)
        await interaction.channel.delete()

    @nextcord.ui.button(
        label='Получить счёт', style=nextcord.ButtonStyle.green, emoji='💵'
    )
    async def get_check(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        p2p.bill(amount=400, lifetime=60,
                 bill_id=int(str(interaction.user.id) + interaction.channel.mention.replace("<#", "").replace(">", "")),
                 comment=('MoonLight | Client version Beta | Your ds =  ' + interaction.user.name))
        await interaction.response.send_message(p2p.check(bill_id=int(
            str(interaction.user.id) + interaction.channel.mention.replace("<#", "").replace(">", ""))).pay_url)
    @nextcord.ui.button(
        label='Проверить оплату', style=nextcord.ButtonStyle.gray, emoji='💬'
    )
    async def check_check(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        global bot
        p2p.bill(amount=400, lifetime=60,
                 bill_id=int(str(interaction.user.id) + interaction.channel.mention.replace("<#", "").replace(">", "")),
                 comment=('MoonLight | Client version Beta | Your ds =  ' + interaction.user.name))
        if (p2p.check(bill_id=int(str(interaction.user.id) + str(interaction.channel.id))).status == "WAITING"):
            await interaction.send('Не оплаченно!')
        elif p2p.check(bill_id=int(str(interaction.user.id) + str(interaction.channel.id))).status == "PAID":
            emb = nextcord.Embed(
                description='**Оплаченно !** \n\n  - ```скачайте и запустите файл,нажмите "Copy" , и отправьте хвид в меню ``` ',
                color=nextcord.Color.dark_blue())
            await interaction.send(embed=emb, view=WhidGetter())


class Ticekt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Cogs is loaded - ticket')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ticket1(self, interaction):
        print('команда работает')
        emb = nextcord.Embed(title='Добро пожаловать в систему тикетов! | MoonLight client', description='Выберите нужный вам раздел', color=nextcord.Color.teal())
        emb.set_image(url='')
        view=CreateTicket()
        await interaction.send(embed=emb, view=view)













async def setup(bot):
    bot.add_cog(Ticekt(bot))