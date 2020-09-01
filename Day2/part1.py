#Reading and pulling the deets from the textFile.
my_file = open('day2/input.txt', 'r')
dimensions = my_file.read()
dimension_list = dimensions.split('\n')

def answer(measurements):
    total = 0
    for item in measurements:
        measurment_list = item.split('x')
        l = int(measurment_list[0])
        w = int(measurment_list[1])
        h = int(measurment_list[2])
        area = 2*l*w + 2*w*h + 2*h*l
        extra = min(l*w, w*h, h*l)
        total = total + area + extra
    print(total)

answer(dimension_list)
