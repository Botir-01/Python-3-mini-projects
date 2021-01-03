# ===================================Numbers==================================
# A simple clock where it plays a sound after x number of minutes/seconds or at a particular time.

import os
from playsound import playsound
from datetime import datetime
import time

os.chdir('../../Music/')

music_list = [
    '`_.mp3', '476739424.m4a', 'BÖ   Serhat Durmus - Elimi Tut (ft.Ecem Telli)',
    'Dorian - La Tormenta de arena - Vídeo oficial.mp3', 'ew.mp3', 'ffd.mp3',
    'Fun. ft Janelle Monae - We Are Young Official Lyrics.mp3',
    'Gotye - Somebody That I Used To Know (feat. Kimbra) - offici.mp3',
    'John Legend - All of Me (Edited Video).mp3', 'Miley Cyrus - Wrecking Ball (Official Video).mp3',
    'N_3_0 - Killing me inside Remix.mp3', 'rer.mp3', 'rw.mp3',
    'TGDTSoundtrack - The Irrepressibles - In This Shirt.mp3',
]


def music_to_play():
    choice = 0
    while True:
        try:
            choice = int(input('What would like to listen to : \n'
                               '1: When the fire starts \n'
                               '2: Set it to the rain \n'
                               '3: Serhat Durmus "Elimi Tut" \n'
                               '4: Dorina - La Tormente de arena \n'
                               '5: Shadows on the water \n'
                               '6: In the Dark \n'
                               '7: We Are Young \n'
                               '8: Somebody That I used to know \n'
                               '9: All of me \n'
                               '10: Wrecking Ball \n'
                               '11: Killing me indise \n'
                               '12: I will grow I will fight \n'
                               '13: Intro \n'
                               '14: The Irrepressibles - In this Shirt: '))
            if 0 >= choice or choice >= 15:
                print('Please choose one of them!')
                continue
        except:
            print('Please provide an integer value!')
            continue
        else:
            break
    return choice


def certain_time():
    hour = 0
    minute = 0
    while True:
        try:
            hour = int(input('Enter a hour: '))
            minute = int(input('Enter a minute: '))
        except:
            print('Please provide correct numbers!')
            continue
        else:
            break
    music_type = music_to_play()
    while True:
        if hour == int(datetime.today().strftime('%H')) and minute == int(datetime.today().strftime('%M')):
            playsound(music_list[music_type - 1])
            break


def after_minutes_seconds():
    user_choice = 0
    seconds = 0
    minutes = 0
    hours = 0
    while True:
        try:
            user_choice = int(input('What type of unit do you want to wait: \n'
                                    '1: Hours \n'
                                    '2: Minutes \n'
                                    '3: Seconds \n'
                                    '4: Combination: '))
            if 0 >= user_choice or user_choice >= 5:
                print("Choose one of above options!")
                continue
        except:
            print('Please provide an integer value!')
            continue
        else:
            break
    music_type = music_to_play()
    if user_choice == 1:
        while True:
            try:
                hours = int(input('Enter a hour: '))
            except:
                print('Please provide an integer value')
                continue
            else:
                break
        seconds = (hours * 60) * 60
        time.sleep(seconds)
        playsound(music_list[music_type - 1])
    elif user_choice == 2:
        while True:
            try:
                minutes = int(input('Enter a minute: '))
            except:
                print('Please provide an integer value')
                continue
            else:
                break
        seconds = minutes * 60
        time.sleep(seconds)
        playsound(music_list[music_type - 1])
    elif user_choice == 3:
        while True:
            try:
                seconds = int(input('Enter a second: '))
            except:
                print('Please provide an integer value')
                continue
            else:
                break
        time.sleep(seconds)
        playsound(music_list[music_type - 1])
    else:
        while True:
            try:
                hours = int(input('Enter a hour: '))
                minutes = int(input('Enter a minute: '))
                seconds = int(input('Enter a second'))
            except:
                print('Please provide an integer value')
                continue
            else:
                break
        seconds = ((hours * 60) * 60) + (minutes * 60) + seconds
        time.sleep(seconds)
        playsound(music_list[music_type - 1])


def main():
    user_input = 0
    while True:
        try:
            user_input = int(input('What type of alarm would you prefer? \n'
                                   '1 - for particular time \n'
                                   '2 - for after hours/minutes/seconds: '))
            if 0 >= user_input or user_input >= 3:
                print('Please choose one of two options')
                continue
        except:
            print('Please provide an integer value!')
            continue
        else:
            break
    if user_input == 1:
        certain_time()
    elif user_input == 2:
        after_minutes_seconds()


if __name__ == '__main__':
    main()
