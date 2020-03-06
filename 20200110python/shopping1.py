class Notebook:
  _sky = 'unknown'
  _price = 0
  _size = 'unknown'
  def __init__(self, sku, price, size):
      self._sku = sku
      self._price = price
      self._size = size
  def getSku(self):
     return self._sku
  def getPrice(self):
      return self._price
  def getSize(self):
      return self._size
  def info(self):
      return 'Notebook: {}{}{}'.format(self._sku, self._price, self._size)
  def prDetails(self):
      print(self.info())

class Pen:
  _sky = 'unknown'
  _price = 0
  _color = 'unknown'
  def __init__(self, sku, price, color):
      self._sku = sku
      self._price = price
      self._color = color
  def getSku(self):
     return self._sku
  def getPrice(self):
      return self._price
  def getColor(self):
      return self._color
  def info(self):
      return 'Pen: {}{}{}'.format(self._sku, self._price, self._color)
  def prDetails(self):
      print(self.info())

def test():
  nb1 = Notebook('#001', 200, '4K')
  p1 = Pen('#001', 20, 'red')
  print(nb1.getSku(), nb1.getPrice(), nb1.getSize())
  nb1.prDetails()
  print(p1.getSku(), p1.getPrice(), p1.getColor())
  p1.prDetails()
test()