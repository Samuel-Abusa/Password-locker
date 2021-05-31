from existingAcount import Accounts
from user import User

def newAccount(social,fName, lName, pWord):
  #This function creates a new user account
  new_account = User(social, fName, lName, pWord)
  return new_account

def saveNewUser(userAcount):
  #Saves the user account info
  userAcount.save_user_info()

def other_account(accName, uName, exPword):
  #Let's user add an existing account
  existingAcc = Accounts(accName, uName, exPword)
  return existingAcc

def store_acc(accnt):
  accnt.store_user_data()

def all():
  name = input('Hello welcome to your pasword locker what is your name:')
  print('\n')
  print(f'Hello {name} what would you like to do')
  print('\n')
  while True:
    print("Use these short coder to : Create account password - ca, Save your existing account - ea")
    short_code = input().lower()
    if short_code == 'ca':
      sMedia = ("What is the name of the platform you'd like to create an account for : ")
      f_name = input('Your first name: ')
      l_name = input('Your last name: ')
      p_word = input('Your password: ')

      saveNewUser(newAccount(sMedia, f_name, l_name, p_word))
      print(f"Your {sMedia} account has been created")
    
    elif short_code == 'ea':
      acc = input('What is the name of your social media platform ')
      usName = input("What was your username? ")
      exstPass = input("What is your account's password: ")

      store_acc(other_account(acc, usName, exstPass))
      print(f'Your {acc} has been saved')

