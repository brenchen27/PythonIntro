def findUnique(list):
    a=[]
    for i in list:
        if i not in a:
            a.append(i)
    print(a)
findUnique([13,13,7,3,4,4,6,6,100,100])
