import random
import string

print('Hello welcome to the password generator')
print('\n')
length = int(input('How long would you like your password to be: '))

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

print(pAssWord)