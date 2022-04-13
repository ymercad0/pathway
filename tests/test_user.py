from model import User 
import unittest 

class TestUser(unittest.TestCase):
    def setUp(self):
        self.valid_email1 = "example@gmail.com"
        self.valid_username = "xavier"
        self.valid_pic = "http://www.test.com"
        self.valid_password = "password1"

        self.user = User(
            self.valid_username,
            self.valid_email1,
            self.valid_password,
            self.valid_pic)

    def test_types(self):
        #username tests
        self.assertRaises(TypeError,User,None,self.valid_email1,"password1",self.valid_pic)
        self.assertRaises(TypeError,User,123,self.valid_email1,"password1",self.valid_pic)
        self.assertRaises(TypeError,User,[],self.valid_email1,"password1",self.valid_pic)
        #email tests
        self.assertRaises(TypeError,User,self.valid_username,[],"password1",self.valid_pic)
        self.assertRaises(TypeError,User,self.valid_username,None,"password1",self.valid_pic)
        self.assertRaises(TypeError,User,self.valid_username,123,"password1",self.valid_pic)
        #password tests
        self.assertRaises(TypeError,User,self.valid_username,self.valid_email1,None,self.valid_pic)
        self.assertRaises(TypeError,User,self.valid_username,self.valid_email1,[],self.valid_pic)
        self.assertRaises(TypeError,User,self.valid_username,self.valid_email1,123,self.valid_pic)
        #url tests
        self.assertRaises(TypeError,User,self.valid_username,self.valid_email1,"password1",None)
        self.assertRaises(TypeError,User,self.valid_username,self.valid_email1,"password1",[])
        self.assertRaises(TypeError,User,self.valid_username,self.valid_email1,"password1",123)

    def test_values(self):
        #username tests
        self.assertRaises(ValueError,User,"tes",self.valid_email1,"password1",self.valid_email1)
        self.assertRaises(ValueError,User,"",self.valid_email1,"password1",self.valid_email1)
        self.assertRaises(ValueError,User,"tes",self.valid_email1,"password1",self.valid_email1)
        #email tests
        self.assertRaises(ValueError,User,self.valid_username,"inv@test","password1",self.valid_email1)
        self.assertRaises(ValueError,User,self.valid_username,"email.com","password1",self.valid_email1)
        self.assertRaises(ValueError,User,self.valid_username,"@test.com","password1",self.valid_email1)
        self.assertRaises(ValueError,User,self.valid_username,"inv@@@","password1",self.valid_email1)
        #password tests
        self.assertRaises(ValueError,User,self.valid_username,self.valid_email1,"",self.valid_pic)
        self.assertRaises(ValueError,User,self.valid_username,self.valid_email1,"1",self.valid_pic)
        self.assertRaises(ValueError,User,self.valid_username,self.valid_email1,"apple",self.valid_pic)
        self.assertRaises(ValueError,User,self.valid_username,self.valid_email1,"test12",self.valid_pic)
        #url tests
        self.assertRaises(ValueError,User,self.valid_username,self.valid_email1,"password1","test.com")
        self.assertRaises(ValueError,User,self.valid_username,self.valid_email1,"password1","")
        self.assertRaises(ValueError,User,self.valid_username,self.valid_email1,"password1","@")
        self.assertRaises(ValueError,User,self.valid_username,self.valid_email1,"password1","@gmail.com")
        self.assertRaises(ValueError,User,self.valid_username,self.valid_email1,"password1","user@")

    def test_set_profile_pic(self):
        self.assertTrue(self.user.set_profile_pic("https://bit.ly/3KF5IT0"))
        self.assertFalse(self.user.set_profile_pic("bit.ly/3KF5IT0"))
        self.assertEqual(self.user.profile_pic,"https://bit.ly/3KF5IT0")