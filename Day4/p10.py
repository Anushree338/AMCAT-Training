n=int(input("Enter the number of students: "))
d={}
for i in range(n):
    name=input("Enter the name of student: ")
    marks=int(input("Enter the marks of student: "))
    d[name]=marks

while True:
    name=input("Enter your name to get marks: ")
    marks=d.get(name,-1)
    if marks==-1:
        print("Name not found")
    else:
        print(f"Marks of {name} is {marks}")
        option=input("Do you want to continue? (yes/no): ")
        if option=="no":
            break   
            print("thanks for using our application")
