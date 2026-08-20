

li=[[1,3],[2,4],[4,1],[3,2]]
min=0
vallist=[]
for i in range(len(li)):
    val=li[i][1]
    vallist.append(val)
vallist.sort()
print(vallist)