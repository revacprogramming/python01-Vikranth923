f = "mbox-short.txt"
c = open(f,"r")
h = c.readlines()   
n=0
for i in h:
    k = i.split()
    if i.find("From ") != -1:
        print(k[1])
        n+=1
c.close()
print("There were",n, "lines in the file with From as the first word")