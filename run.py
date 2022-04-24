import string
from random import *
from user import User
from user import Credentials

def create_user(firstname,lastname,username,userpassword):
    new_user= User(firstname,lastname,username,userpassword)
    return new_user
def save_user(user):
    user.save_user()