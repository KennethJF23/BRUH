src = open("input2.txt").read().splitlines()
mnt,mdt,ala = [],[],{}


i = 0 
while(i<len(src)):
    if(src[i]!="MACRO"):
        i+=1
        continue
    
    head = src[i+1].split()
    name,formals = head[0],head[1:]

    ala[name],mnt[name] = formals,len(mdt)

    i+=2
    while(src[i]!="MEND"):
        mdt.append(src[i])
        i+=1
    mdt.append("MEND")
    i+=1

print("MNT",mnt)
print("MDT",*mdt,sep="\n")

print("\nPASS 2 OUTPUT:")
for line in src:
    token = line.split()
    if token and token[0] in mnt:
        k,actuals = mnt[token[0]],token[1:]
        while mdt[k]!="MEND":
            out = mdt[k]
            for f,a in zip(ala[token[0]],actuals):
                out = out.replace(f,a)
            print(out) 
            k+=1
    elif line not in ("MACRO","MEND") and not line.startswith(("ADD","SUB")):
        print(line)