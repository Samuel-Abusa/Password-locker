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
    '''
    Testing saving_user info to see whether we can save the created account
    '''
    self.aNewUser.save_user_info()
    self.assertEqual(len(User.newUser), 2)
  
  def test_delete_user_info(self):
    self.aNewUser.save_user_info()
    test_new_account = User('Facebool', 'James', 'Mathew', 'yeahyeahyeah234')
    test_new_account.save_user_info()

    self.aNewUser.delete_user_info()
    self.assertEqual(len(User.newUser), 1)

  
  def test_saving_credentials(self):
    '''
    Testing store_user_data to see whether we can save the added existing account account
    '''
    self.existing_account.store_user_data()
    self.assertEqual(len(Accounts.user_data_list), 2)
  
  def test_delete_account(self):
    '''
    Test to see if we can remove the saved account from the user_data_list
    '''
    self.existing_account.store_user_data()
    test_new_existing_account = Accounts('Facebook', 'Samuel', 'blaba234')
    test_new_existing_account.store_user_data()

    test_new_existing_account.remove_account()
    self.assertEqual(len(Accounts.user_data_list), 1)


if __name__ == '__main__':
    unittest.main()