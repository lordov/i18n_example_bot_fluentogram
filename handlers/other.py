from aiogram import Router
from aiogram.types import Message
from fluentogram import TranslatorRunner
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from locales.stub import TranslatorRunner

# Инициализируем роутер уровня модуля
other_router = Router()


# Этот хэндлер будет срабатывать на любые сообщения и
# отправлять пользователю их копию
@other_router.message()
async def send_echo(message: Message, i18n: TranslatorRunner):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=i18n.no.copy())
