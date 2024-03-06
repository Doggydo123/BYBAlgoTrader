class Profile:
    def __init__(self, name, lastname, email, username, address, accountCreationDate, accountType, id=None):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.email = email
        self.username = username
        self.address = address
        self.accountCreationDate = accountCreationDate
        self.accountType = accountType
    
