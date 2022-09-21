sent = "Hello World"
s = sent.split()[::-1]
l = []
for i in s:
    l.append(i)

print(" ".join(l))
