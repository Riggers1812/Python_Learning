motorbikes = ['honda', 'yamaha', 'suzuki']
print(motorbikes)

motorbikes[0] = 'ducati'
print(motorbikes)

motorbikes.append ('ducati')
print(motorbikes)



motorbikes = []

print(motorbikes)

motorbikes.append('honda')

motorbikes.append('yamaha')

motorbikes.append('suzuki')

print(motorbikes)

del(motorbikes[0])
print(motorbikes)

motorbikes = ['honda', 'yamaha', 'suzuki']
print(motorbikes)


popped_motorbike = motorbikes.pop()
print(motorbikes)
print(popped_motorbike)
motorbikes.append ('ducati')

too_expensive = 'ducati'
motorbikes.remove(too_expensive)
print(motorbikes)
print(f"\nA {too_expensive} is too expensive for me.")
      