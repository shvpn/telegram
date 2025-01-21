from telethon import TelegramClient, events, sync

# Replace with your API credentials
api_id = 20702310
api_hash = '9cfebed918ee36a0aea417c2c0be81c8'
#previes ap


# chat we want to sent message
id_user='senghoutork'

# Create the client and connect
client = TelegramClient(
    session='test',
    api_id=api_id,
    api_hash=api_hash,
    device_model='MY BOT',     # Custom device name
    system_version='16.5',         # Custom system version
    app_version='1.0'                   # Custom app version
)
async def auto_reply():
    @client.on(events.NewMessage(incoming=True))  # Listen for new incoming messages
    async def handler(event):
        # Get the sender
        sender = await event.get_sender()
        
        # Avoid replying to yourself or channels or groups
        if sender and not sender.bot and not event.is_channel and not event.is_group:
            reply_message = "This is an auto-reply. I'm currently unavailable. Perhaps 15 minutes later I will be available."
            await event.reply(reply_message)
            print(f"Replied to {sender.username or sender.id} with: {reply_message}")

    print("Auto-reply is active.")
    await client.run_until_disconnected()





if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(auto_reply())
