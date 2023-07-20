qu = "\nPlease enter the name of a city you have visited:"
qu +="\n(Enter 'quit' when you are finished.) "

while True:
    city = input(qu)
    
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")