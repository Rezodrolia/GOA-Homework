required_weight = 50
required_height = 170

users_weight = int(input("Enter your weight here: "))
users_height = int(input("Enter your height here: "))

print(users_weight > required_weight)
print(users_weight == required_weight)
print(users_weight < required_weight)
print(users_weight >= required_weight)
print(users_weight <= required_weight)
print(users_weight > required_weight and users_height < required_height)
print(users_weight < required_weight or users_height > required_height)