import unittest
from user import User
from existingAcount import Accounts

class testUsers (unittest.TestCase):
  def setUp(self):
    self.aNewUser = User("Twitter","Samuel", "Abusa", "blabla34323")
    self.existing_account = Accounts("Twitter", "Samuel Abusa", "56789@/*-")
  
  def test_init(self):
    self.assertEqual(self.aNewUser.social_media, "Twitter")
    self.assertEqual(self.aNewUser.first_name, "Samuel")
    self.assertEqual(self.aNewUser.last_name, "Abusa")
    self.assertEqual(self.aNewUser.pass_word, "blabla34323")
    
    self.assertEqual(self.existing_account.account, "Twitter")
    self.assertEqual(self.existing_account.userName, "Samuel Abusa")
    self.assertEqual(self.existing_account.existingPassword, "56789@/*-")
  
  def test_saving_user_info(self):
    self.aNewUser.save_user_info()
    self.assertEqual(len(User.newUser), 1)
  
  def test_saving_credentials(self):
    self.existing_account.store_user_data()
    self.assertEqual(len(Accounts.user_data_list), 1)


if __name__ == '__main__':
    unittest.main()