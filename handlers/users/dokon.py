from aiogram import filters, types, Router
from aiogram.fsm.context import FSMContext
from states.dokonState import DokonState
router = Router()
@router.message(filters.Command("dokon"))
async def dokon(msg: types.Message, state: FSMContext):
    await msg.answer("dokonimizga xush kelibsiz")
    await msg.answer("kiyim nomi: ")
    await state.set_state(DokonState.name)
@router.message(DokonState.name)
async def name(msg: types.Message, state: FSMContext):
    await msg.answer("kiyim rangi: ")
    await state.update_data(name=msg.text)
    await state.set_state(DokonState.color)
@router.message(DokonState.color)
async def color(msg: types.Message, state: FSMContext):
    await msg.answer("kiyim razmer: ")
    await state.update_data(color=msg.text)
    await state.set_state(DokonState.size)
