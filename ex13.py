def luc(num):

    ticSt = str(num)
    if len(ticSt) % 2 != 0:
        return False
    
    halfZn = len(ticSt) // 2
    firstHulfSum = 0
    secondHulfSum = 0
    
    for i in ticSt[:halfZn]:
        firstHulfSum += int(i)
    for i in ticSt[halfZn:]:
        secondHulfSum += int(i) 
    return firstHulfSum == secondHulfSum


tiCou = 0
while True:
    num = int(input())
    tiCou += 1
    if luc(num):
        print(tiCou)
        break
