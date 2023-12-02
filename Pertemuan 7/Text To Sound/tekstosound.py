import tkinter as tk
from gtts import gTTS
from playsound import playsound

def buat_file_audio():
    global myobj
    if 'myobj' in globals():
        del myobj  # Hapus objek audio sebelumnya
    teks = teks_entry.get()
    bahasa = 'id'  # Kode bahasa Indonesia
    myobj = gTTS(text=teks, lang=bahasa, slow=False)
    myobj.save("tekstosound.mp3")
    status_label.config(text="File audio telah dibuat!")

def mainkan_audio():
    try:
        if 'myobj' in globals():
            playsound("tekstosound.mp3", True)
            status_label.config(text="Audio sedang diputar.")
        else:
            status_label.config(text="Buat audio terlebih dahulu.")
    except Exception as e:
        status_label.config(text="Terjadi kesalahan saat memutar audio.")

# Membuat jendela tkinter
root = tk.Tk()
root.title("Pemutar Teks ke Audio")

# Membuat label dan input teks
teks_label = tk.Label(root, text="Masukkan teks:")
teks_label.pack()
teks_entry = tk.Entry(root)
teks_entry.pack()

# Tombol untuk membuat file audio
buat_audio_button = tk.Button(root, text="Buat Audio", command=buat_file_audio, bg='darkblue', fg='white')
buat_audio_button.pack()

# Tombol untuk memutar audio
mainkan_audio_button = tk.Button(root, text="Mainkan Audio", command=mainkan_audio, bg='darkblue', fg='white')
mainkan_audio_button.pack()

# Label untuk status
status_label = tk.Label(root, text="")
status_label.pack()

# Menampilkan jendela
root.mainloop()
