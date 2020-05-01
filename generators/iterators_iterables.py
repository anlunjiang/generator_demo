# Iterables and Iterators

# Both objects types can be iterated over - but what's the difference?

mylist = [1, 2, 3, 4, 5]

for i in mylist:
    print(i)

# All iterables have a dunder method called __iter__()
dir(mylist)
# e.g. [...__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__']

# Something can be iterated if it has the iter method

# What is an iterator?
# Iterators remembers state during iteration - and know how to get their next value - with the __next__ method
# lists do not have a __next__() method - so no state remembering

# iterables can converted to iterators with the __iter__() method

my_iterator = iter(mylist)
dir(my_iterator) # __next__() dunder method is now available
next(my_iterator)
next(my_iterator)


# This is essentially what a for loop is doing in the background - making an iterator object from an iterable and running 
# the next method repeatedly
my_iterator = iter(mylist)
while True:
    try:
        i = next(my_iterator)
        print(i)
    except StopIteration:
        break

###################

# Generators - they are iterators that yield a value
# When they yield a value - they keep that state until that generator is run again with the next yield

def primes(max):
    number = 1
    while number < max:
        number += 1 
        if check_prime(number):
            yield number

prime_numbers = primes(100)

for i in prime_numbers:
    print(i)


# May have noticed that i had to re-instantiate gen - why?
# Generators calculate values on the fly - they are lazy almost - they dont do anything until you iterate through them
# they only give you one value at a time - once iterated through - the generator is exhuasted and is no longer in memory
# This is great for calculating large sets of data without taking up a huge amount of memory!


# Conclusions
# Iterators are a subset of Iterables 
    # Iterables are defined by the dunder method __iter__() which allow them to be iterated over
# Iterators remember state during iteration - and know the next value they should yield
# Generators are convenient ways to produce make iterators without adding the relevant dunder methods
# Generators calculate values on the fly and are very memory efficient
    # They are exhausted once they have been iterated over
    # They are great for performing calculations on huge datasets with little memory overhead 





