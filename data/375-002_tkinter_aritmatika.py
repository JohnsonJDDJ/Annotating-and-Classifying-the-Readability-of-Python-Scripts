import tkinter as tk
from functools import partial

def pertambahan (labelhasil, bil1, bil2):
    b1 = int(bil1.get())
    b2 = int(bil2.get())
    hasil = b1 + b2
    
    # config digunakan untuk mengakses object atribut setelah inisialisasi
    labelhasil.config(text=hasil)
    return
    
root = tk.Tk()
# 400x200 adalah lebar dan tinggi
# 500 adalah posisi secara horizontal
# 200 adalah posisi secara vertikal
root.geometry("400x200+500+200")
    
# mengubah font
root.option_add("font", ("Verdana", 10, "normal"))
    
# Menampilkan title di window border
root.title('Aritmatika')

# configure untuk mengubah warna
# root.configure(bg= "#FFFFF")

labelbilangan1 = tk.Label(root, text= "Masukkan Bilangan 1")
labelbilangan1.grid(row=0, column=0, padx=(10,20))
labelbilangan2 = tk.Label(root, text="Masukkan Bilangan 2")
labelbilangan2.grid(row=1, column=0, padx=(10,20))
# StringVar() digunakan untuk menampung inputan tipe String
bilangan1 = tk.StringVar()
bilangan2 = tk.StringVar()

inputBilangan1 = tk.Entry(root, textvariable=bilangan1)
inputBilangan1.grid(row=0, column=1)
inputBilangan2 = tk.Entry(root, textvariable=bilangan2)
inputBilangan2.grid(row=1, column=1)

labelHasil = tk.Label(root)
labelHasil.grid(row=2, column=1)

# Functools.partial untuk membuat fungsi baru atau versi baru dengan argumen
pertambahan = partial(pertambahan, labelHasil, bilangan1, bilangan2)
tombolTambah = tk.Button(root, text = "Tambah", command=pertambahan)
# sticky digunakan untuk penyesuaian widget di dalam cell
# sticky="W" yang artinya adalah West adalah posisi widget di kiri (di dalam cell)
# sticky="E" yang artinya adalah East adalah posisi widget di kanan (di dalam cell)
# sticky = "WE" artinya memenuhi cell atau alignment rata penuh
# padx adalah padding horizontal
# pady adalah padding vertikal

tombolTambah.grid(row=2, column=0, sticky="WE", padx=(10,20), pady=(5,0))
tombolTambah.config(bg="#000", fg="#fff")

root.mainloop()