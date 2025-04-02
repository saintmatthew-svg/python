even_numbers = []
cube_numbers = {}

for even in range(2,31,2):
    even_numbers.append(even)
    cube_numbers[even] = even **3
    
#print(even_numbers)
print(cube_numbers) 