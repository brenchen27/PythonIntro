ages={"Peter": 10, "Isabel": 11, "Anna": 9, "Thomas": 10, "Bob": 10, "Joseph": 11, "Maria": 12, "Gabriel": 10}
print(len(ages))
#
print(sum(ages.values())/len(ages))
#
def getOldest(ages):
    oldestStudent=""
    oldestAge=0
    for name,age in ages.items():
        if age>oldestAge:
            oldestAge=age
            oldestStudent=name
    return oldestStudent

print(getOldest(ages))
#
for k in ages.keys():
    ages[k]+=10
print(ages)
