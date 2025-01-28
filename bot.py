from aiogram import types, Bot, Dispatcher
from aiogram.filters import CommandStart
import asyncio
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import I18n
from middlewares import CustomFSMI18nMiddleware
from aiogram.types import PreCheckoutQuery

TOKEN = '7864725145:AAGd1cYg9nhD2ANqJZosvY2HYRIWXSjM9kM'
CLICK_TOKEN = "398062629:TEST:999999999_F91D8F69C042267444B74CC0B3C747757EB0E065"
bot = Bot(token=TOKEN)

i18n = I18n(path="locales", default_locale="uz", domain="messages")

dp = Dispatcher()
dp.message.middleware(CustomFSMI18nMiddleware(i18n))


CHANNEL_IDS = ['@korean_by_nozi']


def buttons():
    kb = [
        [types.InlineKeyboardButton(text='Kanal 1', url="https://t.me/@korean_by_nozi")],
        [types.InlineKeyboardButton(text='Tekshirish', callback_data='check_member_status')]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=kb)


async def check_member(user_id):
    for channel_id in CHANNEL_IDS:
        member = await bot.get_chat_member(channel_id, user_id)
        
        if member.status not in ['creator', 'member', 'administrator']:
            print(member, channel_id, user_id)
            return False
    return True
             




@dp.message(CommandStart())
async def start(message: types.Message):

    if not await check_member(message.from_user.id):
            return await message.answer(text='Botimizdan foydalanish uchun quyidagi kanallarga obuna bo\'ling', reply_markup=buttons())
    await message.answer(text='Siz botimizdan foydalanishingiz mumkin')


    await bot.send_invoice(
        chat_id=message.from_user.id,
        title='Bot uchun oylik obuna',
        description='Botimizda muntazam foydalanish uchun oylik obuna sotib olishingiz kerak',
        provider_token=CLICK_TOKEN,
        currency='uzs',
        prices=[
            types.LabeledPrice(label=_('Oylik obuna'), amount=10000000)
        ],
        start_parameter='make_purchase_click',
        payload=_('oylik obuna')
    )

    
@dp.pre_checkout_query()
async def on_pre_checkout_query(
    pre_checkout_query: PreCheckoutQuery,
):
    # tekshiruv
    await pre_checkout_query.answer(
        ok=True,
        # error_message="Uzr siz 5 soniyaga kech qoldingiz keyingi chegirmada faol bo'ling "
    )



@dp.callback_query()
async def check_user(callback: types.CallbackQuery):
    if callback.data == 'check_member_status':
        if not await check_member(callback.message.from_user.id):
            return await callback.answer(text='Siz shartlarni to\'liq bajarmadingiz')
    await callback.message.answer(text="Botimizdan foydalanishingiz mumkin")
        


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


# kanalga a'zo bo'lishni majburiy qilish 
# botdagi ma'lumotlarni bazaga saqlash
