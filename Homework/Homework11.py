def createSquares(n):
    d={}
    for i in range(1,n+1):
        d.update({i:i*i})
        n+=1
    print(d)
print(createSquares(8))
