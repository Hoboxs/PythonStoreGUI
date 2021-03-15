from BoughtCombo import BoughtCombo
from BoughtItem import BoughtItem
import sqlite3
from contextlib import closing

class AllBoughtItems:
  def __init__(self):
    self.shoppingCart = []
    self.shoppingCartDeals = []
    self.conn = sqlite3.connect("Items.db")
    self.conn.row_factory = sqlite3.Row

  def AddToShoppingCart(self, name, amount, price):
    item = BoughtItem(name, amount, price)
    if item in self.shoppingCart:
      for product in self.shoppingCart:
        if item == product:
          product.AddAmount(amount)
    else:
      self.shoppingCart.append(item)

  def PrintShoppingCart(self):
    s = ""
    with closing(self.conn.cursor()) as c:
        query = '''SELECT * FROM Deals'''
        c.execute(query) 
        deals = c.fetchall()
    s += ("\n======= Shopping Cart =======")
    self.CheckComboDeals(deals)
    totalItemPrice = 0
    s += ("\n------- General Items -------")
    for i in self.shoppingCart:      
      totalItemPrice = totalItemPrice + i.GetFinalPrice()
      s += "\n" + i.PrintFinalPrice()
    s += ("\n                      -------")
    s += ("\nFinal Item Price:     " + str(round(totalItemPrice,2)) + "$")
    s += "\n"
    s += ("\n------ Discount Combos ------")
    totalDiscountPrice = 0
    for i in self.shoppingCartDeals:
      totalDiscountPrice = totalDiscountPrice + i.GetFinalPrice()
      s += "\n" + i.PrintFinalPrice()
    s += ("\n                      -------")
    s += ("\nFinal Discount Price: " + str(round(totalDiscountPrice,2)) + "$")
    s += "\n"
    s += ("\n-----------------------------")
    s += ("\nFinal Price:          " + str(round(totalDiscountPrice+totalItemPrice, 2)) + "$")
    return s

  def CheckComboDeals(self, allDeals):
    for deal in allDeals:
      if self.DealExists(deal):
        product1 = self.GetComboDeal(deal["items_1_name"])
        product2 = self.GetComboDeal(deal["items_2_name"])
        itemOneAmt = product1.amount // deal["items_1_quantity"]
        itemTwoAmt = product2.amount // deal["items_2_quantity"]
        if itemOneAmt > itemTwoAmt:
          dealAmt = itemTwoAmt
        else:
          dealAmt = itemOneAmt
        product1.DelAmount(dealAmt * deal["items_1_quantity"])
        product2.DelAmount(dealAmt * deal["items_2_quantity"])
        self.shoppingCartDeals.append(BoughtCombo(deal["discount"], product1.name, dealAmt * deal["items_1_quantity"], product1.price, 
                                                  product2.name, dealAmt * deal["items_2_quantity"], product2.price))

  def DealExists(self, deal):
    boolItemOne = False
    boolItemTwo = False
    for product in self.shoppingCart:
      if deal["items_1_name"] == product.name and deal["items_1_quantity"] <= product.amount: 
        boolItemOne = True
      if deal["items_2_name"] == product.name and deal["items_2_quantity"] <= product.amount: 
        boolItemTwo = True
    if boolItemOne and boolItemTwo:
      return True
    return False

  def GetComboDeal(self, name):
    for product in self.shoppingCart:
      if name == product.name:
        return product