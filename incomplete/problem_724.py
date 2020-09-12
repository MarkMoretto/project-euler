
"""
Purpose: Project Euler exercises
Date created: 2020-09-05

Problen Number: 724
Name: Drone Delivery
URL: https://projecteuler.net/problem=724

Contributor(s):
    Mark M.

References:
    https://stackoverflow.com/questions/12435211/python-threading-timer-repeat-function-every-n-seconds

Description:
    A depot uses drones to disperse packages containing essential supplies along a long
    straight road.

    Initially all drones are stationary, loaded with a supply package.

    Every second, the depot selects a drone at random and sends it this instruction:
    
        * If you are stationary, start moving at one centimetre per second along the road.
        * If you are moving, increase your speed by one centimetre per second along the
        road without changing direction.
    
    The road is wide enough that drones can overtake one another without risk of collision.
    
    Eventually, there will only be one drone left at the depot waiting to receive its
    first instruction. As soon as that drone has flown one centimetre along the road,
    all drones drop their packages and return to the depot.
    
    Let E(n) be the expected distance in centimetres from the depot that the supply
    packages land.

    For example:
        * E(2) = 7/2
        * E(5) = 12019 / 720
        * E(100) = ~1427.193470
    
    Find E(10^8).
    Give your answer rounded to the nearest integer.
"""


# import threading as th
# from threading import Event, Thread
from random import choice
from collections import UserDict


class Drone:
    def __init__(self):
        self.speed = 0
        self.distance = 0
        self.is_stationary = True


class Drones(UserDict):
    """Class dictionary to handle drones.

    References:
        https://docs.python.org/3/library/stdtypes.html#dict-views
        https://docs.python.org/3/reference/datamodel.html
    """
    def __init__(self, number_of_drones):
        super().__init__()

        for k in range(number_of_drones):
            self[k] = Drone()

    def update(self, drone_id):
        if self[drone_id].is_stationary:
            self[drone_id].is_stationary = False
        else:
            self[drone_id].speed += 1
            self[drone_id].distance += self[drone_id].speed


    @property
    def key_list(self):
        """Helper function to create key list from KeyView object."""
        return list(self.keys())

    @property
    def stationary_count(self):
        """Helper function to count number of stationary drones."""
        # return sum([1 for k in self.key_list if self[k].is_stationary])
        return sum([1 for k in self.key_list if self[k].distance == 0])

    @property
    def total_distance(self):
        """Helper function to return total distance from all drones in collection."""
        return sum([d.distance for d in self.values()])


# N = 4

# drones = Drones(N)

# current_drone = choice(drones.key_list)
# drones.update(current_drone)


def E(n):

    drones = Drones(n)

    while drones.stationary_count > 0:

        curr = choice(drones.key_list)

        drones.update(curr)

        # msg = []
        # msg.append(f"Current Drone: {curr}")
        # msg.append(f"Curr. Drone Spd.: {drones[curr].speed}")
        # msg.append(f"Curr. Drone Dist.: {drones[curr].distance}")
        # msg.append(f"Stationary Ct.: {drones.stationary_count}\n")
        # print("\n".join(msg))
        # if drones.stationary_count == 0:
        #     break

    # tot_dist = drones.total_distance
    return drones


N = 5
E(N).total_distance
res = E(N)
print(f"{res.total_distance}")

[res[i].distance for i in res.key_list]


def run_sim(num_drones=2, epochs=1000):
    distances = []

    for n in range(epochs):
        res = E(num_drones)
        distances.append(res.total_distance)
    print(sum(distances) / epochs)

run_sim(5)



# Interval decorator

# def s_interval(n_seconds):
#     def outer_wrapper(func):
#         def wrapper(*args, **kwargs):
#             stopped = Event()

#             def inner_wrapper():
#                 while not stopped.wait(n_seconds):
#                     func(*args, **kwargs)

#             T = Thread(target = inner_wrapper)
#             T.daemon = True # Stop thread if program exits
#             T.start()
#             return stopped
#         return wrapper
#     return outer_wrapper



# @s_interval(1)
# def test_func():
#     print("Timer is running.")

# stopper = test_func()
# stopper.set()




# @s_interval(1)
# def run(n_drones):
#     # Create full drone list
#     all_drones = [i for i in range(n_drones)]

#     # Distance dictionary
#     ddict = {}

#     nactivated = 0

#     while nactivated <= n_drones:
#         # Select a random drone
#         drone = choice(all_drones)
    
#         # Track active drone distance
#         ddict[drone] = 0
    
#         for k in ddict.keys():
#             ddict[k] += 1

#         # Update drones list with those that aren't selected
#         all_drones = [i for i in all_drones if not i in ddict]

#         nactivated += 1

#     return ddict


# def E(n):
#     res = None
#     while res is None:
#         stopper = run(n)
#     stopper.set()
#     return res



