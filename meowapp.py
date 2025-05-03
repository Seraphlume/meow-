import tkinter as tk
import pygame
import time
import threading

pygame.mixer.init()

meow_sound = pygame.mixer.Sound("meow.mp3")

def show_cat_emote():
    def create_window():
        root = tk.Tk()
        root.title("Cat Emote!")
        root.attributes("-topmost", True)
        label = tk.Label(root, text="Meow~ 🐱", font=("Arial", 40))
        label.pack()
        root.after(3000, root.destroy) 
        root.mainloop()

    threading.Thread(target=create_window, daemon=True).start()

def play_meow_sound():
    meow_sound.play()

while True:
    print("Meow event triggered at", time.strftime("%H:%M:%S"))
    show_cat_emote()
    play_meow_sound()
    time.sleep(10)

#Seraphlume~
