def login():
     username = input("enter username:")
     password = input("enter passsword:")
     if username == password:
        print("login successfully")
     else:
        print("invalid credentials")

login()
