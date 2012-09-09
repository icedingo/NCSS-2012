import math

Earth_Radius = 6353000.0

class City:
    def __init__(self, data):
        name  =   str(data[0])
        theta = float(data[1])
        self.name = name
        self.x    = Earth_Radius * math.sin(theta)
        self.y    = Earth_Radius * math.cos(theta)


class Satellite:
    def __init__(self, data):
        orbit    = float(data[0])
        velocity = float(data[1])
        theta    = float(data[2])
        self.height   = orbit + Earth_Radius
        self.theta    = theta
        self.velocity = velocity*60
        self.angularv = self.velocity/self.height
        #print 'sat', self.height, 'angv =', self.angularv
        self.exttan   = math.sqrt(self.height**2 - Earth_Radius**2)

        self.update_cartesian(theta)

    def update_cartesian(self, theta):
        self.x = self.height * math.sin(theta)
        self.y = self.height * math.cos(theta)

    def update_position(self):
        self.theta += self.angularv
        self.update_cartesian(self.theta)

def distance_between(point1, point2):
    x1 = point1[0]
    x2 = point2[0]
    y1 = point1[1]
    y2 = point2[1]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def feq(a, b):
    return abs(a - b) <= 1e-6

cities     = set()
satellites = set()
for line in open('gpsin.txt'):
    enter = line.split()
    if not enter:
        continue
    citsat  = enter[0]
    therest = enter[1:]
    if citsat == 'city':
        cities.add(City(therest))
    elif citsat == 'satellite':
        satellites.add(Satellite(therest))

blackouts = dict((city, 0) for city in cities)

dump = open('dump.txt','w')

for i in xrange(1440):
    for sat in satellites:
        sat.update_position()
        dump.write('satellite %f %f\n' % (sat.x, sat.y))

    for cit in cities:
        dump.write('city %s %f %f\n' % (cit.name, cit.x, cit.y))
        citpoint = (cit.x, cit.y)
        for sat in satellites:
            satpoint = (sat.x, sat.y)
            if distance_between(citpoint, satpoint) < sat.exttan:
                break
        else:
            blackouts[cit] += 1

    dump.write('\n')

for cit in cities:
    print cit.name, blackouts[cit]

#print blackouts