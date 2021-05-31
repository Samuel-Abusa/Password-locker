import random
import string
from existingAcount import Accounts
from user import User

def newAccount(social,fName, lName, pWord):
  '''
  This function creates a new user account
  '''
  new_account = User(social, fName, lName, pWord)
  return new_account

def saveNewUser(userAcount):
  '''
  Saves the user account info
  '''
  userAcount.save_user_info()

def remove_new_account(rmAccount):
  '''
  Deletes new accounts created
  '''
  rmAccount.delete_user_info()


def other_account(accName, uName, exPword):
  '''
  Let's user add an existing account
  '''
  existingAcc = Accounts(accName, uName, exPword)
  return existingAcc

def store_acc(accnt):
  '''
  Saves the existing account info
  '''
  accnt.store_user_data()

def find_existing_acc(userAcc):
  '''
  Function that finds the account by account name and returns the contact
  '''
  return Accounts.find_existing_account(userAcc)

def check_if_acc_exists(userAcc):
  return Accounts.find_existing_account(userAcc)

def display_all_accounts():
  return Accounts.display_all_accounts()


def all():
  name = input('Hello welcome to your pasword locker what is your name: ')
  print('\n')
  print(f'Hello {name} what would you like to do')
  print('\n')
  while True:
    print("Use these short codes to : Create account - ca, Save your existing account - ea, Generate Password - gen, Find old account - fa, Display all accounts - da, exit - ex")
    short_code = input().lower()
    if short_code == 'ca':
      sMedia = input("What is the name of the platform you'd like to create an account for : ")
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
    
    elif short_code == 'gen':
      print('Hello welcome to the password generator')
      print('\n')
      length = int(input('How many characters would you like your password to have: '))
      
      #We define data of the password
      lower = string.ascii_lowercase
      upper = string.ascii_uppercase
      numbers = string.digits
      symbols = string.punctuation
      #combine the data
      all = lower + upper + numbers + symbols
      
      #use random
      pAss = random.sample(all, length)
      
      #Join the characters geneated with the random sample and put in an array hence creating the password
      pAssWord = ''.join(pAss)
      print(f'Your new password is: {pAssWord}')
    
    elif short_code == 'fa':
      search_account = input("What is the name of the social media platform you'd like to find: ")
      if check_if_acc_exists(search_account):
        account = find_existing_acc(search_account)
        print(f'Your account: {account.account}')
        print(f'Your username: {account.userName}')
        print('-' * 30)
        print(f'Your password: {account.existingPassword}')
      else:
        print('This account does not exist.')
    
    elif short_code == 'da':
      if display_all_accounts():
        for accounts in display_all_accounts():
          print(f'Your social media platform: {accounts.account}\n Your username: {accounts.userName} \n Your Password {accounts.existingPassword}')
      else:
        print("You don't have any accounts saved yet")

    elif short_code == 'ex':
      print('Have a lovely day')
      break

    else:
      print("I didn't get that.... Please use the short codes")

if __name__ == '__main__':

    all()