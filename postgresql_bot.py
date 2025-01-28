from aiogram import Bot, Dispatcher, types
import logging

TOKEN = "7864725145:AAGd1cYg9nhD2ANqJZosvY2HYRIWXSjM9kM"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Foydalanuvchi xabari
@dp.message_handler()
async def handle_message(message: types.Message):
    # Xabarni HTML formatida yuborish
    await message.answer("<b>Sizning xabaringiz saqlandi!</b>", parse_mode="HTML")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)


# postgresqlni ichida users degan bazaga kirish kerak 