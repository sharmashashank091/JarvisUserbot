# created by @Mr_Hops
"""
video meme mashup:
Syntax: .mashup <text>
"""
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from jarvis import CMD_HELP
from jarvis.utils import admin_cmd, sudo_cmd, edit_or_reply


@jarvis.on(admin_cmd(pattern="mashup ?(.*)", outgoing=True))
@jarvis.on(sudo_cmd(pattern="mashup ?(.*)",allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    chat = "@vixtbot"
    await edit_or_reply(event,"```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=285336877)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.edit("Unblock @vixtbot")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("sorry i can't find it")
        else:
            await event.delete()
            await borg.send_file(event.chat_id, response.message, reply_to=reply_to_id)


@jarvis.on(admin_cmd(pattern="mash ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    chat = "@vixtbot"
    await event.delete()
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=285336877)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.reply("Unblock @vixtbot")
            return
        if response.text.startswith("I can't find that"):
            await event.reply("sorry i can't find it")
        else:
            await event.delete()
            await borg.send_file(event.chat_id, response.message, reply_to=reply_to_id)


CMD_HELP.update(
    {
        "mashup": "`.mashup` <text> :\
      \n**USAGE:** Send you the related video message of given text . "
    }
)
