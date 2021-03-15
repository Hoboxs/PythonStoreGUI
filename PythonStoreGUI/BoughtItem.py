class BoughtItem:
  def __init__(self, name, amount, price):
    self.name = name
    self.amount = amount
    self.price = price

  def AddAmount(self, amount):
    self.amount = self.amount + amount

  def DelAmount(self, amount):
    self.amount = self.amount - amount

  def GetFinalPrice(self):
    return self.amount * self.price

  def PrintFinalPrice(self):
    return str(self.amount) + " " + self.name + "              " + str(self.amount * self.price) + "$"