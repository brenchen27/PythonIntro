def drawTriangle(n):
    numLoops=n//2+1
    for i in range(0,numLoops):
        for j in range(0,i+1):
            print("#")

drawTriangle(5)
