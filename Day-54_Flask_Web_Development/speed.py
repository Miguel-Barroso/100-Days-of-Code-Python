import time

current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970


# Write your code below 👇

def speed_calc_decorator(function):

    def wrapper():
        start_time = time.time()
        function()
        end_time = time.time()
        print(end_time-start_time)

    return wrapper  # Has to be returned without being executed

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i

fast_function()

@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i

slow_function()

# Python takes time to perform these operations because each iteration is interpreted
# However, NumPy offloads calculations to C for blazing-fast speeds:

import numpy as np
import time

start = time.time()
x = np.arange(1_000_000) ** 2
end = time.time()
print("NumPy fast function:", end - start)

start = time.time()
x = np.arange(10_000_000) ** 2
end = time.time()
print("NumPy slow function:", end - start)