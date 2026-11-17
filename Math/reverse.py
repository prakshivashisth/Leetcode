def reverse(x):
       sign = -1 if x < 0 else 1
       x = abs(x)
       rev = 0
       while x> 0:
          digit = x % 10
          rev = rev * 10 + digit
          x //= 10
       rev *= sign
       return rev
x = int(input())
reversed_number = reverse(x)
print(reversed_number)     
