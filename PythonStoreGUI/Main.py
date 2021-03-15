import tkinter as tk
from tkinter import ttk
from tkinter import *
from Items import Items

class Main:
    def ShowItems(self):
        temp_items = self.items.PrintItems()
        
        self.lBox_main.delete(*self.lBox_main.get_children())
        
        for i, (name, category, amount, price) in enumerate(temp_items, start=1):
            self.lBox_main.insert("", "end", values=(name, category, amount, price))
    
    def ShowCategory(self):
        temp_itemCategory = self.items.PrintAllCategories()
        
        self.lBox_main.delete(*self.lBox_main.get_children())
        
        for i, (name, category, amount, price) in enumerate(temp_itemCategory, start=1):
            self.lBox_main.insert("", "end", values=(name, category, amount, price))
    
    def ShowDeals(self):
        win_showDeals = tk.Toplevel()
        win_showDeals.title("Combo Deals")
    
        lbl_comboDealsTitle = tk.Label(win_showDeals, text="Combo Deals", font=("Arial",30)).grid(row=0, columnspan=5)
        
        cols_comboDeals = ('Item One Name', 'Item One Amount', 'Item Two Name', 'Item Two Amount', 'Dicount')
        lBox_comboDeals = ttk.Treeview(win_showDeals, columns=cols_comboDeals, show='headings')
        
        for col in cols_comboDeals:
            lBox_comboDeals.heading(col, text=col)    
        lBox_comboDeals.grid(row=1, column=0, rowspan=4, columnspan=5)
        
        temp_comboDeals = self.items.PrintAllDeals()
        
        lBox_comboDeals.delete(*lBox_comboDeals.get_children())
        
        for i, (name1, amount1, name2, amount2, discount) in enumerate(temp_comboDeals, start=1):
            lBox_comboDeals.insert("", "end", values=(name1, amount1, name2, amount2, discount))
        
        # Close Window
        btn_closeDeals = tk.Button(win_showDeals, text="Close", width=15, command=win_showDeals.destroy).grid(row=5, column=2)
    
    def BuyResponse(self, yesno, name, amount):
        win_bought = tk.Toplevel()
        if yesno:
            win_bought.title("Success")
            lbl_boughtTitle = tk.Label(win_bought, text="Added", font=("Arial",30)).grid(row=0, columnspan=5)
            lbl_boughtText = tk.Label(win_bought, text=str(amount)+" "+name+" has been added to your Shopping Cart", font=("Arial",10)).grid(row=1, columnspan=5)
        else:
            win_bought.title("Error")
            lbl_boughtTitle = tk.Label(win_bought, text="Error", font=("Arial",30)).grid(row=0, columnspan=5)
            lbl_boughtText = tk.Label(win_bought, text=str(amount)+" "+name+" has NOT been added to your Shopping Cart", font=("Arial",10)).grid(row=1, columnspan=5)
            
        # Close Window
        btn_closeDeals = tk.Button(win_bought, text="Close", width=15, command=win_bought.destroy).grid(row=4, column=2)
    
    def BuyItemClick(self):
      bool_name = False
      bool_amount = False
      if self.txtBox_name.get() == "":
        self.lbl_nameError.configure(text="* Required")
      else:
        itemName = self.txtBox_name.get()
        self.lbl_nameError.configure(text="")
        bool_name = True
      
      if self.txtBox_amount.get() == "":
        self.lbl_amountError.configure(text="* Required")
      else:
        try:
          itemAmount = int(self.txtBox_amount.get())
          self.lbl_amountError.configure(text="")
          bool_amount = True
        except:
          self.lbl_amountError.configure(text="* Required")    
      
      if bool_name and bool_amount:
        if self.items.BuyItem(itemName, itemAmount):
          self.BuyResponse(True, itemName, itemAmount)          
          self.ShowItems()          
        else:
          self.BuyResponse(False, itemName, itemAmount)
    
    def CheckOut(self):
        self.win_checkOut = tk.Toplevel()
        self.win_checkOut.title("Receipt")
    
        lbl_checkOutTitle = tk.Label(self.win_checkOut, text="Receipt", font=("Arial",30)).grid(row=0, columnspan=2)
        # create a Text widget
        txt_checkOut = tk.Text(self.win_checkOut, width=30)
        txt_checkOut.grid(row=1, column=0, columnspan=2,sticky="nsew", padx=2, pady=2)
        txt_checkOut.insert('end', self.items.CheckOut())
        txt_checkOut.configure(state='disabled')
    
        scrollb_checkOut = tk.Scrollbar(self.win_checkOut, command=txt_checkOut.yview)
        scrollb_checkOut.grid(row=1, column=2, sticky='nsew')
        txt_checkOut['yscrollcommand'] = scrollb_checkOut.set
        
        # Return
        btn_return = tk.Button(self.win_checkOut, text="Return", width=15, command=self.win_checkOut.destroy).grid(row=5, column=0, sticky='w')
        
        # Check Out
        btn_checkOut = tk.Button(self.win_checkOut, text="Check Out", width=15, command=self.CloseApplication).grid(row=5, column=1, sticky='e')
    
    def CloseApplication(self):
        self.win_checkOut.destroy()
        self.win_main.destroy()        
    
    def __init__(self, win_main):
        self.items = Items()
        self.win_main = win_main
        win_main.title('Store')
        lbl_mainTitle = tk.Label(self.win_main, text="Store", font=("Arial",30)).grid(row=0, columnspan=3)
        
        cols_main = ('Name', 'Category', 'Amount', 'Price')
        self.lBox_main = ttk.Treeview(self.win_main, columns=cols_main, show='headings')
        
        for col in cols_main:
            self.lBox_main.heading(col, text=col)    
        self.lBox_main.grid(row=1, column=0, rowspan=4, columnspan=3)
        
        self.ShowItems()
        
        
        # Check Out
        btn_showItems = tk.Button(win_main, text="Check Out", width=10, command=self.CheckOut).grid(row=0, column=6, sticky='ne')
        
        
        # Table
        btn_showItems = tk.Button(win_main, text="Show Items", width=15, command=self.ShowItems).grid(row=5, column=0)
        btn_showByCategory = tk.Button(win_main, text="Show By Category", width=15, command=self.ShowCategory).grid(row=5, column=1)
        btn_showDeals = tk.Button(win_main, text="Show Combo Deals", width=15, command=self.ShowDeals).grid(row=5, column=2)
        
        
        # Buy
        lbl_buyTitle = tk.Label(win_main, text="Buy", font=("Arial",15)).grid(row=1, column= 4, columnspan=3)
        
        self.lbl_name = tk.Label(win_main, text= 'Name: ').grid(row=2, column=4, sticky='e')
        self.txtBox_name = tk.Entry(win_main)
        self.txtBox_name.grid(row=2, column=5, sticky='w')
        self.lbl_nameError = tk.Label(win_main, text= '', width=10)
        self.lbl_nameError.grid(row=2, column=6, sticky='w')
        
        self.lbl_amount = tk.Label(win_main, text= 'Amount: ').grid(row=3, column=4, sticky='e')
        self.txtBox_amount = tk.Entry(win_main)
        self.txtBox_amount.grid(row=3, column=5, sticky='w')
        self.lbl_amountError = tk.Label(win_main, text= '', width=10)
        self.lbl_amountError.grid(row=3, column=6, sticky='w')
        
        btn_buyItem = Button(win_main, text="Buy Item", width=15, command=self.BuyItemClick).grid(row=4, column=5, sticky='w')
        
        win_main.mainloop()

if __name__ == '__main__':
    win = tk.Tk() 
    my_gui = Main(win)
    win.mainloop()