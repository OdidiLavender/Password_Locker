class User:
    '''
    user class generates new instance of the user
    '''
    userlist = [] #Empty userlist
def __init__ (self,Username,Password):
    self.Username = Username
    self.Password = Password

def save_user(self):
    '''
    save user method saves the new user to the userlist
    '''
    User.userlist.append(self)

def delete_user(self):
    '''
    deletes user method from the userlist
    '''
    User.userlist.remove(self)
@classmethod
def find_by_number(cls,number):
    '''
    Method that takes in username and returns a user that matches that number.
        
    '''
    for user in cls.userlist:
        if user.password == number:
            return user
@classmethod
def user_exists(cls,number):
    '''
    method checks if the username exists
    '''
    for user in cls.userlist:
        if user.username == number:
            return True #return true if there is same username

            return False #return false if no username has the same number



@classmethod
def display_user(cls):
    '''
    method returns the userlist
    '''
    return cls.userlist


class Credentials:
    '''
    class generates new instance of credentials
    '''
    account = []
    def __init__(self,accountname,accountusername,accountpassword):
        '''
        init method defines properties for our object
        '''
        self.accountname = accountname
        self.accountusername = accountusername
        self.accountpassword = accountpassword
    
    def save_account(self):
        '''
        this method saves the user credentials in account
        '''
        Credentials.account.append(self)

    def delete_account(self):
        '''
        this method delete user credentials from account 
        '''
        Credentials.account.remove(self)

@classmethod
def display_account(cls):
    '''
    method returns a list of the accounts
    '''
    for account in cls.accounts:
        return cls.accounts

@classmethod
def find_by_number(cls,number):
    for account in cls.accounts:
        if account.accountname == number:
            return account

