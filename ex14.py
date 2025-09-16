def sprWord(word, ugadBukv):
    hidWord = ""
    for i in word:
        if i in ugadBukv:
            hidWord += i
        else:
            hidWord += "*"
    return hidWord

pod = input("Введите подсказку: ")
secWord = input("Введите загаданное слово: ")

popit = 0
ugadBukv = set()

print("\n" * 25)
print(pod)
print(sprWord(secWord, ugadBukv))

while popit < 6:
    popit += 1
    vibor = int(input("Буква или слово (0 - буква, 1 - слово)?: "))
    
    if vibor == 0:
        let = input()
        ugadBukv.add(let)
        hidWord = sprWord(secWord, ugadBukv)
        print(hidWord)

        if hidWord == secWord:
            print("Победа!")
            break

    if vibor == 1:
        slov = input()
        if slov == secWord:
            print("Победа!")
            break
        else:
            print("Проигрыш!")
            break

    if popit == 5:
        print("Проигрыш!")
        break
    
    popit
