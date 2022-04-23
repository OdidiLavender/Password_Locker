import unittest
from user import user

class Testuser(unittest.TestCase):
    '''
    This test class defines test casses for the user class behaviour
    
    Args:
    unittest.TestCase:TestCase class that helps in creating test cases 
    '''
def test_init(self):
    '''
    this is to test if the object is initialized properly
    '''
    self.assertEqual(self.new_user.Username,"Lavender")
    self.assertEqual(self.new_user.Password,"1234")



    
if __name__ == '__main__':
    unittest.main()    
    
