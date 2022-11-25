def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def isPrime(num):
    if (num > 1):
        for i in range(2, int((num / 2) + 6)):
            if (num % i) == 0:
                #print(f"The number is not prime {i} * {int(num/i)}")
                return False
            if i == int((num / 2) + 1):
                #print('The number is prime')
                return True

# if is_prime(pow(2, 61) - 1):
#     print('Prime')
# else:
#     print('Not prime')

primes = [41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]

for i in primes:
    print(pow(2, i))
    if (is_prime(pow(2, i) - 1)):
        print(f"2^{i} - 1 is prime!")
        with open('readme.txt', 'a') as f:
            f.write(f"{i}, ")

# for i in range(40, 500):
#     if is_prime(i):
#         print(i)
#         with open('readme.txt', 'a') as f:
#             f.write(f"{i}, ")
