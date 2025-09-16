st = input()
flag = 0  

for s in st:
    if s == '(':
        flag += 1  
    elif s == ')':
      flag -= 1  
      if flag < 0:
        print('no')
        flag = -1
        break
if flag == 0:
    print('yes')
elif flag > 0:
    print('no')
