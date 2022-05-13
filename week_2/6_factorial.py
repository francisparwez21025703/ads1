def factorial(n):

    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


if __name__ == "__main__":

    print(factorial(5))
