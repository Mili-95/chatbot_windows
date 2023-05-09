import random
import ctypes
import os

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"

WALLPAPER_PATH = "D:\Jesus\crucifixion-latter-day-saints.jpg"
R_OPEN = ctypes.windll.user32.SystemParametersInfoW(20, 0, WALLPAPER_PATH, 3)


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response