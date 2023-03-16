import time
import numpy as np


def profile(func):
    def inner(*args, **kwargs):
        start = time.process_time_ns()
        result = func(*args, **kwargs)
        stop = time.process_time_ns()

        print("Took {0} seconds".format((stop - start) / 1e9))
        return result

    return inner


@profile
def measure_me(n):
    total = 0
    for i in range(n):
        total += i * i

    return total


def attach_names(data, names):
    """Create datastructure containing patient records."""
    output = []

    for i in range(len(data)):
        output.append({'name': names[i],
                       'data': data[i]})

    return output


print(measure_me(1000000))
data = np.array([[1., 2., 3.],[4., 5., 6.]])

output = attach_names(data, ['Alice', 'Bob'])
print(output)

# file: inflammation/models.py

class Patient:
    def __init__(self, name):
        self.name = name
        self.observations = []

alice = Patient('Alice')
print(alice.name)


class Patient:
    """A patient in an inflammation study."""
    def __init__(self, name):
        self.name = name
        self.observations = []

    def add_observation(self, value, day=None):
        if day is None:
            try:
                day = self.observations[-1]['day'] + 1

            except IndexError:
                day = 0

        new_observation = {
            'day': day,
            'value': value,
        }

        self.observations.append(new_observation)
        return new_observation

alice = Patient('Alice')
print(alice)

observation = alice.add_observation(3)
print(observation)
print(alice.observations)