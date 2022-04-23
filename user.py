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
    save user saves the new user to the userlist
    '''
    User.userlist.append(self)

def delete_user(self):
    '''
    deletes user from the userlist
    '''
    User.userlist.remove(self)

