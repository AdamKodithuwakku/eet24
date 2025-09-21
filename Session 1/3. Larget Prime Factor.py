# The prime factor sof 13195 are 5, 7, 13 and 29
# What is the largest prime factor of the number 600851475143


def isprime(number):
        if number <= 0:
                return False;
        if number <= 3:
                return True

        i = 3
        limit = number ** .5
        while i <= limit:
                if number % i == 0:
                        return False
                i += 2

        return True



number = 600851475143
k = number
i = 3
while not isprime(k):
        if k % i == 0:
                k //= i
        i +=2



print(f"Largest Prime factor of {number} is \"{k}\"")


# O(n) time complexity
# O(n^2) space complexity
