alien_0 = {}
alien_1 = {}
alien_2 = {}

aliens = [alien_0, alien_1, alien_2]

alien_0['colour'] ='green'
alien_0['death_points'] = 5
alien_1['colour'] ='blue'
alien_1['death_points'] = 10
alien_2['colour'] ='red'
alien_2['death_points'] = 15


print("\nThe alien is coloured ",alien_0['colour'].title())

new_points = alien_0['death_points']
print(f"\nYou have just earned {new_points} points!\n")

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed']='medium'

print(alien_0,"\n") 

## Moving the alien

print(f"The original position of the alien is ({alien_0['x_position']},{alien_0['y_position']})")

## Move the alien to the right ##

# First, determine the speed
if alien_0['speed'] == 'low':
    x_increment = 1
if alien_0['speed'] == 'medium':
    x_increment = 2
if alien_0['speed'] == 'fast':
    x_increment = 3
if alien_0['speed'] == 'superfast':
    x_increment = 5

# move the the alien position
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"The new position of the alien is ({alien_0['x_position']},{alien_0['y_position']})\n")

#### New lesson

# Make empty list for aliens
aliens = []

# Make 30 aliens
for alien_number in range(30):
    new_alien = {'colour':'green', 'death_points':5, 'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['death_points'] = 10
        alien['speed'] = 'medium'


# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

#Show total number of aliens 
print(f"Total number of aliens: {len(aliens)}")

