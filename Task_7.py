st = str(input())
if st[-1] == '.' or st[-1] == '?' or st[-1] == '!':
	st = st[:-1]
sl = st.split(' ')
minin = len(st)
for i in range(len(sl)):
	if len(sl[i]) < minin:
		minin = len(sl[i])
print(minin)

