# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
sm = 0
n = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        n=n+1
        sm=sm+float(line.split()[1])
avg=sm/n
print("Average spam confidence:",avg)

