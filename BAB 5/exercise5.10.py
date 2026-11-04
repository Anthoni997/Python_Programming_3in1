#Checking Usernames

current_users = ["alice", "bob", "charlie", "diana", "admin"]
new_users = ["edward", "Alice", "Frank", "BOB", "Grace"]

for new_user in new_users:
    if new_user.lower() in [u.lower() for u in current_users]:
        print(f"'{new_user}' is already taken. Please enter a new username.")
    else:
        print(f"'{new_user}' is available!")