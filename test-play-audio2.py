import pygame as pg
import os
import tkinter as tk
import time

audioDirectory = r'F:\Kuliah\PKM\Python\3x7\sound'
#   audioDirectory = os.path.join(os.path.expanduser('~'), 'Documents', '3x7', 'sound')
os.chdir(audioDirectory)

pg.init()
pg.mixer.init()

sounds = [
    ["2lll.wav", "2ll.wav", "2l.wav", "2c.wav", "2r.wav", "2rr.wav", "2rrr.wav"],
    ["0lll.wav", "0ll.wav", "0l.wav", "0c.wav", "0r.wav", "0rr.wav", "0rrr.wav"],
    ["1lll.wav", "1ll.wav", "1l.wav", "1c.wav", "1r.wav", "1rr.wav", "1rrr.wav"]
]

buttonName = [
    ["30LLL", "30LL", "30L", "30C", "30R", "30RR", "30RRR"],
    ["0LLL", "0LL", "0L", "0C", "0R", "0RR", "0RRR"],
    ["-30LLL", "-30LL", "-30L", "-30C", "-30R", "-30RR", "-30RRR"]
]

distance = float(1)
beep = int(1)
beepDelay = float(0.1)

def mapDistanceVolume(distance, from_min, from_max, to_min, to_max):
    percentage = (distance - from_min)/(from_max - from_min)
    mappedDistance = (percentage * (to_max - to_min)) + to_min
    
    return mappedDistance

def playSound(i, j):
    distance = distanceSlider.get()
    if 0.1 <= distance <= 1:
        beep = 4
        beepDelay = 0.2
    elif 1 < distance <= 2:
        beep = 3
        beepDelay = 0.5
    elif 2 < distance <= 3:
        beep = 2
        beepDelay = 0.8
    elif 3 < distance <= 4:
        beep = 1
        beepDelay = 1

    for x in range(beep):
        pg.mixer.music.load(sounds[i][j])
        volume = float(1/(distance**2))
        mappedVolume = mapDistanceVolume(volume, 0.0625, 4, 20, 100)
        pg.mixer.music.set_volume(mappedVolume)
        pg.mixer.music.play()
        time.sleep(beepDelay)

    print(f"i:{i}\nj:{j}")

root = tk.Tk()
root.title("Direction")

for i in range(3):
    for j in range(7):
        button = tk.Button(
            root,
            text = buttonName[i][j],
            width = 8, height = 5,
            command = lambda i=i, j=j: playSound(i, j),
        )

        button.grid(row = i, column = j, padx = 0, pady = 0)

sliderLabel = tk.Label(root, text="Distance (m)", anchor="center")
sliderLabel.grid(row=i+1, column=0, columnspan=7, padx=10, pady=10)

distanceSlider = tk.Scale(
    root,
    from_ = 0.1, to = 4, resolution = 0.1,
    orient = tk.HORIZONTAL,
    length = 300
)
distanceSlider.grid(row=i+2, column=0, columnspan=7, padx=10, pady=0)

root.mainloop()