cars = ['bmw','audi', 'toyota', 'subaru']

print("\nHere is the original list:")
print(cars)
print("\nHere is is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
cars.reverse()
print("\nHere is the reversed list:")
print(cars)
print("\nThe length of the list is ")
print(len(cars))


for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
