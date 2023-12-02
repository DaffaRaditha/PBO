import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Variabel global untuk menyimpan status pemutaran video
playing = False

# Fungsi untuk membuka file video
def buka_file():
    global playing
    playing = True
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi")])
    if file_path:
        cap = cv2.VideoCapture(file_path)
        if not cap.isOpened():
            status_label.config(text="Error opening video file")
        else:
            status_label.config(text="File video dibuka")
            play_video(cap)

# Fungsi untuk memainkan video
def play_video(cap):
    global playing
    ret, frame = cap.read()
    if ret and playing:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (640, 480))  # Ubah ukuran frame jika diperlukan
        img = Image.fromarray(frame)
        img = ImageTk.PhotoImage(image=img)
        label.imgtk = img  # Simpan referensi agar gambar tidak dihapus oleh garbage collector
        label.config(image=img)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            return
        else:
            label.after(25, lambda: play_video(cap))  # Teruskan pemutaran video
    else:
        cap.release()
        status_label.config(text="Video selesai")

# Fungsi untuk menghentikan pemutaran video
def stop_video():
    global playing
    playing = False

# Membuat GUI
root = tk.Tk()
root.title("Pemutar Video")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

button_buka = tk.Button(frame, text="Buka File Video", command=buka_file, bg='darkblue', fg='white')
button_buka.pack(padx=5, pady=5)

button_stop = tk.Button(frame, text="Stop", command=stop_video,  bg='darkblue', fg='white')
button_stop.pack(padx=5, pady=5)

status_label = tk.Label(frame, text="")
status_label.pack(padx=5, pady=5)

label = tk.Label(frame)
label.pack()

root.mainloop()
