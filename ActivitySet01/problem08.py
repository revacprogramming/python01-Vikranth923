fname = "romeo.txt"
fh = open(fname)
k=[]
c=fh.readlines()
for i in c:
    j = i.split()
    for i in j:
        if i not in k:
            k.append(i)
print(sorted(k))