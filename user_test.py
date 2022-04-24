import unittest
from user import User

class Testuser(unittest.TestCase):
    '''
    This test class defines test casses for the user class behaviour
    
    Args:
    unittest.TestCase:TestCase class that helps in creating test cases 
    '''
def setUp(self):
    pass
    '''
    Set up method to run before each test cases
    '''


def test_init(self):
    '''
    this is to test if the object is initialized properly
    '''
    self.assertEqual(self.new_user.Username,"Lavender")
    self.assertEqual(self.new_user.Password,"1234")

def test_save_user(self):
    '''
    test_save_user test case to test if the user object is saved into
    the userlist
    '''
    self.new_user.save_user() # saving the new user
    self.assertEqual(len(User.userlist),1)
    

def test_delete_user(self):
    '''
    test_delete_user to test if you can remove a user from the user list
    '''
    self.new_user.save_user()
    test_user = user('test','user','password')#new user
    test_user.save_user()

    self.new_user.delete_user()#deletes a user object
    self.assertEqual(len(user.userlist),1)


if __name__ == '__main__':
    unittest.main()    
    
