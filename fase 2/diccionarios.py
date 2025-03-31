''''
palabra='brontosaurio'
d=dict()
for c in palabra:
    if c not in d :
        d[c]=1
    else:
        d[c]=d[c]+1

print(d)        
'''
palabra='brontosaurio'
d=dict()
for c in palabra:
    d[c]=d.get(c,0)+1
print(d)

