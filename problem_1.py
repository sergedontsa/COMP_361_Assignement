import matplotlib.pyplot as plt
import numpy as np

"""
    Problem 1
    By Serge Dontsa
    Part 1
"""


def harmonic_sum_part_1(i):
    x = 1
    total = 0
    while x <= i:
        print(x)
        total = total + 1 / x
        x = x + 1
    return total


def harmonic_sum_part_2(i):
    x = 1
    total = 0
    while x < i:
        total = total + 1 / pow(3, x)
        x = x + 1
    return total


def compute_harmonic_sum_part_1():
    # N is in the x axis
    N_value = [pow(10, 1), pow(10, 2), pow(10, 3), pow(10, 4), pow(10, 5), pow(10, 6), pow(10, 7), pow(10, 8)]

    # the harmonic sum is in the y axis
    y_simple_precision = []
    y_double_precision = []

    for m in N_value:
        y_simple_precision.append(format(harmonic_sum_part_1(m), ".1f"))
        y_double_precision.append(format(harmonic_sum_part_1(m), ".2f"))

    # Printing the result on the logs

    for n in N_value:
        print("Single Precision: n = {},  N = {}, Result: {}".format((1 + N_value.index(n)), n,
                                                                     format(harmonic_sum_part_1(n), ".1f")))

    print("")
    for n in N_value:
        print("Double Precision: n = {} N = {}, Result: {}".format((1 + N_value.index(n)), n,
                                                                   format(harmonic_sum_part_1(n), ".2f")))

    # Create the plot
    # Simple Precision

    plt.plot(N_value, y_simple_precision, label="Simple Precision")

    # Double precision
    plt.plot(N_value, y_double_precision, label="Double Precision")

    # Add label
    plt.xlabel("N Value")
    plt.ylabel("Harmonic Sum")

    # Title
    plt.title("Problem I")

    # Legend
    plt.legend()

    # Add a grid
    plt.grid(alpha=.4, linestyle='--')

    # Show plot
    plt.show()


"""
    Problem 1
    By Serge Dontsa
    Part 1
"""


def compute_harmonic_sum_part_2():
    N_value = [pow(10, 1), pow(10, 2), pow(10, 3), pow(10, 4), pow(10, 5), pow(10, 6), pow(10, 7), pow(10, 8)]
    N_value_result = []
    for n in N_value:
        N_value_result.append(harmonic_sum_part_2(n))

    print(N_value_result)


compute_harmonic_sum_part_2()
