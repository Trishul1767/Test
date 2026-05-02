# This is a simple comment
print("Hello, World!")
# Another comment
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))
# End of the script
# two sum problem
def two_sum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return []
# Example usage
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output: [0, 1]