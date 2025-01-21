from telethon import TelegramClient, events

# Define API credentials
API_ID = 20702310
API_HASH = "9cfebed918ee36a0aea417c2c0be81c8"
BOT_TOKEN = "7266086133:AAHzco2d7Lg_o8nbcM2TOgEgpgTsPtxXXzk"

# Initialize the bot client
bot = TelegramClient("bot3", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

async def my_print_handler(event):
    print(event.text)
async def success(event):
    #skip the first message
    #bot.remove_event_handler(success)
    
    if event.text == "/register":
        await bot.send_message(event.chat_id, f"Please Enter Your Name")
    else:
        await bot.send_message(event.chat_id, f"You have Successfully Registered as {event.text}")
        bot.remove_event_handler(success)
        
  
    

async def register(event):
    bot.add_event_handler(success, events.NewMessage(pattern=".*"))


bot.add_event_handler(register, events.NewMessage(pattern="/register"))




# Start the bot
print("Bot is running...")
bot.run_until_disconnected()
