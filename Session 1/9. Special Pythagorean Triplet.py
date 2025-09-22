# Find the product abc for pythagorean triplet for which a + b + c = 1000

# Pythogoras Theorem
# a**2 + b**2 = c**2

##Let;
##        a = m**2 - n**2
##        b = 2mn
##        c = m**2 + n**2
##
##        a**2 = m**4 - 2*mmnn + n**4
##        b**2 = 4mmnn
##        a**2 + b**2 = m**4 + 2mmnn + n**4
##        a**2 + b**2 = c**2
##
##        Then
##        a + b + c = 100
##        m**2 - n**2 + 2mn + m**2 + n**2 = 100
##        m(m+n) = 50

limit = 1000

m = 1
for k in range(int((limit/2)**.5)+1, 1, -1):
        n = (limit/2 - k**2 ) / k
        if n > 0 and n - int(n) == 0:
                n = int(n)
                m = k
                break

a = m ** 2 - n**2
b = 2 * m * n
c = m ** 2 + n ** 2

print(f"Product is \"{a*b*c}\" for pythagorean triplet for which a + b + c = 1000")

# O(logn) time
# O(1) space
