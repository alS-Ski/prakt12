st = str(input())
if st[-1] == '.' or st[-1] == '?' or st[-1] == '!':
	st = st[:-1]
sl = st.split(' ')
cou = 0
for j in range(len(sl)):
	if cou == 2:
			print(sl[j-1])
	i = j
	cou = 0
	for i in range(len(sl)):
		if sl[j] == sl[i]:
			cou += 1
		
