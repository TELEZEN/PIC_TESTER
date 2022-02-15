#created by by @Arjun_La_Lis_A - tg
#codes by @PaulWalker_tg

from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.neededshits.cust_p_filters import f_onw_fliter

# EMOJI CONSTANTS
DICE_E_MOJI = "🎲"
# EMOJI CONSTANTS


@Client.on_message(
    filters.command(["roll", "dice"], COMMAND_HAND_LER) &
    f_onw_fliter
)
async def roll_dice(client, message):
    """ @RollaDie """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=DICE_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )
