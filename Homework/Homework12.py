people={"Allison":str(18),"Benson":str(48),"David":str(20),"Erik":str(20),"Galen":str(15),"Grace":str(25),"Helene":str(40),"Janette":str(18)}
sorted = {}

for k, v in people.items():
    if v not in sorted:
        sorted[v] = [k]
    else:
        sorted[v].append(k)
print(sorted)
