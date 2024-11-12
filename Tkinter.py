# Mengimpor library tkinter untuk GUI dan messagebox
import tkinter as tk
from tkinter import messagebox

# Fungsi untuk melakukan prediksi dan menampilkan hasil
def hasil_prediksi():
    # Memeriksa setiap input untuk memastikan tidak ada nilai yang kosong
    for entry in nilai_entries:
        # Statement if: Jika salah satu entry kosong, tampilkan label kesalahan dibawah
        if entry.get().strip() == "":
            hasil_label.config(text="Harap isi semua nilai mata pelajaran.", fg="red")
            return  # Keluar dari fungsi
    
    try:
        # Memeriksa nilai untuk setiap entry
        for entry in nilai_entries:
            nilai = int(entry.get())  # Mengonversi nilai entry menjadi integer
            # Memastikan nilai berada di antara 0 dan 100
            if not (0 <= nilai <= 100):
                # Menampilkan informasi jika nilai tidak valid
                messagebox.showinfo("Informasi", "Nilai harus antara 0 dan 100.")
                return  # Keluar dari fungsi jika nilai tidak valid
        # Jika semua nilai valid, tampilkan hasil prediksi untuk prodi
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")
    except ValueError as ve:
        # Menampilkan pesan error jika input bukan angka
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka")
        return  # Keluar dari fungsi
    
    # Menampilkan hasil akhir
    hasil_label.config(text="Prodi Pilihan: Teknologi Informasi", fg="black")

# Membuat window utama
window = tk.Tk()
window.title("Aplikasi Prediksi Prodi Pilihan")  # Menetapkan title window

# Membuat label judul
judul_label = tk.Label(window, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
# Menempatkan label
judul_label.grid(row=0, column=0, columnspan=2, pady=10)

# Membuat list untuk menyimpan semua entry input nilai
nilai_entries = []

# Loop untuk membuat 10 input nilai (untuk 10 mata pelajaran)
for i in range(10):
    # Membuat label untuk setiap input nilai
    label = tk.Label(window, text=f"Nilai Mata Pelajaran {i+1} :")
    label.grid(row=i+1, column=0, padx=1, pady=5, sticky="w")  # Menempatkan label (w=west/sebelah kiri)
    # Membuat entry untuk input nilai
    entry = tk.Entry(window)
    entry.grid(row=i+1, column=1, padx=1, pady=5)  # Menempatkan entry
    # Menambahkan entry ke dalam list nilai_entries
    nilai_entries.append(entry)

# Membuat tombol
prediksi_button = tk.Button(window, text="Hasil Prediksi", command=hasil_prediksi)
# Menempatkan tombol
prediksi_button.grid(row=11, column=0, columnspan=2, pady=10)

# Menambahkan label
hasil_label = tk.Label(window, text="", font=("Arial", 14))
# Menempatkan label hasil
hasil_label.grid(row=12, column=0, columnspan=2, pady=10)

# Menjalankan window
window.mainloop()
