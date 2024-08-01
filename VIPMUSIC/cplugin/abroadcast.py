import asyncio
from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import AUTO_GCAST, AUTO_GCAST_MSG
from VIPMUSIC import app
from VIPMUSIC.utils.database import get_served_chats_clone

# Convert AUTO_GCAST to boolean based on "On" or "Off"
AUTO_GCASTS = True

START_IMG_URLS = "https://te.legra.ph/file/58f0f65ff6d4e80a99afd.jpg"

MESSAGES = f"""**"မမဋီကာ (၂)''

ကမ္ဘာကို ကျောခိုင်းပြီး
ကမ္ဘာကြီးဆီ ထွက်လာလိုက်တယ်...
ပျော်ရွှင်ခြင်း ကို ကျနော်မရှာဘူး...
မမ က ယူလာပေးတာ...

ဓားတောင်နဲ့မီးပင်လယ် ဖြတ်မယ့်ကောင်က
မိုးခြိမ်းသံကြားတော့  မမရေ တဲ့...

သည်းပါတယ်ဆိုတဲ့ တိမ်တွေအောက်
ကလေးလို ကျနော်ပြေးဝင်တယ်...

မိုးစက်တွေမဟုတ်ဘူး...
အဲ့ဒါ မမဆံနွယ်တွေ...

🍂💌**"""
BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "๏ ꜱᴜᴘᴘᴏʀᴛ ๏",
                url=f"https://t.me/seriousvs_version20",
            )
        ]
    ]
)

MESSAGE = f"""**๏ ᴛʜɪs ɪs ᴀᴅᴠᴀɴᴄᴇᴅ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs + ᴄʜᴀɴɴᴇʟs ᴠᴄ. 💌

🎧 ᴘʟᴀʏ + ᴠᴘʟᴀʏ + ᴄᴘʟᴀʏ 🎧

➥ sᴜᴘᴘᴏʀᴛᴇᴅ ᴡᴇʟᴄᴏᴍᴇ - ʟᴇғᴛ ɴᴏᴛɪᴄᴇ, ᴛᴀɢᴀʟʟ, ᴠᴄᴛᴀɢ, ʙᴀɴ - ᴍᴜᴛᴇ, sʜᴀʏʀɪ, ʟᴜʀɪᴄs, sᴏɴɢ - ᴠɪᴅᴇᴏ ᴅᴏᴡɴʟᴏᴀᴅ, ᴇᴛᴄ... ❤️

🔐ᴜꜱᴇ » [/start](https://t.me/{app.username}?start=help) ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ

➲ ʙᴏᴛ :** @{app.username}"""

BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "๏ ᴋɪᴅɴᴀᴘ ᴍᴇ ๏",
                url=f"https://t.me/sasuke2ndmusic_bot?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users",
            )
        ]
    ]
)

caption = f"""{AUTO_GCAST_MSG}""" if AUTO_GCAST_MSG else MESSAGES

TEXT = """**ᴀᴜᴛᴏ ɢᴄᴀsᴛ ɪs ᴇɴᴀʙʟᴇᴅ sᴏ ᴀᴜᴛᴏ ɢᴄᴀsᴛ/ʙʀᴏᴀᴅᴄᴀsᴛ ɪs ᴅᴏɪɴɢ ɪɴ ᴀʟʟ ᴄʜᴀᴛs ᴄᴏɴᴛɪɴᴜᴏᴜsʟʏ.**\n**ɪᴛ ᴄᴀɴ ʙᴇ sᴛᴏᴘᴘᴇᴅ ʙʏ ᴘᴜᴛ ᴠᴀʀɪᴀʙʟᴇ [ᴀᴜᴛᴏ_ɢᴄᴀsᴛ = (Off)]**"""


async def send_message_to_chats(client: Client, message: Message):
    try:
        chats = await get_served_chats_clone()

        for chat_info in chats:
            chat_id = chat_info.get("chat_id")
            if isinstance(chat_id, int):
                try:
                    await client.send_photo(
                        chat_id,
                        photo=START_IMG_URLS,
                        caption=caption,
                        reply_markup=BUTTONS,
                    )
                    await asyncio.sleep(20)
                except Exception as e:
                    pass
    except Exception as e:
        pass


async def continuous():
    while True:
        if AUTO_GCASTS:
            try:
                await send_message_to_chats()
            except Exception as e:
                pass
        await asyncio.sleep(100000)


if AUTO_GCASTS:
    asyncio.create_task(continuous())
