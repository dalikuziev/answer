from aiogram.fsm.state import State, StatesGroup

class RegistrationState(StatesGroup):
    first_name = State()
    last_name = State()
    age = State()
    phone = State()

