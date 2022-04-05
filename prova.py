def fc(x,y):
    s=0
    a = x.lower()
    for  i in a:
        if(i==y):
            s = s + 1
    return s
a = 'Aracaju/Sergipe'
x = fc(a, 'a') * 100
y = fc(a, 'e')*10
z = fc(a,'i')
print(x+y+z)

