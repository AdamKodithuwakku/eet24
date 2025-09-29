# If we list all the natural numbers below 10 that are multiples of 3, 5 we get 3,5,6 and 9. The sum of these multiples is 23
# Find the sum of all the multiples of 3 or 5 below the 1000


limit = 1000
#the limit exclusive sum
sum_of_3s = sum(range(0, limit, 3))
sum_of_5s = sum(range(0, limit, 5))
sum_of_15s = sum(range(0, limit, 15))

ans =  sum_of_3s + sum_of_5s - sum_of_15s

print(f"The sum of all the multiples of 3 or 5 below the {limit} is \"{ans}\"")

n = limit
n -= 1
n3 = n // 3
n5 = n // 5 
n15 = n // 15 

value = n3*(n3+1)*3 + n5*(n5+1)*5 - n15*(n15+1)*15
value //= 2

print(value)

#the range and the sum function are both O(n) for time complesity
#O(n) time complexity

#O(n) space complexity


