strok = input()
le = len(strok)
cou, couMax, i = 0, 0, 0
while i < le:
	if strok[i] == ' ':
		cou += 1
	else:
		cou = 0
	if cou > couMax:
		couMax = cou
	i += 1
print(couMax)
		
