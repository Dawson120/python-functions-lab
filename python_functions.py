# Challenges
def sum_to(n):
    return sum(range(1, +1))

print(sum_to(5))

def largest(nums):
    return max(nums)

print(largest([1, 2, 3, 4, 0]))

def occurrences(string, target):
    count = 0
    start_index = 0
    while start_index < len(string):
      index = string.find(target, start_index)
      if index == -1:
          break
      count += 1
      start_index = index + 1
    return count

print(occurrences('fleep floop', 'e'))
print(occurrences('fleep floop', 'p'))
print(occurrences('fleep floop', 'ee'))
print(occurrences('fleep floop', 'fe'))

def product(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result
print(product(-2, 6))