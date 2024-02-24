txt1 = ['olá', 'mundo', 'python']
txt2 = [s.upper() for s in txt1 if len(s)>3]
# A linha nº 2 é equivalente a:
txt3 = []
for i in txt1:
    if len(i)>3:
        txt3.append(i.upper())
        
print(txt1)
print(txt2)
print(txt3)

