from telethon import events
from telethon.utils import pack_jbot_file_id


@tgjbot.on(events.NewMessage(pattern="^/id"))
async def _(event):
    if event.reply_to_msg_id:
        await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            jbot_api_file_id = pack_jbot_file_id(r_msg.media)
            await tgjbot.send_message(
                event.chat_id,
                "Current Chat ID: `{}`\nFrom User ID: `{}`\nBot API File ID: `{}`".format(
                    str(event.chat_id), str(r_msg.sender_id), jbot_api_file_id
                ),
            )
        else:
            await tgjbot.send_message(
                event.chat_id,
                "Current Chat ID: `{}`\nFrom User ID: `{}`".format(
                    str(event.chat_id), str(r_msg.sender_id)
                ),
            )
    else:
        await tgjbot.send_message(
            event.chat_id, "Current Chat ID: `{}`".format(str(event.chat_id))
        )
