"""
Generate all prime numbers less than 100. Print them in a spiral format (like a 
clockwise square spiral) of minimal size that fits all primes.
"""
primes = []
for num in range(2, 100):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            break
    else:
        primes.append(num)

n = 5
grid = [[0]*n for _ in range(n)]
top, bottom = 0, n-1
left, right = 0, n-1
index = 0

while index < len(primes):
    for i in range(left, right+1):
        grid[top][i] = primes[index]
        index += 1
    top += 1

    for i in range(top, bottom+1):
        grid[i][right] = primes[index]
        index += 1
    right -= 1

    for i in range(right, left-1, -1):
        grid[bottom][i] = primes[index]
        index += 1
    bottom -= 1

    for i in range(bottom, top-1, -1):
        grid[i][left] = primes[index]
        index += 1
    left += 1
    
for row in grid:
    print(" ".join(f"{x:2}" for x in row))