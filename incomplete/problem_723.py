
"""
Purpose: Project Euler exercises
Date created: 2020-07-12

Problen Number: 723
Name: Pythagorean Quadrilaterals
URL: https://projecteuler.net/problem=723

Contributor(s):
    Mark M.
"""


import numpy as np

PI = np.math.pi

def degtorad(degrees):
    """Function that converts degrees to radians."""
    one_rad = (180 / PI)
    return degrees / one_rad

def radtodeg(radians):
    """Function that converts radians to degrees."""
    one_rad = (180 / PI)
    return radians * one_rad


def distance(a, b, n_places=6):
    """Function that finds Euclidian distance."""
    return round(np.linalg.norm(a - b), n_places)


def origin_dist(coord, n_places=6):
    return round(distance(origin, coord), n_places)


def edge_len(coord_1, coord_2):
    return ((coord_1[0] - coord_2[0])**2 + (coord_1[1] - coord_2[1])**2) ** 0.5



class GenericMixin:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class Quad(GenericMixin): pass
class Quadrants(GenericMixin): pass
class Vertices(GenericMixin): pass

quad_dict = dict(
    q1 = Quad(**dict(quadrant = 1, domain=(0, 90))),
    q2 = Quad(**dict(quadrant = 2, domain=(90, 180))),
    q3 = Quad(**dict(quadrant = 3, domain=(180, 270))),
    q4 = Quad(**dict(quadrant = 4, domain=(270, 360))),
    )

quads = Quadrants(**quad_dict)
assert (quads.q1.domain == (0, 90)), "Error: Quadrants class instantiation."




# np.tan(np.deg2rad(60))
# np.sin(np.deg2rad(30))

# Example
N = 5
R = np.sqrt(N)
# 8*(R**2) # Should be ~40 for N = 5
origin = np.array((0, 0))
coords_r = np.array((-2, 1))
coords_a = np.array((-1, -2))
coords_b = np.array((2, -1))
coords_c = np.array((2, 1))
coords_d = np.array((-1, 2))





# # Distance from origin
origin_dist = dict(
    length_r = distance(origin, coords_r),
    length_a = distance(origin, coords_a),
    length_b = distance(origin, coords_b),
    length_c = distance(origin, coords_c),
    length_d = distance(origin, coords_d),
)



def coord_degrees(x, y):
    angle = radtodeg(np.arctan2(y, x))
    if y < 0:
        angle * -1
    return angle



class CoordGenerator:

    def __init__(self, radius, degree_domain, increment=0.5, origin=(0, 0)):
        self.set_radius(radius)
        self.set_domain(degree_domain)
        self.set_increment(increment)
        self.set_origin(origin)

    def set_radius(self, value):
        self.radius = value

    def set_domain(self, value):
        self.domain = value

    def set_origin(self, value):
        self.origin = value

    def set_increment(self, value):
        self.increment = value

    @staticmethod
    def rangef(start, stop=None, step=1.):
        """Range function with floating-point values."""
        if stop == None:
            stop = start * 1.
            start = 0.

        while True:
            if step > 0. and start >= stop:
                break
            elif step < 0. and start <= stop:
                break
            yield start

            start = start + step


    def point_gen(self, scale=3):
        """Range function with floating-point values."""

        # Radius and both origin coordinates.
        r, cx, cy = self.radius, self.origin[0], self.origin[1]

        rng = self.rangef(self.domain[0], self.domain[1], self.increment)

        for d_ in rng:
            rad_ = degtorad(d_)
            x_ = cx + r * np.cos(rad_)
            y_ = cy + r * np.sin(rad_)
    
            yield (round(x_, scale), round(y_, scale))

    def run(self):
        """Range function with floating-point values."""
        return list(self.point_gen())



## Evaluation of distance (edges) against target.
"""
Edge notes:
    A -> B = Edge A
    B -> C = Edge B
    C -> D = Edge C
    D -> A = Edge D
"""

# Example
N = 5
R = np.sqrt(N)

R_TARGET = round(np.power(R, 2) * 8, 3)


# 8*(R**2) # Should be ~40 for N = 5
origin = np.array((0, 0))

coords_r = np.array((-2, 1))

coords_a = np.array((-1, -2))
coords_b = np.array((2, -1))
coords_c = np.array((2, 1))
coords_d = np.array((-1, 2))


coord_dist = dict(
    edge_ab = distance(coords_a, coords_b),
    edge_cb = distance(coords_b, coords_c),
    edge_cd = distance(coords_c, coords_d),
    edge_ad = distance(coords_d, coords_a),
    diag_ac = distance(coords_a, coords_c),
    diag_bd = distance(coords_b, coords_d),
    )


def sine(degrees):
    """Function to return sine value. Converts degrees
    to radians first.
    """
    return np.sin(np.deg2rad(degrees))


def get_angle(opposite_edge, adj_edge_1, adj_edge_2):
    a = opposite_edge
    b, c = adj_edge_1, adj_edge_2
    numer = b**2 + c**2 - a**2
    denom = 2 * b * c
    return round(np.rad2deg(np.arccos(numer / denom)), 6)


def calc_half(edge_1, edge_2, angle):
    return np.sqrt(edge_1 * edge_2) * sine(angle)


def quad_area(**dists):
    a_angle = get_angle(dists["diag_bd"], dists["edge_ab"], dists["edge_ad"])
    c_angle = get_angle(dists["diag_bd"], dists["edge_cb"], dists["edge_cd"])

    lhs = calc_half(dists["edge_ab"], dists["edge_ad"], a_angle)
    rhs = calc_half(dists["edge_cb"], dists["edge_cd"], c_angle)
    return round(lhs + rhs, 6)


quad_area(**coord_dist)



# https://en.wikipedia.org/wiki/Quadrilateral

def quadri_area(p, q, *args):
    lhs = 4 * (p**2 * q**2)
    rhs = (args[0]**2 + args[1]**2 - args[2]**2 - args[3]**2)**2
    return (1/4) * np.sqrt(lhs - rhs)

# Diagonal distance
p = distance(coords_a, coords_c)
q = distance(coords_b, coords_d)

lhs = 4 * (p**2 * q**2)

quadri_area(p, q, *coord_dist.values())


1.5+1.5+3+3

circ_area = PI * R**2

base_diag = (R**2 + R**2)**0.5
sq_area = round(base_diag**2 / 2, 6)


angle_a = find_angle(coords_a, coords_b, coords_d)
angle_c = find_angle(coords_c, coords_b, coords_d)

aa = quad_half(coords_a, coords_b, coords_d)
cc = quad_half(coords_c, coords_b, coords_d)
quad_area = aa + cc

def eval_quad(**kwargs):
    tot = round(sum(map(lambda x: x**2, kwargs.values())), 2)
    return tot == R_TARGET

eval_quad(**coord_dist)


q1_coords = CoordGenerator(R, quads.q1.domain, 1).run()

q1_coords = CoordGenerator(R, quads.q1.domain, 1).run()
q2_coords = CoordGenerator(R, quads.q2.domain, 1).run()
q3_coords = CoordGenerator(R, quads.q3.domain, 1).run()
q4_coords = CoordGenerator(R, quads.q4.domain, 1).run()
















# def points_on_circle(r, n=100):
#     PIPI = 2 * PI
#     return [(np.cos(PIPI / n * x) * r, np.sin(PIPI / n * x) * r) for x in range(0, n + 1)]

# def all_floats():
#     for i in range(-2**10, 2**10):
#         for j in range(-2**52, 2**52):
#             yield (j / 2**52) * 2**i


# def all_circle(r, domain = all_floats):

#     target = (r**2)*8

#     for a in domain():
#         for b in domain():
#             aabb = a**2 + b**2
#             if aabb < target:
#                 for c in domain():
#                     aabbcc = aabb + c**2
#                     if aabbcc < target:
#                         for d in domain():
#                             aabbccdd = aabbcc + d**2
#                             if aabbccdd == (r**2)*8:
#                                 return 1

# pts_gen = all_circle(1)






