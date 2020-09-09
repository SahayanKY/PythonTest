list = [[1,2,3],[2,5],[4,8,9],[1]]
newlist = []
for childlist in list:
    newlist.extend(childlist)
print(newlist)