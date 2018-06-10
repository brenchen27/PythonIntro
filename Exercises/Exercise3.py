# Write a Python function that takes a list of words and
# returns the length of the longest one

# myTest = ['this', 'is', 'a', 'list', 'of', 'words']

def getMax(list):
    maxLen = 0
    for i in list:
        if len(i)>maxLen:
            maxLen=len(i)
    return maxLen

print(getMax(['this', 'is', 'a', 'list', 'of', 'words']))
