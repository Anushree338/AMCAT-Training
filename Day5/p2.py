#we can return multiple value at the same time
#function
def msg(): #called function
   val1 = int(input("enter first value"))
   val2 = int(input("enter second value"))
   sum =val1+val2
   mul = val1 * val2
   sub = val1-val2
   div = val1 *val2
   
   return sum, mul, sub, div
    
res=msg()#calling function
print("Result =", res)