import asyncio
from idlelib.undo import Command

from aiogram import Dispatcher, Bot, Router

from aiogram.types import Message
from aiogram.filters import StateFilter, CommandStart
from aiogram.fsm.context import FSMContext


from aiogram.fsm.state import State, StatesGroup

# Класс состояний бота
class BotStates(StatesGroup):
    entering_id = State() # Состояние ввода ID

# Роутер, с помощью которого будем регестрировать наши хендлеры
router = Router()

# Добавляем в роутер обработчик сообщения
@router.message(
    CommandStart("start"),  # Этот обработчик будет принимать команду /start
    StateFilter(None)  # И будет срабатывать при отсутствии состояния
)
async def start_command(message: Message, state: FSMContext):
    await state.set_state(BotStates.entering_id) # Выставляем состояние
    await message.answer("Введите свой ID")


# Следующий обработчик сообщений будет принимать сообщения только если выставлено состояние BotStates.entering_id
@router.message(
    StateFilter(BotStates.entering_id) # Фильтрация по состоянию BotStates.entering_id
)
async def processing_code(message: Message, state: FSMContext):
    processing_code = await process_message(message.text) # Текст, который ввел пользователь после сообщения "Введите свой ID"
    await state.set_state(None) # Убираем состояние
    await message.answer(processing_code)

# Функция-обработчик пользовательского сообщения
# вызываем с ключевым словом await, так как она асинхронная
async def process_message(text: str) -> str:
    # Обработка сообщения пользователя
    return text

# Запуск бота
async def main():
    bot = Bot('7713433364:AAFT9GLnpec9JxIpbaMAcneLUMVmrcns4Iw')
    dp = Dispatcher()

    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True) # Удаляем все обновления
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())