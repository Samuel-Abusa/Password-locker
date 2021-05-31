class User:
  def __init__(self, firstName, lastName, passWord):
    self.first_name = firstName
    self.last_name = lastName
    self.pass_word = passWord
  
  newUser = []

  def save_user_info(self):
    User.newUser.append(self)
  

