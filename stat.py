import os
import os.path as op

p=os.getcwd()
ln=[]
for fn in os.listdir(p):
    if op.isfile(p+"\\"+fn) and fn!="stat.py":
        with open(fn,"rt") as f:
            c=0
            for l in f:
                if l.startswith("##"):
                    break
                sl=l.strip()
                if sl=="" or sl.startswith("#"):
                    continue
                c+=1
            ln.append([c,fn])

ln.sort(key=lambda x:x[1])
print(sum(x[0] for x in ln)/len(ln))

