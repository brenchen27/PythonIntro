def drawtri(a):
    b=a-1
    for i in range(1, a+1):
        print(" "*b, "#"*i)
        a+=1
        b-=1

drawtri(6)
