import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from pytesseract import pytesseract

# Fungsi untuk mengekstrak teks dari gambar yang dipilih
def extract_text():
    path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    pytesseract.tesseract_cmd = path_to_tesseract

    # Membuka dialog untuk memilih gambar
    file_path = filedialog.askopenfilename()
    if file_path:
        # Buka gambar menggunakan PIL
        img = Image.open(file_path)
        
        # Tampilkan gambar pada GUI
        img.thumbnail((300, 300))  # Mengatur ukuran gambar agar sesuai dengan GUI
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo
        
        # Ekstrak teks dari gambar
        text = pytesseract.image_to_string(img)
        
        # Tampilkan teks pada label di GUI
        result_label.config(text=text)

# Fungsi untuk membuat GUI dan menampilkan elemen-elemen GUI
def create_gui():
    root = tk.Tk()
    root.title("Ekstrak Teks dari Gambar")

    # Label untuk menampilkan gambar
    global image_label
    image_label = tk.Label(root)
    image_label.pack(pady=10)

    # Tombol "Pilih Gambar" untuk memilih gambar
    select_image_button = tk.Button(root, text="Pilih Gambar", command=extract_text, bg='darkblue', fg='white')
    select_image_button.pack(pady=10)

    # Label untuk menampilkan hasil ekstraksi teks
    global result_label
    result_label = tk.Label(root, text="", wraplength=300, justify="left")
    result_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()