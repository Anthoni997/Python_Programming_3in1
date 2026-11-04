#More Conditional Tests

username = "admin"
print(f"username == 'admin': {username == 'admin'}")
print(f"username != 'admin': {username != 'admin'}")
print(f"username == 'Admin': {username == 'Admin'}")
print(f"username.lower() == 'ADMIN'.lower(): {username.lower() == 'ADMIN'.lower()}")

score = 85
print(f"\nscore == 85: {score == 85}")
print(f"score != 100: {score != 100}")
print(f"score < 100: {score < 100}")
print(f"score > 100: {score > 100}")
print(f"score <= 85: {score <= 85}")
print(f"score >= 90: {score >= 90}")

print(f"\nscore > 70 and username == 'admin': {score > 70 and username == 'admin'}")
print(f"score > 90 and username == 'admin': {score > 90 and username == 'admin'}")
print(f"score > 90 or username == 'admin': {score > 90 or username == 'admin'}")
print(f"score > 90 or username == 'user': {score > 90 or username == 'user'}")

languages = ["python", "java", "c++"]
print(f"\n'python' in languages: {'python' in languages}")
print(f"'ruby' in languages: {'ruby' in languages}")
print(f"'ruby' not in languages: {'ruby' not in languages}")
print(f"'python' not in languages: {'python' not in languages}")