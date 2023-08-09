import cv2
import time
import datetime
import schedule
from datetime import date
from datetime import datetime
import pywhatkit 
import telepot
# import os

# Initialize parameters
is_recording = False
folder_path = 'recordingsISR'
days_threshold = 30

# System starts
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
timestamp = str(date.today())
filename = 'Lab ISR' + timestamp + '.avi'
out = cv2.VideoWriter(filename, fourcc, 5.0, (1280,720))
cap = cv2.VideoCapture(0)
ret, frame1 = cap.read()
ret, frame2 = cap.read()

image = cv2.resize(frame1, (1280,720))
out.write(image)
date1 = str(datetime.now())
cv2.putText(frame1, date1, (10,50), cv2.LINE_AA, 1, (255,255,0), 2)
cv2.imshow("Lab ISR", frame1)
frame1 = frame2
ret, frame2 = cap.read()

#notify
def alert1(): #WhatsApp Group alert
    myobj = datetime.now()
    pywhatkit.sendwhatmsg_to_group("Group_ID", "Motion detected at " + str(myobj.hour) + ":"+ str(myobj.minute)+ ", please check." , myobj.hour , myobj.minute+1 , 10, True, 5)

def alert2(): #Telegram Group alert
    myobj = datetime.now()
    token = 'Group_Token'
    receiver_id = 'Chat_ID'
    text = "Motion detected at " + str(myobj.hour) + ":"+ str(myobj.minute)+ ", please check."

    bot = telepot.Bot(token)
    bot.sendMessage(receiver_id,text)

# Motion Detection 
def motion_detecting():
    global is_recording

    while cap.isOpened() and is_recording:
        ret, frame1 = cap.read()
        ret, frame2 = cap.read()
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # motion_detected = False
        for contour in contours:
            if cv2.contourArea(contour) > 5000:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame1, "Status: {}".format('Ada maling euy.....'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                alert1()
                alert2()
                print("is it blocking?") #checkpoin1
                break

        image = cv2.resize(frame1, (1280,720))
        out.write(image)
        date1 = str(datetime.now())
        cv2.putText(frame1, date1, (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 2)
        cv2.imshow("Lab ISR", frame1)
        frame1 = frame2

        ret, frame2 = cap.read()

        if cv2.waitKey(10) == ord('q'):
            break

def start_video_recording():
    global is_recording
    # record video 
    is_recording = True


def stop_video_recording():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    global is_recording
    if is_recording:
        #stop record
        out.release()
        is_recording = False



#scheduling
def run_scheduling():
    print("masuk sini....") #checkpoin2

    # scheduled at 17:00
    schedule.every().day.at('17:00').do(start_video_recording)
    schedule.every().day.at('17:00').do(motion_detecting)
    # schedule.every().day.at('17:00').do(alert)


    # scheduled at 9:00 on the next day
    schedule.every().day.at('09:00').do(stop_video_recording)
    # schedule.every().day.at('09:00').do(alert)

    while True:
        print("masuk sini juga...") #checkpoin3
        schedule.run_pending()
        time.sleep(1)


# #delete file > 30 days
# def delete_old_files(folder_path, days_threshold):
#     today = datetime.now()
#     for filename in os.listdir(folder_path):
#         file_path = os.path.join(folder_path, filename)
#         if os.path.isfile(file_path):
#             creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
#             age_in_days = (today - creation_time).days
#             if age_in_days > days_threshold:
#                 os.remove(file_path)
#                 print(f"Deleted file: {file_path}")

if __name__ == "__main__":
    while True:
        run_scheduling()
