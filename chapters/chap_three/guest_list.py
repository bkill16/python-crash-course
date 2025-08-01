guests = ['Hayden Christensen', 'Theo James', 'Paul Mescal']
print(f'\nI invited {guests[0]} to dinner tonight.')
print(f'I invited {guests[1]} to dinner tonight.')
print(f'I invited {guests[2]} to dinner tonight.\n')

print(f'{guests[2]} cannot come to dinner tonight :(\n')

guests.remove('Paul Mescal')

guests.append('David Corenswet')

print(f'I invited {guests[0]} to dinner tonight.')
print(f'I invited {guests[1]} to dinner tonight.')
print(f'I invited {guests[2]} to dinner tonight.\n')

print('Yay I found a bigger table so more people can come to dinner tonight!!!\n')

guests.insert(0, 'Taylor Swift')
guests.insert(3, 'Gracie Abrams')
guests.append('Olivia Rodrigo')

print(f'I invited {guests[0]} to dinner tonight.')
print(f'I invited {guests[1]} to dinner tonight.')
print(f'I invited {guests[2]} to dinner tonight.')
print(f'I invited {guests[3]} to dinner tonight.')
print(f'I invited {guests[4]} to dinner tonight.')
print(f'I invited {guests[5]} to dinner tonight.\n')

print('Oh no! My big table is gone so I cannot have a big dinner party. I can only invite two people.\n')

removed_guest = guests.pop()
print(f"I'm sorry {removed_guest}, but I have to rescind my invitation.")
removed_guest = guests.pop()
print(f"I'm sorry {removed_guest}, but I have to rescind my invitation.")
removed_guest = guests.pop()
print(f"I'm sorry {removed_guest}, but I have to rescind my invitation.")
removed_guest = guests.pop()
print(f"I'm sorry {removed_guest}, but I have to rescind my invitation.\n")

print(f'{guests[0]} and {guests[1]}, you are still invited to dinner tonight.\n')

del guests[0]
del guests[0]

print(guests)

print()