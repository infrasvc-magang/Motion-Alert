import pywhatkit
import datetime

def alert():
    myobj = datetime.now()
    pywhatkit.sendwhatmsg_to_group("Group_ID", "Motion detected at " + str(myobj.hour) + ":"+ str(myobj.minute)+ ", please check." , myobj.hour , myobj.minute+1 , 10, True, 5) #group
    #pywhatkit.sendwhatmsg("Sender_Number", "Message", Hour , Minute, Delay, True/False, Close Tab) #personal chat
