#function
def msg(): #called function
   val1 = int(input("enter first value"))
   val2 = int(input("enter second value"))
   print("val1+val2")
   return val1+val2
    
res=msg()#calling function
print("Result =", res)