from aiogram import Router, types, filters
router = Router()

@router.message(filters.Command("help"))
async def start_hand(msg: types.Message):
    n = "Sizga yordam tariqasida barcha kamandalarni aytaman:\n"
    n += "botni ishga tushirish: /start\n"
    n += "yordam so'rash: /help\n"
    n += "registratsiyadan o'tish: /registration"
    await msg.answer(n)

