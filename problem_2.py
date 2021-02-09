import matplotlib.pyplot as plt

"""
    Problem 2
    @author: Serge Dontsa
    Part 1
"""


def compute_f_of_x(x):
    return (2 * pow(x, 3) + 5) / (3 * pow(x, 2))


def compute_value_of_x_plus_one(N):
    x0 = 1
    y_axis_result_arr = []
    x_value_of_n = []
    for x in range(1, (N + 1)):
        x_value_of_n.append(x)
        x0 = compute_f_of_x(x)
        y_axis_result_arr.append(format(x0, ".1f"))

    # Create the plot
    plt.plot(x_value_of_n, y_axis_result_arr)

    # Title
    plt.title("Sequence")

    # Add a grid
    plt.grid(alpha=.4, linestyle='--')

    # Show plot
    plt.show()
    print(y_axis_result_arr)
    print(x_value_of_n)


def compute_actual_value(x, exp):
    m = exp - 1
    x_exp_1 = pow(x, m)
    value_x = compute_f_of_x(x_exp_1)
    print(value_x)


print("..................SECOND CASE.......................")


def compute_f_of_x_second_case(x, c):
    return c * x * (1 - x)


def second_case():
    x_value_array = [0.1, 0.2, 0.3, 0.4, 0.5]
    c_value_array = [0.95, 1.55, 2, 3.6, 3.98]
    y_result = []
    for x in range(len(x_value_array)):
        y_result.append(format(compute_f_of_x_second_case(x_value_array[x], c_value_array[x]), ".2f"))
    print(y_result)
    plt.plot(x_value_array, y_result)
    plt.title("Sequence Part II")
    plt.grid(alpha=.4, linestyle='--')
    plt.show()


second_case()
