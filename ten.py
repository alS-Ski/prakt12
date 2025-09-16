st = str(input())
if st[-1] == '.' or st[-1] == '?' or st[-1] == '!':
	st = st[:-1]
sl = st.split(' ')
j = 1
for j in range(len(sl)):
	if sl[0] != sl[j]:
		if len(set(sl[j])) == len(sl[j]):
			print(sl[j])
			
			
		
