import string
import random as r
length=4 
otp=''
a = string.ascii_letters + string.digits
print(a)
for i in range(length):
  otp=otp+r.choice(a)
print("OTP: ",otp)
