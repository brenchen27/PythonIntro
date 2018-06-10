string=("SpOnGeBoB")
a=0
b=0
for i in string:
      if(i.islower()):
            a=a+1
      elif(i.isupper()):
            b=b+1
print("No. of lower case characters:", a)
print("No. of upper case characters:", b)
