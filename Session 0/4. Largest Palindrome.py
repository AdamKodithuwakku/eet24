# A palindromic number reads the same both ways. The largest palindrome number using 2 digits is 9009
# Find the largest palindrome made from the product of 3 digits


largest = 0
faA, faB = 0, 0
for a in range(999, 99, -1):
        for b in range(999, 99, -1):
                number = a * b
                stnumber = str(number)
                if stnumber == stnumber[::-1]:
                        largest = number
                        break
        if largest != 0:
                break
        


print(f"The largest palindrome number created using ( {a}*{b} )three digits is \"{largest}\"")
                        


# O(m * n^m) time space for the worst case in hypothetical that we dont find a number that is palindrome at all
# O(m*n) space complexity
