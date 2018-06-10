biggestFamily=({"Lee":3,"Chen":5,"Bryan":2,"White":2})
lee=3
chen=5
bryan=2
white=2
if lee>=chen and lee>=bryan and lee>=white:
    print("Family Lee is biggest")
elif chen>=lee and chen>=bryan and chen>=white:
    print("Family Chen is biggest")
elif bryan>=lee and bryan>=chen and bryan>=white:
    print("Family Bryan is biggest")
else:
    print("Family White is biggest")
