# Declare dictionary for responses

from urllib import response


responses ={}

# Set a flag to indicate that pooling is active
polling_active = True

while polling_active:
    #Prompt for the person name and response
    name = input("\nPlease enter your name: ")
    response = input("Please enter your favourite mountain: ")
    
    # Store the response in the dictionary
    responses[name] = response
    
    # Find out if there any more people to take the poll
    repeat = input("Would you like enter anyone else's name? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Print the results
for name, response in responses.items():
    print(name.title() + " would to climb " + response.title())