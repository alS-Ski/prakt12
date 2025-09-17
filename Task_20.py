ed = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
edF = ["", "одна", "две", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
teens = ["десять","одиннадцать","двенадцать","тринадцать","четырнадцать",
         "пятнадцать","шестнадцать","семнадцать","восемнадцать","девятнадцать"]
tens = ["", "", "двадцать","тридцать","сорок","пятьдесят","шестьдесят",
        "семьдесят","восемьдесят","девяносто"]
hund = ["", "сто", "двести", "триста", "четыреста", "пятьсот",
            "шестьсот", "семьсот", "восемьсот", "девятьсот"]

def triToWords(n, female=False):
    h, t, u = n // 100, (n % 100) // 10, n % 10
    w = []
    if h > 0:
        w.append(hund[h])
    if t == 1:
        w.append(teens[u])
    else:
        if t > 1:
            w.append(tens[t])
        if female:
            w.append(edF[u])
        else:
            w.append(ed[u])
    return " ".join(w)

def suffix(n, forms):
    n = n % 100
    if 11 <= n <= 19:
        return forms[2]
    if n % 10 == 1:
        return forms[0]
    if 2 <= n % 10 <= 4:
        return forms[1]
    return forms[2]

num = int(input())

if num == 0:
    print("ноль")
else:
    millions = num // 1000000
    tisah = (num // 1000) % 1000
    hundNum = num % 1000
    parts = []
    
    if millions > 0:
        parts.append(triToWords(millions))
        parts.append(suffix(millions, ("миллион", "миллиона", "миллионов")))
    if tisah > 0:
        parts.append(triToWords(tisah, True))
        parts.append(suffix(tisah, ("тысяча", "тысячи", "тысяч")))
    if hundNum > 0:
        parts.append(triToWords(hundNum))

    print(" ".join(parts))


