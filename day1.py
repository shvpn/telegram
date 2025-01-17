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
    device_model='IPhone X',     # Custom device name
    system_version='16.5',         # Custom system version
    app_version='1.0'                   # Custom app version
)
async def auto_reply():
    @client.on(events.NewMessage(incoming=True))  # Listen for new incoming messages
    async def handler(event):
        # Get the sender
        sender = await event.get_sender()
        
        # Avoid replying to yourself or channels
        if sender and not sender.bot and not event.is_channel:
            reply_message = "Wait 15 minutes because I'm currently unavailable."
            await event.reply(reply_message)
            print(f"Replied to {sender.username or sender.id} with: {reply_message}")

    print("Auto-reply is active.")
    await client.run_until_disconnected()


def get_list_contact():
    with client:
        for contact in client.iter_dialogs():
            print(contact.name)
            print(contact.id)





if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(auto_reply())
