#!/usr/bin/python

import argparse

# Recieves amount list/array of ints called prices
# Sorts the list/array and finds the biggest int and smallest int
# Must Buy first so smallest int
# Then minus the smallest in from the largest in the same day
# return profit

def find_max_profit(prices):
  profit = 0 #Basically set to 0 to init
  for i, priceMin in enumerate(prices): #i loops through the index and in enumerate loops through the element as well,
    #enumerate has amount hidden cost
    for priceMax in prices[i + 1:]:
      difference = priceMax - priceMin
      if profit == 0 or difference > profit: # Spent way to long on this part, forgot or key word
        profit = difference
  return profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
