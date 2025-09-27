# 10 001st Prime number

limit = 10001


primes = [2, 3]
lengthprimes = len(primes)
i = 3
while lengthprimes < limit:
        for number in range(2, int(i ** .5)):
                if i % number == 0:
                        break
        else:
                primes.append(i)
                lengthprimes += 1
        i += 2

formatfix = ["th","st","nd","rd","th"][limit%10 if limit%10 <= 4 else 4]
print(f"{limit}{formatfix} prime number is {primes[-1]}")

# O(n*lgn) time complexity
# O(n) space
