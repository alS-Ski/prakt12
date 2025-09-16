st = str(input())
znak = ''
if st[-1] == '.' or st[-1] == '?' or st[-1] == '!':
	znak = st[-1]
	st = st[:-1]
sl = st.split(' ')
print(' '.join(list(reversed(sl))) + znak)

