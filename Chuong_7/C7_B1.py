D = { 2:'two',1:'one', 3:'three', 5:'five', 6:'six', 7:'seven', 4:'four'}
A = list(D.keys())
A.sort()
D_sorted = {i: D[i] for i in A}
for key,value in D_sorted.items():
	print(key,value)
#for value in D_sorted.values():
#	print(value)