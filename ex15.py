def couBaC(sec, vib):
    bulls = 0
    cows = 0
    for i in range(4):
        if vib[i] == sec[i]:
            bulls += 1
        elif vib[i] in sec:
            cows += 1
    return bulls, cows

secWord = input()
popit = 0
print("\n" * 25)

while popit < 10:
    popit += 1
    vibor = input()
    
    bulls, cows = couBaC(secWord, vibor)
    print(f"Быков: {bulls} Коров: {cows}")

    if bulls == 4:
        print("Победа!")
        break
else:
    print("Проигрыш!")

