import logging
from aiogram.types import ReplyKeyboardMarkup ,KeyboardButton
from aiogram import Bot ,Dispatcher ,executor,types
from aiogram.types import *
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboards import*


logging.basicConfig(level=logging.INFO)
BOT_TOKEN = "5837029045:AAFZdnzW41i4D_gco1AmrbpX0KmNV-iR4aw"

bot = Bot(token=BOT_TOKEN,parse_mode="html")
storage = MemoryStorage()
dp = Dispatcher(bot=bot,storage=storage)


images = ["1.jpg","2.jpg","3.jpg",]

@dp.message_handler(commands=["start"])
async def start_bot(message:Message):
    await message.answer("Salom.\n\nGalllery:/img")



@dp.message_handler(commands=["img"])
async def img_gallery(message:Message,state:FSMContext):
    btn = await img_btn(1,len(images))
    await state.update_data(page=1)
    await message.answer_photo(InputFile("1.jpg"),reply_markup=btn)

@dp.callback_query_handler(text = 'next')
async def next_img(call: CallbackQuery,state:FSMContext):
    data = await state.get_data()
    if data ["page"] < len(images):
        img_num = data ["page"] +1
        await state.update_data(page = img_num)
        btn = await img_btn(img_num, len(images))
        await call.message.edit_media(InputMediaPhoto(InputFile(images[img_num-1])), reply_markup=btn)


@dp.callback_query_handler(text = 'prev')
async def next_img(call: CallbackQuery,state:FSMContext):
    data = await state.get_data()
    if data ["page"] > 1:
        img_num = data ["page"] - 1  
        await state.update_data(page = img_num)
        btn = await img_btn(img_num, len(images))
        await call.message.edit_media(InputMediaPhoto(InputFile(images[img_num-1])), reply_markup=btn)


if __name__ == "__main__":
    executor.start_polling(dp)