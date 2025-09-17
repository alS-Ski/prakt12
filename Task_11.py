st = str(input())
if st[-1] == '.' or st[-1] == '?' or st[-1] == '!':
	st = st[:-1]
st = st.lower()
sl = st.split(' ')
flag = 1
for j in range(len(sl)-1):
	if sl[j][-1] != sl[j+1][0]:
		if j%2 == 1:
			flag = 0
			print('vasa pobedil')
		else:
			flag = 0
			print('peta pobedil')
if flag == 1:
	if j%2 == 0:
		print('vasa pobedil')
	else:
		print('peta pobedil')

		
	

