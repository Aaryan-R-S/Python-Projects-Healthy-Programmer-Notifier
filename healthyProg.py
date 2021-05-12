from pygame import mixer
from datetime import datetime
from time import time
import os

def audLoop(file, stopAud, msg):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(loops=-1)
    print(f"\n{msg}")

    while True:
        print("\nPress 'd' when DONE!") 
        query = input("  ") 
        if query == stopAud: 
            mixer.music.stop() 
            break


def logFile(msg):
    with open('report.txt', 'a') as e:
        e.write(f"{datetime.now().strftime('%I:%M:%S %p')} : {msg}\n")
    print("Ok!")


if __name__ == "__main__":

    print('\nYour Assistant has Started!')

    if os.path.exists("report.txt"):
        os.remove("report.txt")

    durationInp = time() + float(input('\nEnter Time(in Minutes) Upto Which Assisstant Must Notify You :\n  '))*60

    initDrink = time()
    initEyes = time()
    initExer = time()
    
    drinkSec = 30*60
    eyesSec = 50*60
    exerSec = 80*60

    while durationInp-time() > 0 :
        if time() - initDrink > drinkSec:
            audLoop('drink.mp3', 'd', 'Time to Drink a Glass of Water(250mL)!')
            initDrink = time()
            logFile('Water Drunk - 250 mL')

        if time() - initEyes > eyesSec:
            audLoop('eye.mp3', 'd', 'Time to Relax the Eyes for 2 Minutes!')
            initEyes = time()
            logFile('Eyes Relaxed - 2 Minutes')

        if time() - initExer > exerSec:
            audLoop('exer.mp3', 'd', 'Time to Do Some Exercise for 5 Minutes!')
            initExer = time()
            logFile('Exercise Done - 5 Minutes')

    print('\nAll Done...! Thanks for using Assistant!\n')

