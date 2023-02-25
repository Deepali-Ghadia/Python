# creating a random user password : letters, punctuation and digits of string module
from string import ascii_letters, digits, punctuation
import random
set_of_characters = ascii_letters + digits + punctuation

# use random.SystemRandom() to generate a password
sr = random.SystemRandom() # creating an object of SystemRandom
password = "".join(sr.choice(set_of_characters) for i in range(13)) # length of password is 13 characters
print(password)
# choice() => takes a random element from arbitrary sequence


# creating random integers and floats in a range
print(random.randint(1,10)) # both the values are inclusive
print(random.randrange(1,10)) # last value is excluded


# random floating point number between 0 and 1
print(random.random())

# floating point number in a range
print(random.uniform(1, 10)) # both are inclusive


# Random binary decision
probability = 0.3
if random.random()< 0.3:
    print("Probability is less than 0.3")
else:
    print("Probability is greater than 0.3")
