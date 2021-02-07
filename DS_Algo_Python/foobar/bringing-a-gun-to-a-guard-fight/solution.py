
import math


class Segment: 
    def __init__(self, start, end): 
        self.start = start 
        self.end = end 
    
    def str(self):
        return str(self.start.str())+' , '+str(self.end.str())
    
    def slope(self): # Line slope given two points:
        p1 = self.start
        p2 = self.end
        return (p2.y-p1.y)/(p2.x-p1.x)
    
    def slopeDefined(self):
        try:
            self.slope()
            return True
        except:
            return False
    
    def equals(self,seg):
        if self.start.equals(seg.start) and self.end.equals(seg.end):
            return True
        return False

class Point: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
    
    def str(self):
        return '('+str(self.x)+','+str(self.y)+')'
    
    def equals(self,p):
        if self.x == p.x and self.y == p.y:
            return True
        return False

def line_intersection(seg1,seg2):
    p1 = seg1.start
    p2 = seg1.end
    p3 = seg2.start
    p4 = seg2.end
    line1 = ( (p1.x, p1.y), (p2.x, p2.y) )
    line2 = ( (p3.x, p3.y), (p4.x, p4.y) )

    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return Point(1,1),False

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return Point(x, y), True

def isOnLine(segment, pt3):
    pt1 = segment.start
    pt2 = segment.end
    x1, x2, x3 = pt1.x, pt2.x, pt3.x

    if x2 == x1:
        return False
    y1, y2, y3 = pt1.y, pt2.y, pt3.y
    
    slope = (y2 - y1) / (x2 - x1)

    pt3_on = (y3 - y1) == slope * (x3 - x1)

    pt3_between = (min(x1, x2) <= x3 <= max(x1, x2)) and (min(y1, y2) <= y3 <= max(y1, y2))

    return pt3_on and pt3_between

def distanceBetween(seg):  
    p1 = seg.start
    p2 = seg.end
    dist = math.sqrt( (p2.x - p1.x)**2 + (p2.y - p1.y)**2 )  
    return int(dist)

def getPointFromAngle(iP, angle, dimensions):
    line_length= getLineLength(dimensions)

    x = int(iP.x + line_length*math.cos(angle))
    y = int(iP.y + line_length*math.sin(angle))

    return Point(x, y)

def slope(p1,p2): # Line slope given two points:
    return (p2.y-p1.y)/(p2.x-p1.x)

def intersectAngle(seg1,seg2):
    s = 0
    if not seg1.slopeDefined():
        s = 90 - math.degrees(math.atan(seg2.slope()))
    elif not seg2.slopeDefined():
        s = 90 -math.degrees(math.atan(seg1.slope()))
    else:
        s1 = seg1.slope()
        s2 = seg2.slope()
        s = math.degrees(math.atan((s2-s1)/(1+(s2*s1))))    
    return s

def getLineLength(dim):
    return 1250 + 1250 + 1



def findSegmentStartsWith(p,segments):
    for seg in segments:
        if p.x == seg.start.x and p.y == seg.start.y:
            return seg
    return None

def isCorner(ray,corners):
    for c in corners:
        if ray.equals(c):
            return True
    return False

def reflect(corners, init, dimensions, guard, you , segment, tot_dist, dist, angle_x_axis, walls,rays):
    wall = segment[0]
    ray = segment[1]

    if ray.slopeDefined() and tot_dist < dist:
        isOl = isOnLine(ray, guard)
        # print(rays)
        if isOl:
            d = distanceBetween(Segment(ray.start, guard))
            # print(ray.str(),guard.str())
            if d + tot_dist <= dist:
                # print(ray.str())
                return True
            else:
                return False

        theta = abs(intersectAngle(ray,wall))
        if int(theta) is not 90 and not isCorner(ray.end, corners):
            d = distanceBetween(ray)
            if tot_dist + d <= dist:
                e1 = distanceBetween(Segment(ray.end,wall.end))
                e2 = distanceBetween(Segment(ray.end,wall.start))

                w1 = findSegmentStartsWith(wall.end, walls)
                w2 = findSegmentStartsWith(wall.start, walls)

                nextWall = None
                if e1 < e2:
                    nextWall = w1
                    if nextWall.equals(wall):
                        nextWall = w2
                else:
                    nextWall = w2
                    if nextWall.equals(wall):
                        nextWall = w1
                        
                # print(wall.str()," X ", ray.str(), theta, nextWall.str())
                
                iP = Point(0,0)
                if nextWall.slopeDefined():
                    iP.y = nextWall.start.y
                    iP.x = ray.start.y * abs(math.tan(theta)) % 3
                else:
                    iP.x = nextWall.start.x
                    iP.y = ray.start.x * abs(math.tan(theta)) % 2

                print(wall.str(),nextWall.str(),iP.str(),theta)

                print("&&&&&&&&&&&&&&")
                # print(iP.str())
                nextRay = Segment(ray.end,iP)
                return reflect(corners,ray.end,dimensions,guard,you,[nextWall,nextRay ] ,tot_dist+d,dist,angle_x_axis,walls,rays+[nextRay] )
    return False
    


def startBeam(dimensions, your_position, guard_position, distance):
    x_dim = dimensions[0]
    y_dim = dimensions[1]

    you_x = your_position[0]
    you_y = your_position[1]
    you = Point(you_x, you_y)

    guard_x = guard_position[0]
    guard_y = guard_position[1]
    guard = Point(guard_x, guard_y)

    solutions = 0
    dis = distanceBetween(Segment(you, guard))
    if dis < distance:
        solutions +=1
    
    init = you
    corners = [
        Point(dimensions[0],0),
        Point(dimensions[0], dimensions[1]),
        Point(0, 0),
        Point(0,dimensions[1])
    ]

    walls = [      
                Segment( Point(dimensions[0],0), Point(dimensions[0], dimensions[1])),
                Segment( Point(dimensions[0], dimensions[1]), Point(0, dimensions[1])),
                Segment( Point(0,dimensions[1]), Point(0, 0) ),
                Segment(Point(0, 0), Point(dimensions[0],0))
            ]

    segments = [
        #[wall, Segment ]
    ]

    factor = 0.1
    for wall in walls:
        if wall.slopeDefined():
            
            start = min([wall.start.x,wall.end.x])
            end = max([wall.start.x,wall.end.x])
            point = start
            while point < end:
                seg = Segment(init, Point(point, wall.start.y ))
                segments.append([wall,seg])
                point += factor
        else:
            
            start = min([wall.start.y,wall.end.y])
            end = max([wall.start.y,wall.end.y])
            point = start
            while point < end:
                seg = Segment(init, Point( wall.start.x, point ))
                segments.append([wall,seg])
                point += factor
        
    for segment in segments:
        pos = reflect(corners,init, dimensions, guard,you, segment, 0, distance, 0, walls,[segment[1]])
        r = segment[1]
        print(you.str(),r.end.str())

        if pos:
            # print(segment[0].str())
            solutions += 1
    
    return solutions




def solution(dimensions, your_position, guard_position, distance):
    # check direct distance
    # move in clockwise / anti-clockwise
    # rotate anti-clockwise
    # check intersection with the wall
    # check if distance is less than beam travel
    # if yes : reflect until the point is reached or the distance is exhausted
    # if the point it reached and distance is not exhasted add to the possibility

    sol = startBeam(dimensions, your_position, guard_position, distance)
    
    return sol

print(solution([3,2], [1,1], [2,1], 4))
