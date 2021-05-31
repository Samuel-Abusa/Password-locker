class Accounts:
  def __init__(self, aCcount, user_name, existing_password):
    #collect all the user data from theie existing account    
    self.account = aCcount
    self.userName = user_name
    self.existingPassword = existing_password
  
  #This varriable stores user data in an array
  user_data_list = []
  
  #Get to add new user data in the user_data_list array
  def store_user_data(self):
    Accounts.user_data_list.append(self)

  #Delete an account
  def remove_account(self):
    Accounts.user_data_list.remove(self)
  
  @classmethod
  def check_if_acc_exists(cls, accountName):
    for user_data in cls.user_data_list:
      if user_data.account == accountName:
        return True

  @classmethod
  def find_existing_account(cls, accountName):
    for user_data in cls.user_data_list:
      if user_data.account == accountName:
        return user_data
  
  @classmethod
  def display_all_accounts(cls):
    return cls.user_data_list