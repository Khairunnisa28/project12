import tkinter as tk
from tkinter import messagebox

# Dictionary untuk menyimpan informasi makanan (nama dan harga)
food_menu = {
    "Nasi Goreng": 15000,
    "Soto": 13000,
    "Mie Ayam": 10000,
    "Bakso": 15000,
    "Mie Goreng": 10000,
    "Rawon": 18000,
    "Gado-Gado": 14000,
    "Nasi Kuning": 12000,
    "Ayam Goreng": 17000,
    "Rendang": 20000
}

# Dictionary untuk menyimpan informasi minuman (nama dan harga)
drink_menu = {
    "Es Teh Manis": 5000,
    "Es Jeruk": 9000,
    "Air Mineral": 3000,
    "Aneka Jus": 10000,
    "Es Campur": 10000,
    "Es Cincau": 6000,
    "Soda Gembira": 8000,
    "Teh Tarik": 7000,
    "Kopi Susu": 5000,
    "Es Cendol": 7000
}

# List untuk menyimpan keranjang pesanan
cart = []

def add_to_cart():
    makanan = makanan_var.get().split('. ')[1].split(' (')[0].strip()
    porsi = int(porsi_entry.get())
    makanan_harga = food_menu[makanan]
    cart.append((makanan, porsi, makanan_harga))
    
    minuman = minuman_var.get().split('. ')[1].split(' (')[0].strip()
    gelas = int(gelas_entry.get())
    minuman_harga = drink_menu[minuman]
    cart.append((minuman, gelas, minuman_harga))
    
    update_cart_label()
    hitung_total_belanjaan()

def update_cart_label():
    cart_label.config(text="Keranjang:\n" + "\n".join([f"{item[1]}x {item[0]} (Rp {item[2]} each)" for item in cart]))

def hitung_total_belanjaan():
    total_belanjaan = sum(item[1] * item[2] for item in cart)
    total_belanjaan_label.config(text=f"Total Belanjaan: Rp {total_belanjaan}")

def hitung_tagihan():
    total_pembelian_sebelum_ppn = sum(item[1] * item[2] for item in cart)
    ppn = total_pembelian_sebelum_ppn * 0.11
    total_pembelian = total_pembelian_sebelum_ppn + ppn

    total_pembelian_label_entry.delete(0, tk.END)
    total_pembelian_label_entry.insert(0, f"Rp {total_pembelian}")

    uang_diberikan = int(uang_entry.get())
    kembalian = uang_diberikan - total_pembelian

    if kembalian >= 0:
        notification_msg = f"Selamat Datang, {pembeli_entry.get()}!\n\nTotal Pembelian (belum termasuk PPN 11%): Rp {total_pembelian_sebelum_ppn}\n\nKeranjang:\n"
        for item in cart:
            notification_msg += f"- {item[1]}x {item[0]} (Rp {item[2]} each)\n"
        notification_msg += f"\nPPN 11%: Rp {ppn}\nTotal Pembelian (termasuk PPN 11%): Rp {total_pembelian}\n\nUang yang diberikan: Rp {uang_diberikan}\nKembalian: Rp {kembalian}\n\nTerima kasih telah berbelanja!"
    else:
        notification_msg = "Maaf, uang yang diberikan tidak mencukupi untuk pembelian ini. Silakan masukkan uang yang cukup."

    messagebox.showinfo("Nota Pembayaran", notification_msg)

app = tk.Tk()
app.title("Restoran Pak Mbud")
app.geometry("500x600")

pembeli_label = tk.Label(app, text="Masukkan nama Pembeli:")
pembeli_label.pack()
pembeli_entry = tk.Entry(app)
pembeli_entry.pack()

makanan_label = tk.Label(app, text="Pilih Makanan:")
makanan_label.pack()

makanan_var = tk.StringVar()
makanan_var.set("")
makanan_option = tk.OptionMenu(app, makanan_var, *["{}. {} (Rp {})".format(num, food, price) for num, (food, price) in enumerate(food_menu.items(), start=1)])
makanan_option.pack()

porsi_label = tk.Label(app, text="Berapa Porsi:")
porsi_label.pack()
porsi_entry = tk.Entry(app)
porsi_entry.pack()

minuman_label = tk.Label(app, text="Pilih Minuman:")
minuman_label.pack()

minuman_var = tk.StringVar()
minuman_var.set("")
minuman_option = tk.OptionMenu(app, minuman_var, *["{}. {} (Rp {})".format(num, drink, price) for num, (drink, price) in enumerate(drink_menu.items(), start=1)])
minuman_option.pack()

gelas_label = tk.Label(app, text="Berapa Gelas:")
gelas_label.pack()
gelas_entry = tk.Entry(app)
gelas_entry.pack()

add_button = tk.Button(app, text="Tambah ke Keranjang", command=add_to_cart)
add_button.pack()

cart_label = tk.Label(app, text="Keranjang:")
cart_label.pack()

total_belanjaan_label = tk.Label(app, text="Total Belanjaan: Rp 0")
total_belanjaan_label.pack()

total_pembelian_label = tk.Label(app, text="Total Pembelian:")
total_pembelian_label.pack()
total_pembelian_label_entry = tk.Entry(app)
total_pembelian_label_entry.pack()

uang_label = tk.Label(app, text="Uang Tunai Pembeli:")
uang_label.pack()
uang_entry = tk.Entry(app)
uang_entry.pack()

hitung_button = tk.Button(app, text="Hitung", command=hitung_tagihan)
hitung_button.pack()

app.mainloop()
