
import random
import string
password  = string.ascii_letters + string.digits
length_password = int(input("Enter Length of Password :  "))
a = "".join(random.sample(password, length_password))
print(f"Pass is{a}")
