text = "X-DSPAM-Confidence:    0.8475"
s = text.find(":")
e = text[s+1:]
p = float(e)
print(p)