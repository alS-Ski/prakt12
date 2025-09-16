strok = input()
pop = "".join(set(strok))
sim = ''
i = 0
while i < len(pop):
	if strok.count(str(pop[i])) == 3:
		 sim = pop[i]
	i += 1
print(sim)

