#Conditional Tests

car = "subaru"
print("Is car == 'subaru'? I predict True.")
print(car == "subaru")

print("\nIs car == 'audi'? I predict False.")
print(car == "audi")

city = "jakarta"
print("\nIs city == 'Jakarta'? (case-sensitive) I predict False.")
print(city == "Jakarta")

print("\nIs city.lower() == 'jakarta'? I predict True.")
print(city.lower() == "jakarta")

age = 25
print("\nIs age >= 18? I predict True.")
print(age >= 18)

print("\nIs age < 18? I predict False.")
print(age < 18)

print("\nIs age == 30? I predict False.")
print(age == 30)

print("\nIs age != 30? I predict True.")
print(age != 30)

fruits = ["apple", "banana", "mango"]
print("\nIs 'mango' in fruits? I predict True.")
print("mango" in fruits)

print("\nIs 'grape' in fruits? I predict False.")
print("grape" in fruits)

print("\nIs age >= 18 and city == 'jakarta'? I predict True.")
print(age >= 18 and city == "jakarta")

print("\nIs age < 18 or car == 'subaru'? I predict True.")
print(age < 18 or car == "subaru")