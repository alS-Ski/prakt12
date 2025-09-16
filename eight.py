st = str(input())
st2 = ''
if st[-1] == '.' or st[-1] == '?' or st[-1] == '!':
	st = st[:-1]
sl = st.split(' ')
for j in range(len(sl)):
	men = len(st)
	pep = ''
	ind = 0
	for i in range(len(sl)):
		if len(sl[i]) < men:
			men = len(sl[i])
			pep = sl[i]
			ind = i
	st2 += pep + ' '
	del sl[ind]
print(st2)
