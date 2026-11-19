def countDigits(num):
        count = 0
        for x in str(num):
            x = int(x)
            if num % x == 0:
                count += 1
        return count
num = int(input("Enter a digit: "))
result = countDigits(num)
print(result)
