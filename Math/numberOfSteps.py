def numberOfSteps(num):
        steps = 0

        while num > 0:
            num = num // 2 if num % 2 == 0 else num - 1
            steps += 1

        return steps
num = int(input("Enter a number: "))
result = numberOfSteps(num)
print(result)