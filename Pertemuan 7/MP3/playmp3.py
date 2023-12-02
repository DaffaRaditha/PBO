from playsound import playsound  # Import modul playsound
import tkinter as tk  # Import modul tkinter untuk GUI

def play_music():
    global audio  # Variabel global untuk menyimpan status pemutaran audio
    audio = True
    playsound("musik.mp3", True)  # Memutar file "musik.mp3" tanpa blocking (False)

def stop_music():
    global audio  # Variabel global untuk menyimpan status pemutaran audio
    audio = False

# Fungsi untuk menghentikan pemutaran musik
def stop():
    global audio
    if audio:
        playsound(None)  # Menghentikan pemutaran musik jika sedang berlangsung

# Membuat jendela tkinter
window = tk.Tk()
window.title("Pemutar Musik")  # Judul jendela

# Membuat tombol untuk memutar musik
play_button = tk.Button(window, text="Putar Musik", command=play_music, bg='darkblue', fg='white')
play_button.pack(pady=20)

# Membuat tombol untuk menghentikan musik
stop_button = tk.Button(window, text="Stop Musik", command=stop, bg='darkblue', fg='white')
stop_button.pack(pady=10)

# Menampilkan jendela
window.mainloop()
