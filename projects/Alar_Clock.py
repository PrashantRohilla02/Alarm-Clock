import time
import datetime
import pygame

def set_alarm(timee):
    print(f"alarm set for {timee} ")

    while True:
        current_time = datetime.datetime.now().strftime("%H %M %S")
        print(current_time)

        time.sleep(1)
        if current_time == timee:
            break

if __name__ == "__main__":
    timee= input("enter the time (HH:MM:SS)")
    set_alarm(timee)