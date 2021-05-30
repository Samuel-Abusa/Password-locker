import unittest
from user import User

class testUsers (unittest.TestCase):
  def setUp(self):
    self.aNewUser = User("Samuel", "Abusa", "6991Avin")
  
  def test_init(self):
    self.assertEqual(self.aNewUser.first_name, "Samuel")
    self.assertEqual(self.aNewUser.last_name, "Abusa")
    self.assertEqual(self.aNewUser.pass_word, "6991Avin")
  
  def test_saving_user_info(self):
    self.aNewUser.save_user_info()
    self.assertEqual(len(User.newUser), 1)


if __name__ == '__main__':
    unittest.main()