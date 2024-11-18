
def sieve(x):
    """
        This function will find the prime numbers up to
        x using the Sieve of Eratosthenes

        :param x: int - the max number for which
            to find the prime numbers

        :return: list - prime numbers up to x
        """
    all_numbers = list(range(2, x+1))
    current_index = 0
    for prime in all_numbers:
        for integer in all_numbers[(current_index+1):]:
            if integer % prime == 0:
                all_numbers.remove(integer)
        current_index += 1
    return all_numbers

print(sieve(100))
print("testing push pull")
