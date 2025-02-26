all_users = ["Pasky", "Mercy", "Ebele", "Martins"]
all_users_copy = all_users[:]

all_users_copy.append("Daisy")
print(all_users_copy)
print()
users = {"Daisy": "active", "Mercy": "inactive", "Ebele":"New"}

active_users = {}
for user, status in users.items():
    if status == "active":
        active_users[user] = status
print(active_users)