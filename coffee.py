import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class CoffeeShopApp:
    def __init__(self, master):
        self.master = master
        self.master.title("STARBUCKS")

        self.total_price = 0

        # Frame untuk kata sambutan dan gambar menu
        self.header_frame = tk.Frame(self.master)
        self.header_frame.pack()

        # Kata sambutan
        self.greeting_label = tk.Label(self.header_frame, text="Welcome to Starbucks!", font=("Helvetica", 30))
        self.greeting_label.pack()

        # Gambar menu
        self.menu_image = Image.open("menu.jpg")
        self.menu_photo = ImageTk.PhotoImage(self.menu_image)
        self.menu_label = tk.Label(self.header_frame, image=self.menu_photo)
        self.menu_label.pack()

        # Frame untuk menampilkan daftar menu
        self.menu_frame = tk.Frame(self.master)
        self.menu_frame.pack()

        # Daftar menu dan harga
        self.menu_items = {
            "Nuttela Frappuccino": 8.7,
            "Shrek Frappe": 9.2,
            "Ariana Grande Frappuccino": 10.1,
            "Butterbeer Frappuccino": 8.7,
            "Mango Espresso": 8.1,
            "Rasberry Caramel Macchiato": 7.1,
            "Red Velvet Frappuccino": 8.7,
            "Chocolate Banana Mocha Frappucino": 9.0
        }

        # Membuat tombol untuk setiap menu
        row = 0
        column = 0
        for item, price in self.menu_items.items():
            btn = tk.Button(self.menu_frame, text=f"{item} - ${price}", command=lambda i=item, p=price: self.add_to_cart(i, p))
            btn.grid(row=row, column=column, padx=10, pady=5)
            column += 1
            if column == 3:
                column = 0
                row += 1

        # Frame untuk keranjang belanja
        self.cart_frame = tk.Frame(self.master)
        self.cart_frame.pack()

        # Label dan tombol untuk total harga
        self.total_label = tk.Label(self.cart_frame, text="Total: $0.00")
        self.total_label.pack()
        
        self.checkout_button = tk.Button(self.cart_frame, text="Checkout", command=self.checkout, bg="#90EE90")
        self.checkout_button.pack()

    def add_to_cart(self, item, price):
        self.total_price += price
        self.total_label.config(text=f"Total: ${self.total_price:.2f}")
        messagebox.showinfo("Info", f"{item} ditambahkan ke keranjang.")

    def checkout(self):
        messagebox.showinfo("Checkout", f"Total belanja Anda adalah ${self.total_price:.2f}. Terima kasih telah berbelanja!")
        self.total_price = 0
        self.total_label.config(text="Total: $0.00")


def main():
    root = tk.Tk()
    app = CoffeeShopApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
