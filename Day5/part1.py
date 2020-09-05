#Reading and pulling the deets from the textFile.
my_file = open('day5/input.txt', 'r')
names = my_file.read()
names = names.split('\n')

nice_list = []
#Function to check for 3 or more vowels
def vowels(kid):
    a = kid.count('a')
    e = kid.count('e')
    i = kid.count('i')
    o = kid.count('o')
    u = kid.count('u')
    ctr = a+e+i+o+u
    if ctr >= 3:
        return True
    else:
        return False

#Function to check for prohibited strings
def bad_words(kid):
    if kid.find('ab') == -1 and kid.find('cd') == -1 and kid.find('pq') == -1 and kid.find('xy') == -1:
        return True

#Function to check for duplicate letters
def find_duplicates(kids):
    for i, j in enumerate(kids[:-1]):
        if j  == kids[i+1]: 
            return True

for name in names:
    if vowels(name) == True and bad_words(name) == True and find_duplicates(name) == True:
        nice_list.append(name)

print(len(nice_list))

