import copy

thislist = ["apple", "banana", ["cherry","prune"]]
mylist = copy.deepcopy(thislist)
thislist[2][1] = "peach"
thislist[0] = "pear"
print(mylist)
