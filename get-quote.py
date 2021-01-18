import random
import sys
def primary(n = sys.argv[1]):

  #print("Keep it logically awesome.")
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  
  for i in range(int(n)):
    rnd = random.randint(0,last)
    print(quotes[rnd], end = '')

if __name__== "__main__":
  primary()
