# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum


limit = 100
# (1**2 + 2**2 + )  = 1 + 4 + 9
# n(n+1)(2n+1)/6 by examining the sequnce
n = limit
sqsum = n * (n + 1) * (2*n + 1) // 6
sumsq = (n * (n + 1) // 2 ) ** 2



# n(n+1) * n(n+1)            n(n+1)(2n+1)      (n-1)n(n+1)(3n+2) 
# --------------------  - ----------------- = ----------------------- 
#           4                   6                       12              
difference = sumsq - sqsum


print(f"Difference between sum of squares and the square of the sum of natural numbers is {difference}")

# O(1) time complexity
# O(1) space complexity
