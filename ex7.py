st = str(input())
if st[-1] == '.' or st[-1] == '?' or st[-1] == '!':
	st = st[:-1]
sl = st.split(' ')
men = len(st)
for i in range(len(sl)):
	if len(sl[i]) < men:
		men = len(sl[i])
print(men)

