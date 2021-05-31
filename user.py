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
  

