# samllest number that can be divided with out a remainder from 1 to 10 is 2520
# what is the smallest number that can be divided with out a remainder from 1 to 20

a, b = 1, 20

primes = []
number = 1

for current in range(a, b+1):
        if current == 1:
                continue
        
        for prime in primes:
                if current % prime == 0:                                        
                        break
        else:
                primes.append(current)
                number *= current


nonprimes = [i for i in range(a, b+1) if i not in primes]


for nonprime in nonprimes:
        if nonprime == 1:
                continue
        for prime in primes:
                while nonprime != 0 and number % nonprime != 0 and nonprime % prime == 0:
                        nonprime //= prime
                        number *= prime


print(f"Smallest number that can be divied with out a remainder from 1 to 20 is {number}")

# O(n) time n is b - a
# O(n) space
        

