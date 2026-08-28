from aiogram import Router, types, filters
from aiogram.fsm.context import FSMContext
from states.regState import RegistrationState
router = Router()
@router.message(filters.Command("registration"))
async def registration(msg: types.Message, state: FSMContext):
    await msg.answer("ro'yxatdan o'tish uchun barcha ma'lumotlaringizni kiriting!")
    await msg.answer("ismingizni kiriting: ")
    await state.set_state(RegistrationState.first_name)
@router.message(RegistrationState.first_name)
async def first_name(msg: types.Message, state: FSMContext):
    await msg.answer(f"rahmat, {msg.text} endi familyangizni kiriting: ")
    global ism
    ism = msg.text
    await state.update_data(first_name=msg.text)
    await state.set_state(RegistrationState.last_name)
@router.message(RegistrationState.last_name)
async def last_name(msg: types.Message, state: FSMContext):
    n = f"siz, {ism} - {msg.text}!\n"
    n += "yoshingizni kiriting: "
    await msg.answer(n)
    await state.update_data(last_name=msg.text)
    await state.set_state(RegistrationState.age)
@router.message(RegistrationState.age)
async def age(msg: types.Message, state: FSMContext):
    await msg.answer("telefon nomeringizni kiriting: ")
    await state.update_data(age=msg.text)
    await state.set_state(RegistrationState.phone)
@router.message(RegistrationState.phone)
async def phone(msg: types.Message, state: FSMContext):
    n = "rahmat, siz haqingizda barcha ma'lumotlarni oldim"
    n += f"endi {ism} aka nomingizga kridit oldik!"
    await msg.answer(n)
    await state.update_data(phone=msg.text)
    data = await state.get_data()
    n = f"ism: {data['first_name']}\n"
    n += f"familya: {data['last_name']}\n"
    n += f"yosh: {data['age']}\n"
    n += f"tel: {data['phone']}\n"
    await msg.answer(n)
    await state.clear()

