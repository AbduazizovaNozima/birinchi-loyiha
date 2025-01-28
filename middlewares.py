
from aiogram.types import TelegramObject, Message
from typing import Any, Dict
from aiogram.fsm.middleware import BaseMiddleware 
from aiogram.utils.i18n.middleware import FSMI18nMiddleware
from aiogram import types, Bot, Dispatcher


CHANNEL_ID = "@korean_by_nozi"  

class CheckSubscriptionMiddleware(BaseMiddleware):
    def __init__(self, bot: Bot, **kwargs):
        super().__init__(**kwargs)
        self.bot = bot

    async def dispatch(self, message: types.Message, data: dict):
        user_id = message.from_user.id
        try:
            # Foydalanuvchi kanalga a'zo bo'ladimi?
            chat_member = await self.bot.get_chat_member(CHANNEL_ID, user_id)
            
            if chat_member.status not in ['member', 'administrator']:
                # Foydalanuvchi kanalga a'zo bo'lmasa, xabar yuboramiz
                await message.answer("Siz kanalga a'zo bo'lishingiz kerak!")
                return False  # Kanalga a'zo bo'lmaganlar uchun ishlamaydi

            return True  # Kanalga a'zo bo'lganlar uchun davom etadi

        except Exception as e:
            # Agar xatolik yuzaga kelsa (masalan, kanalni tekshirayotganda), xabar yuboramiz
            await message.answer("Kanalni tekshirishda xatolik yuz berdi.")
            return False
    
class CustomFSMI18nMiddleware(FSMI18nMiddleware):
    async def get_locale(self, event: TelegramObject, data: Dict[str, Any]) -> str:
        # Foydalanuvchi xabarini tekshirib, tilni tanlash
        if isinstance(event, Message) and event.from_user.language_code:
            # Use the language code from the user message
            return event.from_user.language_code

        # Fallback bo'lib, default tilni qaytarish
        return await super().get_locale(event, data)

    # async def __call__(self, handler, event, data):
    #     # I18n instance'ni qo'shish
    #     data['i18n'] = self.i18n
    #     return await super().__call__(handler, event, data)

