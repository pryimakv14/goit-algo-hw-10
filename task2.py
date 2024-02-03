import random
import scipy.integrate as spi


def func(x):
    return x**2


def monte_carlo_integrate(func, a, b, num_samples):
    underline_points = 0

    for _ in range(num_samples):
        x = random.uniform(a, b)
        y = random.uniform(0, func(b))
        if y <= func(x):
            underline_points += 1

    return (underline_points / num_samples) * (b - a) * func(b)

if __name__ == '__main__':
    a = 0
    b = 2

    mc_result = monte_carlo_integrate(func, a, b, 10_000_000)

    print("Монте-Карло: ", mc_result)
    print("quad: ", spi.quad(func, a, b)[0])
