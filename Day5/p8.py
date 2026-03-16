def searchValue(mylist):
    sum=0
    for i in range(len(mylist)):
           sum = sum + mylist[i]

mylist = [4,3,5,2,6,7]
res = searchValue(mylist)
print("sum of array=",res)