# Doing Things to Lists
# what is done here: str.split, str.join, 
# drills: 
# 1 read "whatis class of python" 
# 2 whatis relation between dir(sth) and class of sth
 

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let'sfix that."

stuff = ten_things.split(' ')
# todo: how to fix this style of 80 character
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Gril", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop()
print ' '.join(stuff) # what? cool!
print '#'.join(stuff[3:5]) 
# it seems that, [3,5), not include the latter. similar to range(3,5)
# ''.join(things) => join ('#', things)

# test:
# print join('#', stuff[3:5])

#   File "ex38.py", line 27, in <module>
#     print join('#', stuff[3:5])
# NameError: name 'join' is not defined


