#Reading and pulling the deets from the textFile.
my_file = open('day2/input1.txt', 'r')
dimensions = my_file.read()
dimension_list = dimensions.split('\n')

def answer(measurements):
    total = 0
    for item in measurements:
        measurment_list = item.split('x')
        l = int(measurment_list[0])
        w = int(measurment_list[1])
        h = int(measurment_list[2])
        face = min(l+l+w+w, w+w+h+h, h+h+l+l)
        extra = l*w*h
        total = total + face + extra
    return total

print("The Amount of ribbon is:", answer(dimension_list))