st1 = set(input())
st2 = set(input())
st3 = set(input())
un = set()
for i in st1:
	if i not in st2 and i not in st3:
		un.add(i)
for j in st2:
	if j not in st1 and j not in st3:
		un.add(j) 
for k in st3:
	if k not in st2 and k not in st1:
		un.add(k) 
print(un)



