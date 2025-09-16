import keyword

st = input()
if (st.isidentifier() and keyword.iskeyword(st) != True):
    print("yes")
else:
    print("no")
