strok = input()
le = len(strok)
cou, couMax, i = 1, 0, 1
while i < le:
	if strok[i] == strok[i-1]:
		cou += 1
	else:
		cou = 1
	if cou > couMax:
		couMax = cou
	i += 1
print(couMax)
		
