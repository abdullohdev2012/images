from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
async def img_btn(current_img,total_img):
    btn = InlineKeyboardMarkup()
    btn.add(
        InlineKeyboardButton("⏮️", callback_data="prev"),
        InlineKeyboardButton(f"{current_img}/{total_img}", callback_data="000"),
        InlineKeyboardButton("⏭️", callback_data="next"),
    )
    return btn