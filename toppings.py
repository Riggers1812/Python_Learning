available_toppings = ['cheese', 
                     'tomato', 
                     'peppers', 
                     'onions', 
                     'mushrooms', 
                     'pineapple', 
                     'pepperoni', 
                     'ham']

requested_toppings = ['cheese', 'tomato', 'mushrooms', 'peppers', 'chicken']

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping not in available_toppings:
            print(f"\nSorry, {requested_topping} is currently unavailable")
        else:
            print(f"\nAdded extra {requested_topping}") 
    if requested_toppings != 'anchovies':
        print("\nHold the anchovies!")
else:
    print("\nAre you sure you want plain pizza?")
print("\nFinished making your pizza!\n")

# Store pizza details 

pizza = {
    'crust':'thick', 
    'toppings':requested_toppings
}

# Summarise the order
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")