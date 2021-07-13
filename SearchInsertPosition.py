a=[1,3,5,6]
b=int(input('target-'))
if b in a:
    print(a.index(b))
else:
    a.append(b)
    a.sort()
    print(a.index(b))
    
