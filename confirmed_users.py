unconfirmed_users = ['alice','bob','chris']
confirmed_users= []

# Verify each user until they are no more unconfirmed users
# Move each verified user intot the list of confirmed users
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print(f"Verfiying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display the list of confirmed users
print("\nThe following users are confirmed:")
for confirmed_users in confirmed_users:
    print(confirmed_users.title())