import tkinter as tk
from tkinter import messagebox

class AquaBotUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AquaBot - Water Booking System")
        self.root.geometry("500x500")
        self.root.resizable(False, False)

        self.min_quantity = {"drinking": 5, "construction": 500, "household": 50, "water bottles": 15, "others": 5}
        self.prices = {"Mineral water": 15, "Filtered water": 20, "Tap water": 5, "Borewell water": 5, "Municipal water": 10,
                       "River water": 10, "Alkaline water": 20, "Distilled water": 20, "Spring water": 20, "Half ltr": 10,
                       "One ltr": 20, "Purified water": 15}

        self.create_main_menu()

    def create_main_menu(self):
        self.clear_window()
        tk.Label(self.root, text="Welcome to AquaBot", font=("Arial", 16, "bold")).pack(pady=20)

        menu_options = [
            ("Drinking Purpose", "drinking"),
            ("Construction Purpose", "construction"),
            ("Household Purpose", "household"),
            ("Water Bottles", "water bottles"),
            ("Other Purpose", "others")
        ]

        for text, purpose in menu_options:
            tk.Button(self.root, text=text, command=lambda p=purpose: self.select_water_type(p), width=30, height=2).pack(pady=5)

        tk.Button(self.root, text="Exit", command=self.confirm_exit, width=30, height=2, fg="red").pack(pady=20)

    def select_water_type(self, purpose):
        self.clear_window()
        tk.Label(self.root, text="Select Water Type", font=("Arial", 14, "bold")).pack(pady=10)

        water_options = {
            "drinking": ["Mineral water", "Filtered water", "Purified water"],
            "construction": ["Borewell water", "Municipal water", "River water"],
            "household": ["Tap water", "Borewell water", "Municipal water"],
            "water bottles": ["Half ltr", "One ltr"],
            "others": ["Alkaline water", "Distilled water", "Spring water"]
        }

        for water in water_options[purpose]:
            tk.Button(self.root, text=water, command=lambda w=water: self.book_water(w, purpose), width=30).pack(pady=5)

        tk.Button(self.root, text="Back", command=self.create_main_menu, width=30, fg="blue").pack(pady=20)

    def book_water(self, water_type, purpose):
        self.clear_window()
        unit = "bottles" if purpose == "water bottles" else "liters"
        tk.Label(self.root, text=f"Booking {water_type}", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(self.root, text=f"Enter quantity in {unit} (Min {self.min_quantity[purpose]} {unit}):").pack(pady=5)

        quantity_var = tk.StringVar()
        quantity_entry = tk.Entry(self.root, textvariable=quantity_var, width=10)
        quantity_entry.pack(pady=5)

        def validate_input():
            try:
                quantity = int(quantity_var.get())
                if quantity < self.min_quantity[purpose]:
                    messagebox.showerror("Error", f"Minimum order is {self.min_quantity[purpose]} {unit}.")
                    return
                total_price = quantity * self.prices[water_type]
                self.show_order_summary(water_type, quantity, total_price, unit)
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number")

        tk.Button(self.root, text="Confirm", command=validate_input, width=30, fg="green").pack(pady=5)
        tk.Button(self.root, text="Back", command=lambda: self.select_water_type(purpose), width=30, fg="blue").pack(pady=5)

    def show_order_summary(self, water_type, quantity, total_price, unit):
        self.clear_window()
        tk.Label(self.root, text="Order Summary", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(self.root, text=f"Water Type: {water_type}", font=("Arial", 12)).pack(pady=5)
        tk.Label(self.root, text=f"Quantity: {quantity} {unit}", font=("Arial", 12)).pack(pady=5)
        tk.Label(self.root, text=f"Total Price: ₹{total_price}", font=("Arial", 12, "bold")).pack(pady=5)

        tk.Button(self.root, text="Proceed to Payment", command=lambda: self.payment_options(total_price), width=30, fg="green").pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_main_menu, width=30, fg="blue").pack(pady=10)

    def payment_options(self, price):
        self.clear_window()
        tk.Label(self.root, text=f"Total cost: ₹{price}", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(self.root, text="Choose Payment Method:", font=("Arial", 12)).pack(pady=5)

        payment_methods = ["Cash","PhonePe","Paytm", "GPay"]
        for method in payment_methods:
            tk.Button(self.root, text=method, command=lambda m=method: self.confirm_payment(m, price), width=30).pack(pady=5)

        tk.Button(self.root, text="Back", command=self.create_main_menu, width=30, fg="blue").pack(pady=10)

    def confirm_payment(self, method, price):
        if method == "Cash":
            messagebox.showinfo("Cash Payment", f"Please pay ₹{price} in cash.\nBooking successful. Thank You!")
        else:
            messagebox.showinfo("Payment Successful", f"Payment of ₹{price} done via {method}.\nBooking successful. Thank You!")
        self.create_main_menu()

    def confirm_exit(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.quit()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AquaBotUI(root)
    root.mainloop()
