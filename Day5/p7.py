mylist=[4,2,7,5,4,1,4]
def searchValue(target):
    for i in range(len(mylist)):#len=7 i=0,1,2,
        if mylist[i] == target:
            return i



target = 7
#searchValue()#calling function
res = searchValue(target)
print("value found at index n",res)