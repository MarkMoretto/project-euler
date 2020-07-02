
"""
Purpose: Project Euler exercises
Date created: 2020-06-25

Problen Number: 353
Name: Risky moon
URL: https://projecteuler.net/problem=353

Contributor(s):
    Mark M.

Description HTML:

<p>
A moon could be described by the sphere $C(r)$ with centre $(0,0,0)$ and radius $r$. 
</p>

<p>
There are stations on the moon at the points on the surface of $C(r)$ with integer
coordinates. The station at $(0,0,r)$ is called North Pole station, the station at
$(0,0,-r)$ is called South Pole station.
</p>

<p>
All stations are connected with each other via the shortest road on the great arc
through the stations. A journey between two stations is risky. If <var>d</var> is the
length of the road between two stations, $\left(\frac{d}{\pi r}\right)^2$ is a measure
for the risk of the journey (let us call it the risk of the road). If the journey
includes more than two stations, the risk of the journey is the sum of risks of the
used roads.
</p>

<p>
A direct journey from  the North Pole station to the South Pole station has the length
$\pi r$ and risk 1. The journey from the North Pole station to the South Pole station
via $(0,r,0)$ has the same length, but a smaller risk:</p>
\[
\left(\frac{\frac{1}{2}\pi r}{\pi r}\right)^2+\left(\frac{\frac{1}{2}\pi r}{\pi r}\right)^2=0.5
\]

<p>
The minimal risk of a journey from the North Pole station to the South Pole station
on $C(r)$ is $M(r)$.
</p>

<p>
You are given that $M(7)=0.1784943998$  rounded to 10 digits behind the decimal point. 
</p>

<p>
Find $\displaystyle{\sum_{n=1}^{15}M(2^n-1)}$.
</p>

<p>
Give your answer rounded to 10 digits behind the decimal point in the form a.bcdefghijk.
</p>
"""

import numpy as np

PI = np.math.pi


r: float            # Radius of sphere
d: str              # length of road

origin: tuple       # Center of sphere coordinates
np_coord: tuple     # North Pole coordinates
sp_coord: tuple     # South Pole coordinates



class C:
    origin = np.array([0, 0, 0,], dtype=np.uint32)
    def __init__(self, radius):
        self.np_coord = np.array([0, 0, radius], dtype=np.uint32)
        self.sp_coord = np.array([0, 0, -radius], dtype=np.uint32)
        self.squared_dist = 0.0
        self.distance = 0.0


    def __squared_dist(self, *args):
        if len(args) == 2:
            self.squared_dist = np.sum((args[0] - args[0])**2, axis=0)


    def distance(self, coord1, coord2):
        self.__squared_dist(coord1, coord2)
        self.distance = np.sqrt(self.squared_dist)
        return self.distance


def risk2(r):
    factor = r * PI
    m = ((0.5 * factor) / factor) ** 2
    return m + m

risk2(1)


def circumference(r=None, d=None):
    def get_radius(D):
        return D / 2

    result = None

    if r is None and not d is None:
        r = get_radius(d)

    result = 2 * PI * r

    return result

assert (circumference(r = 10) == circumference(d = 20)), "Error: Circumference formula."




def risk_of_road(d, r):
    """
    Function to measure the risk of a journey.

    If the journey includes more than two stations, the risk of the journey is the sum
    of risks of the used roads. 

    >>> round(risk_of_road(1000, 2435), 10)
    0.0170884363
    >>> risk_of_road(0, 0)
    Please enter a non-zero radius value.
    """

    def get_radius(D):
        return D / 2

    try:
        denom = PI * r
        return (d / denom) ** 2
    except ZeroDivisionError:
        print("Please enter a non-zero radius value.")




















