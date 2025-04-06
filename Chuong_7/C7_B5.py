prices = {"banana":4, "apple":2,"orange":1.5, "pear":3}
stock = {"banana":6, "orange":32, "pear":15}
L = [(w,0 if w not in stock else stock[w]*prices[w]) for w in prices]
L.sort(key = lambda x: (-x[1],x[0]))
print(L)
for w in L:
	print(w[0].ljust(6)," ",w[1])
