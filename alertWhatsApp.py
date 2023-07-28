import pywhatkit
import datetime

def alert():
    myobj = datetime.now()
    pywhatkit.sendwhatmsg_to_group("KGJ5Jc0nRWnIEsIH3MhdCs", "Motion detected at " + str(myobj.hour) + ":"+ str(myobj.minute)+ ", please check." , myobj.hour , myobj.minute+1 , 10, True, 5) #group
    pywhatkit.sendwhatmsg("+6285291612998", "test 1 2 3", myobj.hour , myobj.minute+1) #personal chat
