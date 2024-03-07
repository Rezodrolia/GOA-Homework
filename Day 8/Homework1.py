user_pushups = int(input("Enter your pushup numbers here: "))
user_squats = int(input("Enter your squat numbers here: "))

required_pushups = 25
required_squats = 75

print(required_pushups == user_pushups)
print(required_squats == user_squats)
print(required_squats == user_squats and required_pushups == user_pushups)
print(required_squats == user_squats or required_pushups == user_pushups)

