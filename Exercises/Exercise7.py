d={"dog":"bark","cat":"meow","cow":"moo","horse":"neigh","lion":"roar"}
print(d['cat'])

for k,v in d.items():
    print("The sound of the animal "+k+" is "+v)

d.update({"bee":"buzz"})
print(d)

del d["horse"]
print(d)

print(d.keys())
print(d.values())
