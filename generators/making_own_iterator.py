
def check_prime(number):
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True


# class Primes:

#     def __init__(self, max):
#         self.max = max      
#         self.number = 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.number += 1
#         if self.number >= self.max:
#             raise StopIteration
#         elif check_prime(self.number):
#             return self.number
#         else:
#             return self.__next__()

def Primes(max):
    number = 1
    while number < max:
        number += 1
        if check_prime(number):
            yield number


prime_numbers = Primes(100)

print(prime_numbers)
print(dir(prime_numbers))

# for i in prime_numbers:
#     print(i)






