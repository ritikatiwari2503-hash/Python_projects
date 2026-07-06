import random
import string   #import string from here


string.ascii_letters # a-z + A-Z
string.digits  # 0-9
string.punctuation # special characters 

characters = string.ascii_letters + string.digits + string.punctuation

len = int(input("Enter the length of the password: "))

password = ''.join(random.choice(characters) for _ in range(len))
print(password)
