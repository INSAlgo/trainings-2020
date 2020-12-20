from math import sqrt, floor


def isPrime(nb):
    """
    O(sqrt(n)) algorithm to detemine whether or not a number is prime
    :param nb: integer, which you want to test primality
    :return: True if the number is prime, False otherwise
    """
    if nb <= 1:
        return False

    for i in range(2, floor(sqrt(nb))+1):
        if nb % i == 0:
            return False

    return True


def main():
    for _ in range(int(input())):
        print("Prime" if isPrime(int(input())) else "Not prime")


if __name__ == "__main__":
    main()
