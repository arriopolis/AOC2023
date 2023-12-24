import sys

# Inner product
def inp(p1,p2):
    x1,y1,z1 = p1
    x2,y2,z2 = p2
    return x1*x2 + y1*y2 + z1*z2

# Vector difference
def diff(p1,p2):
    x1,y1,z1 = p1
    x2,y2,z2 = p2
    return (x1-x2, y1-y2, z1-z2)

# Cross product
def cross(p1,p2):
    x1,y1,z1 = p1
    x2,y2,z2 = p2
    return (y1*z2-z1*y2, z1*x2-x1*z2, x1*y2-y1*x2)

# Read the input
stones = []
for line in sys.stdin:
    (x,y,z),(vx,vy,vz) = map(lambda x : map(int,x.split(', ')), line.strip().split(' @ '))
    stones.append(((x,y,z),(vx,vy,vz)))

# First three stones should be enough to determine the initial position
(p1,v1),(p2,v2),(p3,v3) = stones[:3]

# We can write Ap = b, where the rows of A are defined by r1, r2 and r3
r1 = cross(diff(v2,v1), diff(p2,p1))
r2 = cross(diff(v3,v1), diff(p3,p1))
r3 = cross(diff(v3,v2), diff(p3,p2))
b = (inp(diff(p2,p1), diff(cross(p2,v2), cross(p1,v1))), inp(diff(p3,p1), diff(cross(p3,v3), cross(p1,v1))), inp(diff(p3,p2), diff(cross(p3,v3), cross(p2,v2))))

# We compute the solution of Ap = b
D = inp(r1, cross(r2,r3))
c1,c2,c3 = zip(r1,r2,r3)
xD = inp(b,cross(c2,c3))
yD = inp(b,cross(c3,c1))
zD = inp(b,cross(c1,c2))

# Check if the solution is indeed integral
assert xD%D == 0
assert yD%D == 0
assert zD%D == 0

# Compute the result
x = xD // D
y = yD // D
z = zD // D
print(x+y+z)