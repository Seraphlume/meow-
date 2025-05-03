import tkinter as tk
import pygame
import time
import threading

# Inisialisasi pygame mixer
pygame.mixer.init()

# Load file suara kucing (pastikan file 'meow.wav' berada di folder yang sama)
meow_sound = pygame.mixer.Sound("meow.mp3")

# Fungsi untuk menampilkan pop-up dengan emote kucing
def show_cat_emote():
    def create_window():
        root = tk.Tk()
        root.title("Cat Emote!")
        root.attributes("-topmost", True)
        label = tk.Label(root, text="Meow~ 🐱", font=("Arial", 40))
        label.pack()
        root.after(3000, root.destroy)  # Tutup setelah 3 detik
        root.mainloop()

    threading.Thread(target=create_window, daemon=True).start()

# Fungsi untuk memainkan suara kucing asli
def play_meow_sound():
    meow_sound.play()

# Loop utama: jalankan event setiap 10 detik (bisa diganti ke 3600 untuk setiap 1 jam)
while True:
    print("Meow event triggered at", time.strftime("%H:%M:%S"))
    show_cat_emote()
    play_meow_sound()
    time.sleep(10)
