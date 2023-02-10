import time
import tkinter as tk
from tkinter import *
import datetime
from datetime import datetime
from datetime import timedelta
from plyer import notification


def main():
    win = tk.Tk()
    win.title("Work Hours")
    win.geometry("250x250")
    win.minsize(250, 250)
    win.resizable(False, False)

    l = Label(win, text="Hours of the Day")
    l.config(font=("Courier", 14))

    b1 = Button(win, text="16:30", command=lambda: notifyUser(win,"16:30"))
    b2 = Button(win, text="17:00", command=lambda: notifyUser(win,"17:00"))
    b3 = Button(win, text="18:00", command=lambda: notifyUser(win,"18:00"))

    l.pack()
    b1.pack()
    b2.pack()
    b3.pack()

    win.mainloop()
    return


def notifyUser(win,workHours):
    print("User selected: {}" .format(workHours))
    win.destroy()
    while True:
        now_time = datetime.now().strftime("%H:%M")
        if now_time == workHours:
            tme = datetime.now().strftime("%H:%M:%S %d-%m-%y")
            print("Work End - {}".format(tme))
            notification.notify(
                title="Stand up: {}".format(tme),
                message="Time to use your card!",
                app_icon="working.ico",
                timeout=50
            )
            print("Work End - {}".format(tme))
            break
            exit()
        else:
            continue
    return


if __name__ == "__main__":
    main()
