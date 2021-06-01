class User:
  def __init__(self, socialMedia, firstName, lastName, passWord):
    self.social_media = socialMedia
    self.first_name = firstName
    self.last_name = lastName
    self.pass_word = passWord
  
  newUser = []

  def save_user_info(self):
    User.newUser.append(self)
  
  def delete_user_info(self):
    User.newUser.remove(self)

  @classmethod
  def check_newAccount_exists(cls, accName):
    for user in cls.newUser:
      if user.social_media == accName:
        return True
  
  @classmethod
  def find_new_account(cls, accName):
    for user in cls.newUser:
      if user.social_media == accName:
        return user
  
  @classmethod
  def display_all_new_acc(cls):
    return cls.newUser