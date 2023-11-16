import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    for quote in quotes:
       quote_stock = quote['stock']
       quote_bid_price = quote['top_bid']['price']
       quote_ask_price = quote['top_ask']['price']
       quote_price = (quote_bid_price + quote_ask_price) / 2
       self.assertEqual(getDataPoint(quote), (quote_stock, quote_bid_price, quote_ask_price, quote_price))


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    for quote in quotes:
      quote_stock = quote['stock']
      quote_bid_price = quote['top_bid']['price']
      quote_ask_price = quote['top_ask']['price']
      quote_price = (quote_bid_price + quote_ask_price) / 2
      self.assertEqual(getDataPoint(quote), (quote_stock, quote_bid_price, quote_ask_price, quote_price))


  def test_getRatio_calculateRatio(self):
    prices = [
        {'price_a': 119.20, 'price_b': 120.48},
        {'price_a': 120.48, 'price_b': 119.2}
    ]

    for price in prices:
      price_a, price_b = price['price_a'], price['price_b']
      self.assertEqual(getRatio(price_a, price_b), price_a / price_b)


  def test_getRatio_calculateRatioPriceAZero(self):
    prices = [
        {'price_a': 0.00, 'price_b': 120.48},
        {'price_a': 0.00, 'price_b': 119.2}
    ]

    for price in prices:
      price_a, price_b = price['price_a'], price['price_b']
      self.assertEqual(getRatio(price_a, price_b), 0)


  def test_getRatio_calculateRatioPriceBZero(self):
    prices = [
        {'price_a': 120.48, 'price_b': 0.00},
        {'price_a': 19.2, 'price_b': 0.00}
    ]

    for price in prices:
      price_a, price_b = price['price_a'], price['price_b']
      self.assertIsNone(getRatio(price_a, price_b))


  def test_getRatio_calculateRatioPriceAZeroPriceBZero(self):
    self.assertIsNone(getRatio(0, 0))



if __name__ == '__main__':
    unittest.main()
