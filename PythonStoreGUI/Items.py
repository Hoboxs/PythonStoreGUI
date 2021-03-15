from AllBoughtItems import AllBoughtItems
import sqlite3
from contextlib import closing

class Items:
  def __init__(self):
    self.boughtItems = AllBoughtItems()
    self.conn = sqlite3.connect("Items.db")
    self.conn.row_factory = sqlite3.Row
    
  def BuyItem(self, name, amount):
    with closing(self.conn.cursor()) as c:
        query = '''SELECT * FROM Items WHERE name = ?'''
        c.execute(query, (name,)) 
        items = c.fetchone()
    if items is not None:
        if int(items["amount"]) - amount < 0:
            return False
        self.boughtItems.AddToShoppingCart(name, amount, items["price"])
        with closing(self.conn.cursor()) as c: 
            query = '''UPDATE Items SET amount = ? WHERE name = ?'''
            c.execute(query, ((items["amount"]) - amount, name))
            self.conn.commit()
        return True
    return False
    
  def ExistItem(self, itemName):
    with closing(self.conn.cursor()) as c:
        query = '''SELECT * FROM Items WHERE name = ?'''
        c.execute(query, (itemName,))  
        items = c.fetchone()
    if items is not None:
        return True
    return False

  def CheckOut(self):
    return self.boughtItems.PrintShoppingCart()

  def PrintItems(self):
    with closing(self.conn.cursor()) as c:
        query = '''SELECT name, category, amount, price FROM Items'''
        c.execute(query) 
        items = c.fetchall()
    return items

  def PrintAllCategories(self):
      with closing(self.conn.cursor()) as c:
        query = '''SELECT name, category, amount, price FROM Items ORDER BY category'''
        c.execute(query) 
        items = c.fetchall()
      return items

  def PrintAllDeals(self):
      with closing(self.conn.cursor()) as c:
        query = '''SELECT items_1_name, items_1_quantity, items_2_name, items_2_quantity, discount FROM Deals'''
        c.execute(query) 
        deals = c.fetchall()
      return deals