
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
import asyncio
from aiogram.filters.state import StateFilter
from aiogram.types import PreCheckoutQuery

TOKEN = '7922523853:AAHFpvV14jrdyvDnI7IPZ-jx-FLwpbh_OAo' 
CLICK_TOKEN = '398062629:TEST:999999999_F91D8F69C042267444B74CC0B3C747757EB0E065' 
bot = Bot(token=TOKEN)
dp = Dispatcher()
CHANNEL_IDS = ['@test_i_kanal']

def buttons():
    kb = [
        [types.InlineKeyboardButton(text='Kanalga obuna bo\'ling', url="https://t.me/test_i_kanal")],
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
             
async def send_payment(message: types.Message):
    await bot.send_invoice(
        chat_id=message.from_user.id,
        title='Bot uchun oylik obuna',
        description='Botimizda muntazam foydalanish uchun oylik obuna sotib olishingiz kerak',
        provider_token=CLICK_TOKEN,
        currency='uzs',
        prices=[
            types.LabeledPrice(label=('Oylik obuna'), amount=1000000)
        ],
        start_parameter='make_purchase_click',
        payload=('oylik obuna')
    )


def buttonlar():
    kb = [
        [types.KeyboardButton(text = "Sherik kerak"), types.KeyboardButton(text = "Ish joyi kerak")],
        [types.KeyboardButton(text = "Xodim kerak"),types.KeyboardButton(text = "Ustoz kerak")],
        [types.KeyboardButton(text = "Shogird kerak")]
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)


class Sherikkerak(StatesGroup):
    Sherik = State()
    Texnologiya = State()
    Aloqa = State()      
    Hudud = State()
    Narxi = State()
    Kasbi = State()
    Murojaat_qilish_vaqti = State()
    Maqsad = State()

class Ishjoyikerak(StatesGroup):
    Xodim = State()
    Yosh = State()
    Texnologiya = State()
    Aloqa = State()
    Hudud = State()
    Narxi = State()
    Kasbi = State()
    Murojaat_qilish_vaqti = State()
    Maqsad = State()

class Xodimkerak(StatesGroup):
    Idora_nomi = State()
    Texnologiya = State()
    Aloqa = State()
    Hudud = State()
    Masul_ism_sharifi = State()
    Murojaat_qilish_vaqti = State()
    Ish_vaqtini_kiriting = State()
    Maoshni_kiriting = State()
    Qoshimcha_malumotlar = State()

class Ustozkerak(StatesGroup):
    Shogird = State()
    Yosh = State()
    Texnologiya = State()
    Aloqa = State()
    Hudud = State()
    Narxi = State()
    Kasbi = State()
    Murojaat_qilish_vaqti = State()
    Maqsad = State()

class Shogirdkerak(StatesGroup):
    Ustoz = State()
    Yosh = State()
    Texnologiya = State()
    Aloqa = State()
    Hudud = State()
    Narxi = State()
    Kasbi = State()
    Murojaat_qilish_vaqti = State()
    Maqsad = State()

def ha_yoq_buttons():
    kb = [
        [types.KeyboardButton(text = "Ha"),types.KeyboardButton(text = "Yo'q")]
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)


@dp.message(CommandStart())  
async def cmd_start(message: types.Message):
    if not await check_member(message.from_user.id):
        return await message.answer(text='Botimizdan foydalanish uchun quyidagi kanallarga obuna bo\'ling', reply_markup=buttons())
    await message.answer(text='Siz botimizdan foydalanishingiz mumkin')


    await message.reply(f"Assalom alaykum {message.from_user.first_name} \nUstozShogird kanalining rasmiy botiga xush kelibsiz!\n\n/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!", reply_markup=buttonlar())
    

@dp.message(F.text == "Sherik kerak",StateFilter("*"))
async def send_sherik(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Sherik topish uchun ariza berish\n\nHozir sizga birnecha savollar beriladi. \nHar biriga javob bering. \nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.")
    await message.answer("Ism, familiyangizni kiriting?")
    await state.set_state(Sherikkerak.Sherik)  


@dp.message(Sherikkerak.Sherik)
async def get_ism(message: Message, state: FSMContext):
    await state.update_data(Sherik=message.text)  
    await message.answer("📚Texnologiya:\n\nTalab qilinadigan texnologiyalarni kiriting?\nTexnologiya nomlarini vergul bilan ajrating. Masalan, \n\nJava, C++, C# ")
    await state.set_state(Sherikkerak.Texnologiya)

@dp.message(Sherikkerak.Texnologiya)
async def get_texnologiya(message: Message, state: FSMContext):
    await state.update_data(Texnologiya=message.text)  
    await message.answer("📞Aloqa: \n\nBog`lanish uchun raqamingizni kiriting?\nMasalan, +998 90 123 45 67 ")
    await state.set_state(Sherikkerak.Aloqa)

@dp.message(Sherikkerak.Aloqa)
async def get_aloqa(message: Message, state: FSMContext):
    await state.update_data(Aloqa=message.text)  
    await message.answer("🌐Hudud: \n\nQaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.")
    await state.set_state(Sherikkerak.Hudud)



@dp.message(Sherikkerak.Hudud)
async def get_hudud(message: Message, state: FSMContext):
    await state.update_data(Hudud=message.text)  
    await message.answer("💰Narxi:\n\nTolov qilasizmi yoki Tekinmi?\nKerak bo`lsa, Summani kiriting?")
    await state.set_state(Sherikkerak.Narxi)

@dp.message(Sherikkerak.Narxi)
async def get_narxi(message: Message, state: FSMContext):
    await state.update_data(Narxi=message.text)  
    await message.answer("👨🏻‍💻Kasbi: \n\nIshlaysizmi yoki o`qiysizmi?\nMasalan, Talaba ")
    await state.set_state(Sherikkerak.Kasbi)

@dp.message(Sherikkerak.Kasbi)
async def get_kasbi(message: Message, state: FSMContext):
    await state.update_data(Kasbi=message.text)  
    await message.answer("🕰Murojaat qilish vaqti: \n\nQaysi vaqtda murojaat qilish mumkin?\nMasalan, 9:00 - 18:00 ")
    await state.set_state(Sherikkerak.Murojaat_qilish_vaqti)

@dp.message(Sherikkerak.Murojaat_qilish_vaqti)
async def get_murojaat_vaqti(message: Message, state: FSMContext):
    await state.update_data(Murojaat_qilish_vaqti=message.text)  
    await message.answer("🔎Maqsad: \n\nMaqsadingizni qisqacha yozib bering.")
    await state.set_state(Sherikkerak.Maqsad)

@dp.message(Sherikkerak.Maqsad)
async def get_maqsad(message: Message, state: FSMContext):
    if message.text == 'Ha':
        user_data = await state.get_data()
        await message.answer("📪 So`rovingiz tekshirish uchun adminga jo`natildi!\n\nE'lon 24-48 soat ichida kanalda chiqariladi.", reply_markup=buttonlar())
        await send_payment(message)
        return await state.clear()

    elif message.text == "Yo'q":
        await message.answer("Qabul qilinmadi")
        await state.clear()
        await message.answer("/start so`zini bosing. E'lon berish qaytadan boshlanadi️", reply_markup=buttonlar())



    await state.update_data(Maqsad=message.text) 
    user_data = await state.get_data()  
    await message.answer(f"Sherik kerak: \n\n🏅Sherik: {user_data['Sherik']} \n📚Texnologiya: {user_data['Texnologiya']} \n📞Aloqa: {user_data['Aloqa']}\n🌐Hudud: {user_data['Hudud']}\n💰Narxi: {user_data['Narxi']}\n👨🏻‍💻Kasbi: {user_data['Kasbi']}\n🕰Murojaat qilish vaqti: {user_data['Murojaat_qilish_vaqti']}\n🔎Maqsad: {user_data['Maqsad']}")
    await message.answer("Barcha ma'lumotlar to'g'rimi?", reply_markup=ha_yoq_buttons())

#Ish joyi kerak button

@dp.message(F.text == "Ish joyi kerak",StateFilter("*"))
async def send_xodim(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Ish joyi topish uchun ariza berish\n\nHozir sizga birnecha savollar beriladi. \nHar biriga javob bering. \nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.")
    await message.answer("Ism, familiyangizni kiriting?")
    await state.set_state(Ishjoyikerak.Xodim)  


@dp.message(Ishjoyikerak.Xodim)
async def get_xodim(message: Message, state: FSMContext):
    await state.update_data(Xodim=message.text)  
    await message.answer("🕑Yosh:\n\nYoshingizni kiriting?\nMasalan, 19 ")
    await state.set_state(Ishjoyikerak.Yosh)

@dp.message(Ishjoyikerak.Yosh)
async def get_yosh(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(Yosh=message.text)  
        await message.answer("📚Texnologiya:\n\nTalab qilinadigan texnologiyalarni kiriting?\nTexnologiya nomlarini vergul bilan ajrating. Masalan, \n\nJava, C++, C# ")
        await state.set_state(Ishjoyikerak.Texnologiya)
    else:
        await message.answer("Iltimos, yoshingizni faqat raqam sifatida kiriting.")

@dp.message(Ishjoyikerak.Texnologiya)
async def get_texnologiya(message: Message, state: FSMContext):
    await state.update_data(Texnologiya=message.text)  
    await message.answer("📞Aloqa: \n\nBog`lanish uchun raqamingizni kiriting?\nMasalan, +998 90 123 45 67 ")
    await state.set_state(Ishjoyikerak.Aloqa)



@dp.message(Ishjoyikerak.Aloqa)
async def get_aloqa(message: Message, state: FSMContext):
    await state.update_data(Aloqa=message.text)  
    await message.answer("🌐Hudud: \n\nQaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.")
    await state.set_state(Ishjoyikerak.Hudud)

@dp.message(Ishjoyikerak.Hudud)
async def get_hudud(message: Message, state: FSMContext):
    await state.update_data(Hudud=message.text)  
    await message.answer("💰Narxi:\n\nTolov qilasizmi yoki Tekinmi?\nKerak bo`lsa, Summani kiriting?")
    await state.set_state(Ishjoyikerak.Narxi)

@dp.message(Ishjoyikerak.Narxi)
async def get_narxi(message: Message, state: FSMContext):
    await state.update_data(Narxi=message.text)  
    await message.answer("👨🏻‍💻Kasbi: \n\nIshlaysizmi yoki o`qiysizmi?\nMasalan, Talaba ")
    await state.set_state(Ishjoyikerak.Kasbi)

@dp.message(Ishjoyikerak.Kasbi)
async def get_kasbi(message: Message, state: FSMContext):
    await state.update_data(Kasbi=message.text)  
    await message.answer("🕰Murojaat qilish vaqti: \n\nQaysi vaqtda murojaat qilish mumkin?\nMasalan, 9:00 - 18:00 ")
    await state.set_state(Ishjoyikerak.Murojaat_qilish_vaqti)

@dp.message(Ishjoyikerak.Murojaat_qilish_vaqti)
async def get_murojaat_vaqti(message: Message, state: FSMContext):
    await state.update_data(Murojaat_qilish_vaqti=message.text)  
    await message.answer("🔎Maqsad: \n\nMaqsadingizni qisqacha yozib bering.")
    await state.set_state(Ishjoyikerak.Maqsad)

@dp.message(Ishjoyikerak.Maqsad)
async def get_maqsad(message: Message, state: FSMContext):
    if message.text == 'Ha':
        user_data = await state.get_data()
        await message.answer("📪 So`rovingiz tekshirish uchun adminga jo`natildi!\n\nE'lon 24-48 soat ichida kanalda chiqariladi.", reply_markup=buttonlar())
        await send_payment(message)        
        return await state.clear()

    elif message.text == "Yo'q":
        await message.answer("Qabul qilinmadi")
        await state.clear()
        await message.answer("/start so`zini bosing. E'lon berish qaytadan boshlanadi️", reply_markup=buttonlar())



    await state.update_data(Maqsad=message.text)  
    user_data = await state.get_data()  
    await message.answer(f"Ish joyi kerak: \n\n👨‍💼Xodim: {user_data['Xodim']}\n🕑Yosh: {user_data['Yosh']}\n📚Texnologiya: {user_data['Texnologiya']} \n📞Aloqa: {user_data['Aloqa']}\n🌐Hudud: {user_data['Hudud']}\n💰Narxi: {user_data['Narxi']}\n👨🏻‍💻Kasbi: {user_data['Kasbi']}\n🕰Murojaat qilish vaqti: {user_data['Murojaat_qilish_vaqti']}\n🔎Maqsad: {user_data['Maqsad']}")
    await message.answer("Barcha ma'lumotlar to'g'rimi?", reply_markup=ha_yoq_buttons())

# Xodim kerak button

@dp.message(F.text == "Xodim kerak",StateFilter("*"))
async def send_idora(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state:
        await state.clear()
    await message.answer("Xodim topish uchun ariza berish\n\nHozir sizga birnecha savollar beriladi. \nHar biriga javob bering. \nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.")
    await message.answer("🎓 Idora nomi?")
    await state.set_state(Xodimkerak.Idora_nomi)  


@dp.message(Xodimkerak.Idora_nomi)
async def get_idora(message: Message, state: FSMContext):
    await state.update_data(Idora_nomi=message.text)  
    await message.answer("📚 Texnologiya:\n\nTalab qilinadigan texnologiyalarni kiriting?\nTexnologiya nomlarini vergul bilan ajrating. Masalan, \n\nJava, C++, C#")
    await state.set_state(Xodimkerak.Texnologiya)

@dp.message(Xodimkerak.Texnologiya)
async def get_texnologiya(message: Message, state: FSMContext):
    await state.update_data(Texnologiya=message.text)  
    await message.answer("📞 Aloqa: \n\nBog`lanish uchun raqamingizni kiriting?\nMasalan, +998 90 123 45 67 ")
    await state.set_state(Xodimkerak.Aloqa)

@dp.message(Xodimkerak.Aloqa)
async def get_aloqa(message: Message, state: FSMContext):
    await state.update_data(Aloqa=message.text)  
    await message.answer("🌐 Hudud: \n\nQaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.")
    await state.set_state(Xodimkerak.Hudud)



@dp.message(Xodimkerak.Hudud)
async def get_hudud(message: Message, state: FSMContext):
    await state.update_data(Hudud=message.text)  
    await message.answer("✍️Mas'ul ism sharifi?")
    await state.set_state(Xodimkerak.Masul_ism_sharifi)

@dp.message(Xodimkerak.Masul_ism_sharifi)
async def get_masul_ism_sharifi(message: Message, state: FSMContext):
    await state.update_data(Masul_ism_sharifi=message.text)  
    await message.answer("🕰 Murojaat qilish vaqti: \n\nQaysi vaqtda murojaat qilish mumkin?\nMasalan, 9:00 - 18:00")
    await state.set_state(Xodimkerak.Murojaat_qilish_vaqti)

@dp.message(Xodimkerak.Murojaat_qilish_vaqti)
async def get_murojaat_qilish_vaqti(message: Message, state: FSMContext):
    await state.update_data(Murojaat_qilish_vaqti=message.text)  
    await message.answer("🕰 Ish vaqtini kiriting?")
    await state.set_state(Xodimkerak.Ish_vaqtini_kiriting)

@dp.message(Xodimkerak.Ish_vaqtini_kiriting)
async def get_ish_vaqti(message: Message, state: FSMContext):
    await state.update_data(Ish_vaqtini_kiriting=message.text)  
    await message.answer("💰 Maoshni kiriting?")
    await state.set_state(Xodimkerak.Maoshni_kiriting)

@dp.message(Xodimkerak.Maoshni_kiriting)
async def get_maosh(message: Message, state: FSMContext):
    await state.update_data(Maoshni_kiriting=message.text)  
    await message.answer("‼️ Qo`shimcha ma`lumotlar?")
    await state.set_state(Xodimkerak.Qoshimcha_malumotlar)

@dp.message(Xodimkerak.Qoshimcha_malumotlar)
async def get_qoshimcha_malumotlar(message: Message, state: FSMContext):
    if message.text == 'Ha':
        user_data = await state.get_data()
        await message.answer("📪 So`rovingiz tekshirish uchun adminga jo`natildi!\n\nE'lon 24-48 soat ichida kanalda chiqariladi.", reply_markup=buttonlar())
        await send_payment(message)
        return await state.clear()

    elif message.text == "Yo'q":
        await message.answer("Qabul qilinmadi")
        await state.clear()
        await message.answer("/start so`zini bosing. E'lon berish qaytadan boshlanadi️", reply_markup=buttonlar())



    await state.update_data(Qoshimcha_malumotlar=message.text)  
    user_data = await state.get_data()  
    await message.answer(f"Xodim kerak: \n\n🏢Idora: {user_data['Idora_nomi']}\n📚Texnologiya: {user_data['Texnologiya']} \n📞Aloqa: {user_data['Aloqa']}\n🌐Hudud: {user_data['Hudud']}\n✍️Mas'ul: {user_data['Masul_ism_sharifi']}\n🕰Murojaat qilish vaqti: {user_data['Murojaat_qilish_vaqti']}\n🕰Ish vaqti: {user_data['Ish_vaqtini_kiriting']}\n💰Maosh: {user_data['Maoshni_kiriting']}\n‼️Qo'shimcha: {user_data['Qoshimcha_malumotlar']}")
    await message.answer("Barcha ma'lumotlar to'g'rimi?", reply_markup=ha_yoq_buttons())

#Ustoz kerak button

@dp.message(F.text == "Ustoz kerak", StateFilter("*"))
async def send_xodim(message: types.Message, state: FSMContext):
    await message.answer("Ustoz topish uchun ariza berish\n\nHozir sizga birnecha savollar beriladi. \nHar biriga javob bering. \nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.")
    await message.answer("Ism, familiyangizni kiriting?")
    await state.set_state(Ustozkerak.Shogird)  


@dp.message(Ustozkerak.Shogird)
async def get_shogird(message: Message, state: FSMContext):
    await state.update_data(Shogird=message.text)  
    await message.answer("🕑Yosh:\n\nYoshingizni kiriting?\nMasalan, 19 ")
    await state.set_state(Ustozkerak.Yosh)

@dp.message(Ustozkerak.Yosh)
async def get_yosh(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(Yosh=message.text)  
        await message.answer("📚Texnologiya:\n\nTalab qilinadigan texnologiyalarni kiriting?\nTexnologiya nomlarini vergul bilan ajrating. Masalan, \n\nJava, C++, C# ")
        await state.set_state(Ustozkerak.Texnologiya)
    else:
        await message.answer("Iltimos, yoshingizni faqat raqam sifatida kiriting.")



@dp.message(Ustozkerak.Texnologiya)
async def get_texnologiya(message: Message, state: FSMContext):
    await state.update_data(Texnologiya=message.text)  
    await message.answer("📞Aloqa: \n\nBog`lanish uchun raqamingizni kiriting?\nMasalan, +998 90 123 45 67 ")
    await state.set_state(Ustozkerak.Aloqa)

@dp.message(Ustozkerak.Aloqa)
async def get_aloqa(message: Message, state: FSMContext):
    await state.update_data(Aloqa=message.text)  
    await message.answer("🌐Hudud: \n\nQaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.")
    await state.set_state(Ustozkerak.Hudud)

@dp.message(Ustozkerak.Hudud)
async def get_hudud(message: Message, state: FSMContext):
    await state.update_data(Hudud=message.text)  
    await message.answer("💰Narxi:\n\nTolov qilasizmi yoki Tekinmi?\nKerak bo`lsa, Summani kiriting?")
    await state.set_state(Ustozkerak.Narxi)

@dp.message(Ustozkerak.Narxi)
async def get_narxi(message: Message, state: FSMContext):
    await state.update_data(Narxi=message.text)  
    await message.answer("👨🏻‍💻Kasbi: \n\nIshlaysizmi yoki o`qiysizmi?\nMasalan, Talaba ")
    await state.set_state(Ustozkerak.Kasbi)

@dp.message(Ustozkerak.Kasbi)
async def get_kasbi(message: Message, state: FSMContext):
    await state.update_data(Kasbi=message.text)  
    await message.answer("🕰Murojaat qilish vaqti: \n\nQaysi vaqtda murojaat qilish mumkin?\nMasalan, 9:00 - 18:00 ")
    await state.set_state(Ustozkerak.Murojaat_qilish_vaqti)

@dp.message(Ustozkerak.Murojaat_qilish_vaqti)
async def get_murojaat_vaqti(message: Message, state: FSMContext):
    await state.update_data(Murojaat_qilish_vaqti=message.text)  
    await message.answer("🔎Maqsad: \n\nMaqsadingizni qisqacha yozib bering.")
    await state.set_state(Ustozkerak.Maqsad)

@dp.message(Ustozkerak.Maqsad)
async def get_maqsad(message: Message, state: FSMContext):
    if message.text == 'Ha':
        user_data = await state.get_data()
        await message.answer("📪 So`rovingiz tekshirish uchun adminga jo`natildi!\n\nE'lon 24-48 soat ichida kanalda chiqariladi.", reply_markup=buttonlar())
        await send_payment(message)
        return await state.clear()

    elif message.text == "Yo'q":
        await message.answer("Qabul qilinmadi")
        await state.clear()
        return await message.answer("/start so`zini bosing. E'lon berish qaytadan boshlanadi️", reply_markup=buttonlar())



    await state.update_data(Maqsad=message.text)  
    user_data = await state.get_data()  
    await message.answer(f"Ustoz kerak: \n\n🎓Shogird: {user_data['Shogird']}\n🕑Yosh: {user_data['Yosh']}\n📚Texnologiya: {user_data['Texnologiya']} \n📞Aloqa: {user_data['Aloqa']}\n🌐Hudud: {user_data['Hudud']}\n💰Narxi: {user_data['Narxi']}\n👨🏻‍💻Kasbi: {user_data['Kasbi']}\n🕰Murojaat qilish vaqti: {user_data['Murojaat_qilish_vaqti']}\n🔎Maqsad: {user_data['Maqsad']}")
    await message.answer("Barcha ma'lumotlar to'g'rimi?", reply_markup=ha_yoq_buttons())

#Shogird kerak button
@dp.message(F.text == "Shogird kerak")
async def send_ustoz(message: types.Message, state: FSMContext):
    await message.answer("Shogird topish uchun ariza berish\n\nHozir sizga birnecha savollar beriladi. \nHar biriga javob bering. \nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.")
    await message.answer("Ism, familiyangizni kiriting?")
    await state.set_state(Shogirdkerak.Ustoz)  


@dp.message(Shogirdkerak.Ustoz)
async def get_ustoz(message: Message, state: FSMContext):
    await state.update_data(Xodim=message.text)  
    await message.answer("🕑Yosh:\n\nYoshingizni kiriting?\nMasalan, 19 ")
    await state.set_state(Shogirdkerak.Yosh)



@dp.message(Shogirdkerak.Yosh)
async def get_yosh(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(Yosh=message.text)  
        await message.answer("📚Texnologiya:\n\nTalab qilinadigan texnologiyalarni kiriting?\nTexnologiya nomlarini vergul bilan ajrating. Masalan, \n\nJava, C++, C# ")
        await state.set_state(Shogirdkerak.Texnologiya)
    else:
        await message.answer("Iltimos, yoshingizni faqat raqam sifatida kiriting.")

@dp.message(Shogirdkerak.Texnologiya)
async def get_texnologiya(message: Message, state: FSMContext):
    await state.update_data(Texnologiya=message.text)  
    await message.answer("📞Aloqa: \n\nBog`lanish uchun raqamingizni kiriting?\nMasalan, +998 90 123 45 67 ")
    await state.set_state(Shogirdkerak.Aloqa)

@dp.message(Shogirdkerak.Aloqa)
async def get_aloqa(message: Message, state: FSMContext):
    await state.update_data(Aloqa=message.text)  
    await message.answer("🌐Hudud: \n\nQaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.")
    await state.set_state(Shogirdkerak.Hudud)

@dp.message(Shogirdkerak.Hudud)
async def get_hudud(message: Message, state: FSMContext):
    await state.update_data(Hudud=message.text)  
    await message.answer("💰Narxi:\n\nTolov qilasizmi yoki Tekinmi?\nKerak bo`lsa, Summani kiriting?")
    await state.set_state(Shogirdkerak.Narxi)

@dp.message(Shogirdkerak.Narxi)
async def get_narxi(message: Message, state: FSMContext):
    await state.update_data(Narxi=message.text)  
    await message.answer("👨🏻‍💻Kasbi: \n\nIshlaysizmi yoki o`qiysizmi?\nMasalan, Talaba ")
    await state.set_state(Shogirdkerak.Kasbi)

@dp.message(Shogirdkerak.Kasbi)
async def get_kasbi(message: Message, state: FSMContext):
    await state.update_data(Kasbi=message.text)  
    await message.answer("🕰Murojaat qilish vaqti: \n\nQaysi vaqtda murojaat qilish mumkin?\nMasalan, 9:00 - 18:00 ")
    await state.set_state(Shogirdkerak.Murojaat_qilish_vaqti)

@dp.message(Shogirdkerak.Murojaat_qilish_vaqti)
async def get_murojaat_vaqti(message: Message, state: FSMContext):
    await state.update_data(Murojaat_qilish_vaqti=message.text)  
    await message.answer("🔎Maqsad: \n\nMaqsadingizni qisqacha yozib bering.")
    await state.set_state(Shogirdkerak.Maqsad)

@dp.message(Shogirdkerak.Maqsad)
async def get_maqsad(message: Message, state: FSMContext):
    if message.text == 'Ha':
        user_data = await state.get_data()
        await message.answer("📪 So`rovingiz tekshirish uchun adminga jo`natildi!\n\nE'lon 24-48 soat ichida kanalda chiqariladi.", reply_markup=buttonlar())
        await send_payment(message)
        return await state.clear()

    elif message.text == "Yo'q":
        await message.answer("Qabul qilinmadi")
        await state.clear()
        await message.answer("/start so`zini bosing. E'lon berish qaytadan boshlanadi️", reply_markup=buttonlar())



    await state.update_data(Maqsad=message.text)  
    user_data = await state.get_data()  
    await message.answer(f"Ish joyi kerak: \n\n🎓Ustoz: {user_data['Ustoz']}\n🕑Yosh: {user_data['Yosh']}\n📚Texnologiya: {user_data['Texnologiya']} \n📞Aloqa: {user_data['Aloqa']}\n🌐Hudud: {user_data['Hudud']}\n💰Narxi: {user_data['Narxi']}\n👨🏻‍💻Kasbi: {user_data['Kasbi']}\n🕰Murojaat qilish vaqti: {user_data['Murojaat_qilish_vaqti']}\n🔎Maqsad: {user_data['Maqsad']}")
    await message.answer("Barcha ma'lumotlar to'g'rimi?", reply_markup=ha_yoq_buttons())

@dp.callback_query()
async def check_user(callback: types.CallbackQuery):
    if callback.data == 'check_member_status':
        if not await check_member(callback.message.from_user.id):
            return await callback.answer(text='Siz shartlarni to\'liq bajarmadingiz')
    await callback.message.answer(text="Botimizdan foydalanishingiz mumkin")
        
@dp.message(F.text == "To'lovni amalga oshirish")
async def tolov(message: types.Message):
    await send_payment(message)
    

@dp.pre_checkout_query()
async def on_pre_checkout_query(pre_checkout_query: PreCheckoutQuery,):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message(F.content_type == types.ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    await message.answer("To'lov muvaffaqiyatli amalga oshirildi!")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


