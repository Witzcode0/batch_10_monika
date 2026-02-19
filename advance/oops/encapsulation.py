class Auth:
    class Register:
        def __init__(self, username, email, password, confirm_password):
            self.__username = username # private data
            self.email = email
            self.password = password
            self.confirm_password = confirm_password

        def info(self):
            if self.password == self.confirm_password:
                user = {
                    "username": self.username,
                    "email": self.email,
                    "password": self.password
                }
                print("User registration succefully done.", user)
            else:
                print("Password and confirm password does not match.")

p1 = Auth().Register(input("Enter username: "), input("Enter email: "), input("Enter password: "), input("Enter confirm password: "))
p1.info()
print(p1._Register__username)