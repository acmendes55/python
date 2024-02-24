# 'r' -> read, 'w' -> write, 'a' -> append

fin = open('nomes.txt', 'r')

lst = []

for line in fin:
    lst.extend(line.split())
fin.close()
lst.sort()

fout = open('names_sorted.txt', 'w')
for name in lst:
    print(name, file = fout)
    #fout.write(names + '\n')
fout.close()