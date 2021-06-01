def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def get_primes(max_num):
    list_of_primes = []
    for num in range(2, max_num):
        if is_prime(num):
            list_of_primes.append(num)
    return list_of_primes


max_num_to_check = int(input("Search for prime numbers up to: "))
get_list = get_primes(max_num_to_check)
for prime in get_list:
    print(prime)
