from model import User
import unittest
import bcrypt

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
        self.assertRaises(TypeError,User,None,self.valid_email1,self.valid_password,self.valid_pic)
        self.assertRaises(TypeError,User,123,self.valid_email1,self.valid_password,self.valid_pic)
        self.assertRaises(TypeError,User,[],self.valid_email1,self.valid_password,self.valid_pic)
        #email tests
        self.assertRaises(TypeError,User,self.valid_username,[],self.valid_password,self.valid_pic)
        self.assertRaises(TypeError,User,self.valid_username,None,self.valid_password,self.valid_pic)
        self.assertRaises(TypeError,User,self.valid_username,123,self.valid_password,self.valid_pic)
        #password tests
        self.assertRaises(TypeError,User,self.valid_username,self.valid_email1,None,self.valid_pic)
        self.assertRaises(TypeError,User,self.valid_username,self.valid_email1,[],self.valid_pic)
        self.assertRaises(TypeError,User,self.valid_username,self.valid_email1,123,self.valid_pic)
        #url tests
        self.assertRaises(TypeError,User,self.valid_username,self.valid_email1,self.valid_password,None)
        self.assertRaises(TypeError,User,self.valid_username,self.valid_email1,self.valid_password,[])
        self.assertRaises(TypeError,User,self.valid_username,self.valid_email1,self.valid_password,123)

    def test_values(self):
        #username tests
        self.assertRaises(ValueError,User,"tes",self.valid_email1,self.valid_password,self.valid_pic)
        self.assertRaises(ValueError,User,"",self.valid_email1,self.valid_password,self.valid_pic)
        self.assertRaises(ValueError,User,"tes",self.valid_email1,self.valid_password,self.valid_pic)
        self.assertRaises(ValueError,User,"1",self.valid_email1,self.valid_password,self.valid_pic)
        self.assertRaises(ValueError,User,"__",self.valid_email1,self.valid_password,self.valid_pic)
        #email tests
        self.assertRaises(ValueError,User,self.valid_username,"inv@test",self.valid_password,self.valid_pic)
        self.assertRaises(ValueError,User,self.valid_username,"email.com",self.valid_password,self.valid_pic)
        self.assertRaises(ValueError,User,self.valid_username,"@test.com",self.valid_password,self.valid_pic)
        self.assertRaises(ValueError,User,self.valid_username,"inv@@@",self.valid_password,self.valid_pic)
        self.assertRaises(ValueError,User,self.valid_username,"t@",self.valid_password,self.valid_pic)
        self.assertRaises(ValueError,User,self.valid_username,"@.com",self.valid_password,self.valid_pic)
        #password tests
        self.assertRaises(ValueError,User,self.valid_username,self.valid_email1,"",self.valid_pic)
        self.assertRaises(ValueError,User,self.valid_username,self.valid_email1,"1",self.valid_pic)
        self.assertRaises(ValueError,User,self.valid_username,self.valid_email1,"aple",self.valid_pic)
        self.assertRaises(ValueError,User,self.valid_username,self.valid_email1,"apple",self.valid_pic)
        self.assertRaises(ValueError,User,self.valid_username,self.valid_email1,"test12",self.valid_pic)
        #profile_pic tests
        self.assertRaises(ValueError,User,self.valid_username,self.valid_email1,self.valid_password,"")
        
    def test_set_profile_pic(self):
        self.assertTrue(self.user.set_profile_pic("https://bit.ly/3KF5IT0"))
        self.assertFalse(self.user.set_profile_pic("bit.ly/3KF5IT0"))
        self.assertEqual(self.user.profile_pic,"https://bit.ly/3KF5IT0")
        self.assertTrue(self.user.set_profile_pic("https://www.google.com"))
        self.assertEqual(self.user.profile_pic, "https://www.google.com")

    def test_pswd(self):
        self.assertTrue(bcrypt.checkpw("password1".encode("utf-8"),
                        self.user.password))

        self.assertFalse(bcrypt.checkpw("password".encode("utf-8"),
                        self.user.password))