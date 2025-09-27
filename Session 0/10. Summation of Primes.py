# Find the sum of all the primes below two milion

limit = 2 * 10 ** 6

lastprime = 2
sumprime = lastprime
current = 3
while current < limit:
        for i in range(2, int(current**.5)+1):
                if current % i == 0:
                        break
        else:
                lastprime = current

                if lastprime < limit:
                        sumprime += lastprime
                else:
                        break

        current += 2

print(f"Sum of all the primes that are less that {limit} if \"{sumprime}\"")

# O(n*/n) time
# O(sqrtn) space

