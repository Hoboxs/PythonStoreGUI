class BoughtCombo:
  def __init__(self, discount, itemOneName, itemOneAmt, itemOnePrice, itemTwoName, itemTwoAmt, itemTwoPrice):
    self.discount = discount
    self.itemOneName = itemOneName
    self.itemOneAmt = itemOneAmt
    self.itemOnePrice = itemOnePrice
    self.itemTwoName = itemTwoName
    self.itemTwoAmt = itemTwoAmt
    self.itemTwoPrice = itemTwoPrice

  def GetFinalPrice(self):
    price = ((self.itemOneAmt * self.itemOnePrice) + (self.itemTwoAmt * self.itemTwoPrice))
    price = price - (price * (self.discount/100))
    return price

  def PrintFinalPrice(self):
    s = ""
    s += ("\n" + str(self.itemOneAmt) + " " + self.itemOneName + "              " + str(self.itemOneAmt * self.itemOnePrice) + "$")
    s += ("\n" + str(self.itemTwoAmt) + " " + self.itemTwoName + "              " + str(self.itemTwoAmt * self.itemTwoPrice) + "$")
    price = ((self.itemOneAmt * self.itemOnePrice) + (self.itemTwoAmt * self.itemTwoPrice))
    discountPrice = (price * (self.discount/100))
    s += ("\n                      -------")
    s += ("\n                      " + str(round(price,2)) + "$")
    s += ("\n                     -" + str(round(discountPrice,2)) + "$")
    s += ("\n                      -------")
    s += ("\n                      " + str(round(price-discountPrice,2)) + "$")
    return s
    