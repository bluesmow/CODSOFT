import random
import secrets
import string

uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
digits = string.digits
special = string.punctuation
allChars = lowercase_letters + uppercase_letters + digits + special
password = " "

pwLen = int(input("How long should the password be?"))
minUpper = int(input("Minimum Upper Case: "))
minLower = int(input("Minimum Lower Case: "))
mindigits = int(input("Minimum Numbers: "))
minSpec = int(input("Minimum Special: "))

for i in range(minUpper):
    password += "".join(random.choice(secrets.choice(uppercase_letters)))

for i in range(minLower):
    password += "".join(random.choice(secrets.choice(lowercase_letters)))

for i in range(mindigits):
    password += "".join(random.choice(secrets.choice(digits)))

for i in range(minSpec):
    password += "".join(random.choice(secrets.choice(special)))

remaining = pwLen - minLower - minUpper - mindigits - minSpec

for i in range(remaining):
    password += "".join(random.choice(secrets.choice(allChars)))

password = list(password)
random.shuffle(password)
print("".join(password))