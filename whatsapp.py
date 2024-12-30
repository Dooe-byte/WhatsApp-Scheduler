import pywhatkit as kit # type: ignore
from datetime import datetime

def send_whatsapp_message():
    
    phone_number = '+1********' # Don't forget to include the country code
    message = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


    current_time = datetime.now()
    hour = current_time.hour
    minute = current_time.minute + 2  

    
    if minute >= 60:
        minute -= 60  
        hour += 1    

    
    if hour >= 24:
        hour = 0  

    
    print(f"Scheduled message to {phone_number} at {hour:02d}:{minute:02d}")

    
    try:
        kit.sendwhatmsg(phone_number, message, hour, minute)
        print(f"Message sent to {phone_number} at {hour:02d}:{minute:02d}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    send_whatsapp_message()
