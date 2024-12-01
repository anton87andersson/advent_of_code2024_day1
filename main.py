left = []
right = []

diff = 0

sum = 0
sum2 = 0


with open('input.txt') as f:
    lines = f.read().splitlines()
    
    for line in lines:
        left_number, right_number = line.split()  # Split after blankspace
        left.append(int(left_number))  # Add to left list
        right.append(int(right_number))  # Add to right list
        
# sort both list
left.sort()
right.sort()

# First star
for i in range(0, len(left)):
    lowest_left = left[i]
    lowest_right = right[i]
    diff = abs(lowest_left - lowest_right)
    sum += diff
    
# Second star
for i in left:
    sum2 += i * right.count(i)
        
        
print ("Sum for first: " + str(sum))
print ("Sum for second: " + str(sum2))
