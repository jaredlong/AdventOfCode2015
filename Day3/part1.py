#Reading and pulling the data from the textFile.
my_file = open('day3/input.txt', 'r')
directions = my_file.read()

path = ['0-0']
x = 0
y = 0

for direction in directions:
    if direction == '^':
        y+=1
    elif direction == 'v':
        y-=1
    elif direction == ">":
        x+=1
    elif direction == '<':
        x-=1
    path.append(str(x) + '-' + str(y))

print(len(path))

houses = set(path)

print('Santa delivered presents to only ' + str(len(houses)) + ' houses')

