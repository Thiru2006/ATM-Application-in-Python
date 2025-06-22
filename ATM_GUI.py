import tkinter as tk
from tkinter import ttk

class ATM_Program:
    def __init__(self, master):
        self.master = master
        master.title("ATM Program")
        
        self.balance = 1000 #Initial balance
        
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#BBFFFF")
        self.style.configure("TButton", background="#BBFFFF", foreground="red")
        self.style.configure("TLabel", background="#BBFFFF", foreground="dark blue")
        
        self.frame = ttk.Frame(master, style="TFrame")
        self.frame.pack(expand=True)
        
        self.label = ttk.Label(self.frame, text="Welcome to the ATM Program!", font=("Helvetica", 16))
        self.label.pack(pady=10)
        
        self.balance_label = ttk.Label(self.frame, text="Your Current Balance: ₹" + str(self.balance), font=("Helvetica", 14))
        self.balance_label.pack(pady=10)
        
        self.check_balance_button = ttk.Button(self.frame, text="Check Balance", command=self.check_balance)
        self.check_balance_button.pack(pady=10)
        
        self.withdraw_button = ttk.Button(self.frame, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack(pady=10)
        
        self.deposit_button = ttk.Button(self.frame, text="Deposit", command=self.deposit)
        self.deposit_button.pack(pady=10)
        
        self.exit_button = ttk.Button(self.frame, text="Exit", command=master.quit)
        self.exit_button.pack(pady=10)
        
    def check_balance(self):
        self.balance_label.config(text="Your Current Balance: ₹" + str(self.balance))
        
    def withdraw(self):
        self.withdraw_window = tk.Toplevel(self.master)
        self.withdraw_window.title("Withdraw")
        self.withdraw_window.geometry("250x150")
        self.withdraw_window.configure(background="#BBFFFF")
        
        self.withdraw_frame = ttk.Frame(self.withdraw_window, style="TFrame")
        self.withdraw_frame.pack(expand=True)
        
        self.withdraw_label = ttk.Label(self.withdraw_frame, text="Enter amount to withdraw:", font=("Helvetica", 14))
        self.withdraw_label.pack(pady=10)
        
        self.withdraw_entry = ttk.Entry(self.withdraw_frame, font=("Helvetica", 14))
        self.withdraw_entry.pack(pady=10)
        
        self.withdraw_button = ttk.Button(self.withdraw_frame, text="Withdraw", command=self.update_withdraw)
        self.withdraw_button.pack(pady=10)
    def update_withdraw(self):
        try:
            amount = int(self.withdraw_entry.get())
            c=self.balance-amount
            if (amount < self.balance) and (c>=1000):
                self.balance -= amount
                self.balance_label.config(text="Your Current Balance: ₹" + str(self.balance))
                self.withdraw_window.destroy()
            elif (amount < self.balance) and (c<1000):
                self.withdraw_label.config(text="Minimum Balance is ₹ 1000")
            else:
                self.withdraw_label.config(text="Insufficient Funds")
        except ValueError:
            self.withdraw_label.config(text="Invalid Input")
        
    def deposit(self):
        self.deposit_window = tk.Toplevel(self.master)
        self.deposit_window.title("Deposit")
        self.deposit_window.geometry("250x150")
        self.deposit_window.configure(background="#BBFFFF")
    
        self.deposit_frame = ttk.Frame(self.deposit_window, style="TFrame")
        self.deposit_frame.pack(expand=True)
    
        self.deposit_label = ttk.Label(self.deposit_frame, text="Enter amount to deposit:", font=("Helvetica", 14))
        self.deposit_label.pack(pady=10)
        
        self.deposit_entry = ttk.Entry(self.deposit_frame, font=("Helvetica", 14))
        self.deposit_entry.pack(pady=10)
    
        self.deposit_button = ttk.Button(self.deposit_frame, text="Deposit", command=self.update_deposit)
        self.deposit_button.pack(pady=10)
    
    def update_deposit(self):
        try:
            amount = int(self.deposit_entry.get())
            self.balance += amount
            self.balance_label.config(text="Your Current Balance: ₹" + str(self.balance))
            self.deposit_window.destroy()
        except ValueError:
            self.deposit_label.config(text="Invalid Input")
root = tk.Tk()
root.geometry("500x500")
root.configure(bg="#00FA9A")
app = ATM_Program(root)
root.mainloop()
