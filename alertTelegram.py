import telepot
import datetime


myobj = datetime.datetime.now()

token = 'Group_Token'
receiver_id = 'Chat_ID'
text = "Motion detected at " + str(myobj.hour) + ":"+ str(myobj.minute)+ ", please check."


bot = telepot.Bot(token)
bot.sendMessage(receiver_id,text)
