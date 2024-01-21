string,stringb = map(str, input().split())
result = "OK"

for x in range(0,5):
    if string[x]=="T"and stringb[x]=="A" or string[x]=="A" and stringb[x]=="T" or string[x]=="C" and stringb[x]=="G" or string[x]=="G" and stringb[x]=="C":
        result = "OK"
    else:
        result= "CORRUPTED"
        break
    

print(result)