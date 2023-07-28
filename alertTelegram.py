# import requests

# def telebot(bot_message):
#     bot_token = '6161387808:AAHsSfsiA8i19VYG3J0Q95Itg3WJLttRgIc'
#     bot_chatID = '6161387808'
#     send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=MarkdownV2&text=' + bot_message
    
#     response = requests.get(send_text)

#     return response.json()

# telegram_bot_sendtext("halo")
import telepot
import datetime
#timestamp = str(date.today())
myobj = datetime.datetime.now()

token = '6161387808:AAHsSfsiA8i19VYG3J0Q95Itg3WJLttRgIc'
receiver_id = '-852760651'
text = "Motion detected at " + str(myobj.hour) + ":"+ str(myobj.minute)+ ", please check."
#text = ("aueooeoeo" + text)

bot = telepot.Bot(token)
bot.sendMessage(receiver_id,text)
#bot.sendMessage(receiver_id,'hai')