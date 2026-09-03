import random
otp = random.randint(1000, 9999)
print("Your OTP is:", otp)
user_otp = int(input("Enter the OTP: "))
if user_otp == otp:
    print("OTP verified successfully!")
else:
    print("Invalid OTP!")
