from aiogram.fsm.state import StatesGroup, State

class DokonState(StatesGroup):
    name = State()
    color = State()
    size = State()
    price = State()

