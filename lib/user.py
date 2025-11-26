class User: #class name wil be table name in plural e.g users
    def __init__(self,name,email,password,id=None): #attributes will be talbe columns
        self.name = name
        self.email = email
        self.password = password
        self.id = id

        user1 = User("Titus","titus@gmail.com","1234") # resamble table records

        #ORM consept
        User => users
       
        #instance attributes =table columns
        name => email=>password=>id
        instance/object => table records
