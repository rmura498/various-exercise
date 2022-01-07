import sys

print('I am a module')


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i

    return fact


if __name__ == "__main__":
    print("Run as a standalone script")
    fact = factorial(int(sys.argv[1]))
    print (fact)
