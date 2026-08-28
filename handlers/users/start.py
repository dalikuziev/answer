from aiogram import Router, types, filters
router = Router()

@router.message(filters.Command("start"))
async def start_hand(msg: types.Message):
    await msg.answer("Assalomu alaykum!\ndokonga kiring: /dokon")

