f=open("Test.txt",encoding="utf-8")
s=f.readlines()
s=list(map(lambda x: x.strip("\n"),s))
s1=max(map(lambda x: len(x),s))
for line in s:
    if len(line)==s1:
        print(line)
f.close()