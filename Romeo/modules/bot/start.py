from Romeo import app
from pyrogram import filters


@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
   await message.reply_text("𝑇𝒉𝑎𝑛𝑘𝑠 𝑓𝑜𝑟 𝑆𝑡𝑎𝑟𝑡 𝑀𝑒... 𝐼'𝑚 ꪜ𝓲ꪶꪶ𝓲ꪖꪀ 𝐴𝑠𝑠𝑖𝑠𝑡𝑎𝑛𝑡")
